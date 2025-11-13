"""A client library for accessing Sirene API"""

from .client import AuthenticatedClient
from .etl import (
    ETLConfig,
    SIRENExtractResult,
    ValidationMode,
    extract_and_transform_siren,
)

# Backwards compatibility alias
Client = AuthenticatedClient

__all__ = (
    "AuthenticatedClient",
    "Client",  # Alias to AuthenticatedClient
    "ETLConfig",
    "SIRENExtractResult",
    "ValidationMode",
    "extract_and_transform_siren",
)
