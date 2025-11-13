"""
Custom exceptions for the SIREN ETL service.

This module defines specific exception types for different ETL operations.
"""

from __future__ import annotations


class ETLError(Exception):
    """Base exception for ETL operations."""

    def __init__(self, message: str, details: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.details = details or {}


class ValidationError(ETLError):
    """Raised when data validation fails in strict mode."""

    def __init__(
        self, message: str, field: str | None = None, value: str | None = None
    ) -> None:
        details = {}
        if field:
            details["field"] = field
        if value:
            details["value"] = value
        super().__init__(message, details)


class CoordinateConversionError(ETLError):
    """Raised when coordinate conversion fails."""

    def __init__(
        self, message: str, x: str | None = None, y: str | None = None
    ) -> None:
        details = {}
        if x:
            details["x"] = x
        if y:
            details["y"] = y
        super().__init__(message, details)


class ExtractionError(ETLError):
    """Raised when API data extraction fails."""

    def __init__(
        self, message: str, siren: str | None = None, endpoint: str | None = None
    ) -> None:
        details = {}
        if siren:
            details["siren"] = siren
        if endpoint:
            details["endpoint"] = endpoint
        super().__init__(message, details)
        self.siren = siren
        self.endpoint = endpoint


class TransformationError(ETLError):
    """Raised when data transformation fails."""

    def __init__(
        self, message: str, entity_type: str | None = None, entity_id: str | None = None
    ) -> None:
        details = {}
        if entity_type:
            details["entity_type"] = entity_type
        if entity_id:
            details["entity_id"] = entity_id
        super().__init__(message, details)
