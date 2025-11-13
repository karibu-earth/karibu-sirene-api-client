.PHONY: help test test-unit test-integration test-e2e coverage lint format type-check security pre-commit-install pre-commit-run clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ==============================================================================
# TESTING COMMANDS (TDD Policy)
# ==============================================================================

test: ## Run full test suite with coverage (90% threshold)
	uv run pytest -v --cov=sirene_api_client --cov-report=term-missing --cov-report=html --cov-report=xml --cov-fail-under=90

test-unit: ## Run unit tests only (fast feedback)
	uv run pytest -v -m unit --cov=sirene_api_client --cov-report=term-missing

test-integration: ## Run integration tests (with mocked APIs)
	uv run pytest -v -m integration --cov=sirene_api_client --cov-report=term-missing

test-e2e: ## Run end-to-end tests (full workflows)
	uv run pytest -v -m e2e --cov=sirene_api_client --cov-report=term-missing

test-watch: ## Run tests in watch mode (TDD workflow)
	uv run pytest-watch -v --cov=sirene_api_client

coverage-report: ## Generate and open HTML coverage report
	uv run pytest --cov=sirene_api_client --cov-report=html
	@echo "Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ==============================================================================
# CODE QUALITY COMMANDS
# ==============================================================================

lint: ## Run ruff linter
	uv run ruff check sirene_api_client tests

format: ## Format code with ruff
	uv run ruff format sirene_api_client tests

format-check: ## Check formatting without changes
	uv run ruff format --check sirene_api_client tests

type-check: ## Run mypy static type checking
	uv run mypy sirene_api_client

# ==============================================================================
# SECURITY COMMANDS
# ==============================================================================

security: ## Run security scans (bandit + pip-audit)
	uv run bandit -c pyproject.toml -r sirene_api_client
	uv pip audit

security-baseline: ## Update detect-secrets baseline
	uv run detect-secrets scan --baseline .secrets.baseline

# ==============================================================================
# PRE-COMMIT COMMANDS
# ==============================================================================

pre-commit-install: ## Install pre-commit hooks
	uv pip install pre-commit
	uv run pre-commit install

pre-commit-run: ## Run all pre-commit hooks on all files
	uv run pre-commit run --all-files

pre-commit-update: ## Update pre-commit hook versions
	uv run pre-commit autoupdate

pre-commit-develop: ## Run comprehensive checks before pushing to develop
	@echo "Running comprehensive pre-commit checks for develop branch..."
	uv run pre-commit run --all-files
	@echo "✅ All checks passed! Safe to push to develop."

pre-commit-main: ## Run comprehensive checks before PR to main
	@echo "Running comprehensive pre-commit checks for main branch PR..."
	uv run pre-commit run --all-files
	make test
	@echo "✅ All checks passed! Safe to create PR to main."

# ==============================================================================
# UTILITY COMMANDS
# ==============================================================================

clean: ## Clean build artifacts and cache
	rm -rf build/ dist/ *.egg-info htmlcov/ .coverage coverage.xml .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

install-dev: ## Install development dependencies
	uv pip install -e ".[dev]"

build: ## Build distribution packages
	uv build

all: clean lint type-check security test ## Run all quality checks and tests
