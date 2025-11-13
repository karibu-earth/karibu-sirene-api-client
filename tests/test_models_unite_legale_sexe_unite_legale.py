"""Tests for sirene_api_client.models.unite_legale_sexe_unite_legale module."""

import pytest

from sirene_api_client.models.unite_legale_sexe_unite_legale import (
    UniteLegaleSexeUniteLegale,
)


@pytest.mark.requirement("REQ-MODEL-004")
class TestUniteLegaleSexeUniteLegale:
    """Test UniteLegaleSexeUniteLegale enum."""

    def test_enum_values(self):
        """Test enum values."""
        assert UniteLegaleSexeUniteLegale.M == "M"
        assert UniteLegaleSexeUniteLegale.F == "F"
        assert UniteLegaleSexeUniteLegale.NULL == "null"

    def test_enum_membership(self):
        """Test enum membership."""
        assert "M" in UniteLegaleSexeUniteLegale
        assert "F" in UniteLegaleSexeUniteLegale
        assert "null" in UniteLegaleSexeUniteLegale

    def test_enum_iteration(self):
        """Test enum iteration."""
        values = list(UniteLegaleSexeUniteLegale)
        assert len(values) == 4
        assert UniteLegaleSexeUniteLegale.M in values
        assert UniteLegaleSexeUniteLegale.F in values
        assert UniteLegaleSexeUniteLegale.NULL in values

    def test_enum_str_method(self):
        """Test __str__ method."""
        assert str(UniteLegaleSexeUniteLegale.M) == "M"
        assert str(UniteLegaleSexeUniteLegale.F) == "F"
        assert str(UniteLegaleSexeUniteLegale.NULL) == "null"

    def test_enum_inheritance(self):
        """Test enum inheritance from str."""
        assert isinstance(UniteLegaleSexeUniteLegale.M, str)
        assert isinstance(UniteLegaleSexeUniteLegale.F, str)
        assert isinstance(UniteLegaleSexeUniteLegale.NULL, str)

    def test_enum_comparison(self):
        """Test enum comparison."""
        assert UniteLegaleSexeUniteLegale.M == "M"
        assert UniteLegaleSexeUniteLegale.F == "F"
        assert UniteLegaleSexeUniteLegale.NULL == "null"

    def test_enum_name_access(self):
        """Test enum name access."""
        assert UniteLegaleSexeUniteLegale.M.name == "M"
        assert UniteLegaleSexeUniteLegale.F.name == "F"
        assert UniteLegaleSexeUniteLegale.NULL.name == "NULL"

    def test_enum_value_access(self):
        """Test enum value access."""
        assert UniteLegaleSexeUniteLegale.M.value == "M"
        assert UniteLegaleSexeUniteLegale.F.value == "F"
        assert UniteLegaleSexeUniteLegale.NULL.value == "null"
