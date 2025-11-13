"""
Main ETL service interface for the SIREN ETL service.

This module provides the main entry point for extracting and transforming
complete SIREN data from the SIRENE API.
"""

from __future__ import annotations

from datetime import date, datetime
import logging
from typing import TYPE_CHECKING, Any

from sirene_api_client.api.etablissement.find_by_post_etablissement import (
    asyncio as find_by_post_etablissement,
)
from sirene_api_client.models.etablissement_post_multi_criteres import (
    EtablissementPostMultiCriteres,
)

from .config import ETLConfig, ValidationMode
from .extractor import SIRENExtractor
from .models import CompanyData, SIRENExtractResult
from .transformer import SIRENTransformer

if TYPE_CHECKING:
    from collections.abc import Callable

    from sirene_api_client.client import AuthenticatedClient

logger = logging.getLogger(__name__)

__all__ = [
    "ETLConfig",
    "SIRENExtractResult",
    "SIRENExtractor",
    "SIRENTransformer",
    "ValidationMode",
    "extract_and_transform_siren",
    "extract_and_transform_siren_with_progress",
    "extract_company_only",
]


async def extract_and_transform_siren(
    siren: str, client: AuthenticatedClient, config: ETLConfig | None = None
) -> SIRENExtractResult:
    """
    Main entry point: Extract and transform complete SIREN data.

    This function orchestrates the complete ETL process:
    1. Extracts company (UniteLegale) data with all periods
    2. Extracts all associated facilities (Etablissements)
    3. Transforms all data to Django-ready Pydantic models
    4. Performs coordinate conversion (Lambert 93 → WGS84)
    5. Creates comprehensive audit trail

    Args:
        siren: SIREN number to extract (9-digit string)
        client: SIRENE API client instance
        config: Optional ETL configuration (defaults to lenient validation)

    Returns:
        SIRENExtractResult with all transformed data ready for Django ingestion

    Example:
        ```python
        from sirene_api_client import Client, extract_and_transform_siren, ETLConfig, ValidationMode

        # Create API client
        client = Client(base_url="https://api.insee.fr/api-sirene/3.11")

        # Configure ETL with lenient validation
        config = ETLConfig(validation_mode=ValidationMode.LENIENT)

        # Extract and transform complete SIREN data
        result = await extract_and_transform_siren("123456782", client, config)

        # Access transformed data
        print(result.company.name)
        print(result.company.identifiers[0].value)  # SIREN
        print(result.facilities[0].name)
        print(result.facilities[0].identifiers[0].value)  # SIRET
        print(result.addresses[0].coordinates)  # WGS84 (lon, lat)
        ```
    """
    logger.info(f"Starting ETL process for SIREN: {siren}")

    # Use default config if none provided
    if config is None:
        config = ETLConfig()
        logger.debug("Using default ETL configuration")

    # Validate SIREN format
    if not siren or not siren.isdigit() or len(siren) != 9:
        raise ValueError(f"Invalid SIREN format: {siren}. Must be 9 digits.")

    try:
        # Initialize extractor and transformer
        extractor = SIRENExtractor(client, config)
        transformer = SIRENTransformer(config)

        # Extract raw data from API
        logger.info(f"Extracting data for SIREN: {siren}")
        raw_data = await extractor.extract_siren_complete(siren)

        # Transform data to Pydantic models
        logger.info(f"Transforming data for SIREN: {siren}")
        result = transformer.transform_complete(raw_data)

        logger.info(f"Successfully completed ETL process for SIREN: {siren}")
        logger.info(
            f"Extracted: {len(result.facilities)} facilities, "
            f"{len(result.legal_unit_periods)} legal periods, "
            f"{len(result.establishment_periods)} establishment periods, "
            f"{len(result.addresses)} addresses"
        )

        return result

    except Exception as e:
        logger.error(f"ETL process failed for SIREN {siren}: {e}")
        raise


async def extract_and_transform_siren_with_progress(
    siren: str,
    client: AuthenticatedClient,
    config: ETLConfig | None = None,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> SIRENExtractResult:
    """
    Extract and transform SIREN data with progress callbacks.

    This function provides the same functionality as extract_and_transform_siren
    but allows consumers to receive progress updates during facility processing.
    Progress callbacks are invoked at key phases of the ETL process.

    Args:
        siren: SIREN number to extract (9-digit string)
        client: SIRENE API client instance
        config: Optional ETL configuration (defaults to lenient validation)
        progress_callback: Optional callback function for progress updates

    Returns:
        SIRENExtractResult with all transformed data ready for Django ingestion

    Progress Callback Format:
        The callback receives a dictionary with the following keys:
        - phase: "company_extracted", "facilities_processing", "completed", "error"
        - siren: SIREN number being processed
        - company_name: Company name (when available)
        - processed_facilities: Number of facilities processed so far
        - total_facilities: Current estimate of total facilities
        - latest_facility: Name of most recently processed facility (optional)

    Example:
        ```python
        def on_progress(update):
            print(f"Phase: {update['phase']}")
            print(f"Processed {update['processed_facilities']} facilities")

        result = await extract_and_transform_siren_with_progress(
            "123456782", client, config, progress_callback=on_progress
        )
        ```
    """
    logger.info(f"Starting ETL process with progress tracking for SIREN: {siren}")

    # Use default config if none provided
    if config is None:
        config = ETLConfig()
        logger.debug("Using default ETL configuration")

    # Validate SIREN format
    if not siren or not siren.isdigit() or len(siren) != 9:
        raise ValueError(f"Invalid SIREN format: {siren}. Must be 9 digits.")

    try:
        # Initialize extractor and transformer
        extractor = SIRENExtractor(client, config)
        transformer = SIRENTransformer(config)

        # Phase 1: Extract company data immediately
        logger.info(f"Extracting company data for SIREN: {siren}")
        company_data = await extractor._extract_company(siren)
        company_transformed = transformer.transform_unite_legale(company_data)

        # Notify progress callback with company data
        if progress_callback:
            progress_callback(
                {
                    "phase": "company_extracted",
                    "company_name": company_transformed.name,
                    "siren": siren,
                    "processed_facilities": 0,
                    "total_facilities": 0,
                }
            )

        # Phase 2: Extract facilities with progress updates
        logger.info(f"Extracting facilities for SIREN: {siren}")
        facilities_data = []
        original_facilities = []  # Store original facility objects for registry records
        establishment_periods = []
        addresses = []
        facility_ownerships = []
        processed_count = 0
        total_facilities = 0  # Will be set from first API response

        async for facility_batch, total_count in extractor.extract_facilities_streaming(
            siren
        ):
            # Update total facilities count from API response
            if total_count > 0:
                total_facilities = total_count

            for facility in facility_batch:
                # Store original facility object
                original_facilities.append(facility)
                # Transform facility data
                facility_data = transformer.transform_etablissement(facility)
                facilities_data.append(facility_data)

                # Transform establishment periods
                if facility.periodes_etablissement:
                    for period in facility.periodes_etablissement:
                        period_data = transformer.transform_establishment_period(
                            period, facility
                        )
                        establishment_periods.append(period_data)

                # Transform addresses
                if facility.adresse_etablissement:
                    address_data = transformer.transform_address(
                        facility.adresse_etablissement,
                        facility,  # NEW: Pass facility for reference
                        facility.date_creation_etablissement or date.today(),
                    )
                    addresses.append(address_data)

                # Create facility ownership relationship
                ownership_data = transformer.transform_facility_ownership(facility)
                facility_ownerships.append(ownership_data)

                processed_count += 1

                # Notify progress callback
                if progress_callback:
                    progress_callback(
                        {
                            "phase": "facilities_processing",
                            "company_name": company_transformed.name,
                            "siren": siren,
                            "processed_facilities": processed_count,
                            "total_facilities": total_facilities,  # Use total from API response
                            "latest_facility": facility_data.name,
                        }
                    )

        # Phase 3: Transform company legal unit periods
        legal_unit_periods = []
        if company_data and company_data.periodes_unite_legale:
            for legal_period in company_data.periodes_unite_legale:
                legal_period_data = transformer.transform_legal_unit_period(
                    legal_period
                )
                legal_unit_periods.append(legal_period_data)

        # Create registry records
        raw_data = {
            "company": company_data,
            "facilities": original_facilities,  # Use original facility objects for registry records
            "extraction_metadata": {
                "siren": siren,
                "extracted_at": datetime.now().isoformat(),
                "facility_count": len(facilities_data),
            },
        }
        registry_records = transformer._create_registry_records(raw_data)

        # Ensure extraction_metadata is a dict
        extraction_metadata = raw_data.get("extraction_metadata", {})
        if not isinstance(extraction_metadata, dict):
            extraction_metadata = {}

        # Create final result
        result = SIRENExtractResult(
            company=company_transformed,
            facilities=facilities_data,
            legal_unit_periods=legal_unit_periods,
            establishment_periods=establishment_periods,
            addresses=addresses,
            activity_classifications=list(transformer._activity_cache.values()),
            facility_ownerships=facility_ownerships,
            registry_records=registry_records,
            extraction_metadata=extraction_metadata,
        )

        # Final progress notification
        if progress_callback:
            progress_callback(
                {
                    "phase": "completed",
                    "company_name": company_transformed.name,
                    "siren": siren,
                    "processed_facilities": len(facilities_data),
                    "total_facilities": len(facilities_data),
                    "addresses": len(addresses),
                    "legal_periods": len(legal_unit_periods),
                    "establishment_periods": len(establishment_periods),
                }
            )

        logger.info(f"Successfully completed ETL process for SIREN: {siren}")
        logger.info(
            f"Extracted: {len(result.facilities)} facilities, "
            f"{len(result.legal_unit_periods)} legal periods, "
            f"{len(result.establishment_periods)} establishment periods, "
            f"{len(result.addresses)} addresses"
        )

        return result

    except Exception as e:
        logger.error(f"ETL process failed for SIREN {siren}: {e}")
        if progress_callback:
            progress_callback({"phase": "error", "siren": siren, "error": str(e)})
        raise


async def extract_company_only(
    siren: str, client: AuthenticatedClient, config: ETLConfig | None = None
) -> tuple[CompanyData, int]:
    """
    Extract only company data with facility count for immediate feedback.

    This function extracts company (UniteLegale) data and makes a single API call
    to get the facility count without retrieving full facility data. This is useful
    for providing immediate company information while full extraction runs in the
    background.

    Args:
        siren: SIREN number to extract (9-digit string)
        client: SIRENE API client instance
        config: Optional ETL configuration (defaults to lenient validation)

    Returns:
        Tuple of (CompanyData, estimated_facility_count)

    Raises:
        ValueError: If SIREN format is invalid
        ExtractionError: If company extraction fails

    Example:
        ```python
        company_data, facility_count = await extract_company_only("123456782", client)
        print(f"Company: {company_data.name}")
        print(f"Estimated facilities: {facility_count}")
        ```
    """
    logger.info(f"Extracting company data only for SIREN: {siren}")

    # Use default config if none provided
    if config is None:
        config = ETLConfig()
        logger.debug("Using default ETL configuration")

    # Validate SIREN format
    if not siren or not siren.isdigit() or len(siren) != 9:
        raise ValueError(f"Invalid SIREN format: {siren}. Must be 9 digits.")

    try:
        # Initialize extractor and transformer
        extractor = SIRENExtractor(client, config)
        transformer = SIRENTransformer(config)

        # Extract company data
        company_data = await extractor._extract_company(siren)
        company_transformed = transformer.transform_unite_legale(company_data)

        # Get facility count with minimal API call
        facility_count = 0
        try:
            # Make a single API call to get facility count
            search_criteria = EtablissementPostMultiCriteres(
                q=f"siren:{siren}",
                nombre=1,  # Only need 1 to get the count
                debut=0,
                masquer_valeurs_nulles=True,
            )

            response = await find_by_post_etablissement(
                body=search_criteria,
                client=client,
            )

            if response and response.header:
                facility_count = response.header.total or 0

        except Exception as e:
            logger.warning(f"Could not get facility count for SIREN {siren}: {e}")
            facility_count = 0

        logger.info(
            f"Company extraction completed for SIREN {siren}: {facility_count} facilities"
        )

        return company_transformed, facility_count

    except Exception as e:
        logger.error(f"Company extraction failed for SIREN {siren}: {e}")
        raise
