"""Tests for sirene_api_client.models.header module."""

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.header import Header


@pytest.mark.requirement("REQ-MODEL-007")
class TestHeader:
    """Test Header model."""

    def test_header_initialization_with_defaults(self):
        """Test Header initialization with default values."""
        header = Header()

        assert header.statut is UNSET
        assert header.message is UNSET
        assert header.total is UNSET
        assert header.debut is UNSET
        assert header.nombre is UNSET
        assert header.curseur is UNSET
        assert header.curseur_suivant is UNSET
        assert header.additional_properties == {}

    def test_header_initialization_with_values(self):
        """Test Header initialization with specific values."""
        header = Header(
            statut=200,
            message="OK",
            total=100,
            debut=0,
            nombre=20,
            curseur="cursor123",
            curseur_suivant="cursor456",
        )

        assert header.statut == 200
        assert header.message == "OK"
        assert header.total == 100
        assert header.debut == 0
        assert header.nombre == 20
        assert header.curseur == "cursor123"
        assert header.curseur_suivant == "cursor456"

    def test_header_to_dict_with_unset_values(self):
        """Test to_dict method with UNSET values."""
        header = Header()
        result = header.to_dict()

        assert result == {}

    def test_header_to_dict_with_values(self):
        """Test to_dict method with specific values."""
        header = Header(
            statut=200,
            message="OK",
            total=100,
            debut=0,
            nombre=20,
            curseur="cursor123",
            curseur_suivant="cursor456",
        )
        result = header.to_dict()

        assert result["statut"] == 200
        assert result["message"] == "OK"
        assert result["total"] == 100
        assert result["debut"] == 0
        assert result["nombre"] == 20
        assert result["curseur"] == "cursor123"
        assert result["curseurSuivant"] == "cursor456"

    def test_header_from_dict_with_empty_dict(self):
        """Test from_dict method with empty dictionary."""
        result = Header.from_dict({})

        assert result.statut is UNSET
        assert result.message is UNSET
        assert result.total is UNSET
        assert result.debut is UNSET
        assert result.nombre is UNSET
        assert result.curseur is UNSET
        assert result.curseur_suivant is UNSET
        assert result.additional_properties == {}

    def test_header_from_dict_with_values(self):
        """Test from_dict method with specific values."""
        data = {
            "statut": 200,
            "message": "OK",
            "total": 100,
            "debut": 0,
            "nombre": 20,
            "curseur": "cursor123",
            "curseurSuivant": "cursor456",
            "extra_field": "extra_value",
        }

        result = Header.from_dict(data)

        assert result.statut == 200
        assert result.message == "OK"
        assert result.total == 100
        assert result.debut == 0
        assert result.nombre == 20
        assert result.curseur == "cursor123"
        assert result.curseur_suivant == "cursor456"
        assert result.additional_properties == {"extra_field": "extra_value"}

    def test_header_additional_properties_access(self):
        """Test additional properties access methods."""
        header = Header()

        # Test __setitem__
        header["extra_field"] = "extra_value"
        assert header["extra_field"] == "extra_value"

        # Test __getitem__
        assert header["extra_field"] == "extra_value"

        # Test __contains__
        assert "extra_field" in header
        assert "nonexistent" not in header

        # Test additional_keys
        assert "extra_field" in header.additional_keys

        # Test __delitem__
        del header["extra_field"]
        assert "extra_field" not in header

    def test_header_with_mixed_values(self):
        """Test Header with some UNSET and some set values."""
        header = Header(
            statut=200,
            message="OK",
            total=UNSET,
            debut=0,
            nombre=UNSET,
            curseur="cursor123",
            curseur_suivant=UNSET,
        )
        result = header.to_dict()

        assert result["statut"] == 200
        assert result["message"] == "OK"
        assert result["debut"] == 0
        assert result["curseur"] == "cursor123"
        assert "total" not in result
        assert "nombre" not in result
        assert "curseur_suivant" not in result

    def test_header_serialization_roundtrip(self):
        """Test serialization and deserialization roundtrip."""
        original = Header(
            statut=200,
            message="OK",
            total=100,
            debut=0,
            nombre=20,
            curseur="cursor123",
            curseur_suivant="cursor456",
        )
        original["extra"] = "value"

        # Convert to dict and back
        data = original.to_dict()
        restored = Header.from_dict(data)

        assert restored.statut == 200
        assert restored.message == "OK"
        assert restored.total == 100
        assert restored.debut == 0
        assert restored.nombre == 20
        assert restored.curseur == "cursor123"
        assert restored.curseur_suivant == "cursor456"
        assert restored["extra"] == "value"

    def test_header_with_zero_values(self):
        """Test Header with zero values (should be included in dict)."""
        header = Header(
            statut=0,
            message="",
            total=0,
            debut=0,
            nombre=0,
            curseur="",
            curseur_suivant="",
        )
        result = header.to_dict()

        assert result["statut"] == 0
        assert result["message"] == ""
        assert result["total"] == 0
        assert result["debut"] == 0
        assert result["nombre"] == 0
        assert result["curseur"] == ""
        assert result["curseurSuivant"] == ""
