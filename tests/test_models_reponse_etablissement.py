"""Tests for sirene_api_client.models.reponse_etablissement module."""

from datetime import date, datetime

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.etablissement import Etablissement
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_etablissement import ReponseEtablissement


@pytest.mark.requirement("REQ-MODEL-006")
class TestReponseEtablissement:
    """Test ReponseEtablissement model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        header = Header(statut=200, message="OK", total=1)
        etablissement = Etablissement(siren="123456789", siret="12345678901234")

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
        )

        assert reponse.header == header
        assert reponse.etablissement == etablissement

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        reponse = ReponseEtablissement()

        assert reponse.header is UNSET
        assert reponse.etablissement is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        header = Header(statut=200, message="OK", total=1)
        etablissement = Etablissement(siren="123456789", siret="12345678901234")

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
        )

        result = reponse.to_dict()

        assert "header" in result
        assert "etablissement" in result
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["etablissement"]["siren"] == "123456789"
        assert result["etablissement"]["siret"] == "12345678901234"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        reponse = ReponseEtablissement()

        result = reponse.to_dict()

        assert "header" not in result
        assert "etablissement" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 1,
            },
            "etablissement": {
                "siren": "123456789",
                "siret": "12345678901234",
            },
        }

        reponse = ReponseEtablissement.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 1

        assert isinstance(reponse.etablissement, Etablissement)
        assert reponse.etablissement.siren == "123456789"
        assert reponse.etablissement.siret == "12345678901234"

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}  # Empty data

        reponse = ReponseEtablissement.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etablissement is UNSET

    def test_from_dict_with_unset_values(self):
        """Test from_dict with UNSET values."""
        data = {
            "header": UNSET,
            "etablissement": UNSET,
        }

        reponse = ReponseEtablissement.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etablissement is UNSET

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        header = Header(statut=200, message="OK", total=1)
        etablissement = Etablissement(siren="123456789", siret="12345678901234")

        original = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = ReponseEtablissement.from_dict(data)

        # Verify all fields are preserved
        assert isinstance(restored.header, Header)
        assert restored.header.statut == original.header.statut
        assert restored.header.message == original.header.message
        assert restored.header.total == original.header.total

        assert isinstance(restored.etablissement, Etablissement)
        assert restored.etablissement.siren == original.etablissement.siren
        assert restored.etablissement.siret == original.etablissement.siret

        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        reponse = ReponseEtablissement()
        reponse["custom_field"] = "custom_value"

        assert reponse["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        reponse = ReponseEtablissement()
        reponse["custom_field"] = "custom_value"

        assert reponse.additional_properties["custom_field"] == "custom_value"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        reponse = ReponseEtablissement()
        reponse["custom_field"] = "custom_value"

        del reponse["custom_field"]

        assert "custom_field" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        reponse = ReponseEtablissement()
        reponse["custom_field"] = "custom_value"

        assert "custom_field" in reponse
        assert "nonexistent_field" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseEtablissement()
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

        etablissement = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
        )

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
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

        # Verify etablissement serialization
        assert result["etablissement"]["siren"] == "123456789"
        assert result["etablissement"]["siret"] == "12345678901234"
        assert result["etablissement"]["statutDiffusionEtablissement"] == "O"
        assert result["etablissement"]["dateCreationEtablissement"] == "2020-01-01"

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
            "etablissement": {
                "siren": "123456789",
                "siret": "12345678901234",
                "statutDiffusionEtablissement": "O",
                "dateCreationEtablissement": "2020-01-01",
            },
        }

        reponse = ReponseEtablissement.from_dict(data)

        # Verify header deserialization
        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 1
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 20
        assert reponse.header.curseur == "abc123"
        assert reponse.header.curseur_suivant == "def456"

        # Verify etablissement deserialization
        assert isinstance(reponse.etablissement, Etablissement)
        assert reponse.etablissement.siren == "123456789"
        assert reponse.etablissement.siret == "12345678901234"
        assert reponse.etablissement.statut_diffusion_etablissement == "O"
        assert reponse.etablissement.date_creation_etablissement == date(2020, 1, 1)

    def test_partial_nested_models(self):
        """Test handling of partial nested models."""
        # Only header, no etablissement
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
            },
        }

        reponse = ReponseEtablissement.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.etablissement is UNSET

        # Only etablissement, no header
        data = {
            "etablissement": {
                "siren": "123456789",
                "siret": "12345678901234",
            },
        }

        reponse = ReponseEtablissement.from_dict(data)

        assert reponse.header is UNSET
        assert isinstance(reponse.etablissement, Etablissement)
        assert reponse.etablissement.siren == "123456789"
        assert reponse.etablissement.siret == "12345678901234"

    def test_error_response_handling(self):
        """Test handling of error responses."""
        header = Header(statut=404, message="Not Found", total=0)

        reponse = ReponseEtablissement(
            header=header,
            etablissement=UNSET,  # No etablissement in error case
        )

        result = reponse.to_dict()

        assert result["header"]["statut"] == 404
        assert result["header"]["message"] == "Not Found"
        assert result["header"]["total"] == 0
        assert "etablissement" not in result

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        header = Header(message="Établissement trouvé")
        etablissement = Etablissement(siren="123456789", siret="12345678901234")

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
        )
        reponse["unicode_field"] = "Café & Société 🏢"

        result = reponse.to_dict()
        assert result["header"]["message"] == "Établissement trouvé"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = ReponseEtablissement.from_dict(result)
        assert restored.header.message == "Établissement trouvé"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        header = Header(message="")  # Empty string
        etablissement = Etablissement(siren="123456789", siret="12345678901234")

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
        )

        result = reponse.to_dict()
        assert result["header"]["message"] == ""
        assert result["etablissement"]["siren"] == "123456789"

    def test_additional_properties_preservation(self):
        """Test that additional properties are preserved through serialization."""
        reponse = ReponseEtablissement()
        reponse["extra_field1"] = "value1"
        reponse["extra_field2"] = "value2"
        reponse["extra_field3"] = {"nested": "object"}

        data = reponse.to_dict()
        restored = ReponseEtablissement.from_dict(data)

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

        etablissement = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
            date_dernier_traitement_etablissement=datetime(2020, 1, 2, 10, 30, 0),
            etablissement_siege=True,
            nombre_periodes_etablissement=1,
        )

        reponse = ReponseEtablissement(
            header=header,
            etablissement=etablissement,
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

        # Verify all etablissement fields
        assert result["etablissement"]["siren"] == "123456789"
        assert result["etablissement"]["siret"] == "12345678901234"
        assert result["etablissement"]["statutDiffusionEtablissement"] == "O"
        assert result["etablissement"]["dateCreationEtablissement"] == "2020-01-01"
        assert (
            result["etablissement"]["dateDernierTraitementEtablissement"]
            == "2020-01-02T10:30:00"
        )
        assert result["etablissement"]["etablissementSiege"] is True
        assert result["etablissement"]["nombrePeriodesEtablissement"] == 1

        # Test deserialization
        restored = ReponseEtablissement.from_dict(result)

        assert isinstance(restored.header, Header)
        assert isinstance(restored.etablissement, Etablissement)
        assert restored.header.statut == 200
        assert restored.etablissement.siren == "123456789"
