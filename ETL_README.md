# SIREN ETL Service

A comprehensive extraction, transformation, and loading (ETL) service for SIREN/SIRET data from the French SIRENE API. This service extracts complete company histories with all associated establishments, performs data transformations including coordinate conversion, and prepares data for Django model ingestion.

## Features

- **Complete SIREN Extraction**: Fetches company (UniteLegale) data with all historical periods
- **Facility Discovery**: Automatically finds all establishments (SIRET) for a given SIREN
- **Streaming Extraction**: Process large datasets incrementally with real-time progress updates
- **Progress Tracking**: Built-in progress callbacks for Django + HTMX integration
- **Company-Only Extraction**: Get immediate company data while facilities load in background
- **Coordinate Conversion**: Converts Lambert 93 coordinates to WGS84 for geospatial applications
- **Type-Safe Output**: Uses Pydantic models for validated, type-safe data structures
- **Configurable Validation**: Three validation modes (strict, lenient, permissive)
- **Audit Trail**: Complete registry records for compliance and data lineage
- **Django-Ready**: Output models match Django model structure for easy ingestion

## Installation

The ETL service is included in the `sirene-api-client` package. Install the required dependencies:

```bash
uv add pydantic>=2.0.0 pyproj>=3.6.0
```

## Quick Start

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

asyncio.run(main())
```

## Configuration

### Validation Modes

```python
from sirene_api_client import ETLConfig, ValidationMode

# Strict validation - fail on any missing required fields
config = ETLConfig(validation_mode=ValidationMode.STRICT)

# Lenient validation - warn on missing fields but continue (default)
config = ETLConfig(validation_mode=ValidationMode.LENIENT)

# Permissive validation - ignore most validation errors
config = ETLConfig(validation_mode=ValidationMode.PERMISSIVE)
```

### Additional Configuration Options

```python
config = ETLConfig(
    validation_mode=ValidationMode.LENIENT,
    include_personal_data=False,  # GDPR compliance
    coordinate_precision="approximate",  # rooftop, interpolated, approximate, unknown
    max_retries=3,
    timeout_seconds=30,
)
```

## Data Models

The ETL service provides comprehensive Pydantic models that match Django model structure:

### Core Models

- **`CompanyData`**: Company/UniteLegale data with identifiers
- **`FacilityData`**: Facility/Etablissement data with identifiers
- **`CompanyIdentifierData`**: SIREN identifier with verification
- **`FacilityIdentifierData`**: SIRET identifier with verification

### Temporal Models

- **`CompanyLegalUnitPeriodData`**: Time-framed company legal data
- **`FacilityEstablishmentPeriodData`**: Time-framed establishment data
- **`AddressData`**: Time-framed address with WGS84 coordinates and explicit facility SIRET link

### Registry Models

- **`ActivityClassificationData`**: NAF code data
- **`ExternalRegistryRecordData`**: Raw API payload storage
- **`FacilityOwnershipData`**: Company-facility relationship

### Aggregated Output

- **`SIRENExtractResult`**: Complete extraction result containing all data

## Explicit SIRET-Based Address Linking

The ETL service now provides explicit SIRET-based linking between addresses and facilities, ensuring reliable data relationships:

```python
result = await extract_and_transform_siren("123456782", client, config)

# Each address has an explicit facility_siret field
for address in result.addresses:
    print(f"Address: {address.street_address}")
    print(f"Linked to facility SIRET: {address.facility_siret}")

    # Find the corresponding facility
    facility = next(
        (f for f in result.facilities if f.identifiers[0].value == address.facility_siret),
        None
    )
    if facility:
        print(f"Facility name: {facility.name}")
```

This explicit linking replaces the previous positional matching approach, providing more reliable address-facility relationships.

## Coordinate Conversion

The service automatically converts Lambert 93 (EPSG:2154) coordinates to WGS84 (EPSG:4326):

```python
result = await extract_and_transform_siren("123456782", client, config)

for address in result.addresses:
    if address.longitude and address.latitude:
        print(f"Address: {address.street_address}")
        print(f"Coordinates: {address.longitude}, {address.latitude}")
        print(f"Precision: {address.geocode_precision}")
```

### Range Check Behavior

By default, the coordinate conversion uses a **non-strict range check**, which means:

- Coordinates outside the typical Lambert 93 range (x: 0-1200000, y: 6000000-7200000) will log a warning but still attempt conversion
- This supports handling **overseas French territories** (Réunion, Guadeloupe, Martinique, French Guiana, etc.) that may be mislabeled as Lambert 93 but use different coordinate reference systems
- Invalid results are still caught by WGS84 validation (longitude: -180 to 180, latitude: -90 to 90)

If you need strict range checking (for example, to ensure only mainland France coordinates are processed), you can use the `strict_range_check` parameter:

```python
from sirene_api_client.etl.coordinators import lambert93_to_wgs84

# Strict mode: raises CoordinateConversionError for out-of-range coordinates
coords = lambert93_to_wgs84(x, y, strict_range_check=True)

# Non-strict mode (default): attempts conversion with warning
coords = lambert93_to_wgs84(x, y, strict_range_check=False)
# or simply
coords = lambert93_to_wgs84(x, y)
```

## Django Integration

The output models are designed to map directly to Django models:

```python
from django.contrib.gis.geos import Point

# Extract data
result = await extract_and_transform_siren("123456782", client, config)

# Create Django models
company = Company.objects.create(
    name=result.company.name,
    # ... other fields
)

# Create company identifier
CompanyIdentifier.objects.create(
    company=company,
    scheme=result.company.identifiers[0].scheme,
    value=result.company.identifiers[0].value,
    country=result.company.identifiers[0].country,
    is_verified=result.company.identifiers[0].is_verified,
    verified_at=result.company.identifiers[0].verified_at,
)

# Create facilities
for facility_data in result.facilities:
    facility = Facility.objects.create(
        name=facility_data.name,
        # ... other fields
    )

    # Create facility identifier
    FacilityIdentifier.objects.create(
        facility=facility,
        scheme=facility_data.identifiers[0].scheme,
        value=facility_data.identifiers[0].value,
        country=facility_data.identifiers[0].country,
        is_verified=facility_data.identifiers[0].is_verified,
        verified_at=facility_data.identifiers[0].verified_at,
    )

    # Create facility ownership
    FacilityOwnership.objects.create(
        company=company,
        facility=facility,
        role=facility_data.is_headquarters and "owner" or "operator",
        start=facility_data.creation_date or date.today(),
    )

# Create addresses with coordinates and explicit facility linking
for address_data in result.addresses:
    geom = None
    if address_data.longitude and address_data.latitude:
        geom = Point(address_data.longitude, address_data.latitude)

    # Find the facility this address belongs to using explicit SIRET link
    facility = None
    for f in result.facilities:
        if f.identifiers[0].value == address_data.facility_siret:
            facility = f
            break

    if facility:
        Address.objects.create(
            facility=facility,
            country=address_data.country,
            locality=address_data.locality,
            postal_code=address_data.postal_code,
            street_address=address_data.street_address,
            geom=geom,
            provider=address_data.provider,
            geocode_precision=address_data.geocode_precision,
            start=address_data.start,
            end=address_data.end,
        )

# Create legal unit periods
for period_data in result.legal_unit_periods:
    # Get or create activity classification
    activity, _ = ActivityClassification.objects.get_or_create(
        scheme=period_data.activity_scheme,
        code=period_data.activity_code,
        defaults={
            'label': f"{period_data.activity_scheme} {period_data.activity_code}",
            'start': period_data.activity_scheme == "NAFRev2" and date(2008, 1, 1) or date.today(),
        }
    )

    CompanyLegalUnitPeriod.objects.create(
        company=company,
        start=period_data.start,
        end=period_data.end,
        legal_name=period_data.legal_name,
        legal_form_code=period_data.legal_form_code,
        legal_form_scheme=period_data.legal_form_scheme,
        activity_code=activity,
        activity_scheme=period_data.activity_scheme,
        status=period_data.status,
        employee_band=period_data.employee_band,
        employee_band_year=period_data.employee_band_year,
        ess_flag=period_data.ess_flag,
        mission_company_flag=period_data.mission_company_flag,
    )

# Create registry records for audit trail
for record_data in result.registry_records:
    source, _ = ExternalRegistrySource.objects.get_or_create(
        key="sirene",
        defaults={
            'name': "Système d'Identification du Répertoire des Entreprises",
            'country': "FR",
            'version': "3.11",
            'base_url': "https://api.insee.fr/api-sirene/3.11",
        }
    )

    ExternalRegistryRecord.objects.create(
        source=source,
        entity_type=record_data.entity_type,
        external_id=record_data.external_id,
        payload=record_data.payload,
        payload_hash=record_data.payload_hash,
        registry_updated_at=record_data.registry_updated_at,
        ingested_at=record_data.ingested_at,
        company=company if record_data.entity_type == "legal_unit" else None,
        facility=facility if record_data.entity_type == "establishment" else None,
    )
```

## Error Handling

The service provides specific exception types for different error scenarios:

```python
from sirene_api_client.etl.exceptions import (
    ETLError,
    ValidationError,
    CoordinateConversionError,
    ExtractionError,
    TransformationError,
)

try:
    result = await extract_and_transform_siren("123456782", client, config)
except ValidationError as e:
    print(f"Validation error: {e}")
    print(f"Field: {e.details.get('field')}")
    print(f"Value: {e.details.get('value')}")
except CoordinateConversionError as e:
    print(f"Coordinate conversion failed: {e}")
    print(f"X: {e.details.get('x')}")
    print(f"Y: {e.details.get('y')}")
except ExtractionError as e:
    print(f"API extraction failed: {e}")
    print(f"SIREN: {e.details.get('siren')}")
    print(f"Endpoint: {e.details.get('endpoint')}")
except ETLError as e:
    print(f"ETL error: {e}")
    print(f"Details: {e.details}")
```

## Performance Considerations

- **Async Operations**: The service uses async/await for efficient API calls
- **Batch Processing**: Multiple facilities are processed in parallel
- **Caching**: Activity classifications are cached to avoid duplicates
- **Memory Efficient**: Large datasets are processed incrementally

## GDPR Compliance

The service handles personal data according to GDPR requirements:

- Personal data fields are excluded by default (`include_personal_data=False`)
- Personal data is only stored in `ExternalRegistryRecord.payload` for audit purposes
- Access to personal data requires special authorization from CNIL

## Testing

Run the example script to test the ETL service:

```bash
python example_etl_usage.py
```

## API Reference

### Main Function

- `extract_and_transform_siren(siren, client, config=None)`: Main entry point for ETL process

### ETL Configuration

- `ETLConfig`: Configuration class with validation mode and other settings
- `ValidationMode`: Enum for validation modes (STRICT, LENIENT, PERMISSIVE)

### Models

- `SIRENExtractResult`: Complete extraction result
- `CompanyData`, `FacilityData`: Core entity models
- `CompanyIdentifierData`, `FacilityIdentifierData`: Identifier models
- `AddressData`: Address model with coordinates and explicit facility SIRET link
- `CompanyLegalUnitPeriodData`, `FacilityEstablishmentPeriodData`: Temporal models
- `ActivityClassificationData`: Activity classification model
- `ExternalRegistryRecordData`: Registry record model
- `FacilityOwnershipData`: Ownership relationship model

### Exceptions

- `ETLError`: Base ETL exception
- `ValidationError`: Validation error in strict mode
- `CoordinateConversionError`: Coordinate conversion failed
- `ExtractionError`: API extraction failed
- `TransformationError`: Data transformation failed

## Streaming and Progress Tracking

For large datasets or applications requiring real-time feedback, the ETL service provides streaming extraction with progress tracking capabilities.

### Progress-Aware ETL

Use `extract_and_transform_siren_with_progress()` to receive progress updates during extraction:

```python
import asyncio
from sirene_api_client import AuthenticatedClient, extract_and_transform_siren_with_progress, ETLConfig, ValidationMode

async def main():
    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    def progress_callback(update):
        print(f"Phase: {update['phase']}")
        print(f"Company: {update['company_name']}")
        print(f"Processed: {update['processed_facilities']}/{update['total_facilities']} facilities")
        if 'latest_facility' in update:
            print(f"Latest: {update['latest_facility']}")

    result = await extract_and_transform_siren_with_progress(
        "123456782", client, config, progress_callback=progress_callback
    )

    print(f"Completed: {len(result.facilities)} facilities extracted")

asyncio.run(main())
```

### Progress Callback Format

The progress callback receives a dictionary with the following keys:

- `phase`: Current phase (`"company_extracted"`, `"facilities_processing"`, `"completed"`, `"error"`)
- `siren`: SIREN number being processed
- `company_name`: Company name (when available)
- `processed_facilities`: Number of facilities processed so far
- `total_facilities`: Current estimate of total facilities
- `latest_facility`: Name of most recently processed facility (optional)

### Company-Only Extraction

For immediate feedback, extract company data first while facilities load in the background:

```python
import asyncio
from sirene_api_client import AuthenticatedClient, extract_company_only, ETLConfig, ValidationMode

async def main():
    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    # Get company data immediately
    company_data, facility_count = await extract_company_only("123456782", client, config)

    print(f"Company: {company_data.name}")
    print(f"Estimated facilities: {facility_count}")

    # Now start full extraction in background
    # ... (use extract_and_transform_siren_with_progress)

asyncio.run(main())
```

### Streaming Facility Extraction

For advanced use cases, use the streaming extractor directly:

```python
import asyncio
from sirene_api_client import AuthenticatedClient, SIRENExtractor, ETLConfig, ValidationMode

async def main():
    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)
    extractor = SIRENExtractor(client, config)

    # Process facilities in batches
    async for facility_batch in extractor.extract_facilities_streaming("123456782"):
        print(f"Processing batch of {len(facility_batch)} facilities")
        for facility in facility_batch:
            print(f"  - {facility.siret}")

asyncio.run(main())
```

## Django + HTMX Integration

The ETL service is designed to work seamlessly with Django applications using HTMX for progressive enhancement.

### Celery Task with Progress Tracking

```python
# tasks.py
from celery import shared_task
from django.core.cache import cache
from sirene_api_client import AuthenticatedClient, extract_and_transform_siren_with_progress, ETLConfig, ValidationMode

@shared_task
def extract_siren_task(siren: str, task_id: str):
    """Extract SIREN data with progress tracking."""
    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    def progress_callback(update):
        # Store progress in cache for HTMX polling
        cache.set(f"etl_progress_{task_id}", update, timeout=3600)

    try:
        result = extract_and_transform_siren_with_progress(
            siren, client, config, progress_callback=progress_callback
        )

        # Store final result
        cache.set(f"etl_result_{task_id}", result, timeout=3600)

        return {"status": "completed", "facilities": len(result.facilities)}

    except Exception as e:
        cache.set(f"etl_error_{task_id}", str(e), timeout=3600)
        raise
```

### Django Views

```python
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .tasks import extract_siren_task
import uuid

def extract_siren_view(request):
    """Start SIREN extraction."""
    if request.method == "POST":
        siren = request.POST.get("siren")
        task_id = str(uuid.uuid4())

        # Start Celery task
        extract_siren_task.delay(siren, task_id)

        return render(request, "etl/progress.html", {"task_id": task_id})

    return render(request, "etl/form.html")

@require_http_methods(["GET"])
def etl_progress_api(request, task_id):
    """HTMX polling endpoint for progress updates."""
    progress = cache.get(f"etl_progress_{task_id}")
    result = cache.get(f"etl_result_{task_id}")
    error = cache.get(f"etl_error_{task_id}")

    if error:
        return JsonResponse({"status": "error", "error": error})

    if result:
        return JsonResponse({"status": "completed", "result": result})

    if progress:
        return JsonResponse({"status": "processing", "progress": progress})

    return JsonResponse({"status": "pending"})
```

### HTMX Template

```html
<!-- etl/progress.html -->
<!DOCTYPE html>
<html>
<head>
    <title>SIREN Extraction Progress</title>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
</head>
<body>
    <div id="progress-container">
        <h2>Extracting SIREN Data...</h2>
        <div id="progress-bar">
            <div id="progress-fill" style="width: 0%; background: #4CAF50; height: 20px;"></div>
        </div>
        <div id="progress-text">Initializing...</div>
        <div id="company-info" style="display: none;">
            <h3>Company Information</h3>
            <div id="company-name"></div>
            <div id="facility-count"></div>
        </div>
    </div>

    <script>
        // Poll for progress updates
        htmx.ajax('GET', '/etl/progress/{{ task_id }}/', {
            target: '#progress-container',
            swap: 'outerHTML',
            interval: 1000
        });
    </script>

    <template id="progress-template">
        <div id="progress-container">
            <h2>SIREN Extraction Progress</h2>
            <div id="progress-bar">
                <div id="progress-fill" style="width: {{ progress.processed_facilities / progress.total_facilities * 100 }}%; background: #4CAF50; height: 20px;"></div>
            </div>
            <div id="progress-text">
                Phase: {{ progress.phase }}<br>
                Processed: {{ progress.processed_facilities }}/{{ progress.total_facilities }} facilities
            </div>

            {% if progress.phase == 'company_extracted' %}
            <div id="company-info">
                <h3>Company Information</h3>
                <div id="company-name">{{ progress.company_name }}</div>
                <div id="facility-count">Total facilities: {{ progress.total_facilities }}</div>
            </div>
            {% endif %}

            {% if progress.latest_facility %}
            <div>Latest facility: {{ progress.latest_facility }}</div>
            {% endif %}
        </div>
    </template>
</body>
</html>
```

### URL Configuration

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('etl/extract/', views.extract_siren_view, name='etl_extract'),
    path('etl/progress/<str:task_id>/', views.etl_progress_api, name='etl_progress'),
]
```

### Two-Phase Loading Pattern

This pattern provides excellent UX by showing company information immediately while facilities load:

1. **Phase 1**: Extract company data only (`extract_company_only()`)
2. **Phase 2**: Start full extraction with progress tracking (`extract_and_transform_siren_with_progress()`)

```python
# Enhanced view with two-phase loading
def extract_siren_view(request):
    if request.method == "POST":
        siren = request.POST.get("siren")
        task_id = str(uuid.uuid4())

        # Phase 1: Get company data immediately
        try:
            company_data, facility_count = extract_company_only(siren, client, config)
            cache.set(f"etl_company_{task_id}", {
                "name": company_data.name,
                "facility_count": facility_count
            }, timeout=3600)
        except Exception as e:
            cache.set(f"etl_error_{task_id}", str(e), timeout=3600)
            return render(request, "etl/error.html", {"error": str(e)})

        # Phase 2: Start full extraction
        extract_siren_task.delay(siren, task_id)

        return render(request, "etl/progress.html", {"task_id": task_id})

    return render(request, "etl/form.html")
```

## Django Integration Reference
