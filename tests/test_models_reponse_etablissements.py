from datetime import date, datetime

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.etablissement import Etablissement
from sirene_api_client.models.facette import Facette
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_etablissements import ReponseEtablissements


class TestReponseEtablissements:
    """Test ReponseEtablissements model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=2,
            debut=0,
            nombre=2,
        )

        etablissement1 = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
            etablissement_siege=True,
        )

        etablissement2 = Etablissement(
            siren="987654321",
            siret="98765432109876",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2021, 2, 1),
            etablissement_siege=False,
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        reponse = ReponseEtablissements(
            header=header,
            etablissements=[etablissement1, etablissement2],
            facettes=[facette],
        )

        assert reponse.header == header
        assert reponse.etablissements == [etablissement1, etablissement2]
        assert reponse.facettes == [facette]
        assert reponse.additional_properties == {}

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal fields."""
        reponse = ReponseEtablissements()

        assert reponse.header is UNSET
        assert reponse.etablissements is UNSET
        assert reponse.facettes is UNSET
        assert reponse.additional_properties == {}

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=2,
            debut=0,
            nombre=2,
        )

        etablissement1 = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
            etablissement_siege=True,
        )

        etablissement2 = Etablissement(
            siren="987654321",
            siret="98765432109876",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2021, 2, 1),
            etablissement_siege=False,
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        reponse = ReponseEtablissements(
            header=header,
            etablissements=[etablissement1, etablissement2],
            facettes=[facette],
        )

        result = reponse.to_dict()

        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 2
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 2

        assert len(result["etablissements"]) == 2
        assert result["etablissements"][0]["siren"] == "123456789"
        assert result["etablissements"][0]["siret"] == "12345678901234"
        assert result["etablissements"][0]["statutDiffusionEtablissement"] == "O"
        assert result["etablissements"][0]["dateCreationEtablissement"] == "2020-01-01"
        assert result["etablissements"][0]["etablissementSiege"] is True

        assert result["etablissements"][1]["siren"] == "987654321"
        assert result["etablissements"][1]["siret"] == "98765432109876"
        assert result["etablissements"][1]["statutDiffusionEtablissement"] == "O"
        assert result["etablissements"][1]["dateCreationEtablissement"] == "2021-02-01"
        assert result["etablissements"][1]["etablissementSiege"] is False

        assert len(result["facettes"]) == 1
        assert result["facettes"][0]["nom"] == "test_facette"
        assert result["facettes"][0]["total"] == 10
        assert result["facettes"][0]["modalites"] == 5

    def test_to_dict_with_unset_fields(self):
        """Test to_dict with unset fields."""
        reponse = ReponseEtablissements()

        result = reponse.to_dict()

        assert "header" not in result
        assert "etablissements" not in result
        assert "facettes" not in result
        assert result == {}

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 2,
                "debut": 0,
                "nombre": 2,
            },
            "etablissements": [
                {
                    "siren": "123456789",
                    "siret": "12345678901234",
                    "statutDiffusionEtablissement": "O",
                    "dateCreationEtablissement": "2020-01-01",
                    "etablissementSiege": True,
                },
                {
                    "siren": "987654321",
                    "siret": "98765432109876",
                    "statutDiffusionEtablissement": "O",
                    "dateCreationEtablissement": "2021-02-01",
                    "etablissementSiege": False,
                },
            ],
            "facettes": [
                {
                    "nom": "test_facette",
                    "total": 10,
                    "modalites": 5,
                },
            ],
        }

        reponse = ReponseEtablissements.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 2
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 2

        assert len(reponse.etablissements) == 2
        assert isinstance(reponse.etablissements[0], Etablissement)
        assert reponse.etablissements[0].siren == "123456789"
        assert reponse.etablissements[0].siret == "12345678901234"
        assert reponse.etablissements[0].statut_diffusion_etablissement == "O"
        assert reponse.etablissements[0].date_creation_etablissement == date(2020, 1, 1)
        assert reponse.etablissements[0].etablissement_siege is True

        assert isinstance(reponse.etablissements[1], Etablissement)
        assert reponse.etablissements[1].siren == "987654321"
        assert reponse.etablissements[1].siret == "98765432109876"
        assert reponse.etablissements[1].statut_diffusion_etablissement == "O"
        assert reponse.etablissements[1].date_creation_etablissement == date(2021, 2, 1)
        assert reponse.etablissements[1].etablissement_siege is False

        assert len(reponse.facettes) == 1
        assert isinstance(reponse.facettes[0], Facette)
        assert reponse.facettes[0].nom == "test_facette"
        assert reponse.facettes[0].total == 10
        assert reponse.facettes[0].modalites == 5

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}

        reponse = ReponseEtablissements.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etablissements == []
        assert reponse.facettes == []
        assert reponse.additional_properties == {}

    def test_from_dict_with_empty_lists(self):
        """Test from_dict with empty lists."""
        data = {
            "etablissements": [],
            "facettes": [],
        }

        reponse = ReponseEtablissements.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etablissements == []
        assert reponse.facettes == []
        assert reponse.additional_properties == {}

    def test_roundtrip_serialization(self):
        """Test round-trip serialization."""
        header = Header(
            statut=200,
            message="OK",
            total=2,
            debut=0,
            nombre=2,
        )

        etablissement1 = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
            etablissement_siege=True,
        )

        etablissement2 = Etablissement(
            siren="987654321",
            siret="98765432109876",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2021, 2, 1),
            etablissement_siege=False,
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        original = ReponseEtablissements(
            header=header,
            etablissements=[etablissement1, etablissement2],
            facettes=[facette],
        )

        # Serialize to dict
        data = original.to_dict()

        # Deserialize back to object
        restored = ReponseEtablissements.from_dict(data)

        # Verify all fields are preserved
        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 2
        assert restored.header.debut == 0
        assert restored.header.nombre == 2

        assert len(restored.etablissements) == 2
        assert isinstance(restored.etablissements[0], Etablissement)
        assert restored.etablissements[0].siren == "123456789"
        assert restored.etablissements[0].siret == "12345678901234"
        assert restored.etablissements[0].statut_diffusion_etablissement == "O"
        assert restored.etablissements[0].date_creation_etablissement == date(
            2020, 1, 1
        )
        assert restored.etablissements[0].etablissement_siege is True

        assert isinstance(restored.etablissements[1], Etablissement)
        assert restored.etablissements[1].siren == "987654321"
        assert restored.etablissements[1].siret == "98765432109876"
        assert restored.etablissements[1].statut_diffusion_etablissement == "O"
        assert restored.etablissements[1].date_creation_etablissement == date(
            2021, 2, 1
        )
        assert restored.etablissements[1].etablissement_siege is False

        assert len(restored.facettes) == 1
        assert isinstance(restored.facettes[0], Facette)
        assert restored.facettes[0].nom == "test_facette"
        assert restored.facettes[0].total == 10
        assert restored.facettes[0].modalites == 5

    def test_additional_properties_getitem(self):
        """Test additional properties __getitem__."""
        reponse = ReponseEtablissements()
        reponse.additional_properties["extraField"] = "extraValue"

        assert reponse["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test additional properties __setitem__."""
        reponse = ReponseEtablissements()
        reponse["extraField"] = "extraValue"

        assert reponse.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test additional properties __delitem__."""
        reponse = ReponseEtablissements()
        reponse.additional_properties["extraField"] = "extraValue"

        del reponse["extraField"]

        assert "extraField" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test additional properties __contains__."""
        reponse = ReponseEtablissements()
        reponse.additional_properties["extraField"] = "extraValue"

        assert "extraField" in reponse
        assert "nonexistentField" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseEtablissements()
        reponse.additional_properties["field1"] = "value1"
        reponse.additional_properties["field2"] = "value2"

        keys = reponse.additional_keys

        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_complex_nested_structure(self):
        """Test complex nested structure with full data and additional properties."""
        header = Header(
            statut=200,
            message="OK",
            total=3,
            debut=0,
            nombre=3,
            curseur="start",
            curseur_suivant="next",
        )

        etablissement1 = Etablissement(
            siren="123456789",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2020, 1, 1),
            date_dernier_traitement_etablissement=datetime(2020, 1, 2, 10, 30, 0),
            etablissement_siege=True,
            nombre_periodes_etablissement=1,
        )

        etablissement2 = Etablissement(
            siren="987654321",
            siret="98765432109876",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=date(2021, 2, 1),
            etablissement_siege=False,
            nombre_periodes_etablissement=2,
        )

        etablissement3 = Etablissement(
            siren="555666777",
            siret="55566677788888",
            statut_diffusion_etablissement="N",
            date_creation_etablissement=date(2022, 3, 1),
            etablissement_siege=False,
            nombre_periodes_etablissement=1,
        )

        facette1 = Facette(
            nom="statut_diffusion",
            total=2,
            modalites=2,
        )

        facette2 = Facette(
            nom="date_creation",
            total=3,
            modalites=3,
        )

        reponse = ReponseEtablissements(
            header=header,
            etablissements=[etablissement1, etablissement2, etablissement3],
            facettes=[facette1, facette2],
        )

        # Add additional properties to the top-level response
        reponse.additional_properties["extraField"] = "extraValue"
        reponse.additional_properties["metadata"] = {"version": "1.0"}

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 3
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 3
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

        # Verify all etablissements
        assert len(result["etablissements"]) == 3

        # First establishment
        assert result["etablissements"][0]["siren"] == "123456789"
        assert result["etablissements"][0]["siret"] == "12345678901234"
        assert result["etablissements"][0]["statutDiffusionEtablissement"] == "O"
        assert result["etablissements"][0]["dateCreationEtablissement"] == "2020-01-01"
        assert (
            result["etablissements"][0]["dateDernierTraitementEtablissement"]
            == "2020-01-02T10:30:00"
        )
        assert result["etablissements"][0]["etablissementSiege"] is True
        assert result["etablissements"][0]["nombrePeriodesEtablissement"] == 1

        # Second establishment
        assert result["etablissements"][1]["siren"] == "987654321"
        assert result["etablissements"][1]["siret"] == "98765432109876"
        assert result["etablissements"][1]["statutDiffusionEtablissement"] == "O"
        assert result["etablissements"][1]["dateCreationEtablissement"] == "2021-02-01"
        assert result["etablissements"][1]["etablissementSiege"] is False
        assert result["etablissements"][1]["nombrePeriodesEtablissement"] == 2

        # Third establishment
        assert result["etablissements"][2]["siren"] == "555666777"
        assert result["etablissements"][2]["siret"] == "55566677788888"
        assert result["etablissements"][2]["statutDiffusionEtablissement"] == "N"
        assert result["etablissements"][2]["dateCreationEtablissement"] == "2022-03-01"
        assert result["etablissements"][2]["etablissementSiege"] is False
        assert result["etablissements"][2]["nombrePeriodesEtablissement"] == 1

        # Verify all facettes
        assert len(result["facettes"]) == 2
        assert result["facettes"][0]["nom"] == "statut_diffusion"
        assert result["facettes"][0]["total"] == 2
        assert result["facettes"][0]["modalites"] == 2

        assert result["facettes"][1]["nom"] == "date_creation"
        assert result["facettes"][1]["total"] == 3
        assert result["facettes"][1]["modalites"] == 3

        # Verify additional properties
        assert result["extraField"] == "extraValue"
        assert result["metadata"] == {"version": "1.0"}

        # Test deserialization
        restored = ReponseEtablissements.from_dict(result)

        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 3
        assert restored.header.debut == 0
        assert restored.header.nombre == 3
        assert restored.header.curseur == "start"
        assert restored.header.curseur_suivant == "next"

        assert len(restored.etablissements) == 3
        assert isinstance(restored.etablissements[0], Etablissement)
        assert restored.etablissements[0].siren == "123456789"
        assert restored.etablissements[0].siret == "12345678901234"
        assert restored.etablissements[0].statut_diffusion_etablissement == "O"
        assert restored.etablissements[0].date_creation_etablissement == date(
            2020, 1, 1
        )
        assert restored.etablissements[
            0
        ].date_dernier_traitement_etablissement == datetime(2020, 1, 2, 10, 30, 0)
        assert restored.etablissements[0].etablissement_siege is True
        assert restored.etablissements[0].nombre_periodes_etablissement == 1

        assert isinstance(restored.etablissements[1], Etablissement)
        assert restored.etablissements[1].siren == "987654321"
        assert restored.etablissements[1].siret == "98765432109876"
        assert restored.etablissements[1].statut_diffusion_etablissement == "O"
        assert restored.etablissements[1].date_creation_etablissement == date(
            2021, 2, 1
        )
        assert restored.etablissements[1].etablissement_siege is False
        assert restored.etablissements[1].nombre_periodes_etablissement == 2

        assert isinstance(restored.etablissements[2], Etablissement)
        assert restored.etablissements[2].siren == "555666777"
        assert restored.etablissements[2].siret == "55566677788888"
        assert restored.etablissements[2].statut_diffusion_etablissement == "N"
        assert restored.etablissements[2].date_creation_etablissement == date(
            2022, 3, 1
        )
        assert restored.etablissements[2].etablissement_siege is False
        assert restored.etablissements[2].nombre_periodes_etablissement == 1

        assert len(restored.facettes) == 2
        assert isinstance(restored.facettes[0], Facette)
        assert restored.facettes[0].nom == "statut_diffusion"
        assert restored.facettes[0].total == 2
        assert restored.facettes[0].modalites == 2

        assert isinstance(restored.facettes[1], Facette)
        assert restored.facettes[1].nom == "date_creation"
        assert restored.facettes[1].total == 3
        assert restored.facettes[1].modalites == 3

        assert restored.additional_properties["extraField"] == "extraValue"
        assert restored.additional_properties["metadata"] == {"version": "1.0"}
