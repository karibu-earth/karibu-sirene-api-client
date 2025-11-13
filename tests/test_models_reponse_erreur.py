"""Tests for sirene_api_client.models.reponse_erreur module."""

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_erreur import ReponseErreur


class TestReponseErreur:
    """Test ReponseErreur model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        header = Header(
            statut=400,
            message="Bad Request",
            total=0,
            debut=0,
            nombre=0,
            curseur="start",
            curseur_suivant="next",
        )

        reponse = ReponseErreur(header=header)

        assert reponse.header == header

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        reponse = ReponseErreur()

        assert reponse.header is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        header = Header(
            statut=404,
            message="Not Found",
            total=0,
            debut=0,
            nombre=0,
            curseur="start",
            curseur_suivant="next",
        )

        reponse = ReponseErreur(header=header)

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 404
        assert result["header"]["message"] == "Not Found"
        assert result["header"]["total"] == 0
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 0
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        reponse = ReponseErreur()

        result = reponse.to_dict()

        assert "header" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 500,
                "message": "Internal Server Error",
                "total": 0,
                "debut": 0,
                "nombre": 0,
                "curseur": "start",
                "curseurSuivant": "next",
            }
        }

        reponse = ReponseErreur.from_dict(data)

        # Verify header deserialization
        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 500
        assert reponse.header.message == "Internal Server Error"
        assert reponse.header.total == 0
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 0
        assert reponse.header.curseur == "start"
        assert reponse.header.curseur_suivant == "next"

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}

        reponse = ReponseErreur.from_dict(data)

        assert reponse.header is UNSET

    def test_from_dict_with_empty_header(self):
        """Test from_dict with empty header data."""
        data = {
            "header": {
                "statut": 0,
                "message": "",
                "total": 0,
                "debut": 0,
                "nombre": 0,
                "curseur": "",
                "curseurSuivant": "",
            }
        }

        reponse = ReponseErreur.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 0
        assert reponse.header.message == ""
        assert reponse.header.total == 0
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 0
        assert reponse.header.curseur == ""
        assert reponse.header.curseur_suivant == ""

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        header = Header(
            statut=403,
            message="Forbidden",
            total=0,
            debut=0,
            nombre=0,
            curseur="start",
            curseur_suivant="next",
        )

        original = ReponseErreur(header=header)

        data = original.to_dict()
        restored = ReponseErreur.from_dict(data)

        # Verify header roundtrip
        assert restored.header.statut == original.header.statut
        assert restored.header.message == original.header.message
        assert restored.header.total == original.header.total
        assert restored.header.debut == original.header.debut
        assert restored.header.nombre == original.header.nombre
        assert restored.header.curseur == original.header.curseur
        assert restored.header.curseur_suivant == original.header.curseur_suivant

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        reponse = ReponseErreur()
        reponse.additional_properties["errorCode"] = "VALIDATION_ERROR"

        assert reponse["errorCode"] == "VALIDATION_ERROR"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        reponse = ReponseErreur()
        reponse["errorCode"] = "VALIDATION_ERROR"

        assert reponse.additional_properties["errorCode"] == "VALIDATION_ERROR"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        reponse = ReponseErreur()
        reponse.additional_properties["errorCode"] = "VALIDATION_ERROR"

        del reponse["errorCode"]

        assert "errorCode" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        reponse = ReponseErreur()
        reponse.additional_properties["errorCode"] = "VALIDATION_ERROR"

        assert "errorCode" in reponse
        assert "nonexistentField" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseErreur()
        reponse.additional_properties["errorCode"] = "VALIDATION_ERROR"
        reponse.additional_properties["errorDetails"] = "Invalid input"

        keys = reponse.additional_keys
        assert len(keys) == 2
        assert "errorCode" in keys
        assert "errorDetails" in keys

    def test_error_response_with_additional_properties(self):
        """Test error response with additional error properties."""
        header = Header(
            statut=422,
            message="Unprocessable Entity",
            total=0,
            debut=0,
            nombre=0,
            curseur="start",
            curseur_suivant="next",
        )

        reponse = ReponseErreur(header=header)

        # Add error-specific additional properties
        reponse.additional_properties["errorCode"] = "VALIDATION_ERROR"
        reponse.additional_properties["errorDetails"] = {
            "field": "siret",
            "message": "Invalid SIRET format",
        }
        reponse.additional_properties["timestamp"] = "2023-01-15T10:30:00Z"

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 422
        assert result["header"]["message"] == "Unprocessable Entity"

        # Verify additional properties serialization
        assert result["errorCode"] == "VALIDATION_ERROR"
        assert result["errorDetails"]["field"] == "siret"
        assert result["errorDetails"]["message"] == "Invalid SIRET format"
        assert result["timestamp"] == "2023-01-15T10:30:00Z"

        # Test deserialization
        restored = ReponseErreur.from_dict(result)

        # Verify header deserialization
        assert isinstance(restored.header, Header)
        assert restored.header.statut == 422
        assert restored.header.message == "Unprocessable Entity"

        # Verify additional properties deserialization
        assert restored.additional_properties["errorCode"] == "VALIDATION_ERROR"
        assert restored.additional_properties["errorDetails"]["field"] == "siret"
        assert (
            restored.additional_properties["errorDetails"]["message"]
            == "Invalid SIRET format"
        )
        assert restored.additional_properties["timestamp"] == "2023-01-15T10:30:00Z"

    def test_multiple_error_codes(self):
        """Test handling multiple error codes in additional properties."""
        header = Header(
            statut=400,
            message="Bad Request",
            total=0,
            debut=0,
            nombre=0,
            curseur="start",
            curseur_suivant="next",
        )

        reponse = ReponseErreur(header=header)

        # Add multiple error-related properties
        reponse.additional_properties["errors"] = [
            {"field": "siret", "message": "Invalid SIRET format"},
            {"field": "siren", "message": "Invalid SIREN format"},
        ]
        reponse.additional_properties["requestId"] = "req-12345"
        reponse.additional_properties["correlationId"] = "corr-67890"

        result = reponse.to_dict()

        # Verify serialization
        assert len(result["errors"]) == 2
        assert result["errors"][0]["field"] == "siret"
        assert result["errors"][0]["message"] == "Invalid SIRET format"
        assert result["errors"][1]["field"] == "siren"
        assert result["errors"][1]["message"] == "Invalid SIREN format"
        assert result["requestId"] == "req-12345"
        assert result["correlationId"] == "corr-67890"

        # Test deserialization
        restored = ReponseErreur.from_dict(result)

        assert len(restored.additional_properties["errors"]) == 2
        assert restored.additional_properties["errors"][0]["field"] == "siret"
        assert (
            restored.additional_properties["errors"][0]["message"]
            == "Invalid SIRET format"
        )
        assert restored.additional_properties["errors"][1]["field"] == "siren"
        assert (
            restored.additional_properties["errors"][1]["message"]
            == "Invalid SIREN format"
        )
        assert restored.additional_properties["requestId"] == "req-12345"
        assert restored.additional_properties["correlationId"] == "corr-67890"
