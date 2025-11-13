# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to a versioning strategy aligned with the SIRENE API version.

**Versioning Strategy:**

- Major.minor version (e.g., 3.11) aligns with SIRENE API version for compatibility identification
- Patch version (e.g., 3.11.2) represents client library changes (features and fixes)
- This ensures users can quickly identify which SIRENE API version the client supports

## [3.11.2] - 2025-11-04

### Added

- **Optional strict range check for Lambert 93 coordinate conversion**
  - Added `strict_range_check` parameter (default: `False`) to `lambert93_to_wgs84()` function
  - Default non-strict mode allows conversion of coordinates outside typical Lambert 93 range
  - Supports handling overseas French territories (Réunion, Guadeloupe, Martinique, French Guiana) that may be mislabeled as Lambert 93 but use different coordinate reference systems
  - Strict mode (`strict_range_check=True`) preserves original behavior for validation needs

### Changed

- **Coordinate Conversion**: Default behavior now attempts conversion for out-of-range coordinates with warning logs instead of raising exceptions
- **ETL Pipeline**: No longer crashes on overseas territory coordinates; gracefully handles edge cases

### Documentation

- Updated `ETL_README.md` with "Range Check Behavior" section explaining strict vs non-strict modes
- Added versioning policy documentation to `CONTRIBUTING.md`

## [3.11.1] - 2025-10-24

- **Explicit SIRET-based address-facility linking** for reliable data relationships
- **Improved facility name extraction** with proper priority ordering
- **Address-facility matching demonstration script** showing explicit SIRET-based linking

### Changed

- **ETL Data Extraction**: Enhanced address-facility relationship handling
  - Added `facility_siret` field to `AddressData` model for explicit linking
  - Updated `transform_address()` method to accept facility parameter
  - Improved facility name extraction prioritizing establishment-specific names over company names
  - Replaced positional matching with explicit SIRET-based address-facility relationships

## [3.11.0] - 2025-10-18

### Added

- Complete SIRENE API client implementation
- ETL service for comprehensive data extraction and transformation
- Support for both synchronous and asynchronous operations
- Type-safe Pydantic models for all API responses
- Coordinate conversion from Lambert 93 to WGS84
- Django integration models and patterns
- Progress tracking for large data extractions
- GDPR compliance controls for personal data handling
- Comprehensive test suite with 90% coverage requirement
- Makefile commands for all development operations
- Pre-commit hooks for code quality enforcement
- Security scanning with bandit and pip-audit
- Comprehensive README documentation with real SIRENE API examples
- CONTRIBUTING.md with development guidelines
- Apache 2.0 license file
- Documentation roadmap for future enhancements

### API Features

- **API Client**: Full support for SIRENE API v3 endpoints
  - Unité Légale (legal entity) queries by SIREN
  - Établissement (establishment) queries by SIRET
  - Multi-criteria search capabilities
  - Service information endpoints

- **ETL Service**: Complete data extraction and transformation
  - Extract company data with all historical periods
  - Extract all associated establishments
  - Transform data to Django-ready models
  - Coordinate conversion for geospatial applications
  - Audit trail creation for compliance
  - Streaming extraction for large datasets
  - Progress callbacks for real-time updates

- **Data Models**: Comprehensive Pydantic models
  - Type-safe API response models
  - Django-compatible ETL output models
  - Full validation and serialization support
  - Coordinate and address models with geospatial support

- **Integration Support**:
  - Django model mapping
  - Celery task integration
  - HTMX progress tracking
  - Two-phase loading patterns

### Technical Details

- **Python Support**: 3.13+ (tested up to 3.13)
- **Dependencies**: httpx, attrs, pydantic, pyproj, python-dateutil
- **Testing**: pytest with async support, 90% coverage threshold
- **Code Quality**: ruff linting, mypy type checking, black formatting
- **Security**: bandit security scanning, pip-audit vulnerability checks

### Configuration

- ETL validation modes: STRICT, LENIENT, PERMISSIVE
- GDPR compliance controls
- Configurable coordinate precision
- Retry and timeout configuration
- SSL verification controls

### Examples

- Basic API usage examples
- ETL service examples
- Django integration patterns
- Celery + HTMX integration
- Async/await patterns
- Error handling examples
