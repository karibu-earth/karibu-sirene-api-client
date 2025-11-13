"""
Unit tests for ETL transformer module.

Tests cover:
- SIRENTransformer initialization and configuration
- Data transformation logic with mocked API data
- Error handling for invalid data
- Coordinate conversion integration
- Model validation and output generation
"""

from datetime import date, datetime
from unittest.mock import MagicMock, patch

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.etl.config import ETLConfig, ValidationMode
from sirene_api_client.etl.exceptions import TransformationError
from sirene_api_client.etl.models import (
    AddressData,
    CompanyData,
    CompanyIdentifierData,
    CompanyLegalUnitPeriodData,
    FacilityData,
    FacilityEstablishmentPeriodData,
    FacilityIdentifierData,
    FacilityOwnershipData,
    SIRENExtractResult,
)
from sirene_api_client.etl.transformer import SIRENTransformer


class TestSIRENTransformer:
    """Test SIRENTransformer functionality."""

    @pytest.fixture
    def config(self) -> ETLConfig:
        """Create default ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    @pytest.fixture
    def transformer(self, config: ETLConfig) -> SIRENTransformer:
        """Create SIRENTransformer instance."""
        return SIRENTransformer(config)

    def test_transformer_initialization(self, config: ETLConfig) -> None:
        """Test SIRENTransformer initialization."""
        transformer = SIRENTransformer(config)

        assert transformer.config == config

    def test_transformer_initialization_with_none_config(self) -> None:
        """Test SIRENTransformer initialization with None config."""
        with pytest.raises(TypeError):
            SIRENTransformer(None)

    def test_transform_complete_success(self, transformer: SIRENTransformer) -> None:
        """Test successful complete transformation."""
        # Mock raw data
        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"
        mock_company.periodes_unite_legale = []
        mock_company.to_dict = MagicMock(return_value={})

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.denomination_usuelle_etablissement = "Test Facility"
        mock_facility.periodes_etablissement = []
        mock_facility.adresse_etablissement = None
        mock_facility.date_creation_etablissement = None
        mock_facility.to_dict = MagicMock(return_value={})

        raw_data = {
            "company": mock_company,
            "facilities": [mock_facility],
            "extraction_metadata": {
                "siren": "123456782",
                "extracted_at": datetime.now().isoformat(),
                "facility_count": 1,
            },
        }

        with (
            patch.object(
                transformer,
                "transform_unite_legale",
                return_value=CompanyData(name="Test Company", identifiers=[]),
            ) as mock_transform_company,
            patch.object(
                transformer,
                "transform_etablissement",
                return_value=FacilityData(
                    name="Test Facility", identifiers=[], parent_siren="123456782"
                ),
            ) as mock_transform_facility,
            patch.object(
                transformer,
                "transform_facility_ownership",
                return_value=FacilityOwnershipData(
                    company_siren="123456782",
                    facility_siret="12345678200001",
                    start=date.today(),
                ),
            ),
            patch.object(transformer, "_create_registry_records", return_value=[]),
        ):
            result = transformer.transform_complete(raw_data)

            assert isinstance(result, SIRENExtractResult)
            assert result.company is not None
            assert len(result.facilities) == 1
            assert result.extraction_metadata["siren"] == "123456782"

            mock_transform_company.assert_called_once_with(mock_company)
            mock_transform_facility.assert_called_once_with(mock_facility)

    def test_transform_complete_empty_data(self, transformer: SIRENTransformer) -> None:
        """Test transformation with empty data."""
        raw_data = {
            "company": None,
            "facilities": [],
            "extraction_metadata": {
                "siren": "123456782",
                "extracted_at": datetime.now().isoformat(),
                "facility_count": 0,
            },
        }

        with (
            patch.object(
                transformer,
                "transform_unite_legale",
                return_value=CompanyData(name="Unknown Company", identifiers=[]),
            ) as mock_transform_company,
            patch.object(transformer, "_create_registry_records", return_value=[]),
        ):
            result = transformer.transform_complete(raw_data)

            assert isinstance(result, SIRENExtractResult)
            assert result.company is not None
            assert len(result.facilities) == 0
            assert result.extraction_metadata["facility_count"] == 0

            mock_transform_company.assert_called_once_with(None)

    def test_transform_unite_legale_success(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test successful UniteLegale transformation."""
        # Create a mock period with the company name
        mock_period = MagicMock()
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.date_fin = None  # Current period

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.periodes_unite_legale = [mock_period]
        mock_company.date_creation_unite_legale = None
        mock_company.sigle_unite_legale = None
        mock_company.tranche_effectifs_unite_legale = None
        mock_company.annee_effectifs_unite_legale = None
        mock_company.categorie_entreprise = None
        mock_company.annee_categorie_entreprise = None
        mock_company.statut_diffusion_unite_legale = None
        mock_company.unite_purgee_unite_legale = None
        mock_company.date_dernier_traitement_unite_legale = None
        mock_company.nombre_periodes_unite_legale = None
        mock_company.identifiant_association_unite_legale = None

        with patch.object(
            transformer,
            "transform_company_identifier",
            return_value=CompanyIdentifierData(
                scheme="siren",
                value="123456782",
                normalized_value="123456782",
                verified_at=datetime.now(),
            ),
        ) as mock_transform_id:
            result = transformer.transform_unite_legale(mock_company)

            assert result.name == "Test Company"
            assert len(result.identifiers) == 1
            mock_transform_id.assert_called_once()

    def test_transform_etablissement_success(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test successful Etablissement transformation."""
        # Create a mock period with the facility name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = "Test Facility"
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale for company name fallback
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = "Test Company"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.siren = "123456782"
        mock_facility.nic = None
        mock_facility.date_creation_etablissement = None
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        with patch.object(
            transformer,
            "transform_facility_identifier",
            return_value=FacilityIdentifierData(
                scheme="siret",
                value="12345678200001",
                normalized_value="12345678200001",
                verified_at=datetime.now(),
            ),
        ) as mock_transform_id:
            result = transformer.transform_etablissement(mock_facility)

            assert result.name == "Test Facility"
            assert result.parent_siren == "123456782"
            assert len(result.identifiers) == 1
            mock_transform_id.assert_called_once()

    def test_transform_address_success(self, transformer: SIRENTransformer) -> None:
        """Test successful address transformation."""
        mock_address = MagicMock()
        mock_address.numero_voie_etablissement = "123"
        mock_address.indice_repetition_etablissement = None
        mock_address.type_voie_etablissement = "RUE"
        mock_address.libelle_voie_etablissement = "MAIN STREET"
        mock_address.code_postal_etablissement = "75001"
        mock_address.libelle_commune_etablissement = "PARIS"
        mock_address.code_pays_etranger_etablissement = None
        mock_address.coordonnees_etablissement = None

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"

        with patch(
            "sirene_api_client.etl.transformer.lambert93_to_wgs84",
            return_value=(2.3522, 48.8566),
        ):
            result = transformer.transform_address(
                mock_address, mock_facility, date(2020, 1, 1)
            )

            assert result.facility_siret == "12345678200001"
            assert result.street_address == "123 RUE MAIN STREET"
            assert result.locality == "PARIS"
            assert result.postal_code == "75001"
            assert result.country == "FR"
            assert result.longitude == 2.3522
            assert result.latitude == 48.8566
            assert result.start == date(2020, 1, 1)

    def test_transform_address_with_coordinates(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test address transformation with Lambert 93 coordinates."""
        mock_address = MagicMock()
        mock_address.numero_voie_etablissement = "123"
        mock_address.indice_repetition_etablissement = None
        mock_address.type_voie_etablissement = "RUE"
        mock_address.libelle_voie_etablissement = "MAIN STREET"
        mock_address.code_postal_etablissement = "75001"
        mock_address.libelle_commune_etablissement = "PARIS"
        mock_address.code_pays_etranger_etablissement = None
        mock_address.coordonnee_lambert_abscisse_etablissement = None
        mock_address.coordonnee_lambert_ordonnee_etablissement = None
        mock_address.coordonnees_etablissement = MagicMock()
        mock_address.coordonnees_etablissement.longitude = "235220"
        mock_address.coordonnees_etablissement.latitude = "4868566"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"

        with patch(
            "sirene_api_client.etl.transformer.lambert93_to_wgs84",
            return_value=(2.3522, 48.8566),
        ) as mock_coord:
            result = transformer.transform_address(
                mock_address, mock_facility, date(2020, 1, 1)
            )

            assert result.facility_siret == "12345678200001"
            assert result.longitude == 2.3522
            assert result.latitude == 48.8566
            mock_coord.assert_called_once_with("235220", "4868566")

    def test_transform_address_coordinate_conversion_failure(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test address transformation with coordinate conversion failure."""
        mock_address = MagicMock()
        mock_address.numero_voie_etablissement = "123"
        mock_address.indice_repetition_etablissement = None
        mock_address.type_voie_etablissement = "RUE"
        mock_address.libelle_voie_etablissement = "MAIN STREET"
        mock_address.code_postal_etablissement = "75001"
        mock_address.libelle_commune_etablissement = "PARIS"
        mock_address.code_pays_etranger_etablissement = None
        mock_address.coordonnee_lambert_abscisse_etablissement = None
        mock_address.coordonnee_lambert_ordonnee_etablissement = None
        mock_address.coordonnees_etablissement = MagicMock()
        mock_address.coordonnees_etablissement.longitude = "invalid"
        mock_address.coordonnees_etablissement.latitude = "invalid"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"

        with patch(
            "sirene_api_client.etl.transformer.lambert93_to_wgs84", return_value=None
        ) as mock_coord:
            result = transformer.transform_address(
                mock_address, mock_facility, date(2020, 1, 1)
            )

            assert result.facility_siret == "12345678200001"
            assert result.longitude is None
            assert result.latitude is None
            mock_coord.assert_called_once_with("invalid", "invalid")

    def test_transform_activity_code_success(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test successful activity code transformation."""
        result = transformer.transform_activity_code(
            "6201Z", "NAFRev2", "Programmation informatique"
        )

        assert result.code == "6201Z"
        assert result.scheme == "naf_rev2"
        assert result.label == "Programmation informatique"

    def test_transform_activity_code_without_label(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test activity code transformation without label."""
        result = transformer.transform_activity_code("6201Z", "NAFRev2", None)

        assert result.code == "6201Z"
        assert result.scheme == "naf_rev2"
        assert (
            result.label == "NAFRev2 6201Z"
        )  # Should get default label when None is passed

    def test_map_unite_legale_status(self, transformer: SIRENTransformer) -> None:
        """Test UniteLegale status mapping."""
        assert transformer.map_unite_legale_status("A") == "active"
        assert transformer.map_unite_legale_status("C") == "ceased"
        assert transformer.map_unite_legale_status("X") == "ceased"  # Unknown status

    def test_map_etablissement_status(self, transformer: SIRENTransformer) -> None:
        """Test Etablissement status mapping."""
        assert transformer.map_etablissement_status("A") == "active"
        assert transformer.map_etablissement_status("F") == "closed"
        assert transformer.map_etablissement_status("X") == "closed"  # Unknown status

    def test_transformer_with_different_configs(self) -> None:
        """Test transformer with different configurations."""
        strict_config = ETLConfig(validation_mode=ValidationMode.STRICT)
        lenient_config = ETLConfig(validation_mode=ValidationMode.LENIENT)
        permissive_config = ETLConfig(validation_mode=ValidationMode.PERMISSIVE)

        transformer_strict = SIRENTransformer(strict_config)
        transformer_lenient = SIRENTransformer(lenient_config)
        transformer_permissive = SIRENTransformer(permissive_config)

        assert transformer_strict.config.validation_mode == ValidationMode.STRICT
        assert transformer_lenient.config.validation_mode == ValidationMode.LENIENT
        assert (
            transformer_permissive.config.validation_mode == ValidationMode.PERMISSIVE
        )

    def test_transform_complete_with_validation_error_strict_mode(self) -> None:
        """Test transformation with validation error in strict mode."""
        strict_config = ETLConfig(validation_mode=ValidationMode.STRICT)
        transformer = SIRENTransformer(strict_config)

        raw_data = {
            "company": None,  # Invalid data
            "facilities": [],
            "extraction_metadata": {"siren": "123456782"},
        }

        with (
            patch.object(transformer, "_create_registry_records", return_value=[]),
            pytest.raises(TransformationError),
        ):
            transformer.transform_complete(raw_data)

    def test_transform_complete_with_validation_error_lenient_mode(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test transformation with validation error in lenient mode."""
        raw_data = {
            "company": None,  # Invalid data
            "facilities": [],
            "extraction_metadata": {"siren": "123456782"},
        }

        with patch.object(transformer, "_create_registry_records", return_value=[]):
            # Should not raise exception in lenient mode
            result = transformer.transform_complete(raw_data)
            assert isinstance(result, SIRENExtractResult)

    # ===== EDGE CASE TESTS FOR UNSET HANDLING =====

    def test_transform_unite_legale_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test company transformation with UNSET values."""
        # Create a mock period with the company name
        mock_period = MagicMock()
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.date_fin = None  # Current period

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.periodes_unite_legale = [mock_period]

        # Set all optional fields to UNSET
        mock_company.date_creation_unite_legale = UNSET
        mock_company.sigle_unite_legale = UNSET
        mock_company.tranche_effectifs_unite_legale = UNSET
        mock_company.annee_effectifs_unite_legale = UNSET
        mock_company.categorie_entreprise = UNSET
        mock_company.annee_categorie_entreprise = UNSET
        mock_company.statut_diffusion_unite_legale = UNSET
        mock_company.unite_purgee_unite_legale = UNSET
        mock_company.date_dernier_traitement_unite_legale = UNSET
        mock_company.nombre_periodes_unite_legale = UNSET
        mock_company.identifiant_association_unite_legale = UNSET

        result = transformer.transform_unite_legale(mock_company)

        assert isinstance(result, CompanyData)
        assert result.name == "Test Company"
        assert result.acronym is None
        assert result.employee_band is None
        assert result.employee_band_year is None
        assert result.company_size_category is None
        assert result.category_year is None
        assert result.diffusion_status is None
        assert result.is_purged is None
        assert result.last_update is None
        assert result.period_count is None
        assert result.association_id is None

    def test_transform_unite_legale_with_mixed_unset_and_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test company transformation with mix of UNSET and actual values."""
        # Create a mock period with the company name
        mock_period = MagicMock()
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.date_fin = None  # Current period

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.periodes_unite_legale = [mock_period]

        # Mix of UNSET and actual values
        mock_company.date_creation_unite_legale = date(2020, 1, 1)
        mock_company.sigle_unite_legale = "TC"
        mock_company.tranche_effectifs_unite_legale = UNSET
        mock_company.annee_effectifs_unite_legale = 2023
        mock_company.categorie_entreprise = UNSET
        mock_company.annee_categorie_entreprise = UNSET
        mock_company.statut_diffusion_unite_legale = "O"
        mock_company.unite_purgee_unite_legale = UNSET
        mock_company.date_dernier_traitement_unite_legale = "2023-12-01T10:00:00"
        mock_company.nombre_periodes_unite_legale = 5
        mock_company.identifiant_association_unite_legale = UNSET

        result = transformer.transform_unite_legale(mock_company)

        assert isinstance(result, CompanyData)
        assert result.name == "Test Company"
        assert result.creation_date == date(2020, 1, 1)
        assert result.acronym == "TC"
        assert result.employee_band is None  # UNSET
        assert result.employee_band_year == 2023
        assert result.company_size_category is None  # UNSET
        assert result.category_year is None  # UNSET
        assert result.diffusion_status == "O"
        assert result.is_purged is None  # UNSET
        assert result.last_update is not None
        assert result.period_count == 5
        assert result.association_id is None  # UNSET

    def test_transform_etablissement_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test facility transformation with UNSET values."""
        # Create a mock period with the facility name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = "Test Facility"
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale for company name fallback
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = "Test Company"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]

        # Set all optional fields to UNSET
        mock_facility.nic = UNSET
        mock_facility.date_creation_etablissement = UNSET
        mock_facility.etablissement_siege = UNSET
        mock_facility.tranche_effectifs_etablissement = UNSET
        mock_facility.annee_effectifs_etablissement = UNSET
        mock_facility.score = UNSET
        mock_facility.statut_diffusion_etablissement = UNSET
        mock_facility.activite_principale_registre_metiers_etablissement = UNSET
        mock_facility.date_dernier_traitement_etablissement = UNSET
        mock_facility.nombre_periodes_etablissement = UNSET

        result = transformer.transform_etablissement(mock_facility)

        assert isinstance(result, FacilityData)
        assert result.name == "Test Facility"
        assert result.parent_siren == "123456782"
        assert result.nic is None
        assert result.creation_date is None
        assert result.is_headquarters is False  # UNSET defaults to False
        assert result.employee_band is None
        assert result.employee_band_year is None
        assert result.search_score is None
        assert result.diffusion_status is None
        assert result.crafts_activity is None
        assert result.last_update is None
        assert result.period_count is None

    def test_transform_etablissement_with_mixed_unset_and_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test facility transformation with mix of UNSET and actual values."""
        # Create a mock period with the facility name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = "Test Facility"
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale for company name fallback
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = "Test Company"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]

        # Mix of UNSET and actual values
        mock_facility.nic = "001"
        mock_facility.date_creation_etablissement = date(2020, 1, 1)
        mock_facility.etablissement_siege = True
        mock_facility.tranche_effectifs_etablissement = UNSET
        mock_facility.annee_effectifs_etablissement = 2023
        mock_facility.score = 0.95
        mock_facility.statut_diffusion_etablissement = UNSET
        mock_facility.activite_principale_registre_metiers_etablissement = "12345"
        mock_facility.date_dernier_traitement_etablissement = "2023-12-01T10:00:00"
        mock_facility.nombre_periodes_etablissement = UNSET

        result = transformer.transform_etablissement(mock_facility)

        assert isinstance(result, FacilityData)
        assert result.name == "Test Facility"
        assert result.nic == "001"
        assert result.creation_date == date(2020, 1, 1)
        assert result.is_headquarters is True
        assert result.employee_band is None  # UNSET
        assert result.employee_band_year == 2023
        assert result.search_score == 0.95
        assert result.diffusion_status is None  # UNSET
        assert result.crafts_activity == "12345"
        assert result.last_update is not None
        assert result.period_count is None  # UNSET

    def test_transform_address_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test address transformation with UNSET values."""
        mock_address = MagicMock()

        # Set all fields to UNSET
        mock_address.code_pays_etranger_etablissement = UNSET
        mock_address.libelle_commune_etablissement = UNSET
        mock_address.code_postal_etablissement = UNSET
        mock_address.numero_voie_etablissement = UNSET
        mock_address.indice_repetition_etablissement = UNSET
        mock_address.type_voie_etablissement = UNSET
        mock_address.libelle_voie_etablissement = UNSET
        mock_address.coordonnee_lambert_abscisse_etablissement = UNSET
        mock_address.coordonnee_lambert_ordonnee_etablissement = UNSET
        mock_address.coordonnees_etablissement = None  # No coordinates

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"

        result = transformer.transform_address(
            mock_address, mock_facility, date(2020, 1, 1)
        )

        assert isinstance(result, AddressData)
        assert result.facility_siret == "12345678200001"
        assert result.country == "FR"  # Default when UNSET
        assert result.locality is None
        assert result.postal_code is None
        assert result.street_address is None
        assert result.longitude is None
        assert result.latitude is None

    def test_transform_address_with_mixed_unset_and_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test address transformation with mix of UNSET and actual values."""
        mock_address = MagicMock()

        # Mix of UNSET and actual values
        mock_address.code_pays_etranger_etablissement = UNSET
        mock_address.libelle_commune_etablissement = "Paris"
        mock_address.code_postal_etablissement = "75001"
        mock_address.numero_voie_etablissement = "123"
        mock_address.indice_repetition_etablissement = UNSET
        mock_address.type_voie_etablissement = "RUE"
        mock_address.libelle_voie_etablissement = UNSET
        mock_address.coordonnee_lambert_abscisse_etablissement = 652345.0
        mock_address.coordonnee_lambert_ordonnee_etablissement = 6862275.0

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"

        with patch(
            "sirene_api_client.etl.transformer.lambert93_to_wgs84",
            return_value=(2.3522, 48.8566),
        ):
            result = transformer.transform_address(
                mock_address, mock_facility, date(2020, 1, 1)
            )

        assert isinstance(result, AddressData)
        assert result.facility_siret == "12345678200001"
        assert result.country == "FR"  # Default when UNSET
        assert result.locality == "Paris"
        assert result.postal_code == "75001"
        assert result.street_address == "123 RUE"  # Only non-UNSET parts
        assert result.longitude == 2.3522
        assert result.latitude == 48.8566

    def test_parse_boolean_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test boolean parsing with UNSET values."""
        assert transformer._parse_boolean(UNSET) is False
        assert transformer._parse_boolean(None) is False
        assert transformer._parse_boolean("O") is True
        assert transformer._parse_boolean("N") is False
        assert transformer._parse_boolean("") is False
        assert transformer._parse_boolean("true") is False  # Only "O" is True

    def test_parse_datetime_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test datetime parsing with UNSET values."""
        assert transformer._parse_datetime(UNSET) is None
        assert transformer._parse_datetime(None) is None
        assert transformer._parse_datetime("") is None
        assert transformer._parse_datetime("2023-12-01T10:00:00") is not None
        assert transformer._parse_datetime("invalid-date") is None

    def test_transform_legal_unit_period_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test legal unit period transformation with UNSET values."""
        mock_period = MagicMock()
        mock_period.date_debut = date(2020, 1, 1)
        mock_period.date_fin = UNSET
        mock_period.denomination_unite_legale = UNSET
        mock_period.categorie_juridique_unite_legale = UNSET
        mock_period.activite_principale_unite_legale = "6201Z"
        mock_period.nomenclature_activite_principale_unite_legale = MagicMock(
            value="NAFRev2"
        )
        mock_period.etat_administratif_unite_legale = MagicMock(value="A")
        mock_period.economie_sociale_solidaire_unite_legale = UNSET
        mock_period.societe_mission_unite_legale = UNSET

        result = transformer.transform_legal_unit_period(mock_period)

        assert isinstance(result, CompanyLegalUnitPeriodData)
        assert result.start == date(2020, 1, 1)
        assert result.end is None  # UNSET
        assert result.legal_name == ""  # UNSET defaults to empty string
        assert result.legal_form_code == ""  # UNSET defaults to empty string
        assert result.activity_code == "6201Z"
        assert result.status == "active"
        assert result.ess_flag is False  # UNSET defaults to False
        assert result.mission_company_flag is False  # UNSET defaults to False

    def test_transform_establishment_period_with_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test establishment period transformation with UNSET values."""
        mock_period = MagicMock()
        mock_period.date_debut = date(2020, 1, 1)
        mock_period.date_fin = UNSET
        mock_period.etat_administratif_etablissement = MagicMock(value="A")
        mock_period.activite_principale_etablissement = "6201Z"
        mock_period.nomenclature_activite_principale_etablissement = MagicMock(
            value="NAFRev2"
        )

        mock_facility = MagicMock()
        mock_facility.etablissement_siege = UNSET
        mock_facility.date_creation_etablissement = date(2020, 1, 1)

        result = transformer.transform_establishment_period(mock_period, mock_facility)

        assert isinstance(result, FacilityEstablishmentPeriodData)
        assert result.start == date(2020, 1, 1)
        assert result.end is None  # UNSET
        assert result.status == "active"
        assert result.activity_code == "6201Z"
        assert result.is_hq is False  # UNSET defaults to False
        assert result.opening_date == date(2020, 1, 1)

    def test_transform_complete_with_all_unset_values(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test complete transformation with all UNSET values."""
        # Create mock company with UNSET values
        mock_company_period = MagicMock()
        mock_company_period.denomination_unite_legale = "Test Company"
        mock_company_period.date_debut = "2020-01-01"
        mock_company_period.date_fin = None  # Current period
        mock_company_period.activite_principale_unite_legale = "6201Z"
        mock_company_period.nomenclature_activite_principale_unite_legale = "NAFRev2"

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.periodes_unite_legale = [mock_company_period]
        mock_company.date_creation_unite_legale = UNSET
        mock_company.sigle_unite_legale = UNSET
        mock_company.tranche_effectifs_unite_legale = UNSET
        mock_company.annee_effectifs_unite_legale = UNSET
        mock_company.categorie_entreprise = UNSET
        mock_company.annee_categorie_entreprise = UNSET
        mock_company.statut_diffusion_unite_legale = UNSET
        mock_company.unite_purgee_unite_legale = UNSET
        mock_company.date_dernier_traitement_unite_legale = UNSET
        mock_company.nombre_periodes_unite_legale = UNSET
        mock_company.identifiant_association_unite_legale = UNSET

        # Create mock facility with UNSET values
        mock_facility_period = MagicMock()
        mock_facility_period.denomination_usuelle_etablissement = "Test Facility"
        mock_facility_period.date_debut = "2020-01-01"
        mock_facility_period.date_fin = None  # Current period
        mock_facility_period.activite_principale_etablissement = "6201Z"
        mock_facility_period.nomenclature_activite_principale_etablissement = "NAFRev2"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.denomination_usuelle_etablissement = "Test Facility"
        mock_facility.periodes_etablissement = [mock_facility_period]
        mock_facility.nic = UNSET
        mock_facility.date_creation_etablissement = UNSET
        mock_facility.etablissement_siege = UNSET
        mock_facility.tranche_effectifs_etablissement = UNSET
        mock_facility.annee_effectifs_etablissement = UNSET
        mock_facility.score = UNSET
        mock_facility.statut_diffusion_etablissement = UNSET
        mock_facility.activite_principale_registre_metiers_etablissement = UNSET
        mock_facility.date_dernier_traitement_etablissement = UNSET
        mock_facility.nombre_periodes_etablissement = UNSET
        mock_facility.adresse_etablissement = None  # No address

        raw_data = {
            "company": mock_company,
            "facilities": [mock_facility],
            "extraction_metadata": {"siren": "123456782", "facility_count": 1},
        }

        with patch.object(transformer, "_create_registry_records", return_value=[]):
            result = transformer.transform_complete(raw_data)

        assert isinstance(result, SIRENExtractResult)
        assert result.company.name == "Test Company"
        assert result.company.acronym is None
        assert result.company.employee_band is None
        assert len(result.facilities) == 1
        assert result.facilities[0].name == "Test Facility"
        assert result.facilities[0].nic is None
        assert result.facilities[0].search_score is None
        assert result.facilities[0].crafts_activity is None
        assert len(result.addresses) == 0  # No address data

    def test_edge_case_empty_strings_vs_unset(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test handling of empty strings vs UNSET values."""
        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"
        mock_company.periodes_unite_legale = []

        # Empty strings should be preserved, UNSET should become None
        mock_company.date_creation_unite_legale = (
            None  # Use None instead of UNSET for date
        )
        mock_company.sigle_unite_legale = ""  # Empty string
        mock_company.tranche_effectifs_unite_legale = UNSET  # UNSET
        mock_company.annee_effectifs_unite_legale = None
        mock_company.categorie_entreprise = None  # Use None instead of MagicMock
        mock_company.annee_categorie_entreprise = None
        mock_company.statut_diffusion_unite_legale = ""  # Empty string
        mock_company.unite_purgee_unite_legale = UNSET  # UNSET
        mock_company.date_dernier_traitement_unite_legale = None
        mock_company.nombre_periodes_unite_legale = None
        mock_company.identifiant_association_unite_legale = ""  # Empty string

        result = transformer.transform_unite_legale(mock_company)

        assert result.acronym == ""  # Empty string preserved
        assert result.employee_band is None  # UNSET becomes None
        assert result.diffusion_status == ""  # Empty string preserved
        assert result.is_purged is None  # UNSET becomes None

    def test_edge_case_none_vs_unset(self, transformer: SIRENTransformer) -> None:
        """Test handling of None vs UNSET values."""
        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.denomination_usuelle_etablissement = "Test Facility"
        mock_facility.periodes_etablissement = []

        # None should be preserved, UNSET should become None
        mock_facility.nic = None  # None
        mock_facility.date_creation_etablissement = (
            None  # Use None instead of UNSET for date
        )
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None  # None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = UNSET  # UNSET
        mock_facility.statut_diffusion_etablissement = None  # None
        mock_facility.activite_principale_registre_metiers_etablissement = (
            UNSET  # UNSET
        )
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        result = transformer.transform_etablissement(mock_facility)

        assert result.nic is None  # None preserved
        assert result.search_score is None  # UNSET becomes None
        assert result.diffusion_status is None  # None preserved
        assert result.crafts_activity is None  # UNSET becomes None

    # ===== NEW TESTS FOR FACILITY NAME EXTRACTION LOGIC =====

    def test_extract_facility_name_prioritizes_establishment_specific_name(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test that establishment-specific names are prioritized over company name."""
        # Create mock period with establishment-specific name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = "Specific Facility Name"
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale with company name
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = "Company Name"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.nic = None
        mock_facility.date_creation_etablissement = None
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        with patch.object(
            transformer,
            "transform_facility_identifier",
            return_value=FacilityIdentifierData(
                scheme="siret",
                value="12345678200001",
                normalized_value="12345678200001",
                verified_at=datetime.now(),
            ),
        ):
            result = transformer.transform_etablissement(mock_facility)

        # Should use establishment-specific name, not company name
        assert result.name == "Specific Facility Name"

    def test_extract_facility_name_falls_back_to_company_name(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test that company name is used when establishment-specific name is not available."""
        # Create mock period without establishment-specific name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = None
        mock_period.enseigne_1_etablissement = None
        mock_period.enseigne_2_etablissement = None
        mock_period.enseigne_3_etablissement = None
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale with company name
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = "Company Name"

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.nic = None
        mock_facility.date_creation_etablissement = None
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        with patch.object(
            transformer,
            "transform_facility_identifier",
            return_value=FacilityIdentifierData(
                scheme="siret",
                value="12345678200001",
                normalized_value="12345678200001",
                verified_at=datetime.now(),
            ),
        ):
            result = transformer.transform_etablissement(mock_facility)

        # Should fall back to company name
        assert result.name == "Company Name"

    def test_extract_facility_name_handles_no_periods_and_no_company_name(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test facility name extraction when no periods and no company name."""
        # Create mock unite_legale without company name
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = None

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = []  # No periods
        mock_facility.adresse_etablissement = None
        mock_facility.nic = None
        mock_facility.date_creation_etablissement = None
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        with patch.object(
            transformer,
            "transform_facility_identifier",
            return_value=FacilityIdentifierData(
                scheme="siret",
                value="12345678200001",
                normalized_value="12345678200001",
                verified_at=datetime.now(),
            ),
        ):
            result = transformer.transform_etablissement(mock_facility)

        # Should fall back to "Unknown Facility"
        assert result.name == "Unknown Facility"

    def test_extract_facility_name_handles_unset_company_name(
        self, transformer: SIRENTransformer
    ) -> None:
        """Test facility name extraction when company name is UNSET."""
        # Create mock period without establishment-specific name
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = None
        mock_period.enseigne_1_etablissement = None
        mock_period.enseigne_2_etablissement = None
        mock_period.enseigne_3_etablissement = None
        mock_period.date_fin = None  # Current period

        # Create mock unite_legale with UNSET company name
        mock_unite_legale = MagicMock()
        mock_unite_legale.denomination_unite_legale = UNSET

        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.siren = "123456782"
        mock_facility.unite_legale = mock_unite_legale
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.nic = None
        mock_facility.date_creation_etablissement = None
        mock_facility.etablissement_siege = None
        mock_facility.tranche_effectifs_etablissement = None
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.score = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None

        with patch.object(
            transformer,
            "transform_facility_identifier",
            return_value=FacilityIdentifierData(
                scheme="siret",
                value="12345678200001",
                normalized_value="12345678200001",
                verified_at=datetime.now(),
            ),
        ):
            result = transformer.transform_etablissement(mock_facility)

        # Should fall back to "Unknown Facility" when company name is UNSET
        assert result.name == "Unknown Facility"
