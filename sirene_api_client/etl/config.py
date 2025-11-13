"""
ETL configuration and validation settings.

This module provides configurable validation modes and settings for the SIREN ETL service.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ValidationMode(Enum):
    """Validation modes for ETL processing."""

    STRICT = "strict"
    """Strict validation - fail on any missing required fields or validation errors."""

    LENIENT = "lenient"
    """Lenient validation - warn on missing fields but continue processing."""

    PERMISSIVE = "permissive"
    """Permissive validation - ignore most validation errors and continue."""


@dataclass
class ETLConfig:
    """Configuration for SIREN ETL processing."""

    validation_mode: ValidationMode = ValidationMode.LENIENT
    """Validation mode for data processing."""

    include_personal_data: bool = False
    """Whether to include GDPR-sensitive personal data fields."""

    coordinate_precision: str = "approximate"
    """Precision level for converted coordinates (rooftop, interpolated, approximate, unknown)."""

    max_retries: int = 3
    """Maximum number of retries for API calls."""

    timeout_seconds: int = 30
    """Timeout for API calls in seconds."""

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if self.max_retries < 0:
            raise ValueError("max_retries must be non-negative")
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
