"""Tests for sirene_api_client.models.reponse_lien_succession module."""

from datetime import date, datetime

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.header import Header
from sirene_api_client.models.lien_succession import LienSuccession
from sirene_api_client.models.reponse_lien_succession import ReponseLienSuccession


class TestReponseLienSuccession:
    """Test ReponseLienSuccession model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        header = Header(
            statut=200,
            message="OK",
            total=2,
            debut=0,
            nombre=2,
            curseur="start",
            curseur_suivant="next",
        )

        lien1 = LienSuccession(
            siret_etablissement_predecesseur="12345678901234",
            siret_etablissement_successeur="98765432109876",
            date_lien_succession=date(2023, 1, 15),
            transfert_siege=True,
            continuite_economique=True,
            date_dernier_traitement_lien_succession=datetime(2023, 1, 15, 10, 30, 0),
        )

        lien2 = LienSuccession(
            siret_etablissement_predecesseur="11111111111111",
            siret_etablissement_successeur="22222222222222",
            date_lien_succession=date(2023, 2, 20),
            transfert_siege=False,
            continuite_economique=False,
            date_dernier_traitement_lien_succession=datetime(2023, 2, 20, 14, 45, 0),
        )

        reponse = ReponseLienSuccession(header=header, liens_succession=[lien1, lien2])

        assert reponse.header == header
        assert len(reponse.liens_succession) == 2
        assert reponse.liens_succession[0] == lien1
        assert reponse.liens_succession[1] == lien2

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        reponse = ReponseLienSuccession()

        assert reponse.header is UNSET
        assert reponse.liens_succession is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
            curseur="start",
            curseur_suivant="next",
        )

        lien = LienSuccession(
            siret_etablissement_predecesseur="12345678901234",
            siret_etablissement_successeur="98765432109876",
            date_lien_succession=date(2023, 1, 15),
            transfert_siege=True,
            continuite_economique=True,
            date_dernier_traitement_lien_succession=datetime(2023, 1, 15, 10, 30, 0),
        )

        reponse = ReponseLienSuccession(header=header, liens_succession=[lien])

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 1
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

        # Verify liens_succession serialization
        assert len(result["liensSuccession"]) == 1
        lien_data = result["liensSuccession"][0]
        assert lien_data["siretEtablissementPredecesseur"] == "12345678901234"
        assert lien_data["siretEtablissementSuccesseur"] == "98765432109876"
        assert lien_data["dateLienSuccession"] == "2023-01-15"
        assert lien_data["transfertSiege"] is True
        assert lien_data["continuiteEconomique"] is True
        assert lien_data["dateDernierTraitementLienSuccession"] == "2023-01-15T10:30:00"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        reponse = ReponseLienSuccession()

        result = reponse.to_dict()

        assert "header" not in result
        assert "liensSuccession" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 2,
                "debut": 0,
                "nombre": 2,
                "curseur": "start",
                "curseurSuivant": "next",
            },
            "liensSuccession": [
                {
                    "siretEtablissementPredecesseur": "12345678901234",
                    "siretEtablissementSuccesseur": "98765432109876",
                    "dateLienSuccession": "2023-01-15",
                    "transfertSiege": True,
                    "continuiteEconomique": True,
                    "dateDernierTraitementLienSuccession": "2023-01-15T10:30:00",
                },
                {
                    "siretEtablissementPredecesseur": "11111111111111",
                    "siretEtablissementSuccesseur": "22222222222222",
                    "dateLienSuccession": "2023-02-20",
                    "transfertSiege": False,
                    "continuiteEconomique": False,
                    "dateDernierTraitementLienSuccession": "2023-02-20T14:45:00",
                },
            ],
        }

        reponse = ReponseLienSuccession.from_dict(data)

        # Verify header deserialization
        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 2
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 2
        assert reponse.header.curseur == "start"
        assert reponse.header.curseur_suivant == "next"

        # Verify liens_succession deserialization
        assert len(reponse.liens_succession) == 2

        lien1 = reponse.liens_succession[0]
        assert isinstance(lien1, LienSuccession)
        assert lien1.siret_etablissement_predecesseur == "12345678901234"
        assert lien1.siret_etablissement_successeur == "98765432109876"
        assert lien1.date_lien_succession == date(2023, 1, 15)
        assert lien1.transfert_siege is True
        assert lien1.continuite_economique is True
        assert lien1.date_dernier_traitement_lien_succession == datetime(
            2023, 1, 15, 10, 30, 0
        )

        lien2 = reponse.liens_succession[1]
        assert isinstance(lien2, LienSuccession)
        assert lien2.siret_etablissement_predecesseur == "11111111111111"
        assert lien2.siret_etablissement_successeur == "22222222222222"
        assert lien2.date_lien_succession == date(2023, 2, 20)
        assert lien2.transfert_siege is False
        assert lien2.continuite_economique is False
        assert lien2.date_dernier_traitement_lien_succession == datetime(
            2023, 2, 20, 14, 45, 0
        )

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 0,
                "debut": 0,
                "nombre": 0,
                "curseur": "start",
                "curseurSuivant": "next",
            },
            "liensSuccession": [],
        }

        reponse = ReponseLienSuccession.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert len(reponse.liens_succession) == 0

    def test_from_dict_with_empty_lists(self):
        """Test from_dict with empty lists."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 0,
                "debut": 0,
                "nombre": 0,
                "curseur": "start",
                "curseurSuivant": "next",
            },
            "liensSuccession": [],
        }

        reponse = ReponseLienSuccession.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.liens_succession == []

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
            curseur="start",
            curseur_suivant="next",
        )

        lien = LienSuccession(
            siret_etablissement_predecesseur="12345678901234",
            siret_etablissement_successeur="98765432109876",
            date_lien_succession=date(2023, 1, 15),
            transfert_siege=True,
            continuite_economique=True,
            date_dernier_traitement_lien_succession=datetime(2023, 1, 15, 10, 30, 0),
        )

        original = ReponseLienSuccession(header=header, liens_succession=[lien])

        data = original.to_dict()
        restored = ReponseLienSuccession.from_dict(data)

        # Verify header roundtrip
        assert restored.header.statut == original.header.statut
        assert restored.header.message == original.header.message
        assert restored.header.total == original.header.total
        assert restored.header.debut == original.header.debut
        assert restored.header.nombre == original.header.nombre
        assert restored.header.curseur == original.header.curseur
        assert restored.header.curseur_suivant == original.header.curseur_suivant

        # Verify liens_succession roundtrip
        assert len(restored.liens_succession) == len(original.liens_succession)

        original_lien = original.liens_succession[0]
        restored_lien = restored.liens_succession[0]

        assert (
            restored_lien.siret_etablissement_predecesseur
            == original_lien.siret_etablissement_predecesseur
        )
        assert (
            restored_lien.siret_etablissement_successeur
            == original_lien.siret_etablissement_successeur
        )
        assert restored_lien.date_lien_succession == original_lien.date_lien_succession
        assert restored_lien.transfert_siege == original_lien.transfert_siege
        assert (
            restored_lien.continuite_economique == original_lien.continuite_economique
        )
        assert (
            restored_lien.date_dernier_traitement_lien_succession
            == original_lien.date_dernier_traitement_lien_succession
        )

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        reponse = ReponseLienSuccession()
        reponse.additional_properties["extraField"] = "extraValue"

        assert reponse["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        reponse = ReponseLienSuccession()
        reponse["extraField"] = "extraValue"

        assert reponse.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        reponse = ReponseLienSuccession()
        reponse.additional_properties["extraField"] = "extraValue"

        del reponse["extraField"]

        assert "extraField" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        reponse = ReponseLienSuccession()
        reponse.additional_properties["extraField"] = "extraValue"

        assert "extraField" in reponse
        assert "nonexistentField" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseLienSuccession()
        reponse.additional_properties["field1"] = "value1"
        reponse.additional_properties["field2"] = "value2"

        keys = reponse.additional_keys
        assert len(keys) == 2
        assert "field1" in keys
        assert "field2" in keys

    def test_complex_nested_structure(self):
        """Test complex nested structure with multiple liens."""
        header = Header(
            statut=200,
            message="OK",
            total=3,
            debut=0,
            nombre=3,
            curseur="start",
            curseur_suivant="next",
        )

        lien1 = LienSuccession(
            siret_etablissement_predecesseur="12345678901234",
            siret_etablissement_successeur="98765432109876",
            date_lien_succession=date(2023, 1, 15),
            transfert_siege=True,
            continuite_economique=True,
            date_dernier_traitement_lien_succession=datetime(2023, 1, 15, 10, 30, 0),
        )

        lien2 = LienSuccession(
            siret_etablissement_predecesseur="11111111111111",
            siret_etablissement_successeur="22222222222222",
            date_lien_succession=date(2023, 2, 20),
            transfert_siege=False,
            continuite_economique=False,
            date_dernier_traitement_lien_succession=datetime(2023, 2, 20, 14, 45, 0),
        )

        lien3 = LienSuccession(
            siret_etablissement_predecesseur="33333333333333",
            siret_etablissement_successeur="44444444444444",
            date_lien_succession=date(2023, 3, 25),
            transfert_siege=True,
            continuite_economique=False,
            date_dernier_traitement_lien_succession=datetime(2023, 3, 25, 16, 20, 0),
        )

        reponse = ReponseLienSuccession(
            header=header, liens_succession=[lien1, lien2, lien3]
        )

        # Add additional properties to the top-level response
        reponse.additional_properties["extraField"] = "extraValue"
        reponse.additional_properties["metadata"] = {"version": "1.0.0"}

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 3
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 3
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

        # Verify all liens_succession
        assert len(result["liensSuccession"]) == 3

        # First lien
        assert (
            result["liensSuccession"][0]["siretEtablissementPredecesseur"]
            == "12345678901234"
        )
        assert (
            result["liensSuccession"][0]["siretEtablissementSuccesseur"]
            == "98765432109876"
        )
        assert result["liensSuccession"][0]["dateLienSuccession"] == "2023-01-15"
        assert result["liensSuccession"][0]["transfertSiege"] is True
        assert result["liensSuccession"][0]["continuiteEconomique"] is True
        assert (
            result["liensSuccession"][0]["dateDernierTraitementLienSuccession"]
            == "2023-01-15T10:30:00"
        )

        # Second lien
        assert (
            result["liensSuccession"][1]["siretEtablissementPredecesseur"]
            == "11111111111111"
        )
        assert (
            result["liensSuccession"][1]["siretEtablissementSuccesseur"]
            == "22222222222222"
        )
        assert result["liensSuccession"][1]["dateLienSuccession"] == "2023-02-20"
        assert result["liensSuccession"][1]["transfertSiege"] is False
        assert result["liensSuccession"][1]["continuiteEconomique"] is False
        assert (
            result["liensSuccession"][1]["dateDernierTraitementLienSuccession"]
            == "2023-02-20T14:45:00"
        )

        # Third lien
        assert (
            result["liensSuccession"][2]["siretEtablissementPredecesseur"]
            == "33333333333333"
        )
        assert (
            result["liensSuccession"][2]["siretEtablissementSuccesseur"]
            == "44444444444444"
        )
        assert result["liensSuccession"][2]["dateLienSuccession"] == "2023-03-25"
        assert result["liensSuccession"][2]["transfertSiege"] is True
        assert result["liensSuccession"][2]["continuiteEconomique"] is False
        assert (
            result["liensSuccession"][2]["dateDernierTraitementLienSuccession"]
            == "2023-03-25T16:20:00"
        )

        # Verify additional properties
        assert result["extraField"] == "extraValue"
        assert result["metadata"] == {"version": "1.0.0"}

        # Test deserialization
        restored = ReponseLienSuccession.from_dict(result)

        # Verify header deserialization
        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 3
        assert restored.header.debut == 0
        assert restored.header.nombre == 3
        assert restored.header.curseur == "start"
        assert restored.header.curseur_suivant == "next"

        # Verify liens_succession deserialization
        assert len(restored.liens_succession) == 3

        # First lien
        assert isinstance(restored.liens_succession[0], LienSuccession)
        assert (
            restored.liens_succession[0].siret_etablissement_predecesseur
            == "12345678901234"
        )
        assert (
            restored.liens_succession[0].siret_etablissement_successeur
            == "98765432109876"
        )
        assert restored.liens_succession[0].date_lien_succession == date(2023, 1, 15)
        assert restored.liens_succession[0].transfert_siege is True
        assert restored.liens_succession[0].continuite_economique is True
        assert restored.liens_succession[
            0
        ].date_dernier_traitement_lien_succession == datetime(2023, 1, 15, 10, 30, 0)

        # Second lien
        assert isinstance(restored.liens_succession[1], LienSuccession)
        assert (
            restored.liens_succession[1].siret_etablissement_predecesseur
            == "11111111111111"
        )
        assert (
            restored.liens_succession[1].siret_etablissement_successeur
            == "22222222222222"
        )
        assert restored.liens_succession[1].date_lien_succession == date(2023, 2, 20)
        assert restored.liens_succession[1].transfert_siege is False
        assert restored.liens_succession[1].continuite_economique is False
        assert restored.liens_succession[
            1
        ].date_dernier_traitement_lien_succession == datetime(2023, 2, 20, 14, 45, 0)

        # Third lien
        assert isinstance(restored.liens_succession[2], LienSuccession)
        assert (
            restored.liens_succession[2].siret_etablissement_predecesseur
            == "33333333333333"
        )
        assert (
            restored.liens_succession[2].siret_etablissement_successeur
            == "44444444444444"
        )
        assert restored.liens_succession[2].date_lien_succession == date(2023, 3, 25)
        assert restored.liens_succession[2].transfert_siege is True
        assert restored.liens_succession[2].continuite_economique is False
        assert restored.liens_succession[
            2
        ].date_dernier_traitement_lien_succession == datetime(2023, 3, 25, 16, 20, 0)

        # Verify additional properties
        assert restored.additional_properties["extraField"] == "extraValue"
        assert restored.additional_properties["metadata"] == {"version": "1.0.0"}
