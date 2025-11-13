"""
Unit tests for ETL configuration module.

Tests cover:
- ValidationMode enum values and behavior
- ETLConfig dataclass initialization and validation
- Default configuration values
- Configuration validation logic
"""

import pytest

from sirene_api_client.etl.config import ETLConfig, ValidationMode


class TestValidationMode:
    """Test ValidationMode enum functionality."""

    def test_validation_mode_values(self) -> None:
        """Test that ValidationMode has expected values."""
        assert ValidationMode.STRICT.value == "strict"
        assert ValidationMode.LENIENT.value == "lenient"
        assert ValidationMode.PERMISSIVE.value == "permissive"

    def test_validation_mode_membership(self) -> None:
        """Test ValidationMode membership."""
        assert "strict" in ValidationMode
        assert "lenient" in ValidationMode
        assert "permissive" in ValidationMode
        assert "invalid" not in ValidationMode

    @pytest.mark.parametrize("mode", ["strict", "lenient", "permissive"])
    def test_validation_mode_valid_values(self, mode: str) -> None:
        """Test that all expected validation modes are valid."""
        assert mode in ValidationMode

    def test_validation_mode_invalid_value(self) -> None:
        """Test that invalid validation mode raises error."""
        with pytest.raises(ValueError, match="is not a valid ValidationMode"):
            ValidationMode("invalid_mode")


class TestETLConfig:
    """Test ETLConfig dataclass functionality."""

    def test_default_configuration(self) -> None:
        """Test default ETL configuration values."""
        config = ETLConfig()

        assert config.validation_mode == ValidationMode.LENIENT
        assert config.include_personal_data is False
        assert config.coordinate_precision == "approximate"
        assert config.max_retries == 3
        assert config.timeout_seconds == 30

    def test_custom_configuration(self) -> None:
        """Test custom ETL configuration values."""
        config = ETLConfig(
            validation_mode=ValidationMode.STRICT,
            include_personal_data=True,
            coordinate_precision="rooftop",
            max_retries=5,
            timeout_seconds=60,
        )

        assert config.validation_mode == ValidationMode.STRICT
        assert config.include_personal_data is True
        assert config.coordinate_precision == "rooftop"
        assert config.max_retries == 5
        assert config.timeout_seconds == 60

    def test_config_immutability(self) -> None:
        """Test that ETLConfig can be modified after creation."""
        config = ETLConfig()

        # Dataclasses are mutable by default
        config.validation_mode = ValidationMode.STRICT
        assert config.validation_mode == ValidationMode.STRICT

    def test_config_str_representation(self) -> None:
        """Test string representation of ETLConfig."""
        config = ETLConfig(validation_mode=ValidationMode.STRICT)
        config_str = str(config)

        assert "ETLConfig" in config_str
        assert "strict" in config_str

    def test_config_repr_representation(self) -> None:
        """Test repr representation of ETLConfig."""
        config = ETLConfig(validation_mode=ValidationMode.STRICT)
        config_repr = repr(config)

        assert "ETLConfig" in config_repr
        assert "strict" in config_repr

    @pytest.mark.parametrize("max_retries", [-1])
    def test_invalid_max_retries(self, max_retries: int) -> None:
        """Test that invalid max_retries values raise ValueError."""
        with pytest.raises(ValueError, match="max_retries must be non-negative"):
            ETLConfig(max_retries=max_retries)

    @pytest.mark.parametrize("timeout", [-1, 0])
    def test_invalid_timeout(self, timeout: int) -> None:
        """Test that invalid timeout values raise ValueError."""
        with pytest.raises(ValueError, match="timeout_seconds must be positive"):
            ETLConfig(timeout_seconds=timeout)

    def test_config_equality(self) -> None:
        """Test ETLConfig equality comparison."""
        config1 = ETLConfig(validation_mode=ValidationMode.STRICT)
        config2 = ETLConfig(validation_mode=ValidationMode.STRICT)
        config3 = ETLConfig(validation_mode=ValidationMode.LENIENT)

        assert config1 == config2
        assert config1 != config3

    def test_config_with_different_values(self) -> None:
        """Test ETLConfig with different field values."""
        config1 = ETLConfig(validation_mode=ValidationMode.STRICT, max_retries=5)
        config2 = ETLConfig(validation_mode=ValidationMode.STRICT, max_retries=3)

        assert config1 != config2
        assert config1.max_retries == 5
        assert config2.max_retries == 3
