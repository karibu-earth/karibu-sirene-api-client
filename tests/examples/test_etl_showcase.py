"""
Comprehensive tests for the ETL showcase script.

This module tests the complete ETL pipeline including name resolution,
progressive extraction, and JSON output generation.
"""

from __future__ import annotations

from datetime import date, datetime
import json
from pathlib import Path
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# Mock environment variable before importing the module
with patch.dict("os.environ", {"SIRENE_API_TOKEN": "test-token-123"}):
    from examples.etl_showcase import (
        CacheSimulator,
        NameToSIRENResolver,
        ProgressiveETLOrchestrator,
        generate_django_load_script,
        main,
    )

from sirene_api_client import AuthenticatedClient, ETLConfig, ValidationMode
from sirene_api_client.etl.models import SIRENExtractResult


@pytest.fixture(autouse=True)
def mock_api_token():
    """Mock SIRENE_API_TOKEN environment variable for all tests."""
    with patch.dict("os.environ", {"SIRENE_API_TOKEN": "test-token-123"}):
        yield


@pytest.mark.requirement("REQ-ETL-001")
@pytest.mark.example
class TestNameToSIRENResolver:
    """Test company name search and SIREN resolution."""

    @pytest.fixture
    def mock_client(self):
        """Mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        # Mock the API structure
        client.unite_legale = MagicMock()
        client.etablissement = MagicMock()
        return client

    @pytest.fixture
    def resolver(self, mock_client):
        """Create NameToSIRENResolver instance."""
        return NameToSIRENResolver(mock_client)

    @pytest.mark.asyncio
    async def test_search_company_by_name_success(self, resolver):
        """Test successful company name search."""
        # Mock API response
        mock_response = MagicMock()
        mock_response.etablissements = [
            MagicMock(
                siren="123456782",
                unite_legale=MagicMock(
                    denomination_unite_legale="TEST COMPANY",
                    etat_administratif_unite_legale="A",
                    categorie_juridique_unite_legale="5710",
                    date_creation_unite_legale=date(2020, 1, 1),
                ),
            ),
            MagicMock(
                siren="987654321",
                unite_legale=MagicMock(
                    denomination_unite_legale="TEST COMPANY SUBSIDIARY",
                    etat_administratif_unite_legale="A",
                    categorie_juridique_unite_legale="5710",
                    date_creation_unite_legale=date(2020, 1, 1),
                ),
            ),
        ]
        mock_response.header = MagicMock(total=7)  # Total facilities for both companies

        # Mock the API function directly
        with patch(
            "examples.etl_showcase.find_by_get_etablissement", new_callable=AsyncMock
        ) as mock_api:
            # First call returns establishments, second call returns facility count
            mock_api.side_effect = [
                mock_response,  # First call for name search
                MagicMock(
                    header=MagicMock(total=5)
                ),  # Second call for facility count (first company)
                MagicMock(
                    header=MagicMock(total=2)
                ),  # Third call for facility count (second company)
            ]

            results = await resolver.search_company_by_name("TEST COMPANY")

            assert len(results) == 2
            assert results[0].siren == "123456782"
            assert results[0].name == "TEST COMPANY"
            assert results[0].facility_count == 5
            assert results[0].is_active is True

    @pytest.mark.asyncio
    async def test_search_company_by_name_no_results(self, resolver):
        """Test company name search with no results."""
        mock_response = MagicMock()
        mock_response.etablissements = []

        with patch(
            "examples.etl_showcase.find_by_get_etablissement", new_callable=AsyncMock
        ) as mock_api:
            mock_api.return_value = mock_response

            results = await resolver.search_company_by_name("NONEXISTENT COMPANY")

            assert len(results) == 0

    @pytest.mark.asyncio
    async def test_search_company_by_name_api_error(self, resolver):
        """Test company name search with API error."""
        with patch(
            "examples.etl_showcase.find_by_get_etablissement", new_callable=AsyncMock
        ) as mock_api:
            mock_api.side_effect = Exception("API Error")

            with pytest.raises(Exception, match="API Error"):
                await resolver.search_company_by_name("TEST COMPANY")

    def test_validate_siren_format_valid(self, resolver):
        """Test SIREN format validation with valid input."""
        assert resolver.validate_siren_format("123456782") is True
        assert resolver.validate_siren_format("000000000") is True

    def test_validate_siren_format_invalid(self, resolver):
        """Test SIREN format validation with invalid input."""
        assert (
            resolver.validate_siren_format("12345678")  # pragma: allowlist secret
            is False
        )  # Too short
        assert (
            resolver.validate_siren_format("1234567820")  # pragma: allowlist secret
            is False
        )  # Too long
        assert (
            resolver.validate_siren_format("12345678a")  # pragma: allowlist secret
            is False
        )  # Non-numeric
        assert resolver.validate_siren_format("") is False  # Empty
        assert resolver.validate_siren_format("   ") is False  # Whitespace


@pytest.mark.requirement("REQ-ETL-002")
@pytest.mark.example
class TestProgressiveExtraction:
    """Test progressive facility extraction with batching."""

    @pytest.fixture
    def mock_client(self):
        """Mock SIRENE API client."""
        client = MagicMock(spec=AuthenticatedClient)
        # Mock the API structure
        client.unite_legale = MagicMock()
        client.etablissement = MagicMock()
        return client

    @pytest.fixture
    def config(self):
        """Create ETL configuration."""
        return ETLConfig(validation_mode=ValidationMode.LENIENT)

    @pytest.fixture
    def orchestrator(self, mock_client, config):
        """Create ProgressiveETLOrchestrator instance."""
        return ProgressiveETLOrchestrator(mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_with_progress_success(self, orchestrator):
        """Test successful progressive extraction."""
        # Mock the transformer to avoid complex validation
        with patch.object(
            orchestrator.transformer, "transform_complete"
        ) as mock_transform:
            mock_result = MagicMock()
            mock_result.company.name = "TEST COMPANY"
            mock_result.facilities = [MagicMock()]
            mock_transform.return_value = mock_result

            # Mock the extractor methods directly
            with (
                patch.object(
                    orchestrator.extractor, "_extract_company", new_callable=AsyncMock
                ) as mock_extract_company,
                patch.object(
                    orchestrator.extractor, "extract_facilities_streaming"
                ) as mock_streaming,
            ):
                mock_extract_company.return_value = MagicMock()

                # Mock streaming to return facilities
                async def mock_stream_generator():
                    yield [MagicMock()], 1

                mock_streaming.return_value = mock_stream_generator()

                progress_updates = []

                def progress_callback(update):
                    progress_updates.append(update)

                result = await orchestrator.extract_with_progress(
                    "123456782", progress_callback
                )

                assert result.company.name == "TEST COMPANY"
                assert len(result.facilities) == 1
                assert len(progress_updates) > 0

                # Check progress updates
                assert any(
                    update["phase"] == "company_extracted"
                    for update in progress_updates
                )
                assert any(
                    update["phase"] == "facilities_extracted"
                    for update in progress_updates
                )

    @pytest.mark.asyncio
    async def test_extract_with_progress_large_dataset(self, orchestrator):
        """Test progressive extraction with large facility count."""
        # Mock the transformer to avoid complex validation
        with patch.object(
            orchestrator.transformer, "transform_complete"
        ) as mock_transform:
            mock_transform.return_value = MagicMock(
                company=MagicMock(name="LARGE COMPANY"),
                facilities=[MagicMock() for _ in range(2500)],
            )

            # Mock large facilities dataset (simulate 2500 facilities)
            mock_facilities_batch1 = [
                MagicMock(siret=f"123456782{i:04d}") for i in range(1000)
            ]
            mock_facilities_batch2 = [
                MagicMock(siret=f"123456782{i:04d}") for i in range(1000, 2000)
            ]
            mock_facilities_batch3 = [
                MagicMock(siret=f"123456782{i:04d}") for i in range(2000, 2500)
            ]

            # Mock streaming responses
            async def mock_streaming_extraction():
                for batch in [
                    mock_facilities_batch1,
                    mock_facilities_batch2,
                    mock_facilities_batch3,
                ]:
                    yield batch, 2500

            with (
                patch.object(
                    orchestrator.extractor, "_extract_company", new_callable=AsyncMock
                ) as mock_extract_company,
                patch.object(
                    orchestrator.extractor, "extract_facilities_streaming"
                ) as mock_streaming,
            ):
                mock_extract_company.return_value = MagicMock()
                mock_streaming.return_value = mock_streaming_extraction()

                progress_updates = []

                def progress_callback(update):
                    progress_updates.append(update)

                result = await orchestrator.extract_with_progress(
                    "123456782", progress_callback
                )

                assert len(result.facilities) == 2500
                assert len(progress_updates) >= 3  # At least 3 batch updates

    @pytest.mark.asyncio
    async def test_extract_with_progress_api_error(self, orchestrator):
        """Test progressive extraction with API error."""
        with patch.object(
            orchestrator.extractor, "_extract_company", new_callable=AsyncMock
        ) as mock_extract_company:
            mock_extract_company.side_effect = Exception("API Error")

            with pytest.raises(Exception, match="API Error"):
                await orchestrator.extract_with_progress("123456782")

    @pytest.mark.asyncio
    async def test_extract_company_only_success(self, orchestrator):
        """Test company-only extraction."""
        # Mock the extractor to return a company with the expected name
        mock_company = MagicMock()
        mock_company.denomination_unite_legale = "TEST COMPANY"

        with patch.object(
            orchestrator.extractor, "_extract_company", new_callable=AsyncMock
        ) as mock_extract_company:
            mock_extract_company.return_value = mock_company

            company_data, facility_count = await orchestrator.extract_company_only(
                "123456782"
            )

            assert company_data.denomination_unite_legale == "TEST COMPANY"
            assert facility_count == 0


@pytest.mark.requirement("REQ-ETL-003")
@pytest.mark.example
class TestJSONOutput:
    """Test consolidated JSON generation and Django compatibility."""

    @pytest.fixture
    def sample_extract_result(self):
        """Create sample SIRENExtractResult for testing."""
        from sirene_api_client.etl.models import (
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
        )

        return SIRENExtractResult(
            company=CompanyData(
                name="TEST COMPANY",
                identifiers=[
                    CompanyIdentifierData(
                        scheme="siren",
                        value="123456782",
                        normalized_value="123456782",
                        country="FR",
                        is_verified=True,
                        verified_at=datetime.now(),
                    )
                ],
                creation_date=date(2020, 1, 1),
            ),
            facilities=[
                FacilityData(
                    name="TEST FACILITY",
                    identifiers=[
                        FacilityIdentifierData(
                            scheme="siret",
                            value="12345678200001",
                            normalized_value="12345678200001",
                            country="FR",
                            is_verified=True,
                            verified_at=datetime.now(),
                        )
                    ],
                    parent_siren="123456782",
                    is_headquarters=True,
                )
            ],
            legal_unit_periods=[
                CompanyLegalUnitPeriodData(
                    start=date(2020, 1, 1),
                    end=None,
                    legal_name="TEST COMPANY",
                    legal_form_code="5710",
                    legal_form_scheme="sirene",
                    activity_code="4711F",
                    activity_scheme="NAFRev2",
                    status="active",
                )
            ],
            establishment_periods=[
                FacilityEstablishmentPeriodData(
                    start=date(2020, 1, 1),
                    end=None,
                    status="active",
                    activity_code="4711F",
                    activity_scheme="NAFRev2",
                    is_hq=True,
                    opening_date=date(2020, 1, 1),
                )
            ],
            addresses=[
                AddressData(
                    facility_siret="12345678200001",
                    country="FR",
                    locality="PARIS",
                    postal_code="75001",
                    street_address="1 RUE TEST",
                    longitude=2.3522,
                    latitude=48.8566,
                    provider="sirene",
                    geocode_precision="approximate",
                    start=date(2020, 1, 1),
                )
            ],
            activity_classifications=[
                ActivityClassificationData(
                    scheme="NAFRev2",
                    code="4711F",
                    label="Commerce de détail non spécialisé",
                    start=date(2008, 1, 1),
                    end=None,
                )
            ],
            facility_ownerships=[
                FacilityOwnershipData(
                    company_siren="123456782",
                    facility_siret="12345678200001",
                    role="owner",
                    start=date(2020, 1, 1),
                    end=None,
                )
            ],
            registry_records=[
                ExternalRegistryRecordData(
                    entity_type="legal_unit",
                    external_id="123456782",
                    payload={"test": "data"},
                    payload_hash="abc123",
                    registry_updated_at=datetime.now(),
                    ingested_at=datetime.now(),
                )
            ],
            extraction_metadata={
                "siren": "123456782",
                "extracted_at": datetime.now().isoformat(),
            },
        )

    def test_export_to_json_success(self, sample_extract_result):
        """Test successful JSON export."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "test_output.json"

            # Export to JSON
            sample_extract_result.export_to_json(output_path)

            # Verify file exists and is valid JSON
            assert output_path.exists()

            with open(output_path, encoding="utf-8") as f:
                data = json.load(f)

            # Verify structure matches SIRENExtractResult
            assert "company" in data
            assert "facilities" in data
            assert "addresses" in data
            assert "legal_unit_periods" in data
            assert "establishment_periods" in data
            assert "activity_classifications" in data
            assert "facility_ownerships" in data
            assert "registry_records" in data
            assert "extraction_metadata" in data

    def test_export_to_json_django_compatible(self, sample_extract_result):
        """Test JSON export is Django-compatible."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "test_output.json"

            sample_extract_result.export_to_json(output_path)

            with open(output_path, encoding="utf-8") as f:
                data = json.load(f)

            # Verify Django model compatibility
            company = data["company"]
            assert "name" in company
            assert "identifiers" in company
            assert len(company["identifiers"]) > 0
            assert company["identifiers"][0]["scheme"] == "siren"

            facilities = data["facilities"]
            assert len(facilities) > 0
            assert "name" in facilities[0]
            assert "identifiers" in facilities[0]
            assert facilities[0]["identifiers"][0]["scheme"] == "siret"

    def test_generate_summary_success(self, sample_extract_result):
        """Test summary generation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "test_summary.txt"

            sample_extract_result.generate_summary(output_path)

            assert output_path.exists()

            with open(output_path, encoding="utf-8") as f:
                content = f.read()

            # Verify summary contains key information
            assert "TEST COMPANY" in content
            assert "123456782" in content
            assert "Companies: 1" in content
            assert "Facilities: 1" in content
            assert "Addresses: 1" in content


@pytest.mark.example
class TestCacheSimulator:
    """Test cache simulation functionality."""

    @pytest.fixture
    def cache_simulator(self):
        """Create CacheSimulator instance."""
        return CacheSimulator()

    def test_set_get_success(self, cache_simulator):
        """Test successful cache set and get operations."""
        cache_simulator.set("test_key", {"data": "test"}, ttl=3600)

        result = cache_simulator.get("test_key")
        assert result == {"data": "test"}

    def test_get_nonexistent_key(self, cache_simulator):
        """Test getting non-existent cache key."""
        result = cache_simulator.get("nonexistent_key")
        assert result is None

    def test_ttl_expiration(self, cache_simulator):
        """Test TTL expiration."""
        cache_simulator.set("test_key", {"data": "test"}, ttl=0)  # Immediate expiration

        result = cache_simulator.get("test_key")
        assert result is None

    def test_delete_success(self, cache_simulator):
        """Test successful cache deletion."""
        cache_simulator.set("test_key", {"data": "test"})
        cache_simulator.delete("test_key")

        result = cache_simulator.get("test_key")
        assert result is None

    def test_clear_success(self, cache_simulator):
        """Test cache clearing."""
        cache_simulator.set("key1", {"data": "test1"})
        cache_simulator.set("key2", {"data": "test2"})

        cache_simulator.clear()

        assert cache_simulator.get("key1") is None
        assert cache_simulator.get("key2") is None

    def test_get_stats(self, cache_simulator):
        """Test cache statistics."""
        cache_simulator.set("key1", {"data": "test1"})
        cache_simulator.set("key2", {"data": "test2"})

        stats = cache_simulator.get_stats()

        assert stats["total_keys"] == 2
        assert stats["memory_usage"] > 0


@pytest.mark.example
class TestDjangoLoadScript:
    """Test Django load script generation."""

    def test_generate_django_load_script_success(self):
        """Test successful Django load script generation."""
        sample_data = {
            "company": {
                "name": "TEST COMPANY",
                "identifiers": [{"scheme": "siren", "value": "123456782"}],
            },
            "facilities": [
                {
                    "name": "TEST FACILITY",
                    "identifiers": [{"scheme": "siret", "value": "12345678200001"}],
                    "parent_siren": "123456782",
                }
            ],
            "addresses": [
                {
                    "country": "FR",
                    "locality": "PARIS",
                    "postal_code": "75001",
                    "street_address": "1 RUE TEST",
                }
            ],
        }

        script_content = generate_django_load_script(sample_data)

        # Verify script contains Django model operations
        assert "transaction.atomic()" in script_content
        assert "Company.objects.get_or_create" in script_content
        assert "CompanyIdentifier.objects.get_or_create" in script_content
        assert "Facility.objects.get_or_create" in script_content
        assert "Address.objects.get_or_create" in script_content

    def test_generate_django_load_script_empty_data(self):
        """Test Django load script generation with empty data."""
        empty_data = {
            "company": {"name": "", "identifiers": []},
            "facilities": [],
            "addresses": [],
        }

        script_content = generate_django_load_script(empty_data)

        # Should still generate valid script
        assert "transaction.atomic()" in script_content
        assert "Company.objects.get_or_create" in script_content


@pytest.mark.example
class TestMainFunction:
    """Test main function integration."""

    @patch("examples.etl_showcase.interactive_menu")
    def test_main_function_called(self, mock_interactive_menu):
        """Test main function is called correctly."""
        mock_interactive_menu.return_value = None

        main()

        mock_interactive_menu.assert_called_once()

    @patch("examples.etl_showcase.sys.argv", ["etl_showcase.py"])
    @patch("examples.etl_showcase.interactive_menu")
    def test_main_with_no_args(self, mock_interactive_menu):
        """Test main function with no command line arguments."""
        mock_interactive_menu.return_value = None

        main()

        mock_interactive_menu.assert_called_once()
