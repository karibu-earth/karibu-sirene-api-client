# ETL Showcase Script Documentation

## Overview

The ETL Showcase Script (`examples/etl_showcase.py`) demonstrates the complete SIRENE data extraction pipeline optimized for Django+Celery translation. It provides a standalone implementation that showcases the exact patterns needed for production Django applications without requiring Django/Celery dependencies.

## Features

### 🚀 Progressive Loading

- **Phase 1**: Immediate company info extraction for instant user feedback
- **Phase 2**: Progressive facility extraction with real-time progress updates
- **Phase 3**: Consolidated data transformation and JSON export

### 🔍 Dual Search Workflows

- **Name Search**: Company name → SIREN resolution → complete extraction
- **Direct SIREN**: Direct SIREN number → complete extraction

### 📊 Optimized for Large Datasets

- Streaming facility extraction (handles 10,000+ facilities)
- Batch processing with progress callbacks
- Memory-efficient processing for massive companies

### 🗄️ Cache Simulation

- Redis-compatible cache patterns
- TTL and invalidation simulation
- Cache statistics and monitoring

### 🎯 Django-Ready Output

- Single consolidated JSON file matching Pydantic schema
- Human-readable summary files
- Django transaction preview and load script generation

## Installation

### Prerequisites

```bash
# Install required packages
pip install sirene-api-client pyproj

# Set up SIRENE API token
export SIRENE_API_TOKEN="your_token_here"
```

### Quick Start

```bash
# Run the showcase script
python examples/etl_showcase.py
```

## Usage Examples

### Example 1: Company Name Search

``` ascii
ETL Showcase Menu:
1. Search by company name → SIREN → extract
2. Direct SIREN extraction
3. Exit

> 1
Enter company name: CARREFOUR

Found 3 matches:
1. CARREFOUR FRANCE - SIREN: 752617200 (Active, 1,234 facilities)
2. CARREFOUR HYPERMARCHES - SIREN: 820820828 (Active, 245 facilities)
3. CARREFOUR PROXIMITE FRANCE - SIREN: 345130488 (Active, 892 facilities)

Select (1-3): 1

[Phase 1] Fetching company info for SIREN 752617200...
✓ Company: CARREFOUR FRANCE
  - Legal form: SAS (5710)
  - Created: 2012-01-01
  - Status: Active
  - Facilities to extract: 1,234

[Phase 2] Extracting facilities...
  Batch 1/2: 1000 facilities processed (81%)
  Batch 2/2: 1234 facilities processed (100%)
✓ Extraction complete!

[Phase 3] Transforming data...
✓ Transformed:
  - 1 company
  - 1,234 facilities
  - 1,234 addresses
  - 3 legal unit periods
  - 1,234 establishment periods
  - 45 unique activity classifications
```

### Example 2: Direct SIREN Extraction

``` ascii
ETL Showcase Menu:
1. Search by company name → SIREN → extract
2. Direct SIREN extraction
3. Exit

> 2
Enter SIREN number (9 digits): 123456782

[Phase 1] Fetching company info for SIREN 123456782...
✓ Company: EXAMPLE COMPANY
  - Status: Active
  - Facilities to extract: 5

[Phase 2] Extracting facilities...
  Batch 1/1: 5 facilities processed (100%)
✓ Extraction complete!
```

## Output Files

### JSON Export

The script generates a consolidated JSON file with the complete extraction result:

```json
{
  "company": {
    "name": "CARREFOUR FRANCE",
    "identifiers": [
      {
        "scheme": "siren",
        "value": "752617200",
        "normalized_value": "752617200",
        "country": "FR",
        "is_verified": true,
        "verified_at": "2024-01-15T10:30:00"
      }
    ],
    "creation_date": "2012-01-01"
  },
  "facilities": [
    {
      "name": "CARREFOUR PARIS",
      "identifiers": [
        {
          "scheme": "siret",
          "value": "75261720000001",
          "normalized_value": "75261720000001",
          "country": "FR",
          "is_verified": true,
          "verified_at": "2024-01-15T10:30:00"
        }
      ],
      "parent_siren": "752617200",
      "is_headquarters": true
    }
  ],
  "addresses": [
    {
      "country": "FR",
      "locality": "PARIS",
      "postal_code": "75001",
      "street_address": "1 RUE DE LA PAIX",
      "longitude": 2.3522,
      "latitude": 48.8566,
      "provider": "sirene",
      "geocode_precision": "approximate",
      "start": "2012-01-01"
    }
  ],
  "activity_classifications": [
    {
      "scheme": "NAFRev2",
      "code": "4711F",
      "label": "Commerce de détail non spécialisé",
      "start": "2008-01-01",
      "end": null
    }
  ],
  "facility_ownerships": [
    {
      "company_siren": "752617200",
      "facility_siret": "75261720000001",
      "role": "owner",
      "start": "2012-01-01",
      "end": null
    }
  ],
  "registry_records": [
    {
      "entity_type": "legal_unit",
      "external_id": "752617200",
      "payload": {...},
      "payload_hash": "abc123def456", # pragma: allowlist secret
      "registry_updated_at": "2024-01-15T10:30:00",
      "ingested_at": "2024-01-15T10:30:00"
    }
  ],
  "extraction_metadata": {
    "siren": "752617200",
    "extracted_at": "2024-01-15T10:30:00",
    "facility_count": 1234
  }
}
```

### Summary File

A human-readable summary is also generated:

``` ascii
SIREN Extraction Summary
==================================================

Company: CARREFOUR FRANCE
SIREN: 752617200
Creation Date: 2012-01-01

Data Summary:
  - Companies: 1
  - Facilities: 1,234
  - Addresses: 1,234
  - Legal Unit Periods: 3
  - Establishment Periods: 1,234
  - Activity Classifications: 45
  - Facility Ownerships: 1,234
  - Registry Records: 1,235

Facilities:
  - CARREFOUR PARIS (HQ)
  - CARREFOUR LYON
  - CARREFOUR MARSEILLE
  ... and 1,231 more facilities

Activity Classifications:
  - NAFRev2 4711F: Commerce de détail non spécialisé
  - NAFRev2 4719A: Autres commerces de détail en magasin non spécialisé
  ... and 43 more activities

Extraction Metadata:
  - Extracted At: 2024-01-15T10:30:00
  - Facility Count: 1,234

This data is ready for Django loading using the generated load script.
```

## Django Integration

### Cache Patterns

The script demonstrates the exact cache patterns used in Django+Celery:

```python
# Cache keys (as Django+Celery would use):
cache_keys = {
    "etl_company_<task_id>": "Company metadata (45.2 KB)",
    "etl_progress_<task_id>": "Progress state (1.2 KB)",
    "etl_result_<task_id>": "Final result (2.4 MB)",
    "TTL": "3600 seconds"
}
```

### Django Load Script

The script generates a Django load script for atomic database loading:

```python
def load_siren_data():
    """Load SIREN data into Django models."""
    with transaction.atomic():
        # Get or create external registry source
        sirene_source, _ = ExternalRegistrySource.objects.get_or_create(
            key='sirene',
            defaults={
                'name': 'SIRENE API',
                'country': 'FR',
                'version': '3.11',
                'base_url': 'https://api.insee.fr/api-sirene/3.11',
            }
        )

        # 1. Create Company
        company, created = Company.objects.get_or_create(
            name='CARREFOUR FRANCE',
        )

        # 2. Create Company Identifiers
        CompanyIdentifier.objects.get_or_create(
            company=company,
            scheme='siren',
            value='752617200',
            defaults={
                'normalized_value': '752617200',
                'country': 'FR',
                'is_verified': True,
                'verified_at': '2024-01-15T10:30:00',
            }
        )

        # ... (continues with all other models)
```

## Architecture

### Core Components

#### NameToSIRENResolver

- Searches companies by name using SIRENE API
- Returns SIREN candidates with metadata
- Validates SIREN format

#### ProgressiveETLOrchestrator

- Orchestrates the complete extraction process
- Manages progress callbacks and streaming
- Handles large datasets efficiently

#### CacheSimulator

- Simulates Redis cache behavior
- Demonstrates TTL and invalidation patterns
- Provides cache statistics

### Progress Tracking

The script provides detailed progress updates:

```python
progress_updates = [
    {"phase": "company_extraction", "progress": 0},
    {"phase": "company_extracted", "progress": 10},
    {"phase": "facilities_extraction", "progress": 20},
    {"phase": "facilities_extracted", "progress": 90},
    {"phase": "transformation", "progress": 95},
    {"phase": "completed", "progress": 100}
]
```

## Performance Considerations

### Large Companies

The script handles companies with thousands of facilities:

- **La Poste**: ~10,000 facilities
- **Carrefour**: ~1,200 facilities
- **McDonald's**: ~1,500 facilities

### Memory Optimization

- Streaming facility extraction (don't load all in memory)
- Batch processing (1,000 facilities per API call)
- Incremental JSON writing for massive datasets

### API Rate Limits

- Exponential backoff for rate limit handling
- Retry with jitter for network failures
- Progress updates during long operations

## Error Handling

### Common Scenarios

- **Invalid SIREN**: Format validation with user-friendly errors
- **API Failures**: Retry logic with exponential backoff
- **Network Issues**: Graceful degradation and error reporting
- **Large Datasets**: Progress warnings and memory management

### Error Messages

``` ascii
❌ Invalid SIREN format. Must be 9 digits.
❌ No companies found for name: NONEXISTENT COMPANY
❌ API Error: Rate limit exceeded
❌ Extraction failed: Network timeout
```

## Testing

The script includes comprehensive tests covering:

- Name resolution and SIREN validation
- Progressive extraction with batching
- JSON output and Django compatibility
- Cache simulation functionality
- Error handling scenarios

Run tests with:

```bash
make test
```

## Production Translation

### Celery Task Structure

The script demonstrates the exact Celery task structure:

```python
@shared_task(bind=True)
def extract_siren_task(self, siren: str, task_id: str):
    """Extract SIREN data with progress tracking."""

    def progress_callback(update):
        cache.set(f"etl_progress_{task_id}", update, timeout=3600)

    result = extract_and_transform_siren_with_progress(
        siren, client, config, progress_callback=progress_callback
    )

    cache.set(f"etl_result_{task_id}", result, timeout=3600)
    return result
```

### Django Views Integration

```python
def start_extraction(request):
    """Start SIREN extraction with two-phase loading."""
    siren = request.POST.get("siren", "").strip()
    task_id = str(uuid.uuid4())

    # Phase 1: Extract company data immediately
    extract_company_only_task.delay(siren, task_id)

    # Phase 2: Start full extraction
    extract_siren_task.delay(siren, task_id)

    return render(request, "etl/progress.html", {"task_id": task_id})
```

## Troubleshooting

### Common Issues

#### API Token Issues

``` ascii
❌ Failed to initialize SIRENE client: Invalid API token
```

**Solution**: Set `SIRENE_API_TOKEN` environment variable

#### Memory Issues

``` ascii
❌ Memory error during large dataset extraction
```

**Solution**: The script uses streaming extraction to handle large datasets

#### Network Timeouts

``` ascii
❌ Network timeout during API calls
```

**Solution**: The script includes retry logic with exponential backoff

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

When extending the ETL showcase script:

1. **Follow TDD**: Write tests first
2. **Maintain Compatibility**: Ensure Django model compatibility
3. **Add Progress Tracking**: Include progress callbacks for long operations
4. **Handle Errors Gracefully**: Provide user-friendly error messages
5. **Document Changes**: Update this documentation

## License

This script is part of the sirene-api-client package and follows the same license terms.
