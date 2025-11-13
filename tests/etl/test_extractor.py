"""
Unit tests for ETL extractor module.

Tests cover:
- SIRENExtractor initialization and configuration
- API data extraction with mocked responses
- Error handling for API failures
- Data validation and processing
- Edge cases and boundary conditions
"""

from unittest.mock import MagicMock, patch

import pytest

from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.etl.config import ETLConfig, ValidationMode
from sirene_api_client.etl.exceptions import ExtractionError
from sirene_api_client.etl.extractor import SIRENExtractor


class TestSIRENExtractor:
    """Test SIRENExtractor functionality."""

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
    def extractor(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> SIRENExtractor:
        """Create SIRENExtractor instance."""
        return SIRENExtractor(mock_client, config)

    def test_extractor_initialization(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> None:
        """Test SIRENExtractor initialization."""
        extractor = SIRENExtractor(mock_client, config)

        assert extractor.client == mock_client
        assert extractor.config == config

    def test_extractor_initialization_with_none_config(
        self, mock_client: AuthenticatedClient
    ) -> None:
        """Test SIRENExtractor initialization with None config."""
        with pytest.raises(TypeError):
            SIRENExtractor(mock_client, None)

    def test_extractor_initialization_with_none_client(self, config: ETLConfig) -> None:
        """Test SIRENExtractor initialization with None client."""
        with pytest.raises(TypeError):
            SIRENExtractor(None, config)

    @pytest.mark.asyncio
    async def test_extract_siren_complete_success(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test successful complete SIREN extraction."""
        # Mock company data
        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"

        # Mock facility data
        mock_facility = MagicMock()
        mock_facility.siret = "12345678200001"
        mock_facility.denomination_usuelle_etablissement = "Test Facility"

        # Mock API responses
        with (
            patch.object(
                extractor, "_extract_company", return_value=mock_company
            ) as mock_extract_company,
            patch.object(
                extractor, "_extract_facilities", return_value=[mock_facility]
            ) as mock_extract_facilities,
        ):
            result = await extractor.extract_siren_complete("123456782")

            assert isinstance(result, dict)
            assert "company" in result
            assert "facilities" in result
            assert "extraction_metadata" in result

            assert result["company"] == mock_company
            assert result["facilities"] == [mock_facility]
            assert result["extraction_metadata"]["siren"] == "123456782"
            assert result["extraction_metadata"]["facility_count"] == 1

            mock_extract_company.assert_called_once_with("123456782")
            mock_extract_facilities.assert_called_once_with("123456782")

    @pytest.mark.asyncio
    async def test_extract_siren_complete_company_extraction_failure(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test SIREN extraction failure during company extraction."""
        with patch.object(
            extractor, "_extract_company", side_effect=Exception("API Error")
        ) as mock_extract_company:
            with pytest.raises(ExtractionError) as exc_info:
                await extractor.extract_siren_complete("123456782")

            assert "Failed to extract SIREN 123456782" in str(exc_info.value)
            assert exc_info.value.siren == "123456782"
            mock_extract_company.assert_called_once_with("123456782")

    @pytest.mark.asyncio
    async def test_extract_siren_complete_facility_extraction_failure(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test SIREN extraction failure during facility extraction."""
        mock_company = MagicMock()

        with (
            patch.object(
                extractor, "_extract_company", return_value=mock_company
            ) as mock_extract_company,
            patch.object(
                extractor, "_extract_facilities", side_effect=Exception("API Error")
            ) as mock_extract_facilities,
        ):
            with pytest.raises(ExtractionError) as exc_info:
                await extractor.extract_siren_complete("123456782")

            assert "Failed to extract SIREN 123456782" in str(exc_info.value)
            assert exc_info.value.siren == "123456782"
            mock_extract_company.assert_called_once_with("123456782")
            mock_extract_facilities.assert_called_once_with("123456782")

    @pytest.mark.asyncio
    async def test_extract_company_success(self, extractor: SIRENExtractor) -> None:
        """Test successful company extraction."""
        mock_company = MagicMock()
        mock_company.siren = "123456782"
        mock_company.denomination_unite_legale = "Test Company"

        mock_response = MagicMock()
        mock_response.unite_legale = mock_company

        with patch(
            "sirene_api_client.etl.extractor.find_by_siren", return_value=mock_response
        ) as mock_api_call:
            result = await extractor._extract_company("123456782")

            assert result == mock_company
            mock_api_call.assert_called_once_with(
                siren="123456782",
                client=extractor.client,
            )

    @pytest.mark.asyncio
    async def test_extract_company_no_data(self, extractor: SIRENExtractor) -> None:
        """Test company extraction with no data returned."""
        mock_response = MagicMock()
        mock_response.unite_legale = None

        with patch(
            "sirene_api_client.etl.extractor.find_by_siren", return_value=mock_response
        ) as mock_api_call:
            with pytest.raises(ExtractionError) as exc_info:
                await extractor._extract_company("123456782")

            assert "No company data found for SIREN: 123456782" in str(exc_info.value)
            assert exc_info.value.siren == "123456782"
            mock_api_call.assert_called_once_with(
                siren="123456782",
                client=extractor.client,
            )

    @pytest.mark.asyncio
    async def test_extract_company_api_error(self, extractor: SIRENExtractor) -> None:
        """Test company extraction with API error."""
        with patch(
            "sirene_api_client.etl.extractor.find_by_siren",
            side_effect=Exception("API Error"),
        ) as mock_api_call:
            with pytest.raises(ExtractionError) as exc_info:
                await extractor._extract_company("123456782")

            assert "Failed to extract company data for SIREN 123456782" in str(
                exc_info.value
            )
            assert exc_info.value.siren == "123456782"
            assert exc_info.value.endpoint == "unite_legale/find_by_siren"
            mock_api_call.assert_called_once_with(
                siren="123456782",
                client=extractor.client,
            )

    @pytest.mark.asyncio
    async def test_extract_facilities_success_single_page(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test successful facility extraction with single page (no pagination needed)."""
        mock_facility1 = MagicMock()
        mock_facility1.siret = "12345678200001"
        mock_facility1.denomination_usuelle_etablissement = "Facility 1"

        mock_facility2 = MagicMock()
        mock_facility2.siret = "12345678200002"
        mock_facility2.denomination_usuelle_etablissement = "Facility 2"

        mock_response = MagicMock()
        mock_response.etablissements = [mock_facility1, mock_facility2]
        mock_response.header = MagicMock()
        mock_response.header.total = 2  # Total facilities available

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            return_value=mock_response,
        ) as mock_api_call:
            result = await extractor._extract_facilities("123456782")

            assert result == [mock_facility1, mock_facility2]
            mock_api_call.assert_called_once()

            # Verify the search criteria
            call_args = mock_api_call.call_args
            assert call_args[1]["client"] == extractor.client

            search_criteria = call_args[1]["body"]
            assert search_criteria.q == "siren:123456782"
            assert search_criteria.nombre == 1000
            assert search_criteria.debut == 0
            assert search_criteria.masquer_valeurs_nulles

    @pytest.mark.asyncio
    async def test_extract_facilities_success_with_pagination(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test successful facility extraction with pagination (multiple pages)."""
        # Create mock facilities for page 1
        mock_facilities_page1 = []
        for i in range(1000):  # Full page
            facility = MagicMock()
            facility.siret = f"123456782{i:05d}"
            facility.denomination_usuelle_etablissement = f"Facility {i}"
            mock_facilities_page1.append(facility)

        # Create mock facilities for page 2
        mock_facilities_page2 = []
        for i in range(179):  # Partial page
            facility = MagicMock()
            facility.siret = f"123456782{i + 1000:05d}"
            facility.denomination_usuelle_etablissement = f"Facility {i + 1000}"
            mock_facilities_page2.append(facility)

        # Mock responses for pagination
        mock_response_page1 = MagicMock()
        mock_response_page1.etablissements = mock_facilities_page1
        mock_response_page1.header = MagicMock()
        mock_response_page1.header.total = 1179  # Total facilities available

        mock_response_page2 = MagicMock()
        mock_response_page2.etablissements = mock_facilities_page2
        mock_response_page2.header = MagicMock()
        mock_response_page2.header.total = 1179

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=[mock_response_page1, mock_response_page2],
        ) as mock_api_call:
            result = await extractor._extract_facilities("123456782")

            # Should have all facilities from both pages
            assert len(result) == 1179
            assert result == mock_facilities_page1 + mock_facilities_page2

            # Should have made 2 API calls
            assert mock_api_call.call_count == 2

            # Verify first call (page 1)
            first_call_args = mock_api_call.call_args_list[0]
            first_search_criteria = first_call_args[1]["body"]
            assert first_search_criteria.q == "siren:123456782"
            assert first_search_criteria.nombre == 1000
            assert first_search_criteria.debut == 0

            # Verify second call (page 2)
            second_call_args = mock_api_call.call_args_list[1]
            second_search_criteria = second_call_args[1]["body"]
            assert second_search_criteria.q == "siren:123456782"
            assert second_search_criteria.nombre == 1000
            assert second_search_criteria.debut == 1000

    @pytest.mark.asyncio
    async def test_extract_facilities_empty_response(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test facility extraction with empty response."""
        mock_response = MagicMock()
        mock_response.etablissements = None
        mock_response.header = MagicMock()
        mock_response.header.total = 0

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            return_value=mock_response,
        ) as mock_api_call:
            result = await extractor._extract_facilities("123456782")

            assert result == []
            mock_api_call.assert_called_once()

    @pytest.mark.asyncio
    async def test_extract_facilities_api_error(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test facility extraction with API error."""
        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=Exception("API Error"),
        ) as mock_api_call:
            with pytest.raises(ExtractionError) as exc_info:
                await extractor._extract_facilities("123456782")

            assert "Failed to extract facilities for SIREN 123456782" in str(
                exc_info.value
            )
            assert exc_info.value.siren == "123456782"
            assert exc_info.value.endpoint == "etablissement/find_by_post"
            mock_api_call.assert_called_once()

    def test_create_payload_hash(self, extractor: SIRENExtractor) -> None:
        """Test payload hash creation for deduplication."""
        payload1 = {"test": "data", "number": 123}
        payload2 = {"test": "data", "number": 123}
        payload3 = {"test": "different", "number": 123}

        hash1 = extractor._create_payload_hash(payload1)
        hash2 = extractor._create_payload_hash(payload2)
        hash3 = extractor._create_payload_hash(payload3)

        # Same payload should produce same hash
        assert hash1 == hash2

        # Different payload should produce different hash
        assert hash1 != hash3

        # Hash should be a string
        assert isinstance(hash1, str)
        assert len(hash1) == 64  # SHA-256 produces 64-character hex string

    def test_create_payload_hash_with_different_order(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test that payload hash is order-independent."""
        payload1 = {"a": 1, "b": 2, "c": 3}
        payload2 = {"c": 3, "a": 1, "b": 2}

        hash1 = extractor._create_payload_hash(payload1)
        hash2 = extractor._create_payload_hash(payload2)

        # Same data in different order should produce same hash
        assert hash1 == hash2

    def test_create_payload_hash_with_nested_data(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test payload hash with nested data structures."""
        payload = {
            "company": {
                "name": "Test Company",
                "siren": "123456782",
            },
            "facilities": [
                {"siret": "12345678200001", "name": "Facility 1"},
                {"siret": "12345678200002", "name": "Facility 2"},
            ],
        }

        hash_value = extractor._create_payload_hash(payload)

        assert isinstance(hash_value, str)
        assert len(hash_value) == 64

    @pytest.mark.asyncio
    async def test_extract_siren_complete_with_large_facility_count(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test SIREN extraction with large number of facilities (simulating pagination)."""
        mock_company = MagicMock()

        # Create mock facilities (simulate 2500 facilities - would require 3 pages)
        mock_facilities = []
        for i in range(2500):
            facility = MagicMock()
            facility.siret = f"123456782{i:05d}"
            facility.denomination_usuelle_etablissement = f"Facility {i}"
            mock_facilities.append(facility)

        with (
            patch.object(extractor, "_extract_company", return_value=mock_company),
            patch.object(
                extractor, "_extract_facilities", return_value=mock_facilities
            ),
        ):
            result = await extractor.extract_siren_complete("123456782")

            assert result["extraction_metadata"]["facility_count"] == 2500
            assert len(result["facilities"]) == 2500

    @pytest.mark.asyncio
    async def test_extract_siren_complete_with_zero_facilities(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test SIREN extraction with zero facilities."""
        mock_company = MagicMock()

        with (
            patch.object(extractor, "_extract_company", return_value=mock_company),
            patch.object(extractor, "_extract_facilities", return_value=[]),
        ):
            result = await extractor.extract_siren_complete("123456782")

            assert result["extraction_metadata"]["facility_count"] == 0
            assert result["facilities"] == []

    def test_extractor_with_different_configs(
        self, mock_client: AuthenticatedClient
    ) -> None:
        """Test extractor with different configurations."""
        strict_config = ETLConfig(validation_mode=ValidationMode.STRICT)
        lenient_config = ETLConfig(validation_mode=ValidationMode.LENIENT)
        permissive_config = ETLConfig(validation_mode=ValidationMode.PERMISSIVE)

        extractor_strict = SIRENExtractor(mock_client, strict_config)
        extractor_lenient = SIRENExtractor(mock_client, lenient_config)
        extractor_permissive = SIRENExtractor(mock_client, permissive_config)

        assert extractor_strict.config.validation_mode == ValidationMode.STRICT
        assert extractor_lenient.config.validation_mode == ValidationMode.LENIENT
        assert extractor_permissive.config.validation_mode == ValidationMode.PERMISSIVE

    @pytest.mark.asyncio
    async def test_extract_siren_complete_metadata_timestamp(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test that extraction metadata includes timestamp."""
        mock_company = MagicMock()

        with (
            patch.object(extractor, "_extract_company", return_value=mock_company),
            patch.object(extractor, "_extract_facilities", return_value=[]),
        ):
            result = await extractor.extract_siren_complete("123456782")

            assert "extracted_at" in result["extraction_metadata"]
            extracted_at = result["extraction_metadata"]["extracted_at"]

            # Should be a valid ISO format timestamp
            from datetime import datetime

            datetime.fromisoformat(extracted_at)  # Should not raise exception


class TestStreamingExtraction:
    """Test streaming facility extraction functionality."""

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
    def extractor(
        self, mock_client: AuthenticatedClient, config: ETLConfig
    ) -> SIRENExtractor:
        """Create SIRENExtractor instance."""
        return SIRENExtractor(mock_client, config)

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_single_page(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test streaming extraction with single page (< 1000 facilities)."""
        # Create mock facilities
        mock_facility1 = MagicMock()
        mock_facility1.siret = "12345678200001"
        mock_facility1.denomination_usuelle_etablissement = "Facility 1"

        mock_facility2 = MagicMock()
        mock_facility2.siret = "12345678200002"
        mock_facility2.denomination_usuelle_etablissement = "Facility 2"

        mock_response = MagicMock()
        mock_response.etablissements = [mock_facility1, mock_facility2]
        mock_response.header = MagicMock()
        mock_response.header.total = 2

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            return_value=mock_response,
        ) as mock_api_call:
            # Collect all yielded batches
            batches = []
            async for batch, _total in extractor.extract_facilities_streaming(
                "123456782"
            ):
                batches.append(batch)

            # Should have yielded one batch with 2 facilities
            assert len(batches) == 1
            assert len(batches[0]) == 2
            assert batches[0][0] == mock_facility1
            assert batches[0][1] == mock_facility2

            # Should have made one API call
            mock_api_call.assert_called_once()

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_multiple_pages(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test streaming extraction with multiple pages (> 1000 facilities)."""
        # Create mock facilities for page 1 (full page)
        mock_facilities_page1 = []
        for i in range(1000):
            facility = MagicMock()
            facility.siret = f"123456782{i:05d}"
            facility.denomination_usuelle_etablissement = f"Facility {i}"
            mock_facilities_page1.append(facility)

        # Create mock facilities for page 2 (partial page)
        mock_facilities_page2 = []
        for i in range(179):
            facility = MagicMock()
            facility.siret = f"123456782{i + 1000:05d}"
            facility.denomination_usuelle_etablissement = f"Facility {i + 1000}"
            mock_facilities_page2.append(facility)

        # Mock responses for pagination
        mock_response_page1 = MagicMock()
        mock_response_page1.etablissements = mock_facilities_page1
        mock_response_page1.header = MagicMock()
        mock_response_page1.header.total = 1179

        mock_response_page2 = MagicMock()
        mock_response_page2.etablissements = mock_facilities_page2
        mock_response_page2.header = MagicMock()
        mock_response_page2.header.total = 1179

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=[mock_response_page1, mock_response_page2],
        ) as mock_api_call:
            # Collect all yielded batches
            batches = []
            async for batch, _total in extractor.extract_facilities_streaming(
                "123456782"
            ):
                batches.append(batch)

            # Should have yielded two batches
            assert len(batches) == 2
            assert len(batches[0]) == 1000  # First batch
            assert len(batches[1]) == 179  # Second batch

            # Should have made 2 API calls
            assert mock_api_call.call_count == 2

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_empty_results(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test streaming extraction with empty results."""
        mock_response = MagicMock()
        mock_response.etablissements = None
        mock_response.header = MagicMock()
        mock_response.header.total = 0

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            return_value=mock_response,
        ) as mock_api_call:
            # Collect all yielded batches
            batches = []
            async for batch, _total in extractor.extract_facilities_streaming(
                "123456782"
            ):
                batches.append(batch)

            # Should have yielded one empty batch
            assert len(batches) == 1
            assert len(batches[0]) == 0

            # Should have made one API call
            mock_api_call.assert_called_once()

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_api_error(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test streaming extraction with API error."""
        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=Exception("API Error"),
        ) as mock_api_call:
            with pytest.raises(
                ExtractionError, match="Failed to stream facilities for SIREN 123456782"
            ) as exc_info:
                async for _ in extractor.extract_facilities_streaming("123456782"):
                    pass  # Consume the async generator
            assert exc_info.value.siren == "123456782"
            assert exc_info.value.endpoint == "etablissement/find_by_post"
            mock_api_call.assert_called_once()

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_proper_yielding(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test that streaming properly yields batches as they're retrieved."""
        # Create mock facilities for 3 pages
        mock_facilities_page1 = [MagicMock() for _ in range(1000)]
        mock_facilities_page2 = [MagicMock() for _ in range(1000)]
        mock_facilities_page3 = [MagicMock() for _ in range(500)]

        # Mock responses
        mock_response_page1 = MagicMock()
        mock_response_page1.etablissements = mock_facilities_page1
        mock_response_page1.header = MagicMock()
        mock_response_page1.header.total = 2500

        mock_response_page2 = MagicMock()
        mock_response_page2.etablissements = mock_facilities_page2
        mock_response_page2.header = MagicMock()
        mock_response_page2.header.total = 2500

        mock_response_page3 = MagicMock()
        mock_response_page3.etablissements = mock_facilities_page3
        mock_response_page3.header = MagicMock()
        mock_response_page3.header.total = 2500

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=[mock_response_page1, mock_response_page2, mock_response_page3],
        ) as mock_api_call:
            # Test that we can process batches as they come
            batch_count = 0
            total_facilities = 0

            async for batch, _total in extractor.extract_facilities_streaming(
                "123456782"
            ):
                batch_count += 1
                total_facilities += len(batch)

                # Each batch should be yielded immediately
                assert len(batch) > 0

                # Stop after processing a few batches to test streaming behavior
                if batch_count >= 2:
                    break

            # Should have processed 2 batches
            assert batch_count == 2
            assert total_facilities == 2000  # 1000 + 1000

            # Should have made 2 API calls
            assert mock_api_call.call_count == 2

    @pytest.mark.asyncio
    async def test_extract_facilities_streaming_large_dataset(
        self, extractor: SIRENExtractor
    ) -> None:
        """Test streaming extraction with large dataset simulation."""
        # Simulate a company with 5000 facilities (5 pages)
        total_facilities = 5000
        page_size = 1000

        # Create mock responses for all pages
        mock_responses = []
        for page in range(5):
            facilities_in_page = min(page_size, total_facilities - page * page_size)
            mock_facilities = [MagicMock() for _ in range(facilities_in_page)]

            mock_response = MagicMock()
            mock_response.etablissements = mock_facilities
            mock_response.header = MagicMock()
            mock_response.header.total = total_facilities

            mock_responses.append(mock_response)

        # Create a callable that returns the responses in order
        def mock_api_call(*_args, **_kwargs):
            if mock_responses:
                return mock_responses.pop(0)
            return None

        with patch(
            "sirene_api_client.etl.extractor.find_by_post_etablissement",
            side_effect=mock_api_call,
        ) as mock_api_patch:
            # Collect all batches
            batches = []
            async for batch, _total in extractor.extract_facilities_streaming(
                "123456782"
            ):
                batches.append(batch)

            # Should have yielded 5 batches
            assert len(batches) == 5

            # Verify batch sizes
            assert len(batches[0]) == 1000  # Page 1
            assert len(batches[1]) == 1000  # Page 2
            assert len(batches[2]) == 1000  # Page 3
            assert len(batches[3]) == 1000  # Page 4
            assert len(batches[4]) == 1000  # Page 5

            # Should have made 5 API calls (plus one extra call when it gets None)
            assert mock_api_patch.call_count == 6
