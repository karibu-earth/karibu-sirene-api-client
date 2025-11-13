# Contributing to sirene-api-client

Thank you for your interest in contributing to sirene-api-client! This document provides guidelines and instructions for contributing to the project.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Git

### Installation

1. **Fork and clone the repository**:

   ```bash
   git clone https://github.com/karibu-earth/sirene-api-client.git
   cd sirene-api-client
   ```

2. **Install development dependencies**:

   ```bash
   # With uv (recommended)
   uv pip install -e ".[dev]"

   # Or with pip
   pip install -e ".[dev]"
   ```

3. **Install pre-commit hooks**:

   ```bash
   make pre-commit-install
   ```

## Versioning Strategy

This project uses a versioning strategy aligned with the SIRENE API version:

- **Major.minor version** (e.g., `3.11`) aligns with the SIRENE API version for easy compatibility identification
- **Patch version** (e.g., `3.11.2`) represents client library changes (features and bug fixes)

This approach ensures users can quickly identify which SIRENE API version the client supports. When the SIRENE API releases a new major or minor version, the client version will be updated accordingly.

**Examples:**

- `3.11.1` → `3.11.2`: New feature or bug fix (compatible with SIRENE API 3.11)
- `3.11.2` → `3.12.0`: SIRENE API updated to 3.12 (new API version support)
- `3.12.0` → `4.0.0`: SIRENE API major version update (breaking changes)

## Development Workflow

### Test-Driven Development (TDD)

This project follows strict TDD principles. **All code must be written test-first**.

1. **Write a failing test** (RED phase)
2. **Implement minimal code to pass** (GREEN phase)
3. **Refactor while keeping tests green** (REFACTOR phase)

### Testing Requirements

- **Coverage Threshold**: 90% minimum (enforced by CI)
- **Test Types**: Unit (70%), Integration (20%), E2E (10%)
- **Test Isolation**: All tests must be deterministic and isolated
- **Mocking**: Mock all external I/O (HTTP calls, file system, etc.)

### Running Tests

```bash
# Run full test suite with coverage
make test

# Run specific test types
make test-unit        # Fast unit tests
make test-integration # Integration tests with mocked APIs
make test-e2e         # End-to-end tests

# Watch mode for TDD workflow
make test-watch

# Generate coverage report
make coverage-report
```

### Code Quality Standards

#### Formatting and Linting

```bash
# Format code
make format

# Check formatting
make format-check

# Run linting
make lint

# Type checking
make type-check

# Security scanning
make security

# Run all quality checks
make all
```

#### Code Style Requirements

- **PEP 8**: Strict adherence to Python style guidelines
- **Type Hints**: All public functions must have complete type annotations
- **Docstrings**: Google-style docstrings for all public interfaces
- **Import Sorting**: Automatic import organization with ruff
- **Line Length**: 88 characters (Black standard)

#### Design Principles

Follow these principles in all code:

- **KISS**: Keep It Simple, Stupid
- **DRY**: Don't Repeat Yourself
- **SOLID**: Single Responsibility and Dependency Inversion
- **YAGNI**: You Aren't Gonna Need It
- **Fail Fast**: Validate inputs early, explicit error handling

### Pre-commit Hooks

Pre-commit hooks automatically run on every commit:

- Code formatting (ruff)
- Linting (ruff)
- Type checking (mypy)
- Security scanning (bandit)
- Test execution

```bash
# Run pre-commit hooks manually
make pre-commit-run

# Update hook versions
make pre-commit-update
```

### Pre-Push Validation

#### Before Pushing to Develop

Run comprehensive local checks to ensure code quality:

```bash
# Run all pre-commit checks
make pre-commit-develop

# Or run full quality suite
make all
```

#### Before Creating PR to Main

Ensure all quality gates pass locally:

```bash
# Run comprehensive checks including full test suite
make pre-commit-main
```

**Important**: CI only runs on main branch. Local testing is mandatory for develop branch.

## Pull Request Process

### Before Submitting

1. **For develop branch**: Ensure local checks pass:

   ```bash
   make pre-commit-develop
   ```

2. **For main branch PR**: Run comprehensive validation:

   ```bash
   make pre-commit-main
   ```

3. **Update documentation** if needed:
   - Update docstrings for new/changed functions
   - Add examples to README if adding new features
   - Update CHANGELOG.md for user-facing changes

### Pull Request Guidelines

1. **Create a feature branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write tests first** (TDD requirement):
   - Add test files with `test_` prefix
   - Use `@pytest.mark.requirement("REQ-XXX")` for traceability
   - Ensure tests fail initially (RED phase)

3. **Implement minimal code** to make tests pass (GREEN phase)

4. **Refactor** while keeping tests green (REFACTOR phase)

5. **Commit with clear messages**:

   ``` text
   feat: add SIREN validation function
   fix: handle None values in coordinate conversion
   docs: update ETL examples
   test: add integration tests for extractor
   ```

6. **Submit pull request** with:
   - Clear description of changes
   - Reference to any related issues
   - Confirmation that all tests pass
   - Screenshots for UI changes (if applicable)

### Review Process

- All PRs require review from maintainers
- CI must pass all checks (tests, linting, type checking, security)
- Coverage must remain above 90%
- Code must follow project standards

## Issue Reporting

### Bug Reports

When reporting bugs, include:

1. **Environment details**:
   - Python version
   - Operating system
   - Package version

2. **Reproduction steps**:
   - Minimal code example
   - Expected vs actual behavior
   - Error messages/tracebacks

3. **Additional context**:
   - SIREN/SIRET numbers used (if applicable)
   - API token status (without sharing the token)

### Feature Requests

For feature requests:

1. **Describe the use case** and problem it solves
2. **Provide examples** of how the feature would be used
3. **Consider backwards compatibility** implications
4. **Check existing issues** to avoid duplicates

## Code Organization

### Project Structure

``` ascii
sirene_api_client/
├── api/                    # API endpoint modules
│   ├── etablissement/     # Establishment endpoints
│   ├── informations/      # Service info endpoints
│   └── unite_legale/      # Legal entity endpoints
├── etl/                   # ETL service modules
│   ├── config.py          # Configuration classes
│   ├── extractor.py       # Data extraction
│   ├── transformer.py     # Data transformation
│   └── models.py          # ETL data models
├── models/                # API response models
└── client.py              # HTTP client classes
```

### Adding New Features

1. **API Endpoints**: Add to appropriate `api/` subdirectory
2. **ETL Features**: Extend `etl/` modules
3. **Models**: Add to `models/` directory
4. **Tests**: Mirror structure in `tests/` directory

### Import Conventions

```python
# Standard library imports
import os
from typing import Any, Dict

# Third-party imports
import httpx
import pytest

# Local imports
from sirene_api_client.client import Client
from sirene_api_client.etl import ETLConfig
```

## Documentation

### Docstring Format

Use Google-style docstrings:

```python
def extract_siren_data(siren: str, client: Client) -> SIRENExtractResult:
    """Extract complete SIREN data with all establishments.

    This function orchestrates the complete ETL process for a single SIREN,
    including company data, all establishments, and coordinate conversion.

    Args:
        siren: SIREN number to extract (9-digit string)
        client: SIRENE API client instance

    Returns:
        SIRENExtractResult with all transformed data

    Raises:
        ValueError: If SIREN format is invalid
        ExtractionError: If API extraction fails

    Example:
        ```python
        result = await extract_siren_data("123456782", client)
        print(f"Company: {result.company.name}")
        print(f"Facilities: {len(result.facilities)}")
        ```
    """
```

### README Updates

When adding features:

1. **Update main README.md** with basic usage examples
2. **Update ETL_README.md** for ETL-specific features
3. **Add requirement markers** to tests for traceability

## Release Process

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

### Manual Release Workflow

For detailed release instructions, see [RELEASE_PROCESS.md](.github/RELEASE_PROCESS.md).

**Quick Release Steps**:

1. **Prepare Release**: Update version in `pyproject.toml` and `CHANGELOG.md`
2. **Create Tag**: Create annotated git tag (e.g., `git tag -a v3.12.0 -m "Release v3.12.0"`)
3. **Build Package**: Run `make build` to create distribution packages
4. **Create GitHub Release**:
   - Go to GitHub Releases page
   - Create new release from tag
   - Upload built packages from `dist/` directory
   - Add release notes from CHANGELOG.md
5. **Verify**: Test package installation from GitHub release

**Pre-Release Checklist**:

- [ ] All tests pass (`make test`)
- [ ] Coverage ≥ 90% (`make coverage-report`)
- [ ] Code quality checks pass (`make lint`, `make type-check`)
- [ ] Security scan clean (`make security`)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in `pyproject.toml`

### Changelog Updates

Update `CHANGELOG.md` for all releases:

1. **Add new version** under `[Unreleased]`
2. **Categorize changes**: Added, Changed, Deprecated, Removed, Fixed, Security
3. **Include migration notes** for breaking changes
4. **Move to version section** when releasing

## Getting Help

- **Documentation**: Check README.md and ETL_README.md
- **Issues**: Search existing GitHub issues
- **Discussions**: Use GitHub Discussions for questions
- **Code Review**: Ask for help in PR comments

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and improve
- Follow the [Python Community Code of Conduct](https://www.python.org/psf/conduct/)

Thank you for contributing to sirene-api-client!
