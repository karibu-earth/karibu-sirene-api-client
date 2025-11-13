#!/usr/bin/env python3
"""
Simple ETL Example: Employee Band Retrieval

This example demonstrates how to retrieve employee band information
for both company (SIREN) and facility (SIRET) levels using the Sirene API ETL service.

Usage:
    python examples/employee_band_example.py

Requirements:
    - sirene-api-client
    - SIRENE_API_TOKEN environment variable
"""

import asyncio
import os
from dotenv import load_dotenv
from sirene_api_client import AuthenticatedClient, extract_and_transform_siren, ETLConfig, ValidationMode

# Load environment variables
load_dotenv()

# Configuration
SIREN = "061500542"  # Example SIREN number
API_TOKEN = os.getenv("SIRENE_API_TOKEN")

if not API_TOKEN:
    raise ValueError("SIRENE_API_TOKEN environment variable is not set")


async def get_employee_band_data():
    """Retrieve and display employee band data for company and facilities."""

    print(f"[INFO] Retrieving employee band data for SIREN: {SIREN}")
    print("=" * 60)

    # Create authenticated client
    client = AuthenticatedClient(token=API_TOKEN)

    # Configure ETL with lenient validation
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    try:
        # Extract and transform complete SIREN data
        print("[INFO] Extracting data from Sirene API...")
        result = await extract_and_transform_siren(SIREN, client, config)

        print("[SUCCESS] Data extraction completed successfully!")
        print()

        # Display company-level employee band information
        print("COMPANY INFORMATION:")
        print(f"   Name: {result.company.name}")
        print(f"   SIREN: {result.company.identifiers[0].value if result.company.identifiers else 'N/A'}")
        print(f"   Employee Band: {result.company.employee_band or 'Not available'}")
        print(f"   Employee Year: {result.company.employee_band_year or 'Not available'}")
        print(f"   Company Size Category: {result.company.company_size_category or 'Not available'}")
        print()

        # Display facility-level employee band information
        print(f"FACILITIES ({len(result.facilities)} total):")
        print("-" * 40)

        for i, facility in enumerate(result.facilities, 1):
            print(f"   {i}. {facility.name}")
            print(f"      SIRET: {facility.identifiers[0].value if facility.identifiers else 'N/A'}")
            print(f"      Employee Band: {facility.employee_band or 'Not available'}")
            print(f"      Employee Year: {facility.employee_band_year or 'Not available'}")
            print(f"      Headquarters: {'Yes' if facility.is_headquarters else 'No'}")

            # Show address if available
            facility_addresses = [
                addr for addr in result.addresses
                if addr.facility_siret == facility.identifiers[0].value
            ]
            if facility_addresses:
                address = facility_addresses[0]
                print(f"      Address: {address.street_address}")
                if address.locality:
                    print(f"      City: {address.locality}")

            print()

        # Summary
        print("SUMMARY:")
        print(f"   Total facilities: {len(result.facilities)}")
        headquarters_count = sum(1 for f in result.facilities if f.is_headquarters)
        print(f"   Headquarters: {headquarters_count}")

        # Employee band statistics
        company_bands = [f.employee_band for f in result.facilities if f.employee_band]
        if company_bands:
            print(f"   Facilities with employee data: {len(company_bands)}")
            unique_bands = set(company_bands)
            print(f"   Unique employee bands: {sorted(unique_bands)}")

    except Exception as e:
        print(f"[ERROR] Error retrieving data: {e}")
        print(f"   Error type: {type(e).__name__}")
        raise


def decode_employee_band(band_code: str) -> str:
    """Decode employee band code to human-readable description."""
    band_descriptions = {
        "00": "0 employees",
        "01": "1-2 employees",
        "02": "3-5 employees",
        "03": "6-9 employees",
        "11": "10-19 employees",
        "12": "20-49 employees",
        "21": "50-99 employees",
        "22": "100-199 employees",
        "31": "200-249 employees",
        "32": "250-499 employees",
        "41": "500-999 employees",
        "42": "1000-1999 employees",
        "51": "2000-4999 employees",
        "52": "5000-9999 employees",
        "53": "10,000+ employees"
    }
    return band_descriptions.get(band_code, f"Unknown band: {band_code}")


async def main():
    """Main function to run the employee band example."""
    print("Sirene API - Employee Band Example")
    print("=" * 60)

    await get_employee_band_data()

    print("\nEmployee Band Code Reference:")
    print("-" * 30)
    for code, description in [
        ("00", "0 employees"),
        ("01", "1-2 employees"),
        ("02", "3-5 employees"),
        ("03", "6-9 employees"),
        ("11", "10-19 employees"),
        ("12", "20-49 employees"),
        ("21", "50-99 employees"),
        ("22", "100-199 employees"),
        ("31", "200-249 employees"),
        ("32", "250-499 employees"),
        ("41", "500-999 employees"),
        ("42", "1000-1999 employees"),
        ("51", "2000-4999 employees"),
        ("52", "5000-9999 employees"),
        ("53", "10,000+ employees")
    ]:
        print(f"   {code}: {description}")


if __name__ == "__main__":
    asyncio.run(main())
