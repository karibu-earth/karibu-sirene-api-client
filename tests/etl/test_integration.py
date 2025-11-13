"""
Integration tests for ETL service.

Tests cover:
- End-to-end extraction and transformation
- Real API integration (with mocked responses)
- Complete data flow validation
- Error handling scenarios
- Performance characteristics
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.etl import (
    ETLConfig,
    SIRENExtractResult,
    ValidationMode,
    extract_and_transform_siren,
)
from sirene_api_client.etl.exceptions import ExtractionError


class TestETLIntegration:
    """Test end-to-end ETL functionality."""

    def _create_mock_company(self, sample_company_data: dict[str, Any]) -> MagicMock:
        """Create properly configured mock company."""
        mock_company = MagicMock()
        mock_company.siren = sample_company_data["siren"]
        mock_company.denomination_unite_legale = sample_company_data[
            "denomination_unite_legale"
        ]
        mock_company.periodes_unite_legale = [
            MagicMock(**period)
            for period in sample_company_data["periodes_unite_legale"]
        ]
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
        mock_company.to_dict = MagicMock(return_value={})
        return mock_company

    def _create_mock_facilities(
        self, sample_facility_data: list[dict[str, Any]]
    ) -> list[MagicMock]:
        """Create properly configured mock facilities."""
        mock_facilities = []
        for facility_data in sample_facility_data:
            mock_facility = MagicMock()
            mock_facility.siret = facility_data["siret"]
            mock_facility.siren = facility_data["siren"]
            mock_facility.denomination_usuelle_etablissement = facility_data[
                "denomination_usuelle_etablissement"
            ]
            mock_facility.periodes_etablissement = [
                MagicMock(**period)
                for period in facility_data["periodes_etablissement"]
            ]
            mock_facility.adresse_etablissement = (
                MagicMock(**facility_data["adresse_etablissement"])
                if facility_data.get("adresse_etablissement")
                else None
            )
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
            mock_facility.to_dict = MagicMock(return_value={})
            mock_facilities.append(mock_facility)
        return mock_facilities

    @pytest.fixture
    def mock_client(self) -> AuthenticatedClient:
        """Create a mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        return client

    @pytest.fixture
    def config(self) -> ETLConfig:
        """Create default ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    @pytest.fixture
    def sample_company_data(self) -> dict[str, Any]:
        """Create sample company data for testing."""
        return {
            "siren": "123456782",
            "denomination_unite_legale": "Test Company SARL",
            "periodes_unite_legale": [
                {
                    "date_debut": "2020-01-01",
                    "date_fin": None,
                    "denomination_unite_legale": "Test Company SARL",
                    "etat_administratif_unite_legale": "A",
                    "activite_principale_unite_legale": "6201Z",
                    "nomenclature_activite_principale_unite_legale": {
                        "value": "NAFRev2"
                    },
                    "categorie_juridique_unite_legale": "5710",
                    "economie_sociale_solidaire_unite_legale": None,
                    "societe_mission_unite_legale": None,
                }
            ],
        }

    @pytest.fixture
    def sample_facility_data(self) -> list[dict[str, Any]]:
        """Create sample facility data for testing."""
        return [
            {
                "siret": "12345678200001",
                "denomination_usuelle_etablissement": "Test Facility 1",
                "siren": "123456782",
                "periodes_etablissement": [
                    {
                        "date_debut": "2020-01-01",
                        "date_fin": None,
                        "denomination_usuelle_etablissement": "Test Facility 1",
                        "etat_administratif_etablissement": "A",
                        "activite_principale_etablissement": "6201Z",
                        "nomenclature_activite_principale_etablissement": {
                            "value": "NAFRev2"
                        },
                    }
                ],
                "adresse_etablissement": {
                    "numero_voie_etablissement": "123",
                    "type_voie_etablissement": "RUE",
                    "libelle_voie_etablissement": "MAIN STREET",
                    "code_postal_etablissement": "75001",
                    "libelle_commune_etablissement": "PARIS",
                    "code_pays_etranger_etablissement": None,
                    "coordonnees_etablissement": {
                        "latitude": "4868566",
                        "longitude": "235220",
                    },
                },
            },
            {
                "siret": "12345678200002",
                "denomination_usuelle_etablissement": "Test Facility 2",
                "siren": "123456782",
                "periodes_etablissement": [
                    {
                        "date_debut": "2020-01-01",
                        "date_fin": None,
                        "denomination_usuelle_etablissement": "Test Facility 2",
                        "etat_administratif_etablissement": "A",
                        "activite_principale_etablissement": "6202Z",
                        "nomenclature_activite_principale_etablissement": {
                            "value": "NAFRev2"
                        },
                    }
                ],
                "adresse_etablissement": {
                    "numero_voie_etablissement": "456",
                    "type_voie_etablissement": "AVENUE",
                    "libelle_voie_etablissement": "SECOND STREET",
                    "code_postal_etablissement": "75002",
                    "libelle_commune_etablissement": "PARIS",
                    "code_pays_etranger_etablissement": None,
                    "coordonnees_etablissement": {
                        "latitude": "4869000",
                        "longitude": "235500",
                    },
                },
            },
        ]

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_success(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
        sample_company_data: dict[str, Any],
        sample_facility_data: list[dict[str, Any]],
    ) -> None:
        """Test successful end-to-end extraction and transformation."""
        # Mock API responses
        mock_company_response = MagicMock()
        mock_company = self._create_mock_company(sample_company_data)
        mock_company_response.unite_legale = mock_company

        mock_facility_response = MagicMock()
        mock_facilities = self._create_mock_facilities(sample_facility_data)
        mock_facility_response.etablissements = mock_facilities
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = len(mock_facilities)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
            patch(
                "sirene_api_client.etl.transformer.lambert93_to_wgs84",
                return_value=(2.3522, 48.8566),
            ),
        ):
            result = await extract_and_transform_siren("123456782", mock_client, config)

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company SARL"
            assert len(result.facilities) == 2
            assert result.facilities[0].name == "Test Facility 1"
            assert result.facilities[1].name == "Test Facility 2"
            assert result.extraction_metadata["siren"] == "123456782"
            assert result.extraction_metadata["facility_count"] == 2

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_with_coordinate_conversion(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
        sample_company_data: dict[str, Any],
        sample_facility_data: list[dict[str, Any]],
    ) -> None:
        """Test extraction and transformation with coordinate conversion."""
        # Mock API responses
        mock_company_response = MagicMock()
        mock_company = self._create_mock_company(sample_company_data)
        mock_company_response.unite_legale = mock_company

        mock_facility_response = MagicMock()
        mock_facilities = self._create_mock_facilities(sample_facility_data)
        mock_facility_response.etablissements = mock_facilities
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = len(mock_facilities)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
            patch(
                "sirene_api_client.etl.transformer.lambert93_to_wgs84",
                return_value=(2.3522, 48.8566),
            ) as mock_coord,
        ):
            result = await extract_and_transform_siren("123456782", mock_client, config)

            # Verify coordinate conversion was called
            assert mock_coord.call_count == 2  # Called for each facility

            # Verify addresses have coordinates
            assert len(result.addresses) == 2
            assert result.addresses[0].longitude == 2.3522
            assert result.addresses[0].latitude == 48.8566
            assert result.addresses[1].longitude == 2.3522
            assert result.addresses[1].latitude == 48.8566

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_with_default_config(
        self,
        mock_client: AuthenticatedClient,
        sample_company_data: dict[str, Any],
        sample_facility_data: list[dict[str, Any]],
    ) -> None:
        """Test extraction and transformation with default configuration."""
        # Mock API responses
        mock_company_response = MagicMock()
        mock_company_response.unite_legale = self._create_mock_company(
            sample_company_data
        )

        mock_facility_response = MagicMock()
        mock_facility_response.etablissements = self._create_mock_facilities(
            sample_facility_data
        )
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = len(sample_facility_data)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
            patch(
                "sirene_api_client.etl.transformer.lambert93_to_wgs84",
                return_value=(2.3522, 48.8566),
            ),
        ):
            # Call without config (should use default)
            result = await extract_and_transform_siren("123456782", mock_client)

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company SARL"
            assert len(result.facilities) == 2

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_invalid_siren(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test extraction and transformation with invalid SIREN."""
        with pytest.raises(ValueError, match="Invalid SIREN format"):
            await extract_and_transform_siren("invalid", mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_empty_siren(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test extraction and transformation with empty SIREN."""
        with pytest.raises(ValueError, match="Invalid SIREN format"):
            await extract_and_transform_siren("", mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_wrong_length(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test extraction and transformation with wrong SIREN length."""
        with pytest.raises(ValueError, match="Invalid SIREN format"):
            await extract_and_transform_siren(
                "12345678", mock_client, config
            )  # 8 digits instead of 9

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_api_error(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
    ) -> None:
        """Test extraction and transformation with API error."""
        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                side_effect=Exception("API Error"),
            ),
            pytest.raises(ExtractionError),
        ):
            await extract_and_transform_siren("123456782", mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_no_company_data(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
    ) -> None:
        """Test extraction and transformation with no company data."""
        mock_company_response = MagicMock()
        mock_company_response.unite_legale = None

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            pytest.raises(ExtractionError, match="No company data found"),
        ):
            await extract_and_transform_siren("123456782", mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_no_facilities(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
        sample_company_data: dict[str, Any],
    ) -> None:
        """Test extraction and transformation with no facilities."""
        # Mock API responses
        mock_company_response = MagicMock()
        mock_company_response.unite_legale = self._create_mock_company(
            sample_company_data
        )

        mock_facility_response = MagicMock()
        mock_facility_response.etablissements = None
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = 0

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
        ):
            result = await extract_and_transform_siren("123456782", mock_client, config)

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company SARL"
            assert len(result.facilities) == 0
            assert result.extraction_metadata["facility_count"] == 0

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_large_dataset(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
        sample_company_data: dict[str, Any],
    ) -> None:
        """Test extraction and transformation with large dataset."""
        # Create many facilities
        facilities = []
        for i in range(100):
            facility_data = {
                "siret": f"123456782{i:05d}",
                "denomination_usuelle_etablissement": f"Test Facility {i}",
                "siren": "123456782",
                "periodes_etablissement": [
                    {
                        "date_debut": "2020-01-01",
                        "date_fin": None,
                        "denomination_usuelle_etablissement": f"Test Facility {i}",
                        "etat_administratif_etablissement": "A",
                        "activite_principale_etablissement": "6201Z",
                        "nomenclature_activite_principale_etablissement": {
                            "value": "NAFRev2"
                        },
                    }
                ],
                "adresse_etablissement": {
                    "numero_voie_etablissement": str(i + 1),
                    "type_voie_etablissement": "RUE",
                    "libelle_voie_etablissement": f"STREET {i}",
                    "code_postal_etablissement": "75001",
                    "libelle_commune_etablissement": "PARIS",
                    "code_pays_etranger_etablissement": None,
                    "coordonnees_etablissement": {
                        "latitude": f"4868566{i:03d}",
                        "longitude": f"235220{i:03d}",
                    },
                },
            }
            facilities.append(facility_data)

        # Mock API responses
        mock_company_response = MagicMock()
        mock_company_response.unite_legale = self._create_mock_company(
            sample_company_data
        )

        mock_facility_response = MagicMock()
        mock_facility_response.etablissements = self._create_mock_facilities(facilities)
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = 100  # Total facilities available

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
            patch(
                "sirene_api_client.etl.transformer.lambert93_to_wgs84",
                return_value=(2.3522, 48.8566),
            ),
        ):
            result = await extract_and_transform_siren("123456782", mock_client, config)

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company SARL"
            assert len(result.facilities) == 100
            assert result.extraction_metadata["facility_count"] == 100
            assert len(result.addresses) == 100

    def test_etl_config_validation_modes(self) -> None:
        """Test different validation modes."""
        strict_config = ETLConfig(validation_mode=ValidationMode.STRICT)
        lenient_config = ETLConfig(validation_mode=ValidationMode.LENIENT)
        permissive_config = ETLConfig(validation_mode=ValidationMode.PERMISSIVE)

        assert strict_config.validation_mode == ValidationMode.STRICT
        assert lenient_config.validation_mode == ValidationMode.LENIENT
        assert permissive_config.validation_mode == ValidationMode.PERMISSIVE

    @pytest.mark.asyncio
    async def test_extract_and_transform_siren_performance(
        self,
        mock_client: AuthenticatedClient,
        config: ETLConfig,
        sample_company_data: dict[str, Any],
        sample_facility_data: list[dict[str, Any]],
    ) -> None:
        """Test ETL performance characteristics."""
        import time

        # Mock API responses
        mock_company_response = MagicMock()
        mock_company_response.unite_legale = self._create_mock_company(
            sample_company_data
        )

        mock_facility_response = MagicMock()
        mock_facility_response.etablissements = self._create_mock_facilities(
            sample_facility_data
        )
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = len(sample_facility_data)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=mock_company_response,
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
            patch(
                "sirene_api_client.etl.transformer.lambert93_to_wgs84",
                return_value=(2.3522, 48.8566),
            ),
        ):
            start_time = time.time()

            result = await extract_and_transform_siren("123456782", mock_client, config)

            end_time = time.time()
            duration = end_time - start_time

            # Should complete in reasonable time (less than 1 second for mocked data)
            assert duration < 1.0
            assert isinstance(result, SIRENExtractResult)


class TestProgressAwareETL:
    """Test progress-aware ETL functionality."""

    @pytest.fixture
    def mock_client(self) -> AuthenticatedClient:
        """Create a mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        return client

    @pytest.fixture
    def config(self) -> ETLConfig:
        """Create default ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    def _create_mock_company(self) -> MagicMock:
        """Create mock company data."""
        # Create a mock legal period
        mock_period = MagicMock()
        mock_period.date_debut = "2020-01-01"
        mock_period.date_fin = None  # No end date - current period
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.sigle_unite_legale = None
        mock_period.denomination_usuelle1_unite_legale = None
        mock_period.denomination_usuelle2_unite_legale = None
        mock_period.denomination_usuelle3_unite_legale = None
        mock_period.categorie_juridique_unite_legale = None
        mock_period.activite_principale_unite_legale = "6201Z"
        mock_period.nomenclature_activite_principale_unite_legale = "NAFRev2"
        mock_period.caractere_employeur_unite_legale = None

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"
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
        mock_company.to_dict = MagicMock(return_value={})
        return mock_company

    def _create_mock_facility(self, siret: str, name: str) -> MagicMock:
        """Create mock facility data."""
        # Create a mock period with the facility name and activity data
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = name
        mock_period.date_fin = None  # Current period
        mock_period.date_debut = "2020-01-01"  # Start date
        mock_period.activite_principale_etablissement = "6201Z"
        mock_period.nomenclature_activite_principale_etablissement = "NAFRev2"

        mock_facility = MagicMock()
        mock_facility.siret = siret
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.date_creation_etablissement = None
        mock_facility.date_debut_activite = None
        mock_facility.date_fermeture_etablissement = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.unite_purgee_unite_legale = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None
        # Set required fields for transformer
        mock_facility.siren = siret[:9]  # Extract SIREN from SIRET
        mock_facility.nic = "00001"
        mock_facility.tranche_effectifs_etablissement = "00"
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.etablissement_siege = False
        mock_facility.score = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.to_dict = MagicMock(return_value={})
        return mock_facility

    @pytest.mark.asyncio
    async def test_progress_callback_invoked_at_each_phase(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test that progress callback is invoked at each phase."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        # Create mock data
        mock_company = self._create_mock_company()
        mock_facility1 = self._create_mock_facility("12345678200001", "Facility 1")
        mock_facility2 = self._create_mock_facility("12345678200002", "Facility 2")

        # Track progress updates
        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=MagicMock(
                    etablissements=[mock_facility1, mock_facility2],
                    header=MagicMock(total=2),
                ),
            ),
        ):
            result = await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            # Should have received progress updates
            assert (
                len(progress_updates) >= 3
            )  # At least company_extracted, facilities_processing, completed

            # Check first update (company extracted)
            company_update = progress_updates[0]
            assert company_update["phase"] == "company_extracted"
            assert company_update["company_name"] == "Test Company"
            assert company_update["siren"] == "123456782"
            assert company_update["processed_facilities"] == 0

            # Check final update (completed)
            completed_update = progress_updates[-1]
            assert completed_update["phase"] == "completed"
            assert completed_update["company_name"] == "Test Company"
            assert completed_update["siren"] == "123456782"
            assert completed_update["processed_facilities"] == 2
            assert completed_update["total_facilities"] == 2

            # Verify result
            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company"
            assert len(result.facilities) == 2

    @pytest.mark.asyncio
    async def test_progress_callback_correct_data_structure(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test that progress callback receives correct data structure."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        mock_company = self._create_mock_company()
        mock_facility = self._create_mock_facility("12345678200001", "Test Facility")

        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=MagicMock(
                    etablissements=[mock_facility], header=MagicMock(total=1)
                ),
            ),
        ):
            await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            # Check data structure of progress updates
            for update in progress_updates:
                assert "phase" in update
                assert "siren" in update
                assert "company_name" in update
                assert "processed_facilities" in update
                assert "total_facilities" in update

                assert update["phase"] in [
                    "company_extracted",
                    "facilities_processing",
                    "completed",
                ]
                assert update["siren"] == "123456782"
                assert update["company_name"] == "Test Company"
                assert isinstance(update["processed_facilities"], int)
                assert isinstance(update["total_facilities"], int)

    @pytest.mark.asyncio
    async def test_progress_callback_error_handling(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test progress callback with error handling."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with patch(
            "sirene_api_client.etl.extractor.find_by_siren",
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await extract_and_transform_siren_with_progress(
                    "123456782",
                    mock_client,
                    config,
                    progress_callback=progress_callback,
                )

            # Should have received error update
            assert len(progress_updates) >= 1
            error_update = progress_updates[-1]
            assert error_update["phase"] == "error"
            assert error_update["siren"] == "123456782"
            assert "error" in error_update

    @pytest.mark.asyncio
    async def test_progress_callback_with_none(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test progress callback with None (no callback)."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        mock_company = self._create_mock_company()
        mock_facility = self._create_mock_facility("12345678200001", "Test Facility")

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=MagicMock(
                    etablissements=[mock_facility], header=MagicMock(total=1)
                ),
            ),
        ):
            # Should work without errors when callback is None
            result = await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=None
            )

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company"

    @pytest.mark.asyncio
    async def test_progress_data_accuracy(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test that progress data is accurate."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        mock_company = self._create_mock_company()
        mock_facilities = [
            self._create_mock_facility("12345678200001", "Facility 1"),
            self._create_mock_facility("12345678200002", "Facility 2"),
            self._create_mock_facility("12345678200003", "Facility 3"),
        ]

        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=MagicMock(
                    etablissements=mock_facilities, header=MagicMock(total=3)
                ),
            ),
        ):
            await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            # Check facility processing updates
            facility_updates = [
                u for u in progress_updates if u["phase"] == "facilities_processing"
            ]
            assert len(facility_updates) == 3  # One for each facility

            # Check that counts are accurate
            for i, update in enumerate(facility_updates):
                assert update["processed_facilities"] == i + 1
                assert update["total_facilities"] == 3
                assert update["latest_facility"] == f"Facility {i + 1}"

            # Check final update
            final_update = progress_updates[-1]
            assert final_update["phase"] == "completed"
            assert final_update["processed_facilities"] == 3
            assert final_update["total_facilities"] == 3


class TestCompanyOnlyExtraction:
    """Test company-only extraction functionality."""

    @pytest.fixture
    def mock_client(self) -> AuthenticatedClient:
        """Create a mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        return client

    @pytest.fixture
    def config(self) -> ETLConfig:
        """Create default ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    def _create_mock_company(self) -> MagicMock:
        """Create mock company data."""
        # Create a mock legal period
        mock_period = MagicMock()
        mock_period.date_debut = "2020-01-01"
        mock_period.date_fin = None  # No end date - current period
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.sigle_unite_legale = None
        mock_period.denomination_usuelle1_unite_legale = None
        mock_period.denomination_usuelle2_unite_legale = None
        mock_period.denomination_usuelle3_unite_legale = None
        mock_period.categorie_juridique_unite_legale = None
        mock_period.activite_principale_unite_legale = "6201Z"
        mock_period.nomenclature_activite_principale_unite_legale = "NAFRev2"
        mock_period.caractere_employeur_unite_legale = None

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"
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
        mock_company.to_dict = MagicMock(return_value={})
        return mock_company

    @pytest.mark.asyncio
    async def test_extract_company_only_success(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test successful company-only extraction."""
        from sirene_api_client.etl import extract_company_only

        mock_company = self._create_mock_company()
        mock_facility_response = MagicMock()
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = 5

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ) as mock_company_api,
            patch(
                "sirene_api_client.etl.find_by_post_etablissement",
                return_value=mock_facility_response,
            ) as mock_facility_api,
        ):
            company_data, facility_count = await extract_company_only(
                "123456782", mock_client, config
            )

            # Verify company data
            assert company_data.name == "Test Company"
            assert company_data.identifiers[0].value == "123456782"

            # Verify facility count
            assert facility_count == 5

            # Verify API calls
            mock_company_api.assert_called_once()
            mock_facility_api.assert_called_once()

    @pytest.mark.asyncio
    async def test_extract_company_only_no_facilities(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test company-only extraction with no facilities."""
        from sirene_api_client.etl import extract_company_only

        mock_company = self._create_mock_company()
        mock_facility_response = MagicMock()
        mock_facility_response.header = MagicMock()
        mock_facility_response.header.total = 0

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.find_by_post_etablissement",
                return_value=mock_facility_response,
            ),
        ):
            company_data, facility_count = await extract_company_only(
                "123456782", mock_client, config
            )

            # Verify company data
            assert company_data.name == "Test Company"

            # Verify facility count
            assert facility_count == 0

    @pytest.mark.asyncio
    async def test_extract_company_only_api_error(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test company-only extraction with API error."""
        from sirene_api_client.etl import extract_company_only

        with patch(
            "sirene_api_client.etl.extractor.find_by_siren",
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error") as exc_info:
                await extract_company_only("123456782", mock_client, config)

            assert "Failed to extract company data for SIREN 123456782" in str(
                exc_info.value
            )

    @pytest.mark.asyncio
    async def test_extract_company_only_facility_count_error(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test company-only extraction with facility count API error."""
        from sirene_api_client.etl import extract_company_only

        mock_company = self._create_mock_company()

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.find_by_post_etablissement",
                side_effect=Exception("Facility API Error"),
            ),
        ):
            company_data, facility_count = await extract_company_only(
                "123456782", mock_client, config
            )

            # Should still return company data but with 0 facility count
            assert company_data.name == "Test Company"
            assert facility_count == 0

    @pytest.mark.asyncio
    async def test_extract_company_only_invalid_siren(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test company-only extraction with invalid SIREN."""
        from sirene_api_client.etl import extract_company_only

        with pytest.raises(ValueError, match=r".*") as exc_info:
            await extract_company_only("invalid", mock_client, config)

        assert "Invalid SIREN format: invalid. Must be 9 digits." in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_extract_company_only_facility_count_accuracy(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test that facility count is accurate."""
        from sirene_api_client.etl import extract_company_only

        mock_company = self._create_mock_company()

        # Test different facility counts
        test_cases = [0, 1, 100, 1000, 5000]

        for expected_count in test_cases:
            mock_facility_response = MagicMock()
            mock_facility_response.header = MagicMock()
            mock_facility_response.header.total = expected_count

            with (
                patch(
                    "sirene_api_client.etl.extractor.find_by_siren",
                    return_value=MagicMock(unite_legale=mock_company),
                ),
                patch(
                    "sirene_api_client.etl.find_by_post_etablissement",
                    return_value=mock_facility_response,
                ),
            ):
                company_data, facility_count = await extract_company_only(
                    "123456782", mock_client, config
                )

                assert facility_count == expected_count
                assert company_data.name == "Test Company"


class TestStreamingWorkflowIntegration:
    """Test complete streaming workflow integration."""

    @pytest.fixture
    def mock_client(self) -> AuthenticatedClient:
        """Create a mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        return client

    @pytest.fixture
    def config(self) -> ETLConfig:
        """Create default ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    def _create_mock_company(self) -> MagicMock:
        """Create mock company data."""
        # Create a mock legal period
        mock_period = MagicMock()
        mock_period.date_debut = "2020-01-01"
        mock_period.date_fin = None  # No end date - current period
        mock_period.denomination_unite_legale = "Test Company"
        mock_period.sigle_unite_legale = None
        mock_period.denomination_usuelle1_unite_legale = None
        mock_period.denomination_usuelle2_unite_legale = None
        mock_period.denomination_usuelle3_unite_legale = None
        mock_period.categorie_juridique_unite_legale = None
        mock_period.activite_principale_unite_legale = "6201Z"
        mock_period.nomenclature_activite_principale_unite_legale = "NAFRev2"
        mock_period.caractere_employeur_unite_legale = None

        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"
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
        mock_company.to_dict = MagicMock(return_value={})
        return mock_company

    def _create_mock_facility(self, siret: str, name: str) -> MagicMock:
        """Create mock facility data."""
        # Create a mock period with the facility name and activity data
        mock_period = MagicMock()
        mock_period.denomination_usuelle_etablissement = name
        mock_period.date_fin = None  # Current period
        mock_period.date_debut = "2020-01-01"  # Start date
        mock_period.activite_principale_etablissement = "6201Z"
        mock_period.nomenclature_activite_principale_etablissement = "NAFRev2"

        mock_facility = MagicMock()
        mock_facility.siret = siret
        mock_facility.periodes_etablissement = [mock_period]
        mock_facility.adresse_etablissement = None
        mock_facility.date_creation_etablissement = None
        mock_facility.date_debut_activite = None
        mock_facility.date_fermeture_etablissement = None
        mock_facility.statut_diffusion_etablissement = None
        mock_facility.unite_purgee_unite_legale = None
        mock_facility.date_dernier_traitement_etablissement = None
        mock_facility.nombre_periodes_etablissement = None
        # Set required fields for transformer
        mock_facility.siren = siret[:9]  # Extract SIREN from SIRET
        mock_facility.nic = "00001"
        mock_facility.tranche_effectifs_etablissement = "00"
        mock_facility.annee_effectifs_etablissement = None
        mock_facility.etablissement_siege = False
        mock_facility.score = None
        mock_facility.activite_principale_registre_metiers_etablissement = None
        mock_facility.to_dict = MagicMock(return_value={})
        return mock_facility

    @pytest.mark.asyncio
    async def test_full_streaming_etl_workflow(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test complete streaming ETL workflow with progress tracking."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        # Create mock data for large dataset (simulate 2500 facilities)
        mock_company = self._create_mock_company()

        # Create facilities for 3 pages (1000 + 1000 + 500)
        mock_facilities_page1 = [
            self._create_mock_facility(f"123456782{i:05d}", f"Facility {i}")
            for i in range(1000)
        ]
        mock_facilities_page2 = [
            self._create_mock_facility(
                f"123456782{i + 1000:05d}", f"Facility {i + 1000}"
            )
            for i in range(1000)
        ]
        mock_facilities_page3 = [
            self._create_mock_facility(
                f"123456782{i + 2000:05d}", f"Facility {i + 2000}"
            )
            for i in range(500)
        ]

        # Track progress updates
        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ) as mock_company_api,
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                side_effect=[
                    MagicMock(
                        etablissements=mock_facilities_page1,
                        header=MagicMock(total=2500),
                    ),
                    MagicMock(
                        etablissements=mock_facilities_page2,
                        header=MagicMock(total=2500),
                    ),
                    MagicMock(
                        etablissements=mock_facilities_page3,
                        header=MagicMock(total=2500),
                    ),
                ],
            ) as mock_facility_api,
        ):
            result = await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            # Verify result
            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company"
            assert len(result.facilities) == 2500

            # Verify progress updates
            assert (
                len(progress_updates) >= 2502
            )  # company_extracted + 2500 facilities + completed

            # Check phases
            phases = [update["phase"] for update in progress_updates]
            assert "company_extracted" in phases
            assert "completed" in phases
            assert phases.count("facilities_processing") == 2500

            # Check final update
            final_update = progress_updates[-1]
            assert final_update["phase"] == "completed"
            assert final_update["processed_facilities"] == 2500
            assert final_update["total_facilities"] == 2500

            # Verify API calls
            mock_company_api.assert_called_once()
            assert mock_facility_api.call_count == 3  # 3 pages

    @pytest.mark.asyncio
    async def test_company_only_followed_by_full_extraction(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test company-only extraction followed by full extraction."""
        from sirene_api_client.etl import (
            extract_and_transform_siren_with_progress,
            extract_company_only,
        )

        mock_company = self._create_mock_company()
        mock_facilities = [self._create_mock_facility("12345678200001", "Facility 1")]

        # First: Extract company only
        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.find_by_post_etablissement",
                return_value=MagicMock(header=MagicMock(total=1)),
            ),
        ):
            company_data, facility_count = await extract_company_only(
                "123456782", mock_client, config
            )

            assert company_data.name == "Test Company"
            assert facility_count == 1

        # Second: Full extraction with progress
        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                return_value=MagicMock(
                    etablissements=mock_facilities, header=MagicMock(total=1)
                ),
            ),
        ):
            result = await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            assert isinstance(result, SIRENExtractResult)
            assert result.company.name == "Test Company"
            assert len(result.facilities) == 1

            # Should have received progress updates
            assert (
                len(progress_updates) >= 3
            )  # company_extracted + facilities_processing + completed

    @pytest.mark.asyncio
    async def test_large_dataset_handling(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test handling of large datasets (simulated)."""
        from sirene_api_client.etl import extract_and_transform_siren_with_progress

        mock_company = self._create_mock_company()

        # Simulate 10,000 facilities (10 pages)
        total_facilities = 10000
        page_size = 1000

        # Create mock responses for all pages
        mock_responses = []
        for page in range(10):
            facilities_in_page = min(page_size, total_facilities - page * page_size)
            mock_facilities = [
                self._create_mock_facility(
                    f"123456782{i + page * page_size:05d}",
                    f"Facility {i + page * page_size}",
                )
                for i in range(facilities_in_page)
            ]

            mock_response = MagicMock()
            mock_response.etablissements = mock_facilities
            mock_response.header = MagicMock()
            mock_response.header.total = total_facilities

            mock_responses.append(mock_response)

        progress_updates = []

        def progress_callback(update: dict[str, Any]) -> None:
            progress_updates.append(update)

        def mock_api_call(*_args, **_kwargs):
            if mock_responses:
                return mock_responses.pop(0)
            return None

        with (
            patch(
                "sirene_api_client.etl.extractor.find_by_siren",
                return_value=MagicMock(unite_legale=mock_company),
            ),
            patch(
                "sirene_api_client.etl.extractor.find_by_post_etablissement",
                side_effect=mock_api_call,
            ) as mock_facility_api,
        ):
            result = await extract_and_transform_siren_with_progress(
                "123456782", mock_client, config, progress_callback=progress_callback
            )

            # Verify result
            assert isinstance(result, SIRENExtractResult)
            assert len(result.facilities) == 10000

            # Verify progress updates
            assert (
                len(progress_updates) >= 10002
            )  # company_extracted + 10000 facilities + completed

            # Check that we processed all facilities
            facility_updates = [
                u for u in progress_updates if u["phase"] == "facilities_processing"
            ]
            assert len(facility_updates) == 10000

            # Check final update
            final_update = progress_updates[-1]
            assert final_update["processed_facilities"] == 10000
            assert final_update["total_facilities"] == 10000

            # Verify API calls
            assert (
                mock_facility_api.call_count == 11
            )  # 10 pages + 1 extra call to check for more
