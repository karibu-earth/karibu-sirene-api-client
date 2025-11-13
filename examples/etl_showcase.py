"""
ETL Showcase Script with Progressive Loading

A standalone script demonstrating the complete SIRENE ETL pipeline optimized for
Django+Celery translation (without actually using them). Supports both name-based
search and direct SIREN lookup, with progressive facility extraction for companies
with many establishments.

Features:
- Name search → SIREN resolution → complete extraction
- Direct SIREN → complete extraction
- Progressive facility extraction with real-time progress updates
- Consolidated JSON output ready for Django atomic loading
- Cache simulation with Redis-compatible patterns
- Django transaction preview and load script generation

Usage:
    python examples/etl_showcase.py

Requirements:
    - sirene-api-client
    - pyproj (for coordinate conversion)
    - asyncio (built-in)
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
from dotenv import load_dotenv
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, Optional
from dataclasses import dataclass

from sirene_api_client import AuthenticatedClient, ETLConfig, ValidationMode
from sirene_api_client.etl.extractor import SIRENExtractor
from sirene_api_client.etl.transformer import SIRENTransformer
from sirene_api_client.etl.models import SIRENExtractResult
from sirene_api_client.api.etablissement.find_by_get_etablissement import (
    asyncio as find_by_get_etablissement,
)
from sirene_api_client.api.unite_legale.find_by_get_unite_legale import (
    asyncio as find_by_get_unite_legale,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()

API_TOKEN = os.getenv("SIRENE_API_TOKEN")

if not API_TOKEN:
    raise ValueError("SIRENE_API_TOKEN environment variable is not set")


@dataclass
class CompanySearchResult:
    """Result from company name search."""

    siren: str
    name: str
    facility_count: int
    is_active: bool
    legal_form: Optional[str] = None
    creation_date: Optional[date] = None


class NameToSIRENResolver:
    """Resolve company names to SIREN numbers using SIRENE API."""

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize resolver with SIRENE API client."""
        self.client = client

    async def search_company_by_name(self, name: str) -> list[CompanySearchResult]:
        """
        Search for companies by name and return SIREN candidates.

        Args:
            name: Company name to search for

        Returns:
            List of CompanySearchResult objects

        Raises:
            Exception: If API call fails
        """
        logger.info(f"Searching for companies with name: {name}")

        try:
            # Use the /siret endpoint with correct syntax for name search
            query = f'denominationUniteLegale:"{name}"'

            # Call API
            response = await find_by_get_etablissement(
                q=query,
                nombre=10,  # Limit to 10 results
                debut=0,
                client=self.client,
            )

            if not response or not response.etablissements:
                logger.info(f"No companies found for name: {name}")
                return []

            # Convert to CompanySearchResult objects
            # Group by SIREN to avoid duplicates
            seen_sirens = set()
            results = []

            for etab in response.etablissements:
                siren = str(etab.siren)
                if siren in seen_sirens:
                    continue
                seen_sirens.add(siren)

                # Get company name from unite_legale
                company_name = "Unknown"
                if etab.unite_legale and etab.unite_legale.denomination_unite_legale:
                    company_name = etab.unite_legale.denomination_unite_legale

                result = CompanySearchResult(
                    siren=siren,
                    name=company_name,
                    facility_count=1,  # We'll get accurate count later
                    is_active=etab.unite_legale.etat_administratif_unite_legale == "A"
                    if etab.unite_legale
                    else True,
                    legal_form=etab.unite_legale.categorie_juridique_unite_legale
                    if etab.unite_legale
                    else None,
                    creation_date=etab.unite_legale.date_creation_unite_legale
                    if etab.unite_legale
                    else None,
                )
                results.append(result)

            # Get accurate facility counts for each SIREN
            for result in results:
                try:
                    facility_count = await self._get_facility_count(result.siren)
                    result.facility_count = facility_count
                except Exception as e:
                    logger.warning(
                        f"Could not get facility count for SIREN {result.siren}: {e}"
                    )
                    result.facility_count = 1  # Default to 1

            logger.info(f"Found {len(results)} companies for name: {name}")
            return results

        except Exception as e:
            logger.error(f"Failed to search companies by name '{name}': {e}")
            raise

    async def _get_facility_count(self, siren: str) -> int:
        """
        Get the total number of facilities for a SIREN.

        Args:
            siren: SIREN number

        Returns:
            Total facility count
        """
        try:
            # Use /siret endpoint to get facility count
            response = await find_by_get_etablissement(
                q=f"siren:{siren}",
                nombre=1,  # Only need count
                debut=0,
                client=self.client,
            )

            if response and response.header:
                return int(response.header.total) if response.header.total else 0
            return 0

        except Exception as e:
            logger.warning(f"Could not get facility count for SIREN {siren}: {e}")
            return 0

    def validate_siren_format(self, siren: str) -> bool:
        """
        Validate SIREN format.

        Args:
            siren: SIREN string to validate

        Returns:
            True if valid SIREN format, False otherwise
        """
        if not siren or not isinstance(siren, str):
            return False

        siren = siren.strip()
        return len(siren) == 9 and siren.isdigit()


class CacheSimulator:
    """Simulate Redis cache behavior for demonstration purposes."""

    def __init__(self) -> None:
        """Initialize cache simulator."""
        self._cache: dict[str, dict[str, Any]] = {}
        self._stats = {"hits": 0, "misses": 0, "sets": 0, "deletes": 0}

    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """
        Set cache value with TTL.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds
        """
        self._cache[key] = {
            "value": value,
            "expires_at": time.time() + ttl,
        }
        self._stats["sets"] += 1
        logger.debug(f"Cache SET: {key} (TTL: {ttl}s)")

    def get(self, key: str) -> Any:
        """
        Get cache value.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found/expired
        """
        if key not in self._cache:
            self._stats["misses"] += 1
            logger.debug(f"Cache MISS: {key}")
            return None

        entry = self._cache[key]
        if time.time() > entry["expires_at"]:
            # Expired
            del self._cache[key]
            self._stats["misses"] += 1
            logger.debug(f"Cache EXPIRED: {key}")
            return None

        self._stats["hits"] += 1
        logger.debug(f"Cache HIT: {key}")
        return entry["value"]

    def delete(self, key: str) -> None:
        """
        Delete cache key.

        Args:
            key: Cache key to delete
        """
        if key in self._cache:
            del self._cache[key]
            self._stats["deletes"] += 1
            logger.debug(f"Cache DELETE: {key}")

    def clear(self) -> None:
        """Clear all cache entries."""
        self._cache.clear()
        logger.debug("Cache CLEARED")

    def get_stats(self) -> dict[str, Any]:
        """
        Get cache statistics.

        Returns:
            Dictionary with cache statistics
        """
        total_keys = len(self._cache)
        memory_usage = sum(len(str(entry["value"])) for entry in self._cache.values())

        return {
            "total_keys": total_keys,
            "memory_usage": memory_usage,
            "hits": self._stats["hits"],
            "misses": self._stats["misses"],
            "hit_rate": (
                self._stats["hits"] / (self._stats["hits"] + self._stats["misses"])
                if (self._stats["hits"] + self._stats["misses"]) > 0
                else 0
            ),
            "sets": self._stats["sets"],
            "deletes": self._stats["deletes"],
        }


class ProgressiveETLOrchestrator:
    """Orchestrate progressive ETL extraction with streaming facilities."""

    def __init__(self, client: AuthenticatedClient, config: ETLConfig) -> None:
        """Initialize orchestrator with client and configuration."""
        self.client = client
        self.config = config
        self.extractor = SIRENExtractor(client, config)
        self.transformer = SIRENTransformer(config)
        self.cache = CacheSimulator()

    async def extract_with_progress(
        self,
        siren: str,
        progress_callback: Optional[Callable[[dict[str, Any]], None]] = None,
    ) -> SIRENExtractResult:
        """
        Extract complete SIREN data with progress tracking.

        Phase 1: Extract company info (immediate feedback)
        Phase 2: Stream facilities in batches with progress updates
        Phase 3: Transform and consolidate all data

        Args:
            siren: SIREN number to extract
            progress_callback: Optional callback for progress updates

        Returns:
            Complete SIRENExtractResult

        Raises:
            Exception: If extraction fails
        """
        logger.info(f"Starting progressive extraction for SIREN: {siren}")

        # Phase 1: Extract company info immediately
        if progress_callback:
            progress_callback(
                {
                    "phase": "company_extraction",
                    "message": f"Fetching company info for SIREN {siren}...",
                    "progress": 0,
                }
            )

        company_data, facility_count = await self.extract_company_only(siren)

        if progress_callback:
            # Get company name from periods (UniteLegale has name in periods)
            company_name = "Unknown"
            if (
                company_data.periodes_unite_legale
                and len(company_data.periodes_unite_legale) > 0
            ):
                company_name = (
                    company_data.periodes_unite_legale[0].denomination_unite_legale
                    or "Unknown"
                )

            progress_callback(
                {
                    "phase": "company_extracted",
                    "message": f"Company info extracted: {company_name}",
                    "company_name": company_name,
                    "facility_count": facility_count,
                    "progress": 10,
                }
            )

        # Phase 2: Stream facilities with progress updates
        if progress_callback:
            progress_callback(
                {
                    "phase": "facilities_extraction",
                    "message": f"Extracting {facility_count} facilities...",
                    "progress": 20,
                }
            )

        all_facilities = []
        processed_count = 0

        async for (
            facility_batch,
            total_facilities,
        ) in self.extractor.extract_facilities_streaming(siren):
            all_facilities.extend(facility_batch)
            processed_count += len(facility_batch)

            if progress_callback:
                progress_percent = 20 + int((processed_count / total_facilities) * 70)
                progress_callback(
                    {
                        "phase": "facilities_extraction",
                        "message": f"Processed {processed_count}/{total_facilities} facilities",
                        "processed_facilities": processed_count,
                        "total_facilities": total_facilities,
                        "progress": progress_percent,
                    }
                )

        if progress_callback:
            progress_callback(
                {
                    "phase": "facilities_extracted",
                    "message": f"All {len(all_facilities)} facilities extracted",
                    "progress": 90,
                }
            )

        # Phase 3: Transform and consolidate
        if progress_callback:
            progress_callback(
                {
                    "phase": "transformation",
                    "message": "Transforming data...",
                    "progress": 95,
                }
            )

        # Prepare raw data for transformation
        raw_data = {
            "company": company_data,
            "facilities": all_facilities,
            "extraction_metadata": {
                "siren": siren,
                "extracted_at": datetime.now().isoformat(),
                "facility_count": len(all_facilities),
            },
        }

        # Transform to Pydantic models
        result = self.transformer.transform_complete(raw_data)

        if progress_callback:
            progress_callback(
                {
                    "phase": "completed",
                    "message": "Extraction completed successfully",
                    "progress": 100,
                }
            )

        logger.info(f"Successfully completed progressive extraction for SIREN {siren}")
        return result

    async def extract_company_only(self, siren: str) -> tuple[Any, int]:
        """
        Extract only company data for immediate feedback.

        Args:
            siren: SIREN number to extract

        Returns:
            Tuple of (company_data, facility_count)
        """
        logger.debug(f"Extracting company data for SIREN: {siren}")

        # Extract company
        company_data = await self.extractor._extract_company(siren)

        # Get facility count without extracting all facilities
        try:
            response = await find_by_get_etablissement(
                q=f"siren:{siren}",
                nombre=1,  # Only need count
                debut=0,
                client=self.client,
            )

            facility_count = (
                int(response.header.total)
                if response.header and response.header.total
                else 0
            )

        except Exception as e:
            logger.warning(f"Could not get facility count for SIREN {siren}: {e}")
            facility_count = 0

        return company_data, facility_count


def generate_django_load_script(data: dict[str, Any]) -> str:
    """
    Generate Django load script for the extracted data.

    Args:
        data: Extracted data dictionary

    Returns:
        Python script string for Django loading
    """
    script_lines = [
        "# Django Load Script - Generated by ETL Showcase",
        "# This script demonstrates how to load the extracted data into Django models",
        "",
        "from django.db import transaction",
        "from karibu.apps.company.models import (",
        "    Company, CompanyIdentifier, Facility, FacilityIdentifier,",
        "    Address, CompanyLegalUnitPeriod, FacilityEstablishmentPeriod,",
        "    ActivityClassification, FacilityOwnership, ExternalRegistryRecord,",
        "    ExternalRegistrySource",
        ")",
        "",
        "def load_siren_data():",
        '    """Load SIREN data into Django models."""',
        "    with transaction.atomic():",
        "        # Get or create external registry source",
        "        sirene_source, _ = ExternalRegistrySource.objects.get_or_create(",
        "            key='sirene',",
        "            defaults={",
        "                'name': 'SIRENE API',",
        "                'country': 'FR',",
        "                'version': '3.11',",
        "                'base_url': 'https://api.insee.fr/api-sirene/3.11',",
        "            }",
        "        )",
        "",
    ]

    # Company creation
    company = data.get("company", {})
    if company:
        script_lines.extend(
            [
                "        # 1. Create Company",
                f"        company, created = Company.objects.get_or_create(",
                f"            name='{company.get('name', 'Unknown Company')}',",
                "        )",
                "",
                "        # 2. Create Company Identifiers",
            ]
        )

        for identifier in company.get("identifiers", []):
            script_lines.extend(
                [
                    f"        CompanyIdentifier.objects.get_or_create(",
                    f"            company=company,",
                    f"            scheme='{identifier.get('scheme')}',",
                    f"            value='{identifier.get('value')}',",
                    "            defaults={",
                    f"                'normalized_value': '{identifier.get('normalized_value')}',",
                    f"                'country': '{identifier.get('country', 'FR')}',",
                    f"                'is_verified': {str(identifier.get('is_verified', True)).lower()},",
                    f"                'verified_at': '{identifier.get('verified_at')}',",
                    "            }",
                    "        )",
                    "",
                ]
            )

    # Activity classifications
    script_lines.extend(
        [
            "        # 3. Create Activity Classifications",
        ]
    )

    for activity in data.get("activity_classifications", []):
        script_lines.extend(
            [
                f"        activity_classification, _ = ActivityClassification.objects.get_or_create(",
                f"            scheme='{activity.get('scheme')}',",
                f"            code='{activity.get('code')}',",
                "            defaults={",
                f"                'label': '{activity.get('label')}',",
                f"                'start': '{activity.get('start')}',",
                f"                'end': '{activity.get('end') or ''}',",
                "            }",
                "        )",
                "",
            ]
        )

    # Facilities
    script_lines.extend(
        [
            "        # 4. Create Facilities and related data",
        ]
    )

    for facility in data.get("facilities", []):
        script_lines.extend(
            [
                f"        facility, created = Facility.objects.get_or_create(",
                f"            name='{facility.get('name', 'Unknown Facility')}',",
                "        )",
                "",
                "        # Facility Identifiers",
            ]
        )

        for identifier in facility.get("identifiers", []):
            script_lines.extend(
                [
                    f"        FacilityIdentifier.objects.get_or_create(",
                    f"            facility=facility,",
                    f"            scheme='{identifier.get('scheme')}',",
                    f"            value='{identifier.get('value')}',",
                    "            defaults={",
                    f"                'normalized_value': '{identifier.get('normalized_value')}',",
                    f"                'country': '{identifier.get('country', 'FR')}',",
                    f"                'is_verified': {str(identifier.get('is_verified', True)).lower()},",
                    f"                'verified_at': '{identifier.get('verified_at')}',",
                    "            }",
                    "        )",
                    "",
                ]
            )

    # Addresses
    script_lines.extend(
        [
            "        # 5. Create Addresses",
        ]
    )

    for address in data.get("addresses", []):
        script_lines.extend(
            [
                f"        Address.objects.get_or_create(",
                f"            facility=facility,",
                f"            country='{address.get('country', 'FR')}',",
                f"            locality='{address.get('locality', '')}',",
                f"            postal_code='{address.get('postal_code', '')}',",
                f"            street_address='{address.get('street_address', '')}',",
                "            defaults={",
                f"                'administrative_area': '{address.get('administrative_area', '')}',",
                f"                'provider': '{address.get('provider', 'sirene')}',",
                f"                'geocode_precision': '{address.get('geocode_precision', 'unknown')}',",
                f"                'start': '{address.get('start')}',",
                f"                'end': '{address.get('end') or ''}',",
                "            }",
                "        )",
                "",
            ]
        )

    # Registry records
    script_lines.extend(
        [
            "        # 6. Create External Registry Records",
        ]
    )

    for record in data.get("registry_records", []):
        script_lines.extend(
            [
                f"        ExternalRegistryRecord.objects.get_or_create(",
                f"            source=sirene_source,",
                f"            entity_type='{record.get('entity_type')}',",
                f"            external_id='{record.get('external_id')}',",
                f"            payload_hash='{record.get('payload_hash')}',",
                "            defaults={",
                f"                'payload': {record.get('payload')},",
                f"                'registry_updated_at': '{record.get('registry_updated_at')}',",
                f"                'ingested_at': '{record.get('ingested_at')}',",
                "            }",
                "        )",
                "",
            ]
        )

    script_lines.extend(
        [
            "        company_name = company.get('name', 'Unknown')",
            "        print(f'Successfully loaded SIREN data for company: {company_name}')",
            "        return company",
            "",
            "",
            "# Usage:",
            "# python manage.py shell",
            "# exec(open('django_load_script.py').read())",
            "# load_siren_data()",
        ]
    )

    return "\n".join(script_lines)


async def interactive_menu() -> None:
    """Run interactive ETL showcase menu."""
    print("\n" + "=" * 60)
    print("ETL Showcase Script with Progressive Loading")
    print("=" * 60)
    print("Demonstrates complete SIRENE ETL pipeline optimized for Django+Celery")
    print("(without actually using Django/Celery)")
    print()

    # Initialize client and configuration
    try:
        import os

        token = os.getenv("SIRENE_API_TOKEN")
        if not token:
            print("ERROR: SIRENE_API_TOKEN environment variable required")
            print("   Get your token from: https://api.insee.fr/catalogue/")
            return

        client = AuthenticatedClient(token=token)
        config = ETLConfig(validation_mode=ValidationMode.LENIENT)
        resolver = NameToSIRENResolver(client)
        orchestrator = ProgressiveETLOrchestrator(client, config)
    except Exception as e:
        print(f"ERROR: Failed to initialize SIRENE client: {e}")
        print("Please ensure you have a valid SIRENE API token configured.")
        return

    while True:
        print("\nETL Showcase Menu:")
        print("1. Search by company name -> SIREN -> extract")
        print("2. Direct SIREN extraction")
        print("3. Exit")

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            await handle_name_search(resolver, orchestrator)
        elif choice == "2":
            await handle_direct_siren(orchestrator)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("ERROR: Invalid choice. Please select 1, 2, or 3.")


async def handle_name_search(
    resolver: NameToSIRENResolver, orchestrator: ProgressiveETLOrchestrator
) -> None:
    """Handle company name search workflow."""
    print("\n" + "-" * 40)
    print("Company Name Search")
    print("-" * 40)

    name = input("Enter company name: ").strip()
    if not name:
        print("ERROR: Company name cannot be empty.")
        return

    try:
        print(f"\nSearching for companies with name: {name}")
        results = await resolver.search_company_by_name(name)

        if not results:
            print(f"ERROR: No companies found for name: {name}")
            return

        print(f"\nFound {len(results)} matches:")
        for i, result in enumerate(results, 1):
            status = "Active" if result.is_active else "Inactive"
            print(
                f"{i}. {result.name} - SIREN: {result.siren} ({status}, {result.facility_count} facilities)"
            )

        if len(results) == 1:
            selected_result = results[0]
        else:
            while True:
                try:
                    choice = int(input(f"\nSelect company (1-{len(results)}): "))
                    if 1 <= choice <= len(results):
                        selected_result = results[choice - 1]
                        break
                    else:
                        print(
                            f"ERROR: Please enter a number between 1 and {len(results)}"
                        )
                except ValueError:
                    print("ERROR: Please enter a valid number")

        await extract_and_display_results(
            orchestrator, selected_result.siren, selected_result.name
        )

    except Exception as e:
        print(f"ERROR: Error during name search: {e}")


async def handle_direct_siren(orchestrator: ProgressiveETLOrchestrator) -> None:
    """Handle direct SIREN extraction workflow."""
    print("\n" + "-" * 40)
    print("Direct SIREN Extraction")
    print("-" * 40)

    siren = input("Enter SIREN number (9 digits): ").strip()
    if not siren:
        print("ERROR: SIREN number cannot be empty.")
        return

    resolver = NameToSIRENResolver(orchestrator.client)
    if not resolver.validate_siren_format(siren):
        print("ERROR: Invalid SIREN format. Must be 9 digits.")
        return

    try:
        await extract_and_display_results(orchestrator, siren, f"SIREN {siren}")
    except Exception as e:
        print(f"ERROR: Error during SIREN extraction: {e}")


async def extract_and_display_results(
    orchestrator: ProgressiveETLOrchestrator, siren: str, display_name: str
) -> None:
    """Extract data and display results."""
    print(f"\nStarting extraction for {display_name}...")

    # Create output directory
    output_dir = Path("etl_output")
    output_dir.mkdir(exist_ok=True)

    # Progress tracking
    progress_updates = []

    def progress_callback(update: dict[str, Any]) -> None:
        progress_updates.append(update)
        phase = update.get("phase", "unknown")
        message = update.get("message", "")
        progress = update.get("progress", 0)

        print(f"[{progress:3d}%] {phase}: {message}")

    try:
        # Extract with progress
        result = await orchestrator.extract_with_progress(siren, progress_callback)

        # Generate output files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"{display_name.lower().replace(' ', '_')}_{siren}_{timestamp}"

        json_path = output_dir / f"{base_filename}.json"
        summary_path = output_dir / f"{base_filename}_summary.txt"

        # Export to JSON
        print(f"\nExporting data to {json_path}...")
        result.export_to_json(json_path)

        # Generate summary
        print(f"Generating summary: {summary_path}")
        result.generate_summary(summary_path)

        # Display results
        print(f"\nExtraction completed successfully!")
        print(f"Results:")
        print(f"  - Company: {result.company.name}")
        print(f"  - Facilities: {len(result.facilities)}")
        print(f"  - Addresses: {len(result.addresses)}")
        print(f"  - Legal periods: {len(result.legal_unit_periods)}")
        print(f"  - Establishment periods: {len(result.establishment_periods)}")
        print(f"  - Activity classifications: {len(result.activity_classifications)}")
        print(f"  - Registry records: {len(result.registry_records)}")

        # Cache simulation
        print(f"\nCache Simulation (as Django+Celery would use):")
        cache_stats = orchestrator.cache.get_stats()
        print(f"  - Total keys: {cache_stats['total_keys']}")
        print(f"  - Memory usage: {cache_stats['memory_usage']} bytes")
        print(f"  - Hit rate: {cache_stats['hit_rate']:.2%}")

        # Django load preview
        django_preview = input("\nShow Django load preview? [y/N]: ").strip().lower()
        if django_preview == "y":
            print("\n" + "=" * 60)
            print("Django Load Preview")
            print("=" * 60)

            # Convert result to dict for script generation
            result_dict = result.model_dump()
            django_script = generate_django_load_script(result_dict)

            print("This data would be loaded as:")
            print("```python")
            print(
                django_script[:500] + "..."
                if len(django_script) > 500
                else django_script
            )
            print("```")

            save_script = input("\nSave Django load script? [y/N]: ").strip().lower()
            if save_script == "y":
                script_path = output_dir / f"{base_filename}_django_load.py"
                with open(script_path, "w", encoding="utf-8") as f:
                    f.write(django_script)
                print(f"Django load script saved to: {script_path}")

    except Exception as e:
        print(f"ERROR: Extraction failed: {e}")
        logger.exception("Extraction failed")


def main() -> None:
    """Main entry point."""
    try:
        asyncio.run(interactive_menu())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nERROR: Unexpected error: {e}")
        logger.exception("Unexpected error in main")
        sys.exit(1)


if __name__ == "__main__":
    main()
