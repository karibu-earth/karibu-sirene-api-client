"""
External registry integration models.

This module contains country-agnostic models for integrating with external
company registries (SIRENE, Companies House, etc.) and provides structured
data management that works across different countries and regulatory systems.
"""

from __future__ import annotations

from typing import Any, cast

from django.contrib.gis.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from karibu.apps.core.models import (
    TimeFramedModel,
    TimeStampedModel,
    SoftDeletableModel,
)
from karibu.apps.core.validators import (
    validate_country_code,
    validate_scheme_value,
    validate_required_field,
)
from karibu.apps.company.constants import ACTIVITY_SCHEMES, LEGAL_FORM_SCHEMES

# Forward reference for type annotations
if False:
    from karibu.apps.company.models.core import Facility


class ActivityClassification(TimeFramedModel, TimeStampedModel):
    """
    Universal classification system for business activities (NAF, NACE, NAICS, etc.).

    Enables international expansion by abstracting activity taxonomies.
    Each scheme/code combination represents a unique activity classification.
    Uses TimeFramedModel for temporal validity (start/end dates).
    """

    scheme = models.CharField(
        _("scheme"),
        max_length=32,
        help_text=_(
            "Classification scheme name (e.g., 'NAFRev2', 'NACERev2', 'NAICS2017')."
        ),
    )
    code = models.CharField(
        _("code"),
        max_length=16,
        help_text=_("Activity code within the scheme."),
    )
    label = models.CharField(
        _("label"),
        max_length=255,
        help_text=_("Human-readable description of the activity."),
    )
    # Note: start and end fields are provided by TimeFramedModel

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("activity classification")
        verbose_name_plural = _("activity classifications")
        ordering = ["scheme", "code"]
        constraints = [
            models.UniqueConstraint(
                fields=["scheme", "code"],
                condition=models.Q(is_removed=False),
                name="unique_active_activity_classification",
            ),
            models.CheckConstraint(
                condition=models.Q(code__isnull=False)
                & ~models.Q(code="")
                & models.Q(label__isnull=False)
                & ~models.Q(label=""),
                name="activity_required_fields",
            ),
        ]
        indexes = [
            models.Index(fields=["scheme", "code"]),
            models.Index(fields=["scheme"]),
            # start/end indexes are automatically added by TimeFramedModel
            models.Index(fields=["created"]),
        ]
        db_table = "company_activity_classification"

    def __str__(self) -> str:
        return f"{self.scheme} {self.code}: {self.label}"

    def clean(self) -> None:
        """Validate activity classification data."""
        super().clean()

        # Validate scheme is in allowed schemes
        allowed_schemes = [scheme[0] for scheme in ACTIVITY_SCHEMES]
        validate_scheme_value(self.scheme, allowed_schemes)

        # Validate code format
        validate_required_field(self.code, "code")

        # Validate label
        validate_required_field(self.label, "label")

    def cascade_delete(self) -> None:
        """
        No cascade needed for classification deletion.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        pass

    # Note: TimeFramedModel already provides:
    # - is_currently_valid() method
    # - clean() method with date validation
    # - Query methods: current(), valid_at(), etc.


class Address(TimeFramedModel, TimeStampedModel):
    """
    Single, time-framed address model for all entities.
    Replaces all other address fields and models.
    """

    # Core address components
    country = models.CharField(
        _("country"),
        max_length=2,
        validators=[validate_country_code],
        help_text=_("ISO 3166-1 alpha-2 country code."),
    )
    administrative_area = models.CharField(
        _("administrative area"),
        max_length=100,
        blank=True,
        help_text=_("State, province, region, or department."),
    )
    locality = models.CharField(
        _("locality"),
        max_length=100,
        blank=True,
        help_text=_("City or municipality."),
    )
    postal_code = models.CharField(
        _("postal code"),
        max_length=20,
        blank=True,
        help_text=_("Postal or ZIP code."),
    )
    street_address = models.CharField(
        _("street address"),
        max_length=255,
        blank=True,
        help_text=_("Street name and number (e.g., '123 Main Street')."),
    )

    # Unified coordinate system
    geom = models.PointField(
        _("location"),
        geography=True,
        null=True,
        blank=True,
        help_text=_("Geographic coordinates in WGS84 (EPSG:4326)."),
    )

    # Provider metadata for audit
    provider = models.CharField(
        _("provider"),
        max_length=50,
        blank=True,
        help_text=_("Address data provider (e.g., 'sirene', 'google')."),
    )

    # Entity relationship (facility-only)
    facility: models.ForeignKey[Facility] = models.ForeignKey(
        "company.Facility",
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("facility"),
        help_text=_("Facility address with temporal validity."),
    )

    # Django-generated foreign key ID attribute
    facility_id: Any

    # Geocoding metadata
    geocode_precision = models.CharField(
        _("geocode precision"),
        max_length=16,
        choices=[
            ("rooftop", _("Rooftop")),
            ("interpolated", _("Interpolated")),
            ("approximate", _("Approximate")),
            ("unknown", _("Unknown")),
        ],
        default="unknown",
        help_text=_("Precision level of the geocoding."),
    )

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ["country", "locality", "street_address"]
        constraints: list[models.BaseConstraint] = []
        indexes: list[models.Index] = [
            # Facility-based temporal queries (most common)
            models.Index(fields=["facility", "start", "end"]),
            # Geographic lookup pattern
            models.Index(fields=["country", "administrative_area", "locality"]),
            # Postal code lookup (often standalone)
            models.Index(fields=["postal_code"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "facility"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_address"

    def __str__(self) -> str:
        """Human-readable address representation."""
        parts = []
        if self.street_address:
            parts.append(self.street_address)
        if self.locality:
            parts.append(self.locality)
        if self.administrative_area:
            parts.append(self.administrative_area)
        if self.postal_code:
            parts.append(self.postal_code)
        if self.country:
            parts.append(self.country)

        return ", ".join(parts) if parts else str(_("Address"))

    def clean(self) -> None:
        """Validate address data."""
        super().clean()

        # At least one address component should be provided
        address_components = [
            self.street_address,
            self.locality,
            self.administrative_area,
            self.postal_code,
        ]

        if not any(component.strip() for component in address_components if component):
            raise ValidationError(_("At least one address component must be provided."))

        # Address must belong to a facility
        if not self.facility_id:
            raise ValidationError(_("Address must belong to a facility."))

    @property
    def latitude(self) -> float | None:
        """Get the latitude coordinate."""
        return self.geom.y if self.geom else None

    @property
    def longitude(self) -> float | None:
        """Get the longitude coordinate."""
        return self.geom.x if self.geom else None

    @property
    def coordinates(self) -> tuple[float, float] | None:
        """Get coordinates as (longitude, latitude) tuple."""
        if self.geom:
            return (self.geom.x, self.geom.y)
        return None

    def has_coordinates(self) -> bool:
        """Check if this address has geographic coordinates."""
        return self.geom is not None

    def get_overlap_filter(self) -> models.Q:
        """
        Addresses overlap if they belong to the same facility
        and have overlapping time periods.
        """
        if not self.facility_id:
            # If no facility, no overlap possible
            return models.Q(pk__isnull=True)
        return models.Q(facility=self.facility)

    def cascade_delete(self) -> None:
        """
        No cascade needed for address deletion.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        pass


class ExternalRegistrySource(SoftDeletableModel, TimeStampedModel):
    """
    Catalog of external registries (SIRENE, Companies House UK, ORBIS, etc.).

    Enables international expansion by maintaining a registry of data sources.
    Each source represents a specific registry/API with its configuration.
    """

    key = models.SlugField(
        _("key"),
        max_length=32,
        unique=True,
        help_text=_(
            "Unique identifier for the registry (e.g., 'sirene', 'companies-house')."
        ),
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Human-readable name of the registry."),
    )
    country = models.CharField(
        _("country"),
        max_length=2,
        null=True,
        blank=True,
        validators=[validate_country_code],
        help_text=_(
            "ISO 3166-1 alpha-2 country code. Null for multi-country registries."
        ),
    )
    version = models.CharField(
        _("version"),
        max_length=32,
        blank=True,
        help_text=_("API or schema version (e.g., '3.11')."),
    )
    base_url = models.URLField(
        _("base URL"),
        max_length=255,
        blank=True,
        help_text=_("Base URL for the registry API."),
    )

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("external registry source")
        verbose_name_plural = _("external registry sources")
        ordering = ["key"]
        constraints = [
            models.UniqueConstraint(
                fields=["key"],
                condition=models.Q(is_removed=False),
                name="unique_active_registry_source",
            )
        ]
        indexes = [
            models.Index(fields=["key"]),
            models.Index(fields=["country"]),
            models.Index(fields=["created"]),
        ]
        db_table = "company_external_registry_source"

    def __str__(self) -> str:
        return f"{self.key} ({self.name})"

    def cascade_delete(self) -> None:
        """
        Cascade delete related registry records.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        # Cast to help mypy understand the Django model relationships
        source_cast = cast(Any, self)
        # Soft delete all related records
        for record in source_cast.registry_records.filter(is_removed=False):
            record.delete()


class ExternalRegistryRecord(SoftDeletableModel, TimeStampedModel):
    """
    Raw payload storage for external registry data with audit trail.

    Stores complete responses from external registries for observability,
    replay capability, and bitemporal correctness. Essential for compliance
    and data lineage tracking.

    FUTURE OPTIMIZATION NOTES:
    =========================

    This model currently stores complete API responses in the payload field,
    which may lead to storage bloat over time. Consider implementing:

    1. PAYLOAD RETENTION POLICY:
       - Add payload_retention_days field (default: 365)
       - Implement archival job to move old payloads to S3/object storage
       - Keep only essential fields in main database after archival

    2. ESSENTIAL FIELDS EXTRACTION:
       - Create CompanyRegistryData/FacilityRegistryData models with only
         essential fields (legal_name, status, external_id, etc.)
       - Use these for common queries, keep payload for audit trail

    3. PERFORMANCE MONITORING:
       - Monitor query performance as dataset grows
       - Consider JSON field indexing if needed
       - Implement payload size limits if excessive growth detected

    4. COMPLIANCE CONSIDERATIONS:
       - Ensure archival strategy maintains audit trail requirements
       - Consider data retention policies for different jurisdictions
       - Document archival process for regulatory compliance

    Current Usage Analysis:
    - Payload field is used for: form validation, admin display, test factories
    - NOT used for: business logic processing, API responses, calculations
    - Storage impact: Minimal currently, but will grow with registry integration

    Implementation Priority: LOW (monitor and implement when storage/performance
    becomes an issue or when actively integrating multiple registries)
    """

    class EntityType(models.TextChoices):
        LEGAL_UNIT = "legal_unit", _("Legal Unit")
        ESTABLISHMENT = "establishment", _("Establishment")

    source = models.ForeignKey(
        ExternalRegistrySource,
        on_delete=models.CASCADE,
        related_name="registry_records",
        verbose_name=_("source"),
        help_text=_("The external registry source providing this data."),
    )
    entity_type = models.CharField(
        _("entity type"),
        max_length=32,
        choices=EntityType.choices,
        help_text=_("Type of entity (legal unit or establishment)."),
    )
    external_id = models.CharField(
        _("external ID"),
        max_length=64,
        help_text=_("Registry-specific identifier (SIREN, SIRET, etc.)."),
    )
    payload = models.JSONField(
        _("payload"),
        help_text=_("Complete response from the external registry."),
    )
    # TODO: Monitor payload field size and query performance
    # Consider archival when table size exceeds 1GB or average query time > 100ms
    payload_hash = models.CharField(
        _("payload hash"),
        max_length=64,
        help_text=_("SHA-256 hash of payload for deduplication."),
    )
    registry_updated_at = models.DateTimeField(
        _("registry updated at"),
        help_text=_("Last modification timestamp from the external registry."),
    )
    ingested_at = models.DateTimeField(
        _("ingested at"),
        auto_now_add=True,
        help_text=_("Timestamp when this record was created in our system."),
    )

    # Optional relationships - set when matched to existing entities
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="registry_records",
        verbose_name=_("company"),
        help_text=_("Matched company (for legal units)."),
    )
    facility = models.ForeignKey(
        "company.Facility",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="registry_records",
        verbose_name=_("facility"),
        help_text=_("Matched facility (for establishments)."),
    )

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("external registry record")
        verbose_name_plural = _("external registry records")
        ordering = ["-ingested_at", "-registry_updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["source", "entity_type", "external_id", "payload_hash"],
                condition=models.Q(is_removed=False),
                name="unique_active_registry_record",
            )
        ]
        indexes = [
            # Primary lookup pattern
            models.Index(fields=["source", "entity_type", "external_id"]),
            # Payload hash for deduplication
            models.Index(fields=["source", "payload_hash"]),
            # Registry update tracking
            models.Index(fields=["registry_updated_at", "source"]),
            # Ingestion tracking
            models.Index(fields=["ingested_at", "source"]),
            # Entity lookups
            models.Index(fields=["company", "source"]),
            models.Index(fields=["facility", "source"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "source"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_external_registry_record"

    def __str__(self) -> str:
        return f"{self.source.key} {self.entity_type} {self.external_id}"

    def cascade_delete(self) -> None:
        """
        No cascade needed for registry record deletion.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        pass


class CompanyLegalUnitPeriod(TimeFramedModel, TimeStampedModel):
    """
    Time-framed snapshots of legal unit data for companies.

    Stores temporal business data for companies including legal name, form,
    activity classification, and regulatory status during specific periods.
    Maps to SIRENE periodesUniteLegale for French companies.
    """

    class Status(models.TextChoices):
        ACTIVE = "active", _("Active")
        CEASED = "ceased", _("Ceased")

    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        related_name="legal_unit_periods",
        verbose_name=_("company"),
        help_text=_("The company this legal unit period belongs to."),
    )
    # start and end fields are provided by TimeFramedModel

    legal_name = models.CharField(
        _("legal name"),
        max_length=255,
        help_text=_("Official legal denomination of the company."),
    )
    legal_form_code = models.CharField(
        _("legal form code"),
        max_length=4,
        help_text=_(
            "Legal form classification code (e.g., SIRENE categorieJuridique)."
        ),
    )
    activity_code = models.ForeignKey(
        ActivityClassification,
        on_delete=models.PROTECT,
        related_name="company_periods",
        verbose_name=_("activity code"),
        help_text=_("Primary activity classification."),
    )
    activity_scheme = models.CharField(
        _("activity scheme"),
        max_length=32,
        choices=ACTIVITY_SCHEMES,
        help_text=_(
            "Activity classification scheme (e.g., 'NAFRev2', 'NACERev2', 'NAICS2017')."
        ),
    )

    legal_form_scheme = models.CharField(  # ✅ New field for internationalization
        _("legal form scheme"),
        max_length=32,
        choices=LEGAL_FORM_SCHEMES,
        help_text=_(
            "Legal form classification scheme (e.g., 'sirene', 'companies_house')."
        ),
    )
    status = models.CharField(
        _("status"),
        max_length=16,
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text=_("Administrative status of the legal unit."),
    )
    employee_band = models.CharField(
        _("employee band"),
        max_length=2,
        blank=True,
        help_text=_("Employee count band code (e.g., '01', '02')."),
    )
    employee_band_year = models.PositiveIntegerField(
        _("employee band year"),
        null=True,
        blank=True,
        help_text=_("Year for the employee count data."),
    )
    ess_flag = models.BooleanField(
        _("ESS flag"),
        null=True,
        blank=True,
        help_text=_("Social and Solidarity Economy flag (null if unknown)."),
    )
    mission_company_flag = models.BooleanField(
        _("mission company flag"),
        default=False,
        help_text=_("Whether this is a mission-driven company."),
    )
    # Note: start and end fields are provided by TimeFramedModel

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("company legal unit period")
        verbose_name_plural = _("company legal unit periods")
        ordering = ["company", "-start"]
        indexes = [
            # Primary temporal query pattern
            models.Index(fields=["company", "start", "end"]),
            # Status-based queries
            models.Index(fields=["company", "status"]),
            # Legal form lookup
            models.Index(fields=["legal_form_code", "start"]),
            # Activity code lookup
            models.Index(fields=["activity_code", "start"]),
            # Employee band filtering
            models.Index(fields=["employee_band_year", "company"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "company"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_legal_unit_period"

    def __str__(self) -> str:
        company_name = self.company.name if self.company else "Unknown Company"
        start_str = self.start.strftime("%Y-%m-%d") if self.start else "Unknown start"
        end_str = self.end.strftime("%Y-%m-%d") if self.end else "ongoing"
        return f"{company_name}: {self.legal_name} ({start_str} - {end_str})"

    def get_overlap_filter(self) -> models.Q:
        """Periods overlap if they belong to the same company."""
        # Handle case where company is not yet set (during form validation)
        if not hasattr(self, "company") or self.company is None:
            return models.Q(pk__isnull=True)  # Return empty queryset
        return models.Q(company=self.company)

    def cascade_delete(self) -> None:
        """
        No cascade needed for legal unit period deletion.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        pass


class FacilityEstablishmentPeriod(TimeFramedModel, TimeStampedModel):
    """
    Time-framed snapshots of establishment data for facilities.

    Stores temporal establishment data including status, activity classification,
    HQ flag, and opening date during specific periods.
    Maps to SIRENE periodesEtablissement for French facilities.
    """

    class Status(models.TextChoices):
        ACTIVE = "active", _("Active")
        CLOSED = "closed", _("Closed")

    facility = models.ForeignKey(
        "company.Facility",
        on_delete=models.CASCADE,
        related_name="establishment_periods",
        verbose_name=_("facility"),
        help_text=_("The facility this establishment period belongs to."),
    )
    status = models.CharField(
        _("status"),
        max_length=16,
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text=_("Administrative status of the establishment (active/closed)."),
    )
    activity_code = models.ForeignKey(
        ActivityClassification,
        on_delete=models.PROTECT,
        related_name="facility_periods",
        verbose_name=_("activity code"),
        help_text=_("Primary activity classification for this establishment period."),
    )
    activity_scheme = models.CharField(
        _("activity scheme"),
        max_length=32,
        choices=ACTIVITY_SCHEMES,
        help_text=_(
            "Activity classification scheme (e.g., 'NAFRev2', 'NACERev2', 'NAICS2017')."
        ),
    )
    is_hq = models.BooleanField(
        _("is headquarters"),
        default=False,
        help_text=_(
            "Whether this establishment serves as headquarters during this period."
        ),
    )
    opening_date = models.DateField(
        _("opening date"),
        null=True,
        blank=True,
        help_text=_("Date when the establishment was created/opened."),
    )
    # Note: start and end fields are provided by TimeFramedModel

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("facility establishment period")
        verbose_name_plural = _("facility establishment periods")
        ordering = ["facility", "-start"]
        indexes = [
            # Primary temporal query pattern
            models.Index(fields=["facility", "start", "end"]),
            # Status filtering with temporal
            models.Index(fields=["facility", "status", "start"]),
            # Activity code lookup
            models.Index(fields=["activity_code", "start"]),
            # HQ filtering (less common, simpler index)
            models.Index(fields=["is_hq", "facility"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "facility"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_facility_establishment_period"

    def __str__(self) -> str:
        """Human-readable representation of the establishment period."""
        # Handle potential None values for datetime fields
        start_str = self.start.strftime("%Y-%m-%d") if self.start else "unknown"
        period_display = f"{start_str} - "
        if self.end:
            period_display += self.end.strftime("%Y-%m-%d")
        else:
            period_display += "ongoing"

        hq_display = " (HQ)" if self.is_hq else ""
        # Cast to help mypy understand the Django choices method
        period_cast = cast(Any, self)
        return f"{self.facility}: {period_cast.get_status_display()}{hq_display} ({period_display})"

    def get_overlap_filter(self) -> models.Q:
        """Periods overlap if they belong to the same facility."""
        # Handle case where facility is not yet set (during form validation)
        if not hasattr(self, "facility") or self.facility is None:
            return models.Q(pk__isnull=True)  # Return empty queryset
        return models.Q(facility=self.facility)

    def cascade_delete(self) -> None:
        """
        No cascade needed for establishment period deletion.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        pass

    # Note: TimeFramedModel already provides:
    # - is_currently_valid() method
    # - clean() method with date validation
    # - Query methods: current(), valid_at(), etc.
