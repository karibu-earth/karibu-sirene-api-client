"""Tests for sirene_api_client.models.comptage_valeur module."""

import pytest

from sirene_api_client.models.comptage_valeur import ComptageValeur


@pytest.mark.requirement("REQ-MODEL-002")
class TestComptageValeur:
    """Test ComptageValeur model."""

    def test_comptage_valeur_initialization(self):
        """Test ComptageValeur initialization."""
        comptage_valeur = ComptageValeur()

        assert comptage_valeur.additional_properties == {}

    def test_comptage_valeur_to_dict_empty(self):
        """Test to_dict method with empty additional properties."""
        comptage_valeur = ComptageValeur()
        result = comptage_valeur.to_dict()

        assert result == {}

    def test_comptage_valeur_to_dict_with_properties(self):
        """Test to_dict method with additional properties."""
        comptage_valeur = ComptageValeur()
        comptage_valeur["key1"] = "value1"
        comptage_valeur["key2"] = 42

        result = comptage_valeur.to_dict()

        assert result == {"key1": "value1", "key2": 42}

    def test_comptage_valeur_from_dict_empty(self):
        """Test from_dict method with empty dictionary."""
        result = ComptageValeur.from_dict({})

        assert result.additional_properties == {}

    def test_comptage_valeur_from_dict_with_data(self):
        """Test from_dict method with data."""
        data = {"key1": "value1", "key2": 42, "nested": {"inner": "value"}}

        result = ComptageValeur.from_dict(data)

        assert result.additional_properties == data

    def test_comptage_valeur_additional_properties_access(self):
        """Test additional properties access methods."""
        comptage_valeur = ComptageValeur()

        # Test __setitem__
        comptage_valeur["test_key"] = "test_value"
        assert comptage_valeur["test_key"] == "test_value"

        # Test __getitem__
        assert comptage_valeur["test_key"] == "test_value"

        # Test __contains__
        assert "test_key" in comptage_valeur
        assert "nonexistent" not in comptage_valeur

        # Test additional_keys
        assert "test_key" in comptage_valeur.additional_keys

        # Test __delitem__
        del comptage_valeur["test_key"]
        assert "test_key" not in comptage_valeur

    def test_comptage_valeur_additional_properties_dict_access(self):
        """Test direct access to additional_properties dictionary."""
        comptage_valeur = ComptageValeur()

        comptage_valeur.additional_properties["direct"] = "access"
        assert comptage_valeur.additional_properties["direct"] == "access"
        assert comptage_valeur["direct"] == "access"

    def test_comptage_valeur_serialization_roundtrip(self):
        """Test serialization and deserialization roundtrip."""
        original = ComptageValeur()
        original["field1"] = "value1"
        original["field2"] = 123
        original["nested"] = {"key": "value"}

        # Convert to dict and back
        data = original.to_dict()
        restored = ComptageValeur.from_dict(data)

        assert restored["field1"] == "value1"
        assert restored["field2"] == 123
        assert restored["nested"] == {"key": "value"}

    def test_comptage_valeur_multiple_properties(self):
        """Test ComptageValeur with multiple properties."""
        comptage_valeur = ComptageValeur()

        # Add multiple properties
        comptage_valeur["string_prop"] = "string_value"
        comptage_valeur["int_prop"] = 42
        comptage_valeur["float_prop"] = 3.14
        comptage_valeur["bool_prop"] = True
        comptage_valeur["list_prop"] = [1, 2, 3]

        result = comptage_valeur.to_dict()

        assert result["string_prop"] == "string_value"
        assert result["int_prop"] == 42
        assert result["float_prop"] == 3.14
        assert result["bool_prop"] is True
        assert result["list_prop"] == [1, 2, 3]

    def test_comptage_valeur_key_error(self):
        """Test KeyError when accessing non-existent key."""
        comptage_valeur = ComptageValeur()

        with pytest.raises(KeyError):
            _ = comptage_valeur["nonexistent_key"]

    def test_comptage_valeur_key_error_on_delete(self):
        """Test KeyError when deleting non-existent key."""
        comptage_valeur = ComptageValeur()

        with pytest.raises(KeyError):
            del comptage_valeur["nonexistent_key"]
