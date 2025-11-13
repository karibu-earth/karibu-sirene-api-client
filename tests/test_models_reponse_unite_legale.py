"""Tests for sirene_api_client.models.reponse_unite_legale module."""

from datetime import date

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_unite_legale import ReponseUniteLegale
from sirene_api_client.models.unite_legale import UniteLegale


@pytest.mark.requirement("REQ-MODEL-007")
class TestReponseUniteLegale:
    """Test ReponseUniteLegale model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        header = Header(statut=200, message="OK", total=1)
        unite_legale = UniteLegale(siren="123456789")

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        assert reponse.header == header
        assert reponse.unite_legale == unite_legale

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        reponse = ReponseUniteLegale()

        assert reponse.header is UNSET
        assert reponse.unite_legale is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        header = Header(statut=200, message="OK", total=1)
        unite_legale = UniteLegale(siren="123456789")

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        result = reponse.to_dict()

        assert "header" in result
        assert "uniteLegale" in result
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["uniteLegale"]["siren"] == "123456789"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        reponse = ReponseUniteLegale()

        result = reponse.to_dict()

        assert "header" not in result
        assert "uniteLegale" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 1,
            },
            "uniteLegale": {
                "siren": "123456789",
            },
        }

        reponse = ReponseUniteLegale.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 1

        assert isinstance(reponse.unite_legale, UniteLegale)
        assert reponse.unite_legale.siren == "123456789"

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}  # Empty data

        reponse = ReponseUniteLegale.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.unite_legale is UNSET

    def test_from_dict_with_unset_values(self):
        """Test from_dict with UNSET values."""
        data = {
            "header": UNSET,
            "uniteLegale": UNSET,
        }

        reponse = ReponseUniteLegale.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.unite_legale is UNSET

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        header = Header(statut=200, message="OK", total=1)
        unite_legale = UniteLegale(siren="123456789")

        original = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = ReponseUniteLegale.from_dict(data)

        # Verify all fields are preserved
        assert isinstance(restored.header, Header)
        assert restored.header.statut == original.header.statut
        assert restored.header.message == original.header.message
        assert restored.header.total == original.header.total

        assert isinstance(restored.unite_legale, UniteLegale)
        assert restored.unite_legale.siren == original.unite_legale.siren

        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        reponse = ReponseUniteLegale()
        reponse["custom_field"] = "custom_value"

        assert reponse["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        reponse = ReponseUniteLegale()
        reponse["custom_field"] = "custom_value"

        assert reponse.additional_properties["custom_field"] == "custom_value"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        reponse = ReponseUniteLegale()
        reponse["custom_field"] = "custom_value"

        del reponse["custom_field"]

        assert "custom_field" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        reponse = ReponseUniteLegale()
        reponse["custom_field"] = "custom_value"

        assert "custom_field" in reponse
        assert "nonexistent_field" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseUniteLegale()
        reponse["field1"] = "value1"
        reponse["field2"] = "value2"

        keys = reponse.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_nested_model_serialization(self):
        """Test serialization of nested models."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=20,
            curseur="abc123",
            curseur_suivant="def456",
        )

        unite_legale = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
        )

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 20
        assert result["header"]["curseur"] == "abc123"
        assert result["header"]["curseurSuivant"] == "def456"

        # Verify unite_legale serialization
        assert result["uniteLegale"]["siren"] == "123456789"
        assert result["uniteLegale"]["statutDiffusionUniteLegale"] == "O"
        assert result["uniteLegale"]["dateCreationUniteLegale"] == "2020-01-01"

    def test_nested_model_deserialization(self):
        """Test deserialization of nested models."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 1,
                "debut": 0,
                "nombre": 20,
                "curseur": "abc123",
                "curseurSuivant": "def456",
            },
            "uniteLegale": {
                "siren": "123456789",
                "statutDiffusionUniteLegale": "O",
                "dateCreationUniteLegale": "2020-01-01",
            },
        }

        reponse = ReponseUniteLegale.from_dict(data)

        # Verify header deserialization
        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 1
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 20
        assert reponse.header.curseur == "abc123"
        assert reponse.header.curseur_suivant == "def456"

        # Verify unite_legale deserialization
        assert isinstance(reponse.unite_legale, UniteLegale)
        assert reponse.unite_legale.siren == "123456789"
        assert reponse.unite_legale.statut_diffusion_unite_legale == "O"
        assert reponse.unite_legale.date_creation_unite_legale == date(2020, 1, 1)

    def test_partial_nested_models(self):
        """Test handling of partial nested models."""
        # Only header, no unite_legale
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
            },
        }

        reponse = ReponseUniteLegale.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.unite_legale is UNSET

        # Only unite_legale, no header
        data = {
            "uniteLegale": {
                "siren": "123456789",
            },
        }

        reponse = ReponseUniteLegale.from_dict(data)

        assert reponse.header is UNSET
        assert isinstance(reponse.unite_legale, UniteLegale)
        assert reponse.unite_legale.siren == "123456789"

    def test_error_response_handling(self):
        """Test handling of error responses."""
        header = Header(statut=404, message="Not Found", total=0)

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=UNSET,  # No unite_legale in error case
        )

        result = reponse.to_dict()

        assert result["header"]["statut"] == 404
        assert result["header"]["message"] == "Not Found"
        assert result["header"]["total"] == 0
        assert "uniteLegale" not in result

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        header = Header(message="Unité légale trouvée")
        unite_legale = UniteLegale(siren="123456789")

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )
        reponse["unicode_field"] = "Café & Société 🏢"

        result = reponse.to_dict()
        assert result["header"]["message"] == "Unité légale trouvée"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = ReponseUniteLegale.from_dict(result)
        assert restored.header.message == "Unité légale trouvée"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        header = Header(message="")  # Empty string
        unite_legale = UniteLegale(siren="123456789")

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        result = reponse.to_dict()
        assert result["header"]["message"] == ""
        assert result["uniteLegale"]["siren"] == "123456789"

    def test_additional_properties_preservation(self):
        """Test that additional properties are preserved through serialization."""
        reponse = ReponseUniteLegale()
        reponse["extra_field1"] = "value1"
        reponse["extra_field2"] = "value2"
        reponse["extra_field3"] = {"nested": "object"}

        data = reponse.to_dict()
        restored = ReponseUniteLegale.from_dict(data)

        assert restored["extra_field1"] == "value1"
        assert restored["extra_field2"] == "value2"
        assert restored["extra_field3"] == {"nested": "object"}

    def test_complex_nested_structure(self):
        """Test complex nested structure with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
            curseur="start",
            curseur_suivant="next",
        )

        unite_legale = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
            date_dernier_traitement_unite_legale="2020-01-02",
            nombre_periodes_unite_legale=1,
            unite_purgee_unite_legale=False,
            sigle_unite_legale="TC",
        )

        reponse = ReponseUniteLegale(
            header=header,
            unite_legale=unite_legale,
        )

        # Test serialization
        result = reponse.to_dict()

        # Verify all header fields
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 1
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

        # Verify all unite_legale fields
        assert result["uniteLegale"]["siren"] == "123456789"
        assert result["uniteLegale"]["statutDiffusionUniteLegale"] == "O"
        assert result["uniteLegale"]["dateCreationUniteLegale"] == "2020-01-01"
        assert result["uniteLegale"]["dateDernierTraitementUniteLegale"] == "2020-01-02"
        assert result["uniteLegale"]["nombrePeriodesUniteLegale"] == 1
        assert result["uniteLegale"]["unitePurgeeUniteLegale"] is False
        assert result["uniteLegale"]["sigleUniteLegale"] == "TC"

        # Test deserialization
        restored = ReponseUniteLegale.from_dict(result)

        assert isinstance(restored.header, Header)
        assert isinstance(restored.unite_legale, UniteLegale)
        assert restored.header.statut == 200
        assert restored.unite_legale.siren == "123456789"
