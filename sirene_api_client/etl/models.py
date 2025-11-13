"""
Pydantic output models for the SIREN ETL service.

This module defines comprehensive output models that match the Django model structure
and provide type-safe, validated data for Django ingestion.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field, field_validator, model_validator

if TYPE_CHECKING:
    from pathlib import Path


class CompanyIdentifierData(BaseModel):
    """Company identifier data (SIREN, VAT, etc.)."""

    scheme: str = Field(..., description="Identifier scheme (e.g., 'siren', 'vat')")
    value: str = Field(..., description="Raw identifier value")
    normalized_value: str = Field(..., description="Normalized identifier value")
    country: str = Field(default="FR", description="ISO 3166-1 alpha-2 country code")
    is_verified: bool = Field(
        default=True, description="Whether identifier is verified"
    )
    verified_at: datetime = Field(..., description="When identifier was verified")


class FacilityIdentifierData(BaseModel):
    """Facility identifier data (SIRET, building permits, etc.)."""

    scheme: str = Field(..., description="Identifier scheme (e.g., 'siret', 'vat')")
    value: str = Field(..., description="Raw identifier value")
    normalized_value: str = Field(..., description="Normalized identifier value")
    country: str = Field(default="FR", description="ISO 3166-1 alpha-2 country code")
    is_verified: bool = Field(
        default=True, description="Whether identifier is verified"
    )
    verified_at: datetime = Field(..., description="When identifier was verified")


class ActivityClassificationData(BaseModel):
    """Activity classification data (NAF, NACE, etc.)."""

    scheme: str = Field(..., description="Classification scheme (e.g., 'NAFRev2')")
    code: str = Field(..., description="Activity code within the scheme")
    label: str = Field(..., description="Human-readable description")
    start: date = Field(..., description="Scheme version start date")
    end: date | None = Field(
        None, description="Scheme version end date (null for current)"
    )


class AddressData(BaseModel):
    """Address data with WGS84 coordinates and explicit facility link."""

    facility_siret: str = Field(..., description="SIRET of associated facility")
    country: str = Field(..., description="ISO 3166-1 alpha-2 country code")
    administrative_area: str | None = Field(None, description="State, province, region")
    locality: str | None = Field(None, description="City or municipality")
    postal_code: str | None = Field(None, description="Postal or ZIP code")
    street_address: str | None = Field(None, description="Street name and number")
    longitude: float | None = Field(None, description="WGS84 longitude")
    latitude: float | None = Field(None, description="WGS84 latitude")
    provider: str = Field(default="sirene", description="Address data provider")
    geocode_precision: str = Field(
        default="approximate", description="Geocoding precision"
    )
    start: date = Field(..., description="Address validity start date")
    end: date | None = Field(None, description="Address validity end date")

    @field_validator("longitude", "latitude")
    @classmethod
    def validate_coordinates(cls, v: float | None) -> float | None:
        """Validate coordinate ranges."""
        if v is None:
            return v
        if "longitude" in cls.model_fields and v is not None and not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        if "latitude" in cls.model_fields and v is not None and not -90 <= v <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return v

    @model_validator(mode="after")
    def validate_date_range(self) -> AddressData:
        """Validate that end date is not before start date."""
        if self.end is not None and self.start is not None and self.end < self.start:
            raise ValueError("End date cannot be before start date")
        return self


class CompanyLegalUnitPeriodData(BaseModel):
    """Time-framed company legal unit data."""

    start: date | None = Field(..., description="Period start date")
    end: date | None = Field(None, description="Period end date (null for current)")
    legal_name: str = Field(..., description="Official legal denomination")
    legal_form_code: str = Field(..., description="Legal form classification code")
    legal_form_scheme: str = Field(default="sirene", description="Legal form scheme")
    activity_code: str = Field(..., description="Primary activity code")
    activity_scheme: str = Field(
        default="NAFRev2", description="Activity classification scheme"
    )
    status: str = Field(..., description="Administrative status (active/ceased)")
    employee_band: str | None = Field(None, description="Employee count band code")
    employee_band_year: int | None = Field(None, description="Year of employee data")
    ess_flag: bool | None = Field(
        None, description="Social and Solidarity Economy flag"
    )
    mission_company_flag: bool = Field(
        default=False, description="Mission-driven company flag"
    )


class FacilityEstablishmentPeriodData(BaseModel):
    """Time-framed facility establishment data."""

    start: date | None = Field(..., description="Period start date")
    end: date | None = Field(None, description="Period end date (null for current)")
    status: str = Field(..., description="Administrative status (active/closed)")
    activity_code: str = Field(..., description="Primary activity code")
    activity_scheme: str = Field(
        default="NAFRev2", description="Activity classification scheme"
    )
    is_hq: bool = Field(default=False, description="Whether this is headquarters")
    opening_date: date | None = Field(None, description="Establishment opening date")


class FacilityOwnershipData(BaseModel):
    """Company-facility ownership relationship."""

    company_siren: str = Field(..., description="Company SIREN number")
    facility_siret: str = Field(..., description="Facility SIRET number")
    role: str = Field(
        default="owner", description="Ownership role (owner/operator/tenant)"
    )
    start: date = Field(..., description="Ownership start date")
    end: date | None = Field(None, description="Ownership end date (null for current)")


class ExternalRegistryRecordData(BaseModel):
    """External registry record for audit trail."""

    entity_type: str = Field(..., description="Entity type (legal_unit/establishment)")
    external_id: str = Field(..., description="Registry-specific identifier")
    payload: dict[str, Any] = Field(..., description="Complete API response")
    payload_hash: str = Field(..., description="SHA-256 hash of payload")
    registry_updated_at: datetime = Field(..., description="Last update from registry")
    ingested_at: datetime = Field(..., description="When record was ingested")


class CompanyData(BaseModel):
    """Company/UniteLegale data."""

    name: str = Field(..., description="Company legal name")
    identifiers: list[CompanyIdentifierData] = Field(default_factory=list)
    creation_date: date | None = Field(None, description="Company creation date")
    acronym: str | None = Field(None, description="Company acronym")
    employee_band: str | None = Field(None, description="Employee count band")
    employee_band_year: int | None = Field(None, description="Year of employee data")
    company_size_category: str | None = Field(None, description="Company size category")
    category_year: int | None = Field(None, description="Year of category data")
    diffusion_status: str | None = Field(None, description="Diffusion status")
    is_purged: bool | None = Field(None, description="Purged unit flag")
    last_update: datetime | None = Field(None, description="Last update timestamp")
    period_count: int | None = Field(None, description="Number of temporal periods")
    association_id: str | None = Field(None, description="Association identifier")


class FacilityData(BaseModel):
    """Facility/Etablissement data."""

    name: str = Field(..., description="Facility name")
    identifiers: list[FacilityIdentifierData] = Field(default_factory=list)
    parent_siren: str = Field(..., description="Parent company SIREN")
    nic: str | None = Field(None, description="Internal classification number")
    creation_date: date | None = Field(None, description="Establishment creation date")
    is_headquarters: bool = Field(
        default=False, description="Whether this is headquarters"
    )
    employee_band: str | None = Field(None, description="Employee count band")
    employee_band_year: int | None = Field(None, description="Year of employee data")
    search_score: float | None = Field(None, description="Search relevance score")
    diffusion_status: str | None = Field(None, description="Diffusion status")
    crafts_activity: str | None = Field(
        None, description="Crafts registry activity code"
    )
    last_update: datetime | None = Field(None, description="Last update timestamp")
    period_count: int | None = Field(None, description="Number of temporal periods")


class SIRENExtractResult(BaseModel):
    """Complete SIREN extraction result."""

    company: CompanyData = Field(..., description="Main company data")
    facilities: list[FacilityData] = Field(default_factory=list)
    legal_unit_periods: list[CompanyLegalUnitPeriodData] = Field(default_factory=list)
    establishment_periods: list[FacilityEstablishmentPeriodData] = Field(
        default_factory=list
    )
    addresses: list[AddressData] = Field(default_factory=list)
    activity_classifications: list[ActivityClassificationData] = Field(
        default_factory=list
    )
    facility_ownerships: list[FacilityOwnershipData] = Field(default_factory=list)
    registry_records: list[ExternalRegistryRecordData] = Field(default_factory=list)
    extraction_metadata: dict[str, Any] = Field(default_factory=dict)

    def export_to_json(self, output_path: Path) -> None:
        """
        Export the extraction result to a JSON file.

        Args:
            output_path: Path to the output JSON file
        """
        import json

        # Convert to dict with proper serialization
        data = self.model_dump(mode="json")

        # Write to file with pretty formatting
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)

    def generate_summary(self, output_path: Path) -> None:
        """
        Generate a human-readable summary of the extraction result.

        Args:
            output_path: Path to the output summary file
        """
        summary_lines = [
            "SIREN Extraction Summary",
            "=" * 50,
            "",
            f"Company: {self.company.name}",
            f"SIREN: {self.company.identifiers[0].value if self.company.identifiers else 'N/A'}",
            f"Creation Date: {self.company.creation_date or 'N/A'}",
            "",
            "Data Summary:",
            "  - Companies: 1",
            f"  - Facilities: {len(self.facilities)}",
            f"  - Addresses: {len(self.addresses)}",
            f"  - Legal Unit Periods: {len(self.legal_unit_periods)}",
            f"  - Establishment Periods: {len(self.establishment_periods)}",
            f"  - Activity Classifications: {len(self.activity_classifications)}",
            f"  - Facility Ownerships: {len(self.facility_ownerships)}",
            f"  - Registry Records: {len(self.registry_records)}",
            "",
            "Facilities:",
        ]

        for facility in self.facilities[:10]:  # Show first 10 facilities
            hq_indicator = " (HQ)" if facility.is_headquarters else ""
            summary_lines.append(f"  - {facility.name}{hq_indicator}")

        if len(self.facilities) > 10:
            summary_lines.append(
                f"  ... and {len(self.facilities) - 10} more facilities"
            )

        summary_lines.extend(
            [
                "",
                "Activity Classifications:",
            ]
        )

        for activity in self.activity_classifications[:10]:  # Show first 10 activities
            summary_lines.append(
                f"  - {activity.scheme} {activity.code}: {activity.label}"
            )

        if len(self.activity_classifications) > 10:
            summary_lines.append(
                f"  ... and {len(self.activity_classifications) - 10} more activities"
            )

        summary_lines.extend(
            [
                "",
                "Extraction Metadata:",
                f"  - Extracted At: {self.extraction_metadata.get('extracted_at', 'N/A')}",
                f"  - Facility Count: {self.extraction_metadata.get('facility_count', 'N/A')}",
                "",
                "This data is ready for Django loading using the generated load script.",
            ]
        )

        # Write summary to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(summary_lines))
