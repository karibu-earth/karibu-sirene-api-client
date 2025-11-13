# sirene-api-client

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)](htmlcov/index.html)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-black.svg)](https://github.com/astral-sh/ruff)
[![Type Checking](https://img.shields.io/badge/type%20checking-mypy%20strict-blue.svg)](https://github.com/karibu-earth/sirene-api-client/actions)
[![Security](https://img.shields.io/badge/security-bandit%20%2B%20pip--audit-green.svg)](https://bandit.readthedocs.io/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![CI/CD](https://github.com/karibu-earth/sirene-api-client/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/karibu-earth/sirene-api-client/actions)

A professional Python client for the [French SIRENE API](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee) provided by [INSEE](https://www.insee.fr/) (Institut National de la Statistique et des Études Économiques).

The SIRENE database is France's official business registry, containing comprehensive information on over 19 million businesses and 27 million establishments since 1973. This library provides both low-level API access and high-level ETL services for extracting, transforming, and integrating French business registry data into your applications.

## About SIRENE

**SIRENE** (Système d'Identification du Répertoire des Entreprises) is the official French business identification system managed by INSEE. It provides:

- **SIREN**: 9-digit identifier for legal entities (companies)
- **SIRET**: 14-digit identifier for establishments (physical locations)
- **Complete business histories**: Status changes, mergers, acquisitions, and closures
- **Geographic data**: Addresses and coordinates for all establishments

This client library is **not affiliated with or endorsed by INSEE** - it's an independent tool to help developers access and utilize the SIRENE API effectively.

## Features

- **Complete SIREN/SIRET Data Access**: Query French business registry data by SIREN (legal entity) or SIRET (establishment)
- **ETL Service**: Extract, transform, and load complete company histories with all associated establishments
- **Type-Safe Models**: Full Pydantic model support with comprehensive type hints
- **Async/Sync Support**: Both synchronous and asynchronous API clients
- **Coordinate Conversion**: Automatic Lambert 93 to WGS84 coordinate transformation
- **Django Integration**: Ready-to-use models for Django applications
- **Progress Tracking**: Real-time progress updates for large data extractions
- **GDPR Compliance**: Built-in personal data handling controls

## Installation

### From PyPI (when published)

```bash
pip install sirene-api-client
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/karibu-earth/sirene-api-client.git
cd sirene-api-client

# Install with uv (recommended)
uv pip install -e ".[dev]"

# Or with pip
pip install -e ".[dev]"
```

## Quick Start

### 1. Get Your INSEE API Token

First, register at [api.insee.fr](https://api.insee.fr) to get your API token.

### 2. Basic API Usage

```python
from sirene_api_client import AuthenticatedClient
from sirene_api_client.api.unite_legale.find_by_siren import sync as find_by_siren
from sirene_api_client.api.etablissement.find_by_siret import sync as find_by_siret

# Create authenticated client
client = AuthenticatedClient(token="your_insee_api_token_here")

# Find a company by SIREN
with client as client:
    response = find_by_siren.sync(client=client, siren="123456782")
    if response and response.unite_legale:
        company = response.unite_legale[0]
        print(f"Company: {company.denomination_unite_legale}")
        print(f"SIREN: {company.siren}")

# Find an establishment by SIRET
with client as client:
    response = find_by_siret.sync(client=client, siret="12345678200012")
    if response and response.etablissement:
        establishment = response.etablissement[0]
        print(f"Establishment: {establishment.denomination_usuelle_etablissement}")
        print(f"SIRET: {establishment.siret}")
```

### 3. Async Usage

```python
import asyncio
from sirene_api_client import AuthenticatedClient
from sirene_api_client.api.unite_legale.find_by_siren import asyncio as find_by_siren_async

async def main():
    client = AuthenticatedClient(token="your_insee_api_token_here")

    async with client as client:
        response = await find_by_siren_async(client=client, siren="123456782")
        if response and response.unite_legale:
            company = response.unite_legale[0]
            print(f"Company: {company.denomination_unite_legale}")

asyncio.run(main())
```

## ETL Service

For complete data extraction with transformation, use the ETL service:

```python
import asyncio
from sirene_api_client import AuthenticatedClient, extract_and_transform_siren, ETLConfig, ValidationMode

async def main():
    # Create API client
    client = AuthenticatedClient(token="your_token")

    # Configure ETL with lenient validation
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    # Extract and transform complete SIREN data
    result = await extract_and_transform_siren("123456782", client, config)

    # Access transformed data
    print(f"Company: {result.company.name}")
    print(f"SIREN: {result.company.identifiers[0].value}")
    print(f"Facilities: {len(result.facilities)}")

    for facility in result.facilities:
        print(f"  - {facility.name} (SIRET: {facility.identifiers[0].value})")
        print(f"    Headquarters: {facility.is_headquarters}")

        # Show addresses linked to this facility
        facility_addresses = [addr for addr in result.addresses if addr.facility_siret == facility.identifiers[0].value]
        for address in facility_addresses:
            print(f"    Address: {address.street_address}")
            if address.longitude and address.latitude:
                print(f"    Coordinates: {address.longitude}, {address.latitude}")

asyncio.run(main())
```

For advanced ETL features including Django integration, progress tracking, and streaming extraction, see [ETL_README.md](ETL_README.md).

For a practical demonstration of address-facility matching with explicit SIRET-based linking, see [examples/address_facility_matching_demo.py](examples/address_facility_matching_demo.py).

## API Reference

### Core Endpoints

- **Unité Légale (Legal Entity)**:
  - `find_by_siren()` - Find company by SIREN number
  - `find_by_post_unite_legale()` - Search companies with criteria

- **Établissement (Establishment)**:
  - `find_by_siret()` - Find establishment by SIRET number
  - `find_by_post_etablissement()` - Search establishments with criteria

- **Informations**:
  - `informations()` - Get API service information

### Response Models

All API responses use Pydantic models with full type safety:

```python
from sirene_api_client.models.reponse_unite_legale import ReponseUniteLegale
from sirene_api_client.models.unite_legale import UniteLegale

# Response contains header and data
response: ReponseUniteLegale = find_by_siren.sync(client=client, siren="123456782")
if response.unite_legale:
    company: UniteLegale = response.unite_legale[0]
    # Access all company fields with type hints
```

## Configuration

### Client Configuration

```python
from sirene_api_client import AuthenticatedClient

client = AuthenticatedClient(
    token="your_token",
    timeout=30.0,  # Request timeout
    verify_ssl=True,  # SSL verification (recommended)
    headers={"User-Agent": "MyApp/1.0"},  # Custom headers
)
```

### ETL Configuration

```python
from sirene_api_client import ETLConfig, ValidationMode

config = ETLConfig(
    validation_mode=ValidationMode.LENIENT,  # STRICT, LENIENT, PERMISSIVE
    include_personal_data=False,  # GDPR compliance
    coordinate_precision="approximate",  # Coordinate conversion precision
    max_retries=3,  # API retry attempts
    timeout_seconds=30,  # Request timeout
)
```

## Error Handling

The client provides specific exception types for different error scenarios:

```python
from sirene_api_client import errors
from sirene_api_client.etl.exceptions import ETLError, ValidationError

try:
    response = find_by_siren.sync(client=client, siren="123456782")
except errors.UnexpectedStatusError as e:
    print(f"API returned unexpected status: {e.status_code}")
except errors.ClientError as e:
    print(f"Client error: {e}")
except ETLError as e:
    print(f"ETL error: {e}")
```

## Testing and Development

This project follows Test-Driven Development (TDD) principles with comprehensive test coverage.

### Running Tests

```bash
# Run all tests with coverage (90% threshold)
make test

# Run specific test types
make test-unit      # Fast unit tests
make test-integration  # Integration tests
make test-e2e       # End-to-end tests

# Generate coverage report
make coverage-report
```

### Code Quality

```bash
# Format code
make format

# Run linting
make lint

# Type checking
make type-check

# Security scanning
make security

# Run all quality checks
make all
```

## Quality Assurance

This project maintains high standards through comprehensive quality checks and automated testing.

### Quality Standards

- **Python Version**: Python 3.13 only (no backward compatibility)
- **Test Coverage**: 90% minimum threshold (enforced by CI/CD)
- **Code Style**: PEP 8 compliance via Ruff formatter
- **Type Safety**: Strict MyPy type checking
- **Security**: Bandit + pip-audit vulnerability scanning
- **Documentation**: Google-style docstrings required

### Quality Tools

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Ruff** | Linting & Formatting | PEP 8, line-length 88, Python 3.13 target |
| **MyPy** | Static Type Checking | Strict mode, no untyped defs, explicit optionals |
| **Bandit** | Security Linting | Scans for common security vulnerabilities |
| **pip-audit** | Dependency Security | Checks for known vulnerabilities in dependencies |
| **pytest** | Testing Framework | 90% coverage threshold, TDD enforcement |
| **detect-secrets** | Secret Detection | Prevents accidental secret commits |
| **markdownlint** | Documentation Quality | Ensures consistent Markdown formatting |

### Pre-commit Hooks

All quality checks are automated via pre-commit hooks that run before each commit:

```bash
# Install pre-commit hooks
make pre-commit-install

# Run all hooks manually
make pre-commit-run
```

**Automated Checks Include:**

- File integrity (trailing whitespace, line endings, large files)
- YAML/TOML/JSON syntax validation
- Cross-platform compatibility checks
- Python code linting and formatting (Ruff)
- Python syntax modernization (pyupgrade)
- Static type checking (MyPy)
- Security scanning (Bandit)
- Secret detection (detect-secrets)
- Documentation formatting (markdownlint)
- Dependency vulnerability audit (pip-audit)
- Test execution with coverage requirements

### CI/CD Pipeline

The GitHub Actions workflow enforces quality standards on production code:

- **Trigger**: Runs on pushes to `main` and pull requests to `main`
- **Python Version**: 3.13 only
- **Quality Gates**: All pre-commit hooks must pass
- **Coverage**: Tests must maintain 90% coverage
- **Release Process**: Manual via GitHub tags and releases

**Local Testing**: For develop branch, run `make pre-commit-develop` before pushing.

**Release Process**: See [RELEASE_PROCESS.md](.github/RELEASE_PROCESS.md) for detailed release workflow.

View the [CI/CD Pipeline](https://github.com/karibu-earth/sirene-api-client/actions) for current status.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Key requirements:

- Follow TDD principles (write tests first)
- Maintain 90% test coverage
- Use `make` commands for all operations
- Follow PEP 8 and project coding standards

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and migration notes.

## Documentation Roadmap

For planned documentation enhancements, see [DOCUMENTATION_TODO.md](DOCUMENTATION_TODO.md).

## Support

- **Issues**: Report bugs and request features on GitHub Issues
- **Documentation**: See [ETL_README.md](ETL_README.md) for advanced usage
- **API Reference**: All models and functions have comprehensive docstrings

## Related Projects

- [SIRENE API Documentation](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee)
- [INSEE API Portal](https://api.insee.fr)
