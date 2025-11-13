"""
Core company business entity models.

This module contains the fundamental business entities:
- Company: Primary tenant entity
- Facility: Physical locations
- FacilityOwnership: Temporal relationships between companies and facilities
"""

from __future__ import annotations

import uuid
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
from karibu.apps.core.validators import validate_name_field

# Forward reference for type annotations
if False:
    pass


class Company(SoftDeletableModel, TimeStampedModel):
    """
    Represents a company as the primary tenant in the system.

    According to Module 01 specification, Company is the core tenant entity
    with no hierarchical relationships. Each company is independent and
    represents a legal entity that can own facilities over time.
    """

    # Django automatically creates: id = models.BigAutoField(primary_key=True)

    # UUID for secure company creation process (prevents name enumeration)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        help_text=_("Unique identifier for secure company creation"),
    )

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("The legal name of the company."),
    )
    history = HistoricalRecords()

    # created and modified are automatically added by TimeStampedModel

    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(name__isnull=False) & ~models.Q(name=""),
                name="company_name_not_empty",
            ),
        ]
        indexes = [
            models.Index(fields=["name"]),
            # automatically added by TimeStampedModel
            models.Index(fields=["created"]),
            # For secure company creation lookups
            models.Index(fields=["uuid"]),
        ]
        db_table = "company_company"

    def __str__(self) -> str:
        return f"{self.name} - ({self.uuid})"

    def clean(self) -> None:
        """Validate company data."""
        super().clean()

        # Validate name using reusable validator
        validate_name_field(self.name, field_name="name")

    def cascade_delete(self) -> None:
        """
        Define cascade deletion behavior for this model.

        When a company is soft-deleted, all related data should also be soft-deleted
        to maintain consistency from a user perspective.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        # Soft-delete all related memberships
        self.memberships.all().soft_delete()  # type: ignore[attr-defined]

        # Soft-delete all related identifiers
        self.identifiers.all().soft_delete()  # type: ignore[attr-defined]

        # Soft-delete all facility ownerships (relationships)
        self.facility_ownerships.all().soft_delete()  # type: ignore[attr-defined]

    def get_deletion_warning(self) -> dict[str, Any]:
        """
        Get warning information about what will be deleted when this company is deleted.

        Returns:
            A dictionary containing warning information about the scope of deletion.
        """
        return {
            "title": _("Delete Company"),
            "message": _(
                "This will delete the company and all associated data including:"
            ),
            "items": [
                _("- All company memberships and user access"),
                _("- All company identifiers and verification data"),
                _("- All facility ownership relationships"),
                _("- All historical ownership records"),
            ],
            "recovery_note": _(
                "Note: This data can be recovered by administrators if needed."
            ),
            "confirmation_text": _(
                "I understand this action cannot be undone by regular users"
            ),
        }


class Facility(SoftDeletableModel, TimeStampedModel):
    """
    Represents a physical facility or establishment.

    Facilities are independent entities that can be owned by companies
    over time through the FacilityOwnership model. This allows for
    temporal ownership tracking.
    """

    # UUID for secure facility creation process (prevents name enumeration)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        help_text=_("Unique identifier for secure facility creation"),
    )

    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("The name of the facility."),
    )
    history = HistoricalRecords()

    # created and modified are automatically added by TimeStampedModel

    # Many-to-many relationship to Company through FacilityOwnership
    companies: models.ManyToManyField[Company, FacilityOwnership] = (
        models.ManyToManyField(
            Company,
            through="FacilityOwnership",
            related_name="facilities",
            verbose_name=_("companies"),
            help_text=_("Companies that own or operate this facility."),
        )
    )

    # Reverse relationship to addresses (Django-generated attribute)
    addresses: Any

    class Meta:
        verbose_name = _("facility")
        verbose_name_plural = _("facilities")
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(name__isnull=False) & ~models.Q(name=""),
                name="facility_name_not_empty",
            ),
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["uuid"]),
            # automatically added by TimeStampedModel
            models.Index(fields=["created"]),
        ]
        db_table = "company_facility"

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        """Validate facility data."""
        super().clean()

        # Validate name using reusable validator
        validate_name_field(self.name, field_name="name")

    def cascade_delete(self) -> None:
        """
        Define cascade deletion behavior for this model.

        When a facility is soft-deleted, all related data should also be soft-deleted
        to maintain consistency from a user perspective.

        CASCADING BEHAVIOR:
        - All active facility ownership relationships are automatically soft-deleted
        - This prevents orphaned relationships and ensures clean deletion
        - Historical data is preserved through soft deletion
        - Facility identifiers are also soft-deleted for consistency

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        # Soft-delete all facility ownerships (relationships)
        self.company_ownerships.all().soft_delete()  # type: ignore[attr-defined]

        # Soft-delete all facility identifiers
        self.identifiers.all().soft_delete()  # type: ignore[attr-defined]

    def get_deletion_warning(self) -> dict[str, Any]:
        """
        Get warning information about what will be deleted when this facility is deleted.

        Returns:
            A dictionary containing warning information about the scope of deletion.
        """
        return {
            "title": _("Delete Facility"),
            "message": _(
                "This will delete the facility and all associated data including:"
            ),
            "items": [
                _("- All facility ownership relationships (automatically removed)"),
                _("- All facility identifiers and verification data"),
                _("- All historical ownership records"),
            ],
            "recovery_note": _(
                "Note: This data can be recovered by administrators if needed."
            ),
            "confirmation_text": _(
                "I understand this action cannot be undone by regular users"
            ),
        }


class FacilityOwnership(TimeFramedModel, TimeStampedModel):
    """
    Temporal relationship between a company and a facility.

    This model tracks when a company owns or operates a facility,
    allowing for historical ownership tracking and compliance reporting.

    DESIGN DECISION: We use TimeFramedModel's built-in functionality completely.
    This includes:
    - 'start' and 'end' fields for temporal validity
    - Built-in methods to check if a record is currently active

    - 'start' field: Date when the company started owning/operating this facility
    - 'end' field: Date when the company stopped owning/operating this facility (nullable)
    - 'created' and 'modified' fields: Provided by TimeStampedModel for audit trails
    """

    class Role(models.TextChoices):
        """Role of the company in the facility relationship."""

        OWNER = "owner", _("Owner")
        OPERATOR = "operator", _("Operator")
        TENANT = "tenant", _("Tenant")
        MANAGER = "manager", _("Manager")
        PARTNER = "partner", _("Partner")

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="facility_ownerships",
        verbose_name=_("company"),
    )
    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="company_ownerships",
        verbose_name=_("facility"),
    )
    role = models.CharField(
        _("role"),
        max_length=16,
        choices=Role.choices,
        default=Role.OWNER,
        help_text=_("Role of the company in this facility relationship."),
    )
    # Note: 'start' and 'end' fields are automatically provided by TimeFramedModel

    history = HistoricalRecords()

    # created and modified are automatically added by TimeStampedModel

    class Meta:
        verbose_name = _("facility ownership")
        verbose_name_plural = _("facility ownerships")
        constraints = [
            models.UniqueConstraint(
                fields=["company", "facility", "start", "role"],
                condition=models.Q(is_removed=False),
                name="unique_active_facility_ownership",
            ),
        ]
        indexes = [
            # Primary temporal query: company+temporal filter
            models.Index(fields=["company", "start", "end"]),
            # Facility-based temporal query
            models.Index(fields=["facility", "start", "end"]),
            # Role-filtered temporal query
            models.Index(fields=["company", "role", "start", "end"]),
            # Soft deletion filter
            models.Index(fields=["is_removed", "company", "start"]),
            # Audit/ordering
            models.Index(fields=["created"]),
        ]
        db_table = "company_facility_ownership"

    def __str__(self) -> str:
        end_text = f" to {self.end}" if self.end else " (current)"
        # Cast to help mypy understand the Django-generated get_role_display method
        role_display = cast(Any, self).get_role_display()
        return (
            f"{self.company} {role_display} {self.facility} from {self.start}{end_text}"
        )

    def clean(self) -> None:
        """Validate date ranges for business logic."""
        super().clean()
        if self.end and self.start and self.end < self.start:
            raise ValidationError({"end": _("End date must be after start date.")})

    def cascade_delete(self) -> None:
        """
        Define cascade deletion behavior for this model.

        FacilityOwnership is a relationship model that connects companies and facilities.
        When a facility ownership is deleted, it only removes the relationship between
        the company and facility, but doesn't delete the underlying company or facility
        entities. Therefore, no cascade deletion is needed.

        IMPORTANT: This method should ONLY soft-delete related objects and should
        NOT mark the current object as removed (i.e., should not set
        self.is_removed = True). The parent object's is_removed flag is handled
        by the calling soft_delete() method to avoid double-soft-deletion.
        """
        # No cascade needed for ownership deletion
        pass
