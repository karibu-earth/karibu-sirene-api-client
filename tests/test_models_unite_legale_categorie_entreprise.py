"""Tests for sirene_api_client.models.unite_legale_categorie_entreprise module."""

import pytest

from sirene_api_client.models.unite_legale_categorie_entreprise import (
    UniteLegaleCategorieEntreprise,
)


@pytest.mark.requirement("REQ-MODEL-003")
class TestUniteLegaleCategorieEntreprise:
    """Test UniteLegaleCategorieEntreprise enum."""

    def test_enum_values(self):
        """Test enum values."""
        assert UniteLegaleCategorieEntreprise.PME == "PME"
        assert UniteLegaleCategorieEntreprise.ETI == "ETI"
        assert UniteLegaleCategorieEntreprise.GE == "GE"
        assert UniteLegaleCategorieEntreprise.NULL == "null"

    def test_enum_membership(self):
        """Test enum membership."""
        assert "PME" in UniteLegaleCategorieEntreprise
        assert "ETI" in UniteLegaleCategorieEntreprise
        assert "GE" in UniteLegaleCategorieEntreprise
        assert "null" in UniteLegaleCategorieEntreprise

    def test_enum_iteration(self):
        """Test enum iteration."""
        values = list(UniteLegaleCategorieEntreprise)
        assert len(values) == 4
        assert UniteLegaleCategorieEntreprise.PME in values
        assert UniteLegaleCategorieEntreprise.ETI in values
        assert UniteLegaleCategorieEntreprise.GE in values
        assert UniteLegaleCategorieEntreprise.NULL in values

    def test_enum_str_method(self):
        """Test __str__ method."""
        assert str(UniteLegaleCategorieEntreprise.PME) == "PME"
        assert str(UniteLegaleCategorieEntreprise.ETI) == "ETI"
        assert str(UniteLegaleCategorieEntreprise.GE) == "GE"
        assert str(UniteLegaleCategorieEntreprise.NULL) == "null"

    def test_enum_inheritance(self):
        """Test enum inheritance from str."""
        assert isinstance(UniteLegaleCategorieEntreprise.PME, str)
        assert isinstance(UniteLegaleCategorieEntreprise.ETI, str)
        assert isinstance(UniteLegaleCategorieEntreprise.GE, str)
        assert isinstance(UniteLegaleCategorieEntreprise.NULL, str)

    def test_enum_comparison(self):
        """Test enum comparison."""
        assert UniteLegaleCategorieEntreprise.PME == "PME"
        assert UniteLegaleCategorieEntreprise.ETI == "ETI"
        assert UniteLegaleCategorieEntreprise.GE == "GE"
        assert UniteLegaleCategorieEntreprise.NULL == "null"

    def test_enum_name_access(self):
        """Test enum name access."""
        assert UniteLegaleCategorieEntreprise.PME.name == "PME"
        assert UniteLegaleCategorieEntreprise.ETI.name == "ETI"
        assert UniteLegaleCategorieEntreprise.GE.name == "GE"
        assert UniteLegaleCategorieEntreprise.NULL.name == "NULL"

    def test_enum_value_access(self):
        """Test enum value access."""
        assert UniteLegaleCategorieEntreprise.PME.value == "PME"
        assert UniteLegaleCategorieEntreprise.ETI.value == "ETI"
        assert UniteLegaleCategorieEntreprise.GE.value == "GE"
        assert UniteLegaleCategorieEntreprise.NULL.value == "null"
