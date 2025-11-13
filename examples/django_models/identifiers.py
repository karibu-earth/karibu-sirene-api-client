"""
Company and facility identifier models.

This module contains models for tracking legal identifiers:
- CompanyIdentifier: Legal identifiers for companies (SIREN, VAT, etc.)
- FacilityIdentifier: Legal identifiers for facilities (SIRET, building permits, etc.)
"""

from __future__ import annotations

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from karibu.apps.core.models import BaseIdentifier
from karibu.apps.core.validators import (
    validate_siren,
    validate_siret,
    validate_country_code,
    validate_identifier_scheme,
)
from karibu.apps.company.constants import IDENTIFIER_SCHEMES

# Import Company and Facility from core module
from .core import Company, Facility


class CompanyIdentifier(BaseIdentifier):
    """
    Legal identifiers for companies (SIREN, VAT, etc.).

    This model extends BaseIdentifier with company-specific validation
    for different identifier schemes across countries.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="identifiers",
        verbose_name=_("company"),
    )

    # Override scheme field to add validators and company-specific help text
    scheme = models.CharField(
        _("scheme"),
        max_length=50,
        choices=IDENTIFIER_SCHEMES,
        validators=[validate_identifier_scheme],
        help_text=_("The identifier scheme (e.g., 'siren', 'siret', 'vat')."),
    )

    # Override country field to add validator
    country = models.CharField(
        _("country"),
        max_length=2,
        validators=[validate_country_code],
        help_text=_("ISO 3166-1 alpha-2 country code."),
    )

    class Meta:
        verbose_name = _("company identifier")
        verbose_name_plural = _("company identifiers")
        constraints = [
            models.UniqueConstraint(
                fields=["company", "scheme", "value"],
                condition=models.Q(is_removed=False),
                name="unique_active_company_identifier",
            ),
        ]
        indexes = [
            # Primary lookup pattern: company + scheme + value
            models.Index(fields=["company", "scheme", "value"]),
            # Normalized value lookup
            models.Index(fields=["scheme", "normalized_value"]),
            # Verification queries
            models.Index(fields=["is_verified", "company"]),
            # Country-based filtering
            models.Index(fields=["country", "scheme"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "company", "scheme"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_company_identifier"

    def clean(self) -> None:
        """Validate the identifier based on its scheme."""
        super().clean()
        # Company-specific validation: both SIREN and SIRET allowed
        if self.scheme == "siren" and self.value:
            validate_siren(self.value)
        elif self.scheme == "siret" and self.value:
            validate_siret(self.value)

    def _normalize_identifier(self, value: str) -> str:
        """Normalize identifier value for comparison."""
        if not value:
            return value

        # Get base normalization from parent
        normalized = super()._normalize_identifier(value)

        # For SIREN/SIRET, ensure it's numeric (company-specific)
        if self.scheme in ["siren", "siret"]:
            normalized = "".join(filter(str.isdigit, normalized))

        return normalized

    def cascade_delete(self) -> None:
        """No cascade needed for identifier deletion."""
        pass


class FacilityIdentifier(BaseIdentifier):
    """
    Legal identifiers for facilities (SIRET, building permits, etc.).

    This model extends BaseIdentifier with facility-specific validation
    for establishment-level identifiers.
    """

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="identifiers",
        verbose_name=_("facility"),
    )

    # Override scheme field to add validators and facility-specific help text
    scheme = models.CharField(
        _("scheme"),
        max_length=50,
        choices=IDENTIFIER_SCHEMES,
        validators=[validate_identifier_scheme],
        help_text=_("The identifier scheme (e.g., 'siret', 'vat', 'building_permit')."),
    )

    # Override country field to add validator
    country = models.CharField(
        _("country"),
        max_length=2,
        validators=[validate_country_code],
        help_text=_("ISO 3166-1 alpha-2 country code."),
    )

    class Meta:
        verbose_name = _("facility identifier")
        verbose_name_plural = _("facility identifiers")
        constraints = [
            models.UniqueConstraint(
                fields=["facility", "scheme", "value"],
                condition=models.Q(is_removed=False),
                name="unique_active_facility_identifier",
            ),
        ]
        indexes = [
            # Primary lookup pattern: facility + scheme + value
            models.Index(fields=["facility", "scheme", "value"]),
            # Normalized value lookup
            models.Index(fields=["scheme", "normalized_value"]),
            # Verification queries
            models.Index(fields=["is_verified", "facility"]),
            # Country-based filtering
            models.Index(fields=["country", "scheme"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "facility", "scheme"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_facility_identifier"

    def clean(self) -> None:
        """Validate the identifier based on its scheme."""
        super().clean()
        # Facility-specific validation: primarily SIRET
        if self.scheme == "siret" and self.value:
            validate_siret(self.value)

    def _normalize_identifier(self, value: str) -> str:
        """Normalize identifier value for comparison."""
        if not value:
            return value

        # Get base normalization from parent
        normalized = super()._normalize_identifier(value)

        # For SIRET, ensure it's numeric (facility-specific)
        if self.scheme == "siret":
            normalized = "".join(filter(str.isdigit, normalized))

        return normalized

    def cascade_delete(self) -> None:
        """No cascade needed for identifier deletion."""
        pass
