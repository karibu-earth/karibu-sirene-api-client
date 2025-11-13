"""
Data extraction module for the SIREN ETL service.

This module handles extraction of complete SIREN data from the SIRENE API,
including all associated establishments and their historical data.
"""

from __future__ import annotations

from datetime import datetime
import hashlib
import json
import logging
from typing import TYPE_CHECKING, Any

from sirene_api_client.api.etablissement.find_by_post_etablissement import (
    asyncio as find_by_post_etablissement,
)
from sirene_api_client.api.unite_legale.find_by_siren import asyncio as find_by_siren
from sirene_api_client.api_types import UNSET
from sirene_api_client.models.etablissement_post_multi_criteres import (
    EtablissementPostMultiCriteres,
)

from .exceptions import ExtractionError

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from sirene_api_client.client import AuthenticatedClient
    from sirene_api_client.models.etablissement import Etablissement
    from sirene_api_client.models.unite_legale import UniteLegale

    from .config import ETLConfig

logger = logging.getLogger(__name__)


class SIRENExtractor:
    """Extract complete SIREN history from SIRENE API."""

    def __init__(self, client: AuthenticatedClient, config: ETLConfig) -> None:
        if client is None:
            raise TypeError("client cannot be None")
        if config is None:
            raise TypeError("config cannot be None")
        self.client = client
        self.config = config

    async def extract_siren_complete(self, siren: str) -> dict[str, Any]:
        """
        Extract complete SIREN data including:
        1. UniteLegale (company) with all periods
        2. All Etablissements (facilities) for this SIREN
        3. All establishment periods
        4. Related succession links

        Args:
            siren: SIREN number to extract

        Returns:
            Dictionary containing all extracted data

        Raises:
            ExtractionError: If extraction fails
        """
        logger.info(f"Starting complete extraction for SIREN: {siren}")

        try:
            # Extract company (UniteLegale) data
            company_data = await self._extract_company(siren)

            # Extract all facilities (Etablissements) for this SIREN
            facilities_data = await self._extract_facilities(siren)

            # Combine all data
            result = {
                "company": company_data,
                "facilities": facilities_data,
                "extraction_metadata": {
                    "siren": siren,
                    "extracted_at": datetime.now().isoformat(),
                    "facility_count": len(facilities_data),
                },
            }

            logger.info(
                f"Successfully extracted SIREN {siren} with {len(facilities_data)} facilities"
            )
            return result

        except Exception as e:
            logger.error(f"Failed to extract SIREN {siren}: {e}")
            raise ExtractionError(
                f"Failed to extract SIREN {siren}: {e}", siren=siren
            ) from e

    async def _extract_company(self, siren: str) -> UniteLegale:
        """Extract company (UniteLegale) data."""
        logger.debug(f"Extracting company data for SIREN: {siren}")

        try:
            response = await find_by_siren(
                siren=siren,
                client=self.client,
            )

            if (
                not response
                or not hasattr(response, "unite_legale")
                or not response.unite_legale
            ):
                raise ExtractionError(
                    f"No company data found for SIREN: {siren}", siren=siren
                )

            logger.debug(f"Successfully extracted company data for SIREN: {siren}")
            return response.unite_legale

        except Exception as e:
            logger.error(f"Failed to extract company data for SIREN {siren}: {e}")
            raise ExtractionError(
                f"Failed to extract company data for SIREN {siren}: {e}",
                siren=siren,
                endpoint="unite_legale/find_by_siren",
            ) from e

    async def _extract_facilities(self, siren: str) -> list[Etablissement]:
        """Extract all facilities (Etablissements) for a SIREN."""
        logger.debug(f"Extracting facilities for SIREN: {siren}")

        try:
            # Use POST endpoint for multi-criteria search with pagination

            all_facilities: list[Etablissement] = []
            page_size = 1000  # Maximum per request
            current_page = 0
            total_facilities = 0

            while True:
                search_criteria = EtablissementPostMultiCriteres(
                    q=f"siren:{siren}",
                    nombre=page_size,
                    debut=current_page * page_size,
                    masquer_valeurs_nulles=True,  # Hide null values in response
                )

                response = await find_by_post_etablissement(
                    body=search_criteria,
                    client=self.client,
                )

                if response is not None and hasattr(response, "etablissements"):
                    facilities = response.etablissements or []
                    all_facilities.extend(facilities)

                    # Get total count from first response
                    if current_page == 0:
                        total_facilities = (
                            int(response.header.total)
                            if response.header
                            and response.header.total is not UNSET
                            and isinstance(response.header.total, int | str)
                            else 0
                        )
                        logger.debug(
                            f"Total facilities available for SIREN {siren}: {total_facilities}"
                        )

                    logger.debug(
                        f"Page {current_page + 1}: Retrieved {len(facilities)} facilities"
                    )

                    # Check if we got all facilities
                    if (
                        len(facilities) < page_size
                        or len(all_facilities) >= total_facilities
                    ):
                        break

                    current_page += 1
                else:
                    logger.warning(
                        f"No response or establishments for SIREN {siren} on page {current_page + 1}"
                    )
                    break

            logger.debug(
                f"Found {len(all_facilities)} facilities for SIREN: {siren} (across {current_page + 1} pages)"
            )

            return all_facilities

        except Exception as e:
            logger.error(f"Failed to extract facilities for SIREN {siren}: {e}")
            raise ExtractionError(
                f"Failed to extract facilities for SIREN {siren}: {e}",
                siren=siren,
                endpoint="etablissement/find_by_post",
            ) from e

    async def extract_facilities_streaming(
        self, siren: str
    ) -> AsyncIterator[tuple[list[Etablissement], int]]:
        """
        Stream facilities in batches for progressive loading.

        Yields batches of up to 1000 facilities as they're retrieved from the API,
        allowing consumers to process results incrementally and provide real-time
        progress updates.

        Args:
            siren: SIREN number to extract facilities for

        Yields:
            Tuple of (facilities_batch, total_facilities_count)

        Raises:
            ExtractionError: If extraction fails

        Example:
            ```python
            async for facility_batch in extractor.extract_facilities_streaming("123456782"):
                for facility in facility_batch:
                    print(f"Processing facility: {facility.siret}")
            ```
        """
        logger.debug(f"Starting streaming extraction for SIREN: {siren}")

        try:
            page_size = 1000  # Maximum per request
            current_page = 0
            total_facilities = 0

            while True:
                search_criteria = EtablissementPostMultiCriteres(
                    q=f"siren:{siren}",
                    nombre=page_size,
                    debut=current_page * page_size,
                    masquer_valeurs_nulles=True,  # Hide null values in response
                )

                response = await find_by_post_etablissement(
                    body=search_criteria,
                    client=self.client,
                )

                if response is not None and hasattr(response, "etablissements"):
                    facilities = response.etablissements or []

                    # Get total count from first response
                    if current_page == 0:
                        total_facilities = (
                            int(response.header.total)
                            if response.header
                            and response.header.total is not UNSET
                            and isinstance(response.header.total, int | str)
                            else 0
                        )
                        logger.debug(
                            f"Total facilities available for SIREN {siren}: {total_facilities}"
                        )

                    logger.debug(
                        f"Page {current_page + 1}: Retrieved {len(facilities)} facilities"
                    )

                    # Yield batch immediately with total count
                    yield facilities, total_facilities

                    # Check if we got all facilities
                    if (
                        len(facilities) < page_size
                        or len(facilities) >= total_facilities
                    ):
                        break

                    current_page += 1
                else:
                    logger.warning(
                        f"No response or establishments for SIREN {siren} on page {current_page + 1}"
                    )
                    break

            logger.debug(
                f"Completed streaming extraction for SIREN {siren}: {total_facilities} total facilities"
            )

        except Exception as e:
            logger.error(f"Failed to stream facilities for SIREN {siren}: {e}")
            raise ExtractionError(
                f"Failed to stream facilities for SIREN {siren}: {e}",
                siren=siren,
                endpoint="etablissement/find_by_post",
            ) from e

    def _create_payload_hash(self, payload: dict[str, Any]) -> str:
        """Create SHA-256 hash of payload for deduplication."""
        payload_str = json.dumps(payload, sort_keys=True, default=str)
        return hashlib.sha256(payload_str.encode()).hexdigest()
