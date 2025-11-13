"""
Django + Celery + HTMX Integration Example for SIREN ETL Service

This example demonstrates how to integrate the SIREN ETL service with Django
using Celery for background processing and HTMX for progressive enhancement.

Features demonstrated:
- Two-phase loading (company data immediately, facilities in background)
- Real-time progress updates via HTMX polling
- Celery task with progress callbacks
- Django views and templates
- Error handling and user feedback

Requirements:
- Django 4.0+
- Celery 5.0+
- Redis (for Celery broker and Django cache)
- HTMX 1.9+
- sirene-api-client

Setup:
1. Install dependencies: pip install django celery redis sirene-api-client
2. Configure Django settings (see settings.py section)
3. Start Redis: redis-server
4. Start Celery worker: celery -A your_project worker --loglevel=info
5. Run Django: python manage.py runserver
"""

# =============================================================================
# Django Settings Configuration
# =============================================================================

"""
# settings.py additions

import os

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Django Cache Configuration (for progress tracking)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://localhost:6379/1',
    }
}

# SIRENE API Configuration
SIRENE_API_BASE_URL = 'https://api.insee.fr/api-sirene/3.11'
SIRENE_API_TOKEN = os.getenv('SIRENE_API_TOKEN')  # Set your API token
"""

# =============================================================================
# Celery Tasks
# =============================================================================

import logging

from celery import shared_task
from django.core.cache import cache

from sirene_api_client import (
    AuthenticatedClient,
    ETLConfig,
    ValidationMode,
    extract_and_transform_siren_with_progress,
)

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def extract_siren_task(self, siren: str, task_id: str):
    """
    Extract SIREN data with progress tracking.

    This task demonstrates the two-phase approach:
    1. Extract company data immediately for instant feedback
    2. Extract facilities with progress updates

    Args:
        siren: SIREN number to extract
        task_id: Unique task identifier for progress tracking
    """
    logger.info(f"Starting SIREN extraction task for {siren}")

    # Initialize API client and configuration
    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    def progress_callback(update):
        """Store progress updates in cache for HTMX polling."""
        cache.set(f"etl_progress_{task_id}", update, timeout=3600)
        logger.debug(f"Progress update for {siren}: {update['phase']}")

    try:
        # Extract and transform SIREN data with progress tracking
        result = extract_and_transform_siren_with_progress(
            siren, client, config, progress_callback=progress_callback
        )

        # Store final result
        cache.set(
            f"etl_result_{task_id}",
            {
                "status": "completed",
                "company": {
                    "name": result.company.name,
                    "siren": result.company.identifiers[0].value,
                },
                "facilities": [
                    {
                        "name": facility.name,
                        "siret": facility.identifiers[0].value,
                        "is_headquarters": facility.is_headquarters,
                    }
                    for facility in result.facilities
                ],
                "addresses": [
                    {
                        "street": addr.street,
                        "city": addr.city,
                        "postal_code": addr.postal_code,
                        "coordinates": addr.coordinates,
                    }
                    for addr in result.addresses
                ],
                "summary": {
                    "total_facilities": len(result.facilities),
                    "total_addresses": len(result.addresses),
                    "legal_periods": len(result.legal_unit_periods),
                    "establishment_periods": len(result.establishment_periods),
                },
            },
            timeout=3600,
        )

        logger.info(
            f"Successfully completed SIREN extraction for {siren}: {len(result.facilities)} facilities"
        )

        return {
            "status": "completed",
            "facilities": len(result.facilities),
            "addresses": len(result.addresses),
        }

    except Exception as e:
        logger.error(f"SIREN extraction failed for {siren}: {e}")
        cache.set(
            f"etl_error_{task_id}",
            {"status": "error", "error": str(e), "siren": siren},
            timeout=3600,
        )
        raise


@shared_task
def extract_company_only_task(siren: str, task_id: str):
    """
    Extract only company data for immediate feedback.

    This task provides instant company information while the full extraction
    runs in the background.
    """
    from sirene_api_client import extract_company_only

    logger.info(f"Extracting company data only for {siren}")

    client = AuthenticatedClient(token="your_token")
    config = ETLConfig(validation_mode=ValidationMode.LENIENT)

    try:
        company_data, facility_count = extract_company_only(siren, client, config)

        # Store company data for immediate display
        cache.set(
            f"etl_company_{task_id}",
            {
                "status": "completed",
                "company": {
                    "name": company_data.name,
                    "siren": company_data.identifiers[0].value,
                },
                "facility_count": facility_count,
            },
            timeout=3600,
        )

        logger.info(
            f"Company data extracted for {siren}: {company_data.name} ({facility_count} facilities)"
        )

        return {
            "status": "completed",
            "company_name": company_data.name,
            "facility_count": facility_count,
        }

    except Exception as e:
        logger.error(f"Company extraction failed for {siren}: {e}")
        cache.set(
            f"etl_error_{task_id}",
            {"status": "error", "error": str(e), "siren": siren},
            timeout=3600,
        )
        raise


# =============================================================================
# Django Views
# =============================================================================

import uuid

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def extract_siren_form(request):
    """Display SIREN extraction form."""
    return render(request, "etl/form.html")


@csrf_exempt
@require_http_methods(["POST"])
def start_extraction(request):
    """
    Start SIREN extraction with two-phase loading.

    Phase 1: Extract company data immediately
    Phase 2: Start full extraction in background
    """
    siren = request.POST.get("siren", "").strip()
    task_id = str(uuid.uuid4())

    # Validate SIREN format
    if not siren or not siren.isdigit() or len(siren) != 9:
        messages.error(request, "Invalid SIREN format. Must be 9 digits.")
        return render(request, "etl/form.html")

    try:
        # Phase 1: Extract company data immediately
        extract_company_only_task.delay(siren, task_id)

        # Phase 2: Start full extraction
        extract_siren_task.delay(siren, task_id)

        # Redirect to progress page
        return render(
            request, "etl/progress.html", {"task_id": task_id, "siren": siren}
        )

    except Exception as e:
        logger.error(f"Failed to start extraction for {siren}: {e}")
        messages.error(request, f"Failed to start extraction: {e}")
        return render(request, "etl/form.html")


@require_http_methods(["GET"])
def extraction_progress(request, task_id):
    """
    HTMX polling endpoint for progress updates.

    Returns JSON response with current progress, company data, or final result.
    """
    # Check for errors first
    error = cache.get(f"etl_error_{task_id}")
    if error:
        return JsonResponse(error)

    # Check for final result
    result = cache.get(f"etl_result_{task_id}")
    if result:
        return JsonResponse(result)

    # Check for company data (immediate feedback)
    company_data = cache.get(f"etl_company_{task_id}")
    if company_data:
        return JsonResponse(company_data)

    # Check for progress updates
    progress = cache.get(f"etl_progress_{task_id}")
    if progress:
        return JsonResponse({"status": "processing", "progress": progress})

    # No data available yet
    return JsonResponse({"status": "pending", "message": "Extraction starting..."})


def extraction_result(request, task_id):
    """Display final extraction results."""
    result = cache.get(f"etl_result_{task_id}")
    error = cache.get(f"etl_error_{task_id}")

    if error:
        return render(request, "etl/error.html", {"error": error})

    if result:
        return render(request, "etl/result.html", {"result": result})

    # Still processing
    return render(request, "etl/progress.html", {"task_id": task_id})


# =============================================================================
# Django Templates
# =============================================================================

"""
# templates/etl/form.html
<!DOCTYPE html>
<html>
<head>
    <title>SIREN Data Extraction</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"] { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #007cba; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #005a87; }
        .error { color: red; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>SIREN Data Extraction</h1>
    <p>Enter a SIREN number to extract complete company and facility data.</p>

    <form method="post" action="{% url 'start_extraction' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="siren">SIREN Number:</label>
            <input type="text" id="siren" name="siren" placeholder="123456782" maxlength="9" required>
            <small>Enter a 9-digit SIREN number</small>
        </div>
        <button type="submit">Extract Data</button>
    </form>

    {% if messages %}
        {% for message in messages %}
            <div class="error">{{ message }}</div>
        {% endfor %}
    {% endif %}
</body>
</html>
"""

"""
# templates/etl/progress.html
<!DOCTYPE html>
<html>
<head>
    <title>SIREN Extraction Progress</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .progress-container { background: #f5f5f5; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .progress-bar { background: #e0e0e0; height: 20px; border-radius: 10px; overflow: hidden; }
        .progress-fill { background: #4CAF50; height: 100%; transition: width 0.3s ease; }
        .company-info { background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 15px 0; }
        .facility-list { max-height: 300px; overflow-y: auto; }
        .facility-item { padding: 5px 0; border-bottom: 1px solid #eee; }
        .error { color: red; background: #ffe6e6; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div id="main-container">
        <h1>SIREN Data Extraction Progress</h1>
        <div id="progress-container">
            <h2>Extracting SIREN {{ siren }}...</h2>
            <div class="progress-bar">
                <div id="progress-fill" class="progress-fill" style="width: 0%;"></div>
            </div>
            <div id="progress-text">Initializing...</div>

            <div id="company-info" class="company-info" style="display: none;">
                <h3>Company Information</h3>
                <div id="company-name"></div>
                <div id="facility-count"></div>
            </div>

            <div id="facilities-preview" style="display: none;">
                <h3>Facilities Preview</h3>
                <div id="facility-list" class="facility-list"></div>
            </div>
        </div>
    </div>

    <script>
        // Poll for progress updates
        function pollProgress() {
            htmx.ajax('GET', '{% url "extraction_progress" task_id %}', {
                target: '#main-container',
                swap: 'outerHTML',
                interval: 1000
            });
        }

        // Start polling
        pollProgress();
    </script>

    <!-- Progress update template -->
    <template id="progress-template">
        <div id="main-container">
            <h1>SIREN Data Extraction Progress</h1>
            <div id="progress-container">
                <h2>Extracting SIREN {{ siren }}...</h2>
                <div class="progress-bar">
                    <div id="progress-fill" class="progress-fill" style="width: {{ progress.processed_facilities / progress.total_facilities * 100 }}%;"></div>
                </div>
                <div id="progress-text">
                    <strong>Phase:</strong> {{ progress.phase }}<br>
                    <strong>Processed:</strong> {{ progress.processed_facilities }}/{{ progress.total_facilities }} facilities
                </div>

                {% if progress.phase == 'company_extracted' %}
                <div id="company-info" class="company-info">
                    <h3>Company Information</h3>
                    <div id="company-name"><strong>{{ progress.company_name }}</strong></div>
                    <div id="facility-count">Total facilities: {{ progress.total_facilities }}</div>
                </div>
                {% endif %}

                {% if progress.latest_facility %}
                <div><strong>Latest facility:</strong> {{ progress.latest_facility }}</div>
                {% endif %}
            </div>
        </div>
    </template>
</body>
</html>
"""

"""
# templates/etl/result.html
<!DOCTYPE html>
<html>
<head>
    <title>SIREN Extraction Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }
        .summary { background: #e8f5e8; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        .section { margin-bottom: 30px; }
        .facility-item, .address-item { background: #f9f9f9; padding: 10px; margin: 5px 0; border-radius: 4px; }
        .coordinates { font-family: monospace; color: #666; }
        .headquarters { background: #fff3cd; border-left: 4px solid #ffc107; }
    </style>
</head>
<body>
    <h1>SIREN Extraction Results</h1>

    <div class="summary">
        <h2>Summary</h2>
        <p><strong>Company:</strong> {{ result.company.name }}</p>
        <p><strong>SIREN:</strong> {{ result.company.siren }}</p>
        <p><strong>Total Facilities:</strong> {{ result.summary.total_facilities }}</p>
        <p><strong>Total Addresses:</strong> {{ result.summary.total_addresses }}</p>
        <p><strong>Legal Periods:</strong> {{ result.summary.legal_periods }}</p>
        <p><strong>Establishment Periods:</strong> {{ result.summary.establishment_periods }}</p>
    </div>

    <div class="section">
        <h2>Facilities ({{ result.facilities|length }})</h2>
        {% for facility in result.facilities %}
        <div class="facility-item {% if facility.is_headquarters %}headquarters{% endif %}">
            <strong>{{ facility.name }}</strong>
            {% if facility.is_headquarters %}<span style="color: #856404;">(Headquarters)</span>{% endif %}
            <br>
            <small>SIRET: {{ facility.siret }}</small>
        </div>
        {% endfor %}
    </div>

    <div class="section">
        <h2>Addresses ({{ result.addresses|length }})</h2>
        {% for address in result.addresses %}
        <div class="address-item">
            <strong>{{ address.street }}</strong><br>
            {{ address.postal_code }} {{ address.city }}<br>
            <span class="coordinates">Coordinates: {{ address.coordinates.0 }}, {{ address.coordinates.1 }}</span>
        </div>
        {% endfor %}
    </div>

    <p><a href="{% url 'extract_form' %}">Extract Another SIREN</a></p>
</body>
</html>
"""

"""
# templates/etl/error.html
<!DOCTYPE html>
<html>
<head>
    <title>SIREN Extraction Error</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .error { background: #ffe6e6; color: #d63384; padding: 20px; border-radius: 8px; border-left: 4px solid #d63384; }
    </style>
</head>
<body>
    <h1>SIREN Extraction Error</h1>

    <div class="error">
        <h2>Error Details</h2>
        <p><strong>SIREN:</strong> {{ error.siren }}</p>
        <p><strong>Error:</strong> {{ error.error }}</p>
    </div>

    <p><a href="{% url 'extract_form' %}">Try Again</a></p>
</body>
</html>
"""

# =============================================================================
# URL Configuration
# =============================================================================

"""
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('etl/', views.extract_siren_form, name='extract_form'),
    path('etl/extract/', views.start_extraction, name='start_extraction'),
    path('etl/progress/<str:task_id>/', views.extraction_progress, name='extraction_progress'),
    path('etl/result/<str:task_id>/', views.extraction_result, name='extraction_result'),
]
"""

# =============================================================================
# Usage Instructions
# =============================================================================

"""
USAGE INSTRUCTIONS:

1. Setup:
   - Install dependencies: pip install django celery redis sirene-api-client
   - Configure Django settings (see settings.py section above)
   - Set SIRENE_API_TOKEN environment variable

2. Start Services:
   - Start Redis: redis-server
   - Start Celery worker: celery -A your_project worker --loglevel=info
   - Run Django: python manage.py runserver

3. Usage:
   - Navigate to /etl/
   - Enter a SIREN number (e.g., 123456782)
   - Click "Extract Data"
   - Watch real-time progress updates
   - View final results

4. Features Demonstrated:
   - Two-phase loading (company data immediately, facilities in background)
   - Real-time progress updates via HTMX polling
   - Celery background task processing
   - Django template rendering
   - Error handling and user feedback
   - Responsive design

5. Customization:
   - Modify progress callback frequency by changing the interval in the JavaScript
   - Add more detailed progress information in the progress_callback function
   - Customize templates for your application's design
   - Add authentication and authorization as needed
   - Implement data persistence to database instead of cache
"""

if __name__ == "__main__":
    print("This is a Django integration example.")
    print("See the usage instructions at the bottom of this file.")
    print("Copy the relevant sections to your Django project.")
