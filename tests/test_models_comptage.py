"""Tests for sirene_api_client.models.comptage module."""

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.comptage import Comptage
from sirene_api_client.models.comptage_valeur import ComptageValeur


@pytest.mark.requirement("REQ-MODEL-001")
class TestComptage:
    """Test Comptage model."""

    def test_comptage_initialization_with_defaults(self):
        """Test Comptage initialization with default values."""
        comptage = Comptage()

        assert comptage.valeur is UNSET
        assert comptage.nombre is UNSET
        assert comptage.additional_properties == {}

    def test_comptage_initialization_with_values(self):
        """Test Comptage initialization with specific values."""
        valeur = ComptageValeur()
        nombre = 42

        comptage = Comptage(valeur=valeur, nombre=nombre)

        assert comptage.valeur == valeur
        assert comptage.nombre == nombre
        assert comptage.additional_properties == {}

    def test_comptage_to_dict_with_unset_values(self):
        """Test to_dict method with UNSET values."""
        comptage = Comptage()
        result = comptage.to_dict()

        assert result == {}

    def test_comptage_to_dict_with_values(self):
        """Test to_dict method with specific values."""
        valeur = ComptageValeur()
        nombre = 42

        comptage = Comptage(valeur=valeur, nombre=nombre)
        result = comptage.to_dict()

        assert result["valeur"] == valeur.to_dict()
        assert result["nombre"] == nombre

    def test_comptage_from_dict_with_empty_dict(self):
        """Test from_dict method with empty dictionary."""
        result = Comptage.from_dict({})

        assert result.valeur is UNSET
        assert result.nombre is UNSET
        assert result.additional_properties == {}

    def test_comptage_from_dict_with_values(self):
        """Test from_dict method with specific values."""
        data = {"valeur": {}, "nombre": 42, "extra_field": "extra_value"}

        result = Comptage.from_dict(data)

        assert isinstance(result.valeur, ComptageValeur)
        assert result.nombre == 42
        assert result.additional_properties == {"extra_field": "extra_value"}

    def test_comptage_additional_properties_access(self):
        """Test additional properties access methods."""
        comptage = Comptage()

        # Test __setitem__
        comptage["extra_field"] = "extra_value"
        assert comptage["extra_field"] == "extra_value"

        # Test __getitem__
        assert comptage["extra_field"] == "extra_value"

        # Test __contains__
        assert "extra_field" in comptage
        assert "nonexistent" not in comptage

        # Test additional_keys
        assert "extra_field" in comptage.additional_keys

        # Test __delitem__
        del comptage["extra_field"]
        assert "extra_field" not in comptage

    def test_comptage_additional_properties_dict_access(self):
        """Test direct access to additional_properties dictionary."""
        comptage = Comptage()

        comptage.additional_properties["test"] = "value"
        assert comptage.additional_properties["test"] == "value"
        assert comptage["test"] == "value"

    def test_comptage_with_mixed_values(self):
        """Test Comptage with some UNSET and some set values."""
        valeur = ComptageValeur()

        comptage = Comptage(valeur=valeur, nombre=UNSET)
        result = comptage.to_dict()

        assert result["valeur"] == valeur.to_dict()
        assert "nombre" not in result

    def test_comptage_serialization_roundtrip(self):
        """Test serialization and deserialization roundtrip."""
        original = Comptage()
        original["extra"] = "value"

        # Convert to dict and back
        data = original.to_dict()
        restored = Comptage.from_dict(data)

        assert restored.valeur is UNSET
        assert restored.nombre is UNSET
        assert restored["extra"] == "value"
