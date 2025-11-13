"""
Coordinate conversion utilities for the SIREN ETL service.

This module handles conversion from Lambert 93 (EPSG:2154) to WGS84 (EPSG:4326).

The range check for Lambert 93 coordinates is optional and defaults to non-strict mode,
allowing conversion of coordinates outside the typical range. This supports handling
overseas territories that may be mislabeled as Lambert 93 but use different coordinate
reference systems (e.g., Réunion, Guadeloupe, Martinique, French Guiana).
"""

from __future__ import annotations

import logging

from pyproj import Transformer

from .exceptions import CoordinateConversionError

logger = logging.getLogger(__name__)

# Lambert 93 to WGS84 transformer
_LAMBERT93_TO_WGS84 = Transformer.from_crs("EPSG:2154", "EPSG:4326", always_xy=True)


def lambert93_to_wgs84(
    x: str | float | int, y: str | float | int, *, strict_range_check: bool = False
) -> tuple[float, float] | None:
    """
    Convert Lambert 93 (EPSG:2154) coordinates to WGS84 (EPSG:4326).

    Args:
        x: Lambert 93 X coordinate as string, float, or int
        y: Lambert 93 Y coordinate as string, float, or int
        strict_range_check: If True, raises CoordinateConversionError for coordinates
            outside the typical Lambert 93 range (x: 0-1200000, y: 6000000-7200000).
            If False (default), logs a warning but attempts conversion anyway.
            This allows handling overseas territories that may be mislabeled as Lambert 93
            but use different coordinate reference systems.

    Returns:
        Tuple of (longitude, latitude) in WGS84, or None if conversion fails

    Raises:
        CoordinateConversionError: If coordinates are invalid or conversion fails.
            When strict_range_check=True, also raises for out-of-range coordinates.
    """
    # Handle different input types
    if isinstance(x, int | float) and isinstance(y, int | float):
        # Direct numeric inputs
        x_float = float(x)
        y_float = float(y)
    else:
        # String inputs - check for empty/whitespace
        if (
            not x
            or not y
            or (isinstance(x, str) and not x.strip())
            or (isinstance(y, str) and not y.strip())
        ):
            logger.debug("Empty coordinates provided, returning None")
            return None

        # Convert string coordinates to float
        try:
            x_float = float(x)
            y_float = float(y)
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid coordinate format: x={x}, y={y}, error={e}")
            raise CoordinateConversionError(
                f"Coordinate conversion failed - invalid format: {e}",
                x=str(x) if x is not None else None,
                y=str(y) if y is not None else None,
            ) from e

    try:
        # Check for reasonable Lambert 93 coordinate ranges (France)
        # Note: Overseas territories use different CRS but may be mislabeled
        is_in_range = (0 <= x_float <= 1200000) and (6000000 <= y_float <= 7200000)

        if not is_in_range:
            if strict_range_check:
                logger.warning(
                    f"Coordinates out of expected Lambert 93 range: x={x_float}, y={y_float}"
                )
                raise CoordinateConversionError(
                    f"Coordinates out of Lambert 93 range: x={x_float}, y={y_float}",
                    x=str(x) if x is not None else None,
                    y=str(y) if y is not None else None,
                )
            else:
                logger.warning(
                    f"Coordinates outside typical Lambert 93 range (x={x_float}, y={y_float}). "
                    f"Attempting conversion anyway - may be overseas territory or edge case."
                )

        # Perform coordinate transformation
        lon, lat = _LAMBERT93_TO_WGS84.transform(x_float, y_float)

        # Validate WGS84 coordinates
        if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
            logger.warning(f"Invalid WGS84 coordinates: lon={lon}, lat={lat}")
            return None

        logger.debug(
            f"Converted Lambert 93 ({x_float}, {y_float}) to WGS84 ({lon}, {lat})"
        )
        return (lon, lat)
    except CoordinateConversionError:
        # Re-raise our custom exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Coordinate conversion failed: x={x}, y={y}, error={e}")
        raise CoordinateConversionError(
            f"Failed to convert coordinates: {e}",
            x=str(x) if x is not None else None,
            y=str(y) if y is not None else None,
        ) from e


def is_valid_lambert93_coordinate(x: str, y: str) -> bool:
    """
    Check if coordinates are valid Lambert 93 format.

    Args:
        x: X coordinate as string
        y: Y coordinate as string

    Returns:
        True if coordinates are valid Lambert 93 format
    """
    try:
        x_float = float(x)
        y_float = float(y)
        return (0 <= x_float <= 1200000) and (6000000 <= y_float <= 7200000)
    except (ValueError, TypeError):
        return False
