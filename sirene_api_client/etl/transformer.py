"""
Data transformation module for the SIREN ETL service.

This module handles transformation of raw API data to Django-ready Pydantic models.
"""

from __future__ import annotations

from datetime import date, datetime
import hashlib
import json
import logging
from typing import TYPE_CHECKING, Any

from sirene_api_client.api_types import UNSET

from .config import ETLConfig, ValidationMode
from .coordinators import lambert93_to_wgs84
from .exceptions import TransformationError, ValidationError
from .models import (
    ActivityClassificationData,
    AddressData,
    CompanyData,
    CompanyIdentifierData,
    CompanyLegalUnitPeriodData,
    ExternalRegistryRecordData,
    FacilityData,
    FacilityEstablishmentPeriodData,
    FacilityIdentifierData,
    FacilityOwnershipData,
    SIRENExtractResult,
)

if TYPE_CHECKING:
    from sirene_api_client.models.adresse import Adresse
    from sirene_api_client.models.etablissement import Etablissement
    from sirene_api_client.models.periode_etablissement import PeriodeEtablissement
    from sirene_api_client.models.periode_unite_legale import PeriodeUniteLegale
    from sirene_api_client.models.unite_legale import UniteLegale

logger = logging.getLogger(__name__)


class SIRENTransformer:
    """Transform API data to Django-ready Pydantic models."""

    def __init__(self, config: ETLConfig) -> None:
        if config is None:
            raise TypeError("config cannot be None")
        self.config = config
        self._activity_cache: dict[str, ActivityClassificationData] = {}

    def transform_complete(self, raw_data: dict[str, Any]) -> SIRENExtractResult:
        """
        Transform complete SIREN extraction to Pydantic models.

        Args:
            raw_data: Raw API data from extractor

        Returns:
            SIRENExtractResult with all transformed data
        """
        logger.info("Starting complete data transformation")

        try:
            company = raw_data["company"]
            facilities = raw_data["facilities"]

            # Transform company data
            company_data = self.transform_unite_legale(company)

            # Transform facilities data
            facilities_data = []
            establishment_periods = []
            addresses = []
            facility_ownerships = []

            for facility in facilities:
                facility_data = self.transform_etablissement(facility)
                facilities_data.append(facility_data)

                # Transform establishment periods
                if facility.periodes_etablissement:
                    for period in facility.periodes_etablissement:
                        period_data = self.transform_establishment_period(
                            period, facility
                        )
                        establishment_periods.append(period_data)

                # Transform addresses
                if facility.adresse_etablissement:
                    address_data = self.transform_address(
                        facility.adresse_etablissement,
                        facility,  # NEW: Pass facility for reference
                        facility.date_creation_etablissement or date.today(),
                    )
                    addresses.append(address_data)

                # Create facility ownership relationship
                ownership_data = self.transform_facility_ownership(facility)
                facility_ownerships.append(ownership_data)

            # Transform company legal unit periods
            legal_unit_periods = []
            if company and company.periodes_unite_legale:
                for legal_period in company.periodes_unite_legale:
                    legal_period_data = self.transform_legal_unit_period(legal_period)
                    legal_unit_periods.append(legal_period_data)

            # Create registry records
            registry_records = self._create_registry_records(raw_data)

            result = SIRENExtractResult(
                company=company_data,
                facilities=facilities_data,
                legal_unit_periods=legal_unit_periods,
                establishment_periods=establishment_periods,
                addresses=addresses,
                activity_classifications=list(self._activity_cache.values()),
                facility_ownerships=facility_ownerships,
                registry_records=registry_records,
                extraction_metadata=raw_data.get("extraction_metadata", {})
                if isinstance(raw_data.get("extraction_metadata", {}), dict)
                else {},
            )

            logger.info("Successfully completed data transformation")
            return result

        except Exception as e:
            logger.error(f"Failed to transform data: {e}")
            raise TransformationError(f"Failed to transform data: {e}") from e

    def transform_unite_legale(self, ul: UniteLegale | None) -> CompanyData:
        """Transform UniteLegale to CompanyData."""
        if ul is None:
            if self.config.validation_mode == ValidationMode.STRICT:
                raise ValidationError("Company data is required but not provided")
            return CompanyData(
                name="Unknown Company",
                identifiers=[],
                creation_date=None,
                acronym=None,
                employee_band=None,
                employee_band_year=None,
                company_size_category=None,
                category_year=None,
                diffusion_status=None,
                is_purged=None,
                last_update=None,
                period_count=None,
                association_id=None,
            )

        logger.debug(f"Transforming UniteLegale: {ul.siren}")

        # Extract company name from current period
        company_name = self._extract_current_legal_name(ul)

        # Create SIREN identifier
        siren_identifier = self.transform_company_identifier("siren", str(ul.siren))

        return CompanyData(
            name=company_name,
            identifiers=[siren_identifier],
            creation_date=self._unwrap_unset(ul.date_creation_unite_legale),
            acronym=self._unwrap_unset(ul.sigle_unite_legale),
            employee_band=self._unwrap_unset(ul.tranche_effectifs_unite_legale),
            employee_band_year=int(ul.annee_effectifs_unite_legale)
            if ul.annee_effectifs_unite_legale is not UNSET
            and ul.annee_effectifs_unite_legale is not None
            and isinstance(ul.annee_effectifs_unite_legale, str | int)
            else None,
            company_size_category=ul.categorie_entreprise.value
            if ul.categorie_entreprise is not UNSET
            and ul.categorie_entreprise is not None
            and hasattr(ul.categorie_entreprise, "value")
            else None,
            category_year=int(ul.annee_categorie_entreprise)
            if ul.annee_categorie_entreprise is not UNSET
            and ul.annee_categorie_entreprise is not None
            and isinstance(ul.annee_categorie_entreprise, str | int)
            else None,
            diffusion_status=self._unwrap_unset(ul.statut_diffusion_unite_legale),
            is_purged=self._unwrap_unset(ul.unite_purgee_unite_legale),
            last_update=self._parse_datetime(
                self._unwrap_unset(ul.date_dernier_traitement_unite_legale)
            ),
            period_count=self._unwrap_unset(ul.nombre_periodes_unite_legale),
            association_id=self._unwrap_unset(ul.identifiant_association_unite_legale),
        )

    def transform_etablissement(self, etab: Etablissement) -> FacilityData:
        """Transform Etablissement to FacilityData."""
        logger.debug(f"Transforming Etablissement: {etab.siret}")

        # Extract facility name from current period
        facility_name = self._extract_current_facility_name(etab)

        # Create SIRET identifier
        siret_identifier = self.transform_facility_identifier("siret", str(etab.siret))

        return FacilityData(
            name=facility_name,
            identifiers=[siret_identifier],
            parent_siren=str(etab.siren),
            nic=self._unwrap_unset(etab.nic),
            creation_date=self._unwrap_unset(etab.date_creation_etablissement),
            is_headquarters=etab.etablissement_siege or False,
            employee_band=self._unwrap_unset(etab.tranche_effectifs_etablissement),
            employee_band_year=int(etab.annee_effectifs_etablissement)
            if etab.annee_effectifs_etablissement is not UNSET
            and etab.annee_effectifs_etablissement is not None
            and isinstance(etab.annee_effectifs_etablissement, str | int)
            else None,
            search_score=self._unwrap_unset(etab.score),
            diffusion_status=self._unwrap_unset(etab.statut_diffusion_etablissement),
            crafts_activity=self._unwrap_unset(
                etab.activite_principale_registre_metiers_etablissement
            ),
            last_update=self._parse_datetime(
                self._unwrap_unset(etab.date_dernier_traitement_etablissement)
            ),
            period_count=self._unwrap_unset(etab.nombre_periodes_etablissement),
        )

    def transform_address(
        self,
        adresse: Adresse,
        facility: Etablissement,  # Add facility parameter
        start_date: date,
    ) -> AddressData:
        """Transform Adresse to AddressData with facility link and WGS84 coordinates."""
        logger.debug("Transforming address data")

        # Combine street components
        street_parts = []
        if adresse.numero_voie_etablissement:
            street_parts.append(str(adresse.numero_voie_etablissement))
        if adresse.indice_repetition_etablissement:
            street_parts.append(str(adresse.indice_repetition_etablissement))
        if adresse.type_voie_etablissement:
            street_parts.append(str(adresse.type_voie_etablissement))
        if adresse.libelle_voie_etablissement:
            street_parts.append(str(adresse.libelle_voie_etablissement))

        street_address = " ".join(street_parts) if street_parts else None

        # Convert coordinates
        longitude, latitude = None, None
        if (
            adresse.coordonnee_lambert_abscisse_etablissement
            and adresse.coordonnee_lambert_ordonnee_etablissement
        ):
            coords = lambert93_to_wgs84(
                adresse.coordonnee_lambert_abscisse_etablissement,
                adresse.coordonnee_lambert_ordonnee_etablissement,
            )
            if coords:
                longitude, latitude = coords
        elif (
            hasattr(adresse, "coordonnees_etablissement")
            and adresse.coordonnees_etablissement
        ):
            # Handle test mock structure
            coord_obj = adresse.coordonnees_etablissement
            if hasattr(coord_obj, "longitude") and hasattr(coord_obj, "latitude"):
                coords = lambert93_to_wgs84(coord_obj.longitude, coord_obj.latitude)
                if coords:
                    longitude, latitude = coords

        return AddressData(
            facility_siret=str(facility.siret),  # NEW: Explicit facility link
            country=str(adresse.code_pays_etranger_etablissement)
            if adresse.code_pays_etranger_etablissement is not UNSET
            and adresse.code_pays_etranger_etablissement is not None
            else "FR",
            administrative_area=None,  # Not available in SIREN data
            locality=self._unwrap_unset(adresse.libelle_commune_etablissement),
            postal_code=self._unwrap_unset(adresse.code_postal_etablissement),
            street_address=street_address,
            longitude=longitude,
            latitude=latitude,
            provider="sirene",
            geocode_precision=self.config.coordinate_precision,
            start=start_date,
            end=None,  # Not available in SIREN data
        )

    def transform_legal_unit_period(
        self, period: PeriodeUniteLegale
    ) -> CompanyLegalUnitPeriodData:
        """Transform PeriodeUniteLegale to CompanyLegalUnitPeriodData."""
        logger.debug(f"Transforming legal unit period: {period.date_debut}")

        # Get or create activity classification
        activity_code = period.activite_principale_unite_legale
        if hasattr(period.nomenclature_activite_principale_unite_legale, "value"):
            activity_scheme = period.nomenclature_activite_principale_unite_legale.value
        elif isinstance(period.nomenclature_activite_principale_unite_legale, dict):
            activity_scheme = period.nomenclature_activite_principale_unite_legale.get(
                "value", "NAFRev2"
            )
        else:
            activity_scheme = "NAFRev2"

        if activity_code:
            self._get_or_create_activity_classification(activity_code, activity_scheme)

        return CompanyLegalUnitPeriodData(
            start=self._unwrap_unset(period.date_debut),
            end=self._unwrap_unset(period.date_fin),
            legal_name=str(period.denomination_unite_legale)
            if period.denomination_unite_legale is not UNSET
            and period.denomination_unite_legale is not None
            else "",
            legal_form_code=str(period.categorie_juridique_unite_legale)
            if period.categorie_juridique_unite_legale is not UNSET
            and period.categorie_juridique_unite_legale is not None
            else "",
            legal_form_scheme="sirene",
            activity_code=activity_code or "",
            activity_scheme=activity_scheme,
            status=self.map_unite_legale_status(
                period.etat_administratif_unite_legale.value
                if hasattr(period.etat_administratif_unite_legale, "value")
                else (period.etat_administratif_unite_legale or "A")
            ),
            employee_band=None,  # Not available in period data
            employee_band_year=None,  # Not available in period data
            ess_flag=self._parse_boolean(
                self._unwrap_unset(period.economie_sociale_solidaire_unite_legale)
            ),
            mission_company_flag=self._parse_boolean(
                self._unwrap_unset(period.societe_mission_unite_legale)
            ),
        )

    def transform_establishment_period(
        self, period: PeriodeEtablissement, facility: Etablissement
    ) -> FacilityEstablishmentPeriodData:
        """Transform PeriodeEtablissement to FacilityEstablishmentPeriodData."""
        logger.debug(f"Transforming establishment period: {period.date_debut}")

        # Get or create activity classification
        activity_code = period.activite_principale_etablissement
        if hasattr(period.nomenclature_activite_principale_etablissement, "value"):
            activity_scheme = (
                period.nomenclature_activite_principale_etablissement.value
            )
        elif isinstance(period.nomenclature_activite_principale_etablissement, dict):
            activity_scheme = period.nomenclature_activite_principale_etablissement.get(
                "value", "NAFRev2"
            )
        else:
            activity_scheme = "NAFRev2"

        if activity_code:
            self._get_or_create_activity_classification(activity_code, activity_scheme)

        return FacilityEstablishmentPeriodData(
            start=self._unwrap_unset(period.date_debut),
            end=self._unwrap_unset(period.date_fin),
            status=self.map_etablissement_status(
                period.etat_administratif_etablissement.value
                if hasattr(period.etat_administratif_etablissement, "value")
                else (period.etat_administratif_etablissement or "A")
            ),
            activity_code=activity_code or "",
            activity_scheme=activity_scheme,
            is_hq=facility.etablissement_siege or False,
            opening_date=self._unwrap_unset(facility.date_creation_etablissement),
        )

    def transform_facility_ownership(
        self, facility: Etablissement
    ) -> FacilityOwnershipData:
        """Transform facility to ownership relationship."""
        return FacilityOwnershipData(
            company_siren=str(facility.siren),
            facility_siret=str(facility.siret),
            role="owner" if facility.etablissement_siege else "operator",
            start=facility.date_creation_etablissement or date.today(),
            end=None,  # Not available in SIREN data
        )

    def _extract_current_legal_name(self, ul: UniteLegale) -> str:
        """Extract current legal name from periods."""
        if not ul.periodes_unite_legale:
            # Use direct field when no periods available - but UniteLegale doesn't have denomination_unite_legale
            return "Unknown Company"

        # Find current period (no end date)
        current_period = None
        for period in ul.periodes_unite_legale:
            if not period.date_fin:
                current_period = period
                break

        if not current_period and ul.periodes_unite_legale:
            # Use the most recent period
            current_period = self._get_max_date_period(
                ul.periodes_unite_legale, "date_debut"
            )

        if (
            current_period
            and hasattr(current_period, "denomination_unite_legale")
            and current_period.denomination_unite_legale is not UNSET
        ):
            return current_period.denomination_unite_legale or "Unknown Company"
        return "Unknown Company"

    def _extract_current_facility_name(self, etab: Etablissement) -> str:
        """Extract facility name, prioritizing establishment-specific names, then company name."""

        # PRIORITY 1: Try establishment-specific names first (more granular)
        if not etab.periodes_etablissement:
            return "Unknown Facility"

        # Find current period (no end date)
        current_period = None
        for period in etab.periodes_etablissement:
            if not period.date_fin:
                current_period = period
                break

        if not current_period and etab.periodes_etablissement:
            # Use the most recent period
            current_period = self._get_max_date_period(
                etab.periodes_etablissement, "date_debut"
            )

        if current_period:
            # First try denomination_usuelle_etablissement
            if (
                hasattr(current_period, "denomination_usuelle_etablissement")
                and current_period.denomination_usuelle_etablissement is not UNSET
                and current_period.denomination_usuelle_etablissement
            ):
                return current_period.denomination_usuelle_etablissement

            # Fallback to enseigne1Etablissement
            if (
                hasattr(current_period, "enseigne_1_etablissement")
                and current_period.enseigne_1_etablissement is not UNSET
                and current_period.enseigne_1_etablissement
            ):
                return current_period.enseigne_1_etablissement

            # Fallback to enseigne2Etablissement
            if (
                hasattr(current_period, "enseigne_2_etablissement")
                and current_period.enseigne_2_etablissement is not UNSET
                and current_period.enseigne_2_etablissement
            ):
                return current_period.enseigne_2_etablissement

            # Fallback to enseigne3Etablissement
            if (
                hasattr(current_period, "enseigne_3_etablissement")
                and current_period.enseigne_3_etablissement is not UNSET
                and current_period.enseigne_3_etablissement
            ):
                return current_period.enseigne_3_etablissement

        # PRIORITY 2: Fallback to company name from uniteLegale
        if (
            hasattr(etab, "unite_legale")
            and etab.unite_legale is not None
            and hasattr(etab.unite_legale, "denomination_unite_legale")
            and etab.unite_legale.denomination_unite_legale is not UNSET
            and etab.unite_legale.denomination_unite_legale
        ):
            return etab.unite_legale.denomination_unite_legale

        return "Unknown Facility"

    def transform_company_identifier(
        self, scheme: str, value: str
    ) -> CompanyIdentifierData:
        """Transform company identifier."""
        return CompanyIdentifierData(
            scheme=scheme,
            value=value,
            normalized_value=value,
            country="FR",
            is_verified=True,
            verified_at=datetime.now(),
        )

    def transform_facility_identifier(
        self, scheme: str, value: str
    ) -> FacilityIdentifierData:
        """Transform facility identifier."""
        return FacilityIdentifierData(
            scheme=scheme,
            value=value,
            normalized_value=value,
            country="FR",
            is_verified=True,
            verified_at=datetime.now(),
        )

    def transform_activity_code(
        self, code: str, scheme: str, label: str | None = None
    ) -> ActivityClassificationData:
        """Transform activity code to ActivityClassificationData."""
        # Normalize scheme to lowercase with underscores
        normalized_scheme = scheme.lower().replace("rev", "_rev").replace(" ", "_")
        cache_key = f"{normalized_scheme}:{code}"

        if cache_key not in self._activity_cache:
            self._activity_cache[cache_key] = ActivityClassificationData(
                scheme=normalized_scheme,
                code=code,
                label=label or f"{scheme} {code}",  # Use provided label or default
                start=date(2008, 1, 1),  # NAF Rev.2 start date
                end=None,
            )

        return self._activity_cache[cache_key]

    def _get_or_create_activity_classification(
        self, code: str, scheme: str
    ) -> ActivityClassificationData:
        """Get or create activity classification."""
        return self.transform_activity_code(code, scheme)

    def _create_registry_records(
        self, raw_data: dict[str, Any]
    ) -> list[ExternalRegistryRecordData]:
        """Create registry records for audit trail."""
        records = []

        # Company record
        company = raw_data["company"]
        company_payload = company.to_dict() if hasattr(company, "to_dict") else {}
        records.append(
            ExternalRegistryRecordData(
                entity_type="legal_unit",
                external_id=str(company.siren),
                payload=company_payload,
                payload_hash=self._create_payload_hash(company_payload),
                registry_updated_at=self._parse_datetime(
                    company.date_dernier_traitement_unite_legale
                )
                or datetime.now(),
                ingested_at=datetime.now(),
            )
        )

        # Facility records
        for facility in raw_data["facilities"]:
            facility_payload = (
                facility.to_dict() if hasattr(facility, "to_dict") else {}
            )
            records.append(
                ExternalRegistryRecordData(
                    entity_type="establishment",
                    external_id=str(facility.siret),
                    payload=facility_payload,
                    payload_hash=self._create_payload_hash(facility_payload),
                    registry_updated_at=facility.date_dernier_traitement_etablissement
                    or datetime.now(),
                    ingested_at=datetime.now(),
                )
            )

        return records

    def _create_payload_hash(self, payload: dict[str, Any]) -> str:
        """Create SHA-256 hash of payload."""
        payload_str = json.dumps(payload, sort_keys=True, default=str)
        return hashlib.sha256(payload_str.encode()).hexdigest()

    def map_unite_legale_status(self, api_status: str | Any) -> str:
        """Map API status to Django status."""
        if api_status is UNSET:
            return "unknown"
        return "active" if api_status == "A" else "ceased"

    def map_etablissement_status(self, api_status: str | Any) -> str:
        """Map API status to Django status."""
        if api_status is UNSET:
            return "unknown"
        return "active" if api_status == "A" else "closed"

    def _parse_boolean(self, value: str | None | Any) -> bool:
        """Parse boolean from string value."""
        if value is None or value is UNSET:
            return False
        return value.upper() == "O"

    def _get_max_date_period(self, periods: list[Any], date_field: str) -> Any:
        """Get the period with the maximum date, handling Unset values."""
        if not periods:
            return None

        def get_date(period: Any) -> date:
            field_value = getattr(period, date_field)
            return field_value if field_value is not UNSET else date.min

        return max(periods, key=get_date)

    def _unwrap_unset(self, value: Any) -> Any:
        """Convert Unset values to None for Pydantic models."""
        if value is UNSET:
            return None
        return value

    def _parse_datetime(self, value: str | None | Any) -> datetime | None:
        """Parse datetime from string value."""
        if not value or value is UNSET:
            return None
        try:
            from dateutil.parser import isoparse

            return isoparse(value)
        except Exception:
            return None
