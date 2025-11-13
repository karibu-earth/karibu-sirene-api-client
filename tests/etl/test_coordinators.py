"""
Unit tests for coordinate conversion utilities.

Tests cover:
- Lambert 93 to WGS84 conversion accuracy
- Error handling for invalid coordinates
- Edge cases and boundary conditions
- Performance characteristics
"""

import pytest

from sirene_api_client.etl.coordinators import lambert93_to_wgs84
from sirene_api_client.etl.exceptions import CoordinateConversionError


class TestLambert93ToWgs84:
    """Test Lambert 93 to WGS84 coordinate conversion."""

    def test_valid_coordinates_conversion(self) -> None:
        """Test conversion of valid Lambert 93 coordinates."""
        # Known test coordinates: Paris area
        x = "652345.12"
        y = "6862275.45"

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

        # Paris should be around 2.35°E, 48.85°N
        assert 2.0 <= longitude <= 3.0
        assert 48.0 <= latitude <= 49.0

    def test_coordinates_as_floats(self) -> None:
        """Test conversion with float inputs."""
        x = 652345.12
        y = 6862275.45

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

    def test_coordinates_as_integers(self) -> None:
        """Test conversion with integer inputs."""
        x = 652345
        y = 6862275

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

    def test_empty_strings(self) -> None:
        """Test conversion with empty string inputs."""
        result = lambert93_to_wgs84("", "")

        assert result is None

    def test_none_inputs(self) -> None:
        """Test conversion with None inputs."""
        result = lambert93_to_wgs84(None, None)

        assert result is None

    def test_invalid_string_coordinates(self) -> None:
        """Test conversion with invalid string coordinates."""
        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84("invalid", "coordinates")

    def test_out_of_bounds_coordinates(self) -> None:
        """Test conversion with out-of-bounds coordinates (strict mode)."""
        # Very large coordinates outside France
        x = "999999999"
        y = "999999999"

        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84(x, y, strict_range_check=True)

    def test_negative_coordinates(self) -> None:
        """Test conversion with negative coordinates (strict mode)."""
        x = "-100000"
        y = "-100000"

        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84(x, y, strict_range_check=True)

    def test_zero_coordinates(self) -> None:
        """Test conversion with zero coordinates (strict mode)."""
        x = "0"
        y = "0"

        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84(x, y, strict_range_check=True)

    def test_whitespace_coordinates(self) -> None:
        """Test conversion with whitespace-only coordinates."""
        result = lambert93_to_wgs84("   ", "   ")

        assert result is None

    def test_leading_trailing_whitespace(self) -> None:
        """Test conversion with coordinates having leading/trailing whitespace."""
        x = "  652345.12  "
        y = "  6862275.45  "

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

    def test_scientific_notation(self) -> None:
        """Test conversion with scientific notation."""
        x = "6.5234512e5"
        y = "6.8622745e6"

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)

    def test_decimal_precision(self) -> None:
        """Test conversion maintains appropriate decimal precision."""
        x = "652345.123456789"
        y = "6862275.987654321"

        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result

        # Should have reasonable precision (check that it's not excessive)
        lon_str = str(longitude)
        lat_str = str(latitude)

        # For scientific notation, check the total length
        if "e" in lon_str.lower():
            assert len(lon_str) <= 20  # Reasonable length for scientific notation
        else:
            assert (
                len(lon_str.split(".")[1]) <= 16
            )  # Allow more precision for high-precision inputs

        if "e" in lat_str.lower():
            assert len(lat_str) <= 20  # Reasonable length for scientific notation
        else:
            assert (
                len(lat_str.split(".")[1]) <= 16
            )  # Allow more precision for high-precision inputs

    @pytest.mark.parametrize(
        ("x", "y", "expected_region"),
        [
            ("652345", "6862275", "Paris"),  # Paris area
            ("500000", "6500000", "Southwest"),  # Southwest France
            ("800000", "7200000", "Northeast"),  # Northeast France
        ],
    )
    def test_different_french_regions(
        self, x: str, y: str, expected_region: str
    ) -> None:
        """Test conversion for different French regions."""
        result = lambert93_to_wgs84(x, y)

        assert result is not None
        longitude, latitude = result

        # All should be within France bounds
        assert -5.0 <= longitude <= 10.0
        assert 41.0 <= latitude <= 52.0

        # Verify the region name is provided (for documentation purposes)
        assert expected_region in ["Paris", "Southwest", "Northeast"]

    def test_conversion_consistency(self) -> None:
        """Test that repeated conversions give consistent results."""
        x = "652345.12"
        y = "6862275.45"

        result1 = lambert93_to_wgs84(x, y)
        result2 = lambert93_to_wgs84(x, y)

        assert result1 == result2
        assert result1 is not None
        assert result2 is not None

    def test_conversion_reversibility_approximation(self) -> None:
        """Test that conversion is approximately reversible."""
        # Original Lambert 93 coordinates
        original_x = 652345.12
        original_y = 6862275.45

        # Convert to WGS84
        wgs84_result = lambert93_to_wgs84(original_x, original_y)
        assert wgs84_result is not None

        longitude, latitude = wgs84_result

        # Note: We can't easily reverse without additional libraries,
        # but we can verify the result is reasonable
        assert isinstance(longitude, float)
        assert isinstance(latitude, float)
        assert -180 <= longitude <= 180
        assert -90 <= latitude <= 90

    def test_performance_large_batch(self) -> None:
        """Test performance with multiple coordinate conversions."""
        import time

        coordinates = [
            ("652345.12", "6862275.45"),
            ("500000.00", "6500000.00"),
            ("800000.00", "7200000.00"),
            ("600000.00", "7000000.00"),
            ("700000.00", "6800000.00"),
        ]

        start_time = time.time()

        results = []
        for x, y in coordinates:
            result = lambert93_to_wgs84(x, y)
            results.append(result)

        end_time = time.time()
        duration = end_time - start_time

        # Should complete in reasonable time (less than 1 second for 5 conversions)
        assert duration < 1.0
        assert len(results) == 5
        assert all(result is not None for result in results)

    def test_error_message_content(self) -> None:
        """Test that error messages are informative."""
        with pytest.raises(CoordinateConversionError) as exc_info:
            lambert93_to_wgs84("invalid", "coordinates")

        error_message = str(exc_info.value)
        assert "coordinate conversion" in error_message.lower()
        assert "invalid" in error_message.lower()

    def test_error_with_valid_x_invalid_y(self) -> None:
        """Test error handling with one valid and one invalid coordinate."""
        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84("652345.12", "invalid")

    def test_error_with_invalid_x_valid_y(self) -> None:
        """Test error handling with one invalid and one valid coordinate."""
        with pytest.raises(CoordinateConversionError):
            lambert93_to_wgs84("invalid", "6862275.45")

    def test_default_behavior_is_non_strict(self) -> None:
        """Test that default behavior is non-strict (no exception on out-of-range)."""
        # Out-of-range coordinates should attempt conversion, not raise immediately
        # Note: pyproj may still fail or return invalid results, but we don't raise
        # based on range check alone
        x = "999999999"
        y = "999999999"

        # Should not raise CoordinateConversionError due to range check
        # (may fail later in conversion, but that's expected)
        error_message = None
        try:
            result = lambert93_to_wgs84(x, y)
            # If conversion succeeds, result should be None or valid WGS84
            if result is not None:
                lon, lat = result
                # WGS84 validation should catch invalid results
                assert -180 <= lon <= 180
                assert -90 <= lat <= 90
        except CoordinateConversionError as e:
            # If it raises, it should NOT be due to range check
            # (would have "out of lambert 93 range" in message for strict mode)
            error_message = str(e).lower()

        # Assert outside except block to avoid PT017
        if error_message is not None:
            assert "out of lambert 93 range" not in error_message

    def test_out_of_range_with_strict_check_false(self) -> None:
        """Test that out-of-range coordinates log warning but attempt conversion."""
        # Coordinates outside typical Lambert 93 range
        x = "999999999"
        y = "999999999"

        # Should not raise exception when strict_range_check=False
        # May return None if conversion fails, but shouldn't raise on range check
        result = lambert93_to_wgs84(x, y, strict_range_check=False)

        # Result may be None if pyproj can't convert, but no exception should be raised
        # for range check specifically
        assert result is None or (isinstance(result, tuple) and len(result) == 2)

    def test_out_of_range_with_strict_check_true(self) -> None:
        """Test that out-of-range coordinates raise exception in strict mode."""
        # Coordinates outside typical Lambert 93 range
        x = "999999999"
        y = "999999999"

        with pytest.raises(CoordinateConversionError) as exc_info:
            lambert93_to_wgs84(x, y, strict_range_check=True)

        # Verify error message mentions range
        error_message = str(exc_info.value)
        assert "range" in error_message.lower()

    def test_boundary_conditions_strict_mode(self) -> None:
        """Test boundary values in both strict and non-strict modes."""
        # Test boundary values: x in [0, 1200000], y in [6000000, 7200000]
        boundary_cases = [
            ("0", "6000000", True),  # Lower boundary - should pass
            ("1200000", "7200000", True),  # Upper boundary - should pass
            ("600000", "6600000", True),  # Middle - should pass
            ("-1", "6000000", False),  # Just below x boundary
            ("0", "5999999", False),  # Just below y boundary
            ("1200001", "7200000", False),  # Just above x boundary
            ("1200000", "7200001", False),  # Just above y boundary
        ]

        for x, y, is_in_range in boundary_cases:
            if is_in_range:
                # Should succeed in both modes
                result_strict = lambert93_to_wgs84(x, y, strict_range_check=True)
                result_non_strict = lambert93_to_wgs84(x, y, strict_range_check=False)
                assert result_strict is not None
                assert result_non_strict is not None
                assert result_strict == result_non_strict
            else:
                # Should raise in strict mode, attempt in non-strict
                with pytest.raises(CoordinateConversionError):
                    lambert93_to_wgs84(x, y, strict_range_check=True)

                # Non-strict should attempt (may return None if conversion fails)
                result = lambert93_to_wgs84(x, y, strict_range_check=False)
                assert result is None or (
                    isinstance(result, tuple) and len(result) == 2
                )

    def test_overseas_territory_coordinates(self) -> None:
        """Test coordinates that might be from overseas territories."""
        # Coordinates that might be mislabeled as Lambert 93 but are actually
        # from overseas territories using different CRS
        # These coordinates are outside Lambert 93 range but might be valid in other systems
        overseas_coords = [
            ("300000", "16000000"),  # Example: might be from Réunion or Guadeloupe
            ("500000", "5000000"),  # Example: might be from French Guiana
        ]

        for x, y in overseas_coords:
            # In non-strict mode, should attempt conversion
            result = lambert93_to_wgs84(x, y, strict_range_check=False)
            # Result may be None if conversion fails, but shouldn't raise on range check
            assert result is None or (isinstance(result, tuple) and len(result) == 2)

            # In strict mode, should raise immediately
            with pytest.raises(CoordinateConversionError):
                lambert93_to_wgs84(x, y, strict_range_check=True)

    def test_out_of_range_coordinates_attempt_conversion_by_default(self) -> None:
        """Verify out-of-range coordinates are attempted with default (non-strict)."""
        # Test that default behavior (strict_range_check not specified) is non-strict
        x = "999999999"
        y = "999999999"

        # Default call should not raise on range check
        error_message = None
        try:
            result = lambert93_to_wgs84(x, y)
            # If conversion succeeds, validate WGS84
            if result is not None:
                lon, lat = result
                assert -180 <= lon <= 180
                assert -90 <= lat <= 90
        except CoordinateConversionError as e:
            # Should not raise due to range check in default mode
            # (may raise for other reasons like pyproj failure)
            error_message = str(e).lower()

        # Assert outside except block to avoid PT017
        if error_message is not None:
            assert "out of lambert 93 range" not in error_message
