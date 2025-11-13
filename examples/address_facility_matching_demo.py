#!/usr/bin/env python3
"""
Address-Facility Matching Demonstration Script

This script demonstrates how addresses are matched to facilities in the SIRENE ETL system
using SIREN 061500542 as an example. It shows the 1:1 relationship between facilities
and their addresses, including coordinate conversion from Lambert 93 to WGS84.

Features:
- Complete SIREN extraction with address-facility matching
- Detailed output showing the matching process
- Coordinate conversion demonstration
- JSON export with matched data
- Visual representation of the matching relationship

Usage:
    python examples/address_facility_matching_demo.py

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
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from sirene_api_client import AuthenticatedClient, ETLConfig, ValidationMode
from sirene_api_client.etl import extract_and_transform_siren

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()

API_TOKEN = os.getenv("SIRENE_API_TOKEN")

if not API_TOKEN:
    raise ValueError("SIRENE_API_TOKEN environment variable is not set")


class AddressFacilityMatcher:
    """Demonstrates address-facility matching in SIRENE ETL."""

    def __init__(self, client: AuthenticatedClient, config: ETLConfig) -> None:
        """Initialize the matcher with client and configuration."""
        self.client = client
        self.config = config

    async def demonstrate_matching(self, siren: str) -> None:
        """
        Demonstrate address-facility matching for a given SIREN.

        Args:
            siren: SIREN number to extract and demonstrate matching
        """
        print(f"\n{'=' * 80}")
        print(f"ADDRESS-FACILITY MATCHING DEMONSTRATION")
        print(f"SIREN: {siren}")
        print(f"{'=' * 80}")

        try:
            # Extract complete SIREN data
            print(f"\n[INFO] Extracting data for SIREN {siren}...")
            result = await extract_and_transform_siren(siren, self.client, self.config)

            # Display company information
            self._display_company_info(result)

            # Demonstrate address-facility matching
            self._demonstrate_matching_process(result)

            # Show coordinate conversion
            self._show_coordinate_conversion(result)

            # Export matched data
            self._export_matched_data(result, siren)

            # Summary statistics
            self._show_summary_statistics(result)

        except Exception as e:
            logger.error(f"Demonstration failed for SIREN {siren}: {e}")
            raise

    def _display_company_info(self, result: Any) -> None:
        """Display company information."""
        print(f"\n[COMPANY] COMPANY INFORMATION")
        print(f"{'-' * 50}")
        print(f"Name: {result.company.name}")
        print(
            f"SIREN: {result.company.identifiers[0].value if result.company.identifiers else 'N/A'}"
        )
        print(f"Creation Date: {result.company.creation_date or 'N/A'}")
        print(f"Total Facilities: {len(result.facilities)}")
        print(f"Total Addresses: {len(result.addresses)}")

    def _demonstrate_matching_process(self, result: Any) -> None:
        """Demonstrate the address-facility matching process."""
        print(f"\n[MATCHING] ADDRESS-FACILITY MATCHING PROCESS")
        print(f"{'-' * 50}")
        print(f"This demonstrates how addresses are matched to facilities:")
        print(f"• Each facility has at most one address")
        print(f"• Matching is done by explicit SIRET reference (facility_siret)")
        print(f"• Address.facility_siret links to Facility.identifiers[0].value")
        print(f"• Some facilities may not have address data")

        print(f"\n[RESULTS] DETAILED MATCHING RESULTS:")
        print(f"{'-' * 80}")
        print(
            f"{'Index':<6} {'Facility Name':<30} {'SIRET':<15} {'Has Address':<12} {'Address Preview':<20}"
        )
        print(f"{'-' * 80}")

        for i, facility in enumerate(result.facilities):
            facility_name = (
                facility.name[:28] + ".." if len(facility.name) > 30 else facility.name
            )
            siret = facility.identifiers[0].value if facility.identifiers else "N/A"

            # Find address by SIRET reference instead of index
            matching_address = None
            for address in result.addresses:
                if address.facility_siret == siret:
                    matching_address = address
                    break

            has_address = "Yes" if matching_address else "No"

            address_preview = ""
            if matching_address:
                if matching_address.street_address:
                    address_preview = (
                        matching_address.street_address[:18] + ".."
                        if len(matching_address.street_address) > 20
                        else matching_address.street_address
                    )
                elif matching_address.locality:
                    address_preview = (
                        matching_address.locality[:18] + ".."
                        if len(matching_address.locality) > 20
                        else matching_address.locality
                    )
                else:
                    address_preview = "No street data"

            print(
                f"{i:<6} {facility_name:<30} {siret:<15} {has_address:<12} {address_preview:<20}"
            )

    def _show_coordinate_conversion(self, result: Any) -> None:
        """Show coordinate conversion from Lambert 93 to WGS84."""
        print(f"\n[COORDS] COORDINATE CONVERSION DEMONSTRATION")
        print(f"{'-' * 50}")
        print(
            f"Addresses with coordinates are converted from Lambert 93 (EPSG:2154) to WGS84 (EPSG:4326)"
        )

        addresses_with_coords = [
            addr for addr in result.addresses if addr.longitude and addr.latitude
        ]

        if not addresses_with_coords:
            print(f"No addresses with coordinate data found.")
            return

        print(f"\nFound {len(addresses_with_coords)} addresses with coordinates:")
        print(f"{'-' * 80}")
        print(f"{'Facility':<25} {'Street':<25} {'WGS84 Coordinates':<20}")
        print(f"{'-' * 80}")

        for address in addresses_with_coords:
            # Find corresponding facility by SIRET reference
            facility_name = "Unknown"
            for facility in result.facilities:
                if (
                    facility.identifiers
                    and facility.identifiers[0].value == address.facility_siret
                ):
                    facility_name = (
                        facility.name[:23] + ".."
                        if len(facility.name) > 25
                        else facility.name
                    )
                    break

            street = (
                address.street_address[:23] + ".."
                if address.street_address and len(address.street_address) > 25
                else (address.street_address or "No street")
            )
            coords = f"{address.longitude:.6f}, {address.latitude:.6f}"

            print(f"{facility_name:<25} {street:<25} {coords:<20}")

    def _export_matched_data(self, result: Any, siren: str) -> None:
        """Export matched data to JSON file."""
        print(f"\n[EXPORT] EXPORTING MATCHED DATA")
        print(f"{'-' * 50}")

        # Create output directory
        output_dir = Path("etl_output")
        output_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"address_facility_matching_{siren}_{timestamp}.json"
        output_path = output_dir / filename

        # Create matched data structure
        matched_data = {
            "extraction_metadata": {
                "siren": siren,
                "extracted_at": datetime.now().isoformat(),
                "company_name": result.company.name,
                "total_facilities": len(result.facilities),
                "total_addresses": len(result.addresses),
                "matching_method": "siret_based_explicit_link",
            },
            "company": result.company.model_dump(),
            "facility_address_pairs": [],
        }

        # Create explicit facility-address pairs using SIRET-based matching
        for i, facility in enumerate(result.facilities):
            pair = {
                "facility_index": i,
                "facility": facility.model_dump(),
                "address": None,
                "has_address": False,
            }

            # Find address by SIRET reference
            facility_siret = (
                facility.identifiers[0].value if facility.identifiers else None
            )
            if facility_siret:
                for address in result.addresses:
                    if address.facility_siret == facility_siret:
                        pair["address"] = address.model_dump()
                        pair["has_address"] = True
                        break

            matched_data["facility_address_pairs"].append(pair)

        # Write to file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(matched_data, f, indent=2, ensure_ascii=False, default=str)

        print(f"[SUCCESS] Matched data exported to: {output_path}")
        print(
            f"[INFO] File contains {len(matched_data['facility_address_pairs'])} facility-address pairs"
        )

    def _show_summary_statistics(self, result: Any) -> None:
        """Show summary statistics about the matching."""
        print(f"\n[STATS] SUMMARY STATISTICS")
        print(f"{'-' * 50}")

        total_facilities = len(result.facilities)
        total_addresses = len(result.addresses)

        # Count facilities with addresses using SIRET-based matching
        facilities_with_addresses = 0
        for facility in result.facilities:
            facility_siret = (
                facility.identifiers[0].value if facility.identifiers else None
            )
            if facility_siret:
                for address in result.addresses:
                    if address.facility_siret == facility_siret:
                        facilities_with_addresses += 1
                        break

        facilities_without_addresses = total_facilities - facilities_with_addresses

        print(f"Total Facilities: {total_facilities}")
        print(f"Total Addresses: {total_addresses}")
        print(f"Facilities with Addresses: {facilities_with_addresses}")
        print(f"Facilities without Addresses: {facilities_without_addresses}")
        print(
            f"Address Coverage: {(facilities_with_addresses / total_facilities) * 100:.1f}%"
            if total_facilities > 0
            else "Address Coverage: 0%"
        )

        # Address data quality
        addresses_with_coords = len(
            [addr for addr in result.addresses if addr.longitude and addr.latitude]
        )
        addresses_with_street = len(
            [addr for addr in result.addresses if addr.street_address]
        )

        print(f"\nAddress Data Quality:")
        print(
            f"Addresses with Coordinates: {addresses_with_coords}/{total_addresses} ({(addresses_with_coords / total_addresses) * 100:.1f}%)"
            if total_addresses > 0
            else "Addresses with Coordinates: 0/0 (0%)"
        )
        print(
            f"Addresses with Street Data: {addresses_with_street}/{total_addresses} ({(addresses_with_street / total_addresses) * 100:.1f}%)"
            if total_addresses > 0
            else "Addresses with Street Data: 0/0 (0%)"
        )

    def _show_matching_visualization(self, result: Any) -> None:
        """Show a visual representation of the matching."""
        print(f"\n[VISUAL] MATCHING VISUALIZATION")
        print(f"{'-' * 50}")

        print(f"Facility-Address Relationship Diagram:")
        print(f"")
        print(f"Company: {result.company.name}")
        print(
            f"├── Facility[0] ──→ Address[0] {'✓' if len(result.addresses) > 0 else '✗'}"
        )

        for i in range(1, min(len(result.facilities), 5)):  # Show first 5
            has_address = "✓" if i < len(result.addresses) else "✗"
            print(f"├── Facility[{i}] ──→ Address[{i}] {has_address}")

        if len(result.facilities) > 5:
            print(f"├── ... ({len(result.facilities) - 5} more facilities)")

        print(f"")
        print(f"Legend: ✓ = Address available, ✗ = No address data")


async def main() -> None:
    """Main demonstration function."""
    print("SIRENE Address-Facility Matching Demonstration")
    print("=" * 60)

    # Initialize client and configuration
    try:
        client = AuthenticatedClient(token=API_TOKEN)
        config = ETLConfig(validation_mode=ValidationMode.LENIENT)
        matcher = AddressFacilityMatcher(client, config)

        # Demonstrate with SIREN 061500542
        siren = "061500542"
        print(f"Using SIREN: {siren}")

        await matcher.demonstrate_matching(siren)

        print(f"\n[SUCCESS] Demonstration completed successfully!")
        print(f"[INFO] Check the 'etl_output' directory for exported data.")

    except Exception as e:
        print(f"[ERROR] Demonstration failed: {e}")
        logger.exception("Demonstration failed")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Demonstration interrupted by user.")
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        logger.exception("Unexpected error in main")
        sys.exit(1)
