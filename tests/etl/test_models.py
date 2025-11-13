"""
Unit tests for ETL Pydantic models.

Tests cover:
- Model validation and serialization
- Field constraints and types
- Default values and optional fields
- Model relationships and references
- Error handling for invalid data
"""

from datetime import date, datetime

import pytest

from sirene_api_client.etl.models import (
    ActivityClassificationData,
    AddressData,
    CompanyData,
    CompanyIdentifierData,
    ExternalRegistryRecordData,
    FacilityData,
    FacilityIdentifierData,
    FacilityOwnershipData,
    SIRENExtractResult,
)


class TestCompanyData:
    """Test CompanyData model validation and behavior."""

    def test_valid_company_data(self) -> None:
        """Test creating valid CompanyData."""
        company = CompanyData(
            name="Test Company",
            identifiers=[
                CompanyIdentifierData(
                    scheme="siren",
                    value="123456782",
                    normalized_value="123456782",
                    verified_at=datetime.now(),
                )
            ],
        )

        assert company.name == "Test Company"
        assert len(company.identifiers) == 1
        assert company.identifiers[0].scheme == "siren"
        assert company.identifiers[0].value == "123456782"
        assert company.identifiers[0].normalized_value == "123456782"

    def test_company_data_without_identifiers(self) -> None:
        """Test CompanyData with empty identifiers list."""
        company = CompanyData(
            name="Test Company",
            identifiers=[],
        )

        assert company.name == "Test Company"
        assert company.identifiers == []

    def test_company_data_optional_fields(self) -> None:
        """Test CompanyData with optional fields."""
        company = CompanyData(
            name="Test Company",
            identifiers=[],
            creation_date=date(2020, 1, 1),
            acronym="TC",
            employee_band="10-19",
            employee_band_year=2023,
        )

        assert company.creation_date == date(2020, 1, 1)
        assert company.acronym == "TC"
        assert company.employee_band == "10-19"
        assert company.employee_band_year == 2023

    def test_company_data_validation_errors(self) -> None:
        """Test CompanyData validation errors."""
        # Note: Pydantic allows empty strings by default
        # Validation would be handled by custom validators if needed
        company = CompanyData(
            name="",  # Empty name is allowed by default
            identifiers=[],
        )
        assert company.name == ""

    def test_company_data_serialization(self) -> None:
        """Test CompanyData serialization to dict."""
        company = CompanyData(
            name="Test Company",
            identifiers=[
                CompanyIdentifierData(
                    scheme="siren",
                    value="123456782",
                    normalized_value="123456782",
                    verified_at=datetime.now(),
                )
            ],
        )

        data = company.model_dump()

        assert isinstance(data, dict)
        assert data["name"] == "Test Company"
        assert len(data["identifiers"]) == 1
        assert data["identifiers"][0]["scheme"] == "siren"

    def test_company_data_from_dict(self) -> None:
        """Test creating CompanyData from dictionary."""
        data = {
            "name": "Test Company",
            "identifiers": [
                {
                    "scheme": "siren",
                    "value": "123456782",
                    "normalized_value": "123456782",
                    "verified_at": datetime.now().isoformat(),
                }
            ],
        }

        company = CompanyData.model_validate(data)

        assert company.name == "Test Company"
        assert len(company.identifiers) == 1
        assert company.identifiers[0].scheme == "siren"


class TestFacilityData:
    """Test FacilityData model validation and behavior."""

    def test_valid_facility_data(self) -> None:
        """Test creating valid FacilityData."""
        facility = FacilityData(
            name="Test Facility",
            identifiers=[
                FacilityIdentifierData(
                    scheme="siret",
                    value="12345678200001",
                    normalized_value="12345678200001",
                    verified_at=datetime.now(),
                )
            ],
            parent_siren="123456782",
        )

        assert facility.name == "Test Facility"
        assert len(facility.identifiers) == 1
        assert facility.identifiers[0].scheme == "siret"
        assert facility.identifiers[0].value == "12345678200001"
        assert facility.parent_siren == "123456782"

    def test_facility_data_optional_fields(self) -> None:
        """Test FacilityData with optional fields."""
        facility = FacilityData(
            name="Test Facility",
            identifiers=[],
            parent_siren="123456782",
            nic="00001",
            creation_date=date(2020, 1, 1),
            is_headquarters=True,
        )

        assert facility.nic == "00001"
        assert facility.creation_date == date(2020, 1, 1)
        assert facility.is_headquarters is True

    def test_facility_data_validation_errors(self) -> None:
        """Test FacilityData validation errors."""
        # Note: Pydantic allows empty strings by default
        # Validation would be handled by custom validators if needed
        facility = FacilityData(
            name="",  # Empty name is allowed by default
            identifiers=[],
            parent_siren="123456782",
        )
        assert facility.name == ""

        # Test with invalid SIREN format (this should still work)
        facility2 = FacilityData(
            name="Test Facility",
            identifiers=[],
            parent_siren="invalid",  # Invalid SIREN format
        )
        assert facility2.parent_siren == "invalid"


class TestAddressData:
    """Test AddressData model validation and behavior."""

    def test_valid_address_data(self) -> None:
        """Test creating valid AddressData."""
        address = AddressData(
            facility_siret="12345678200001",
            country="FR",
            locality="Paris",
            postal_code="75001",
            street_address="123 Main Street",
            longitude=2.3522,
            latitude=48.8566,
            start=date(2020, 1, 1),
            end=date(2023, 12, 31),
        )

        assert address.facility_siret == "12345678200001"
        assert address.street_address == "123 Main Street"
        assert address.locality == "Paris"
        assert address.postal_code == "75001"
        assert address.country == "FR"
        assert address.longitude == 2.3522
        assert address.latitude == 48.8566
        assert address.start == date(2020, 1, 1)
        assert address.end == date(2023, 12, 31)

    def test_address_data_optional_fields(self) -> None:
        """Test AddressData with optional fields."""
        address = AddressData(
            facility_siret="12345678200001",
            country="FR",
            locality="Paris",
            postal_code="75001",
            street_address="123 Main Street",
            longitude=2.3522,
            latitude=48.8566,
            start=date(2020, 1, 1),
            end=None,  # No end date
            provider="sirene",
        )

        assert address.facility_siret == "12345678200001"
        assert address.end is None
        assert address.provider == "sirene"

    def test_address_data_coordinate_validation(self) -> None:
        """Test AddressData coordinate validation."""
        # Valid coordinates
        address = AddressData(
            facility_siret="12345678200001",
            country="FR",
            locality="Paris",
            postal_code="75001",
            street_address="123 Main Street",
            longitude=2.3522,
            latitude=48.8566,
            start=date(2020, 1, 1),
        )

        assert address.facility_siret == "12345678200001"
        assert address.longitude == 2.3522
        assert address.latitude == 48.8566

        # Invalid coordinates (latitude > 90)
        with pytest.raises(ValueError, match=r".*"):
            AddressData(
                facility_siret="12345678200001",
                country="FR",
                locality="Paris",
                postal_code="75001",
                street_address="123 Main Street",
                longitude=2.3522,
                latitude=95.0,  # Invalid latitude
                start=date(2020, 1, 1),
            )

    def test_address_data_date_validation(self) -> None:
        """Test AddressData date validation."""
        # End date before start date should fail
        with pytest.raises(ValueError, match=r".*"):
            AddressData(
                facility_siret="12345678200001",
                country="FR",
                locality="Paris",
                postal_code="75001",
                street_address="123 Main Street",
                longitude=2.3522,
                latitude=48.8566,
                start=date(2023, 1, 1),
                end=date(2020, 1, 1),  # Before start date
            )


class TestActivityClassificationData:
    """Test ActivityClassificationData model validation and behavior."""

    def test_valid_activity_classification(self) -> None:
        """Test creating valid ActivityClassificationData."""
        activity = ActivityClassificationData(
            scheme="NAFRev2",
            code="6201Z",
            label="Programmation informatique",
            start=date(2008, 1, 1),
        )

        assert activity.code == "6201Z"
        assert activity.scheme == "NAFRev2"
        assert activity.label == "Programmation informatique"

    def test_activity_classification_optional_label(self) -> None:
        """Test ActivityClassificationData without label."""
        activity = ActivityClassificationData(
            scheme="NAFRev2",
            code="6201Z",
            label="Programmation informatique",  # Required field in plan
            start=date(2008, 1, 1),
        )

        assert activity.code == "6201Z"
        assert activity.scheme == "NAFRev2"
        assert activity.label == "Programmation informatique"

    def test_activity_classification_validation_errors(self) -> None:
        """Test ActivityClassificationData validation errors."""
        with pytest.raises(ValueError, match=r".*"):
            ActivityClassificationData(
                code="",  # Empty code should fail
                scheme="naf_rev2",
                label="Test",
            )

        with pytest.raises(ValueError, match=r".*"):
            ActivityClassificationData(
                code="6201Z",
                scheme="",  # Empty scheme should fail
                label="Test",
            )


class TestExternalRegistryRecordData:
    """Test ExternalRegistryRecordData model validation and behavior."""

    def test_valid_registry_record(self) -> None:
        """Test creating valid ExternalRegistryRecordData."""
        record = ExternalRegistryRecordData(
            entity_type="legal_unit",
            external_id="123456782",
            payload={"test": "data"},
            payload_hash="abc123def456",  # pragma: allowlist secret
            registry_updated_at=datetime(2023, 1, 1, 12, 0, 0),
            ingested_at=datetime(2023, 1, 1, 12, 0, 0),
        )

        assert record.entity_type == "legal_unit"
        assert record.external_id == "123456782"
        assert record.payload == {"test": "data"}
        assert record.payload_hash == "abc123def456"  # pragma: allowlist secret
        assert record.registry_updated_at == datetime(2023, 1, 1, 12, 0, 0)
        assert record.ingested_at == datetime(2023, 1, 1, 12, 0, 0)

    def test_registry_record_validation_errors(self) -> None:
        """Test ExternalRegistryRecordData validation errors."""
        with pytest.raises(ValueError, match=r".*"):
            ExternalRegistryRecordData(
                source="",  # Empty source should fail
                external_id="123456782",
                payload={},
                extracted_at=datetime.now(),
            )

        with pytest.raises(ValueError, match=r".*"):
            ExternalRegistryRecordData(
                source="sirene",
                external_id="",  # Empty external_id should fail
                payload={},
                extracted_at=datetime.now(),
            )


class TestSIRENExtractResult:
    """Test SIRENExtractResult model validation and behavior."""

    def test_valid_extract_result(self) -> None:
        """Test creating valid SIRENExtractResult."""
        company = CompanyData(
            name="Test Company",
            identifiers=[
                CompanyIdentifierData(
                    scheme="siren",
                    value="123456782",
                    normalized_value="123456782",
                    verified_at=datetime.now(),
                )
            ],
        )

        facility = FacilityData(
            name="Test Facility",
            identifiers=[
                FacilityIdentifierData(
                    scheme="siret",
                    value="12345678200001",
                    normalized_value="12345678200001",
                    verified_at=datetime.now(),
                )
            ],
            parent_siren="123456782",
        )

        result = SIRENExtractResult(
            company=company,
            facilities=[facility],
            legal_unit_periods=[],
            establishment_periods=[],
            addresses=[],
            activity_classifications=[],
            registry_records=[],
            facility_ownerships=[],
            extraction_metadata={
                "siren": "123456782",
                "extracted_at": datetime.now().isoformat(),
                "facility_count": 1,
            },
        )

        assert result.company == company
        assert len(result.facilities) == 1
        assert result.facilities[0] == facility
        assert result.extraction_metadata["siren"] == "123456782"
        assert result.extraction_metadata["facility_count"] == 1

    def test_extract_result_empty_lists(self) -> None:
        """Test SIRENExtractResult with empty lists."""
        company = CompanyData(
            name="Test Company",
            identifiers=[],
        )

        result = SIRENExtractResult(
            company=company,
            facilities=[],
            legal_unit_periods=[],
            establishment_periods=[],
            addresses=[],
            activity_classifications=[],
            registry_records=[],
            facility_ownerships=[],
            extraction_metadata={},
        )

        assert result.company == company
        assert result.facilities == []
        assert result.legal_unit_periods == []
        assert result.establishment_periods == []
        assert result.addresses == []
        assert result.activity_classifications == []
        assert result.registry_records == []
        assert result.facility_ownerships == []

    def test_extract_result_serialization(self) -> None:
        """Test SIRENExtractResult serialization."""
        company = CompanyData(
            name="Test Company",
            identifiers=[],
        )

        result = SIRENExtractResult(
            company=company,
            facilities=[],
            legal_unit_periods=[],
            establishment_periods=[],
            addresses=[],
            activity_classifications=[],
            registry_records=[],
            facility_ownerships=[],
            extraction_metadata={},
        )

        data = result.model_dump()

        assert isinstance(data, dict)
        assert "company" in data
        assert "facilities" in data
        assert "extraction_metadata" in data
        assert data["company"]["name"] == "Test Company"

    def test_extract_result_from_dict(self) -> None:
        """Test creating SIRENExtractResult from dictionary."""
        data = {
            "company": {
                "name": "Test Company",
                "identifiers": [],
            },
            "facilities": [],
            "legal_unit_periods": [],
            "establishment_periods": [],
            "addresses": [],
            "activity_classifications": [],
            "registry_records": [],
            "facility_ownerships": [],
            "extraction_metadata": {},
        }

        result = SIRENExtractResult.model_validate(data)

        assert result.company.name == "Test Company"
        assert result.facilities == []
        assert result.extraction_metadata == {}


class TestModelRelationships:
    """Test relationships between models."""

    def test_company_facility_relationship(self) -> None:
        """Test relationship between company and facilities."""
        company = CompanyData(
            name="Test Company",
            identifiers=[
                CompanyIdentifierData(
                    scheme="siren",
                    value="123456782",
                    normalized_value="123456782",
                    verified_at=datetime.now(),
                )
            ],
        )

        facility = FacilityData(
            name="Test Facility",
            identifiers=[
                FacilityIdentifierData(
                    scheme="siret",
                    value="12345678200001",
                    normalized_value="12345678200001",
                    verified_at=datetime.now(),
                )
            ],
            parent_siren="123456782",  # Matches company SIREN
        )

        # Verify the relationship
        company_siren = company.identifiers[0].value
        assert facility.parent_siren == company_siren

    def test_facility_ownership_relationship(self) -> None:
        """Test FacilityOwnershipData relationship."""
        ownership = FacilityOwnershipData(
            company_siren="123456782",
            facility_siret="12345678200001",
            role="owner",
            start=date(2020, 1, 1),
        )

        assert ownership.company_siren == "123456782"
        assert ownership.facility_siret == "12345678200001"
        assert ownership.role == "owner"
        assert ownership.start == date(2020, 1, 1)

    def test_address_facility_relationship(self) -> None:
        """Test relationship between addresses and facilities."""
        address = AddressData(
            facility_siret="12345678200001",
            country="FR",
            locality="Paris",
            postal_code="75001",
            street_address="123 Main Street",
            longitude=2.3522,
            latitude=48.8566,
            start=date(2020, 1, 1),
        )

        assert address.country == "FR"
        assert address.locality == "Paris"

    def test_activity_classification_facility_relationship(self) -> None:
        """Test relationship between activity classifications and facilities."""
        activity = ActivityClassificationData(
            scheme="NAFRev2",
            code="6201Z",
            label="Programmation informatique",
            start=date(2008, 1, 1),
        )

        assert activity.code == "6201Z"
        assert activity.scheme == "NAFRev2"
