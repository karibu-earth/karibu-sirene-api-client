from datetime import date

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.facette import Facette
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_unites_legales import ReponseUnitesLegales
from sirene_api_client.models.unite_legale import UniteLegale


class TestReponseUnitesLegales:
    """Test ReponseUnitesLegales model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=2,
            debut=0,
            nombre=2,
        )

        unite_legale1 = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="TC",
        )

        unite_legale2 = UniteLegale(
            siren="987654321",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2021, 2, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="SNCF",
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        reponse = ReponseUnitesLegales(
            header=header,
            unites_legales=[unite_legale1, unite_legale2],
            facettes=[facette],
        )

        assert reponse.header == header
        assert reponse.unites_legales == [unite_legale1, unite_legale2]
        assert reponse.facettes == [facette]
        assert reponse.additional_properties == {}

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal fields."""
        reponse = ReponseUnitesLegales()

        assert reponse.header is UNSET
        assert reponse.unites_legales is UNSET
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

        unite_legale1 = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="TC",
        )

        unite_legale2 = UniteLegale(
            siren="987654321",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2021, 2, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="SNCF",
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        reponse = ReponseUnitesLegales(
            header=header,
            unites_legales=[unite_legale1, unite_legale2],
            facettes=[facette],
        )

        result = reponse.to_dict()

        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 2
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 2

        assert len(result["unitesLegales"]) == 2
        assert result["unitesLegales"][0]["siren"] == "123456789"
        assert result["unitesLegales"][0]["statutDiffusionUniteLegale"] == "O"
        assert result["unitesLegales"][0]["dateCreationUniteLegale"] == "2020-01-01"
        assert result["unitesLegales"][0]["unitePurgeeUniteLegale"] is False
        assert result["unitesLegales"][0]["sigleUniteLegale"] == "TC"

        assert result["unitesLegales"][1]["siren"] == "987654321"
        assert result["unitesLegales"][1]["statutDiffusionUniteLegale"] == "O"
        assert result["unitesLegales"][1]["dateCreationUniteLegale"] == "2021-02-01"
        assert result["unitesLegales"][1]["unitePurgeeUniteLegale"] is False
        assert result["unitesLegales"][1]["sigleUniteLegale"] == "SNCF"

        assert len(result["facettes"]) == 1
        assert result["facettes"][0]["nom"] == "test_facette"
        assert result["facettes"][0]["total"] == 10
        assert result["facettes"][0]["modalites"] == 5

    def test_to_dict_with_unset_fields(self):
        """Test to_dict with unset fields."""
        reponse = ReponseUnitesLegales()

        result = reponse.to_dict()

        assert "header" not in result
        assert "unitesLegales" not in result
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
            "unitesLegales": [
                {
                    "siren": "123456789",
                    "statutDiffusionUniteLegale": "O",
                    "dateCreationUniteLegale": "2020-01-01",
                    "unitePurgeeUniteLegale": False,
                    "sigleUniteLegale": "TC",
                },
                {
                    "siren": "987654321",
                    "statutDiffusionUniteLegale": "O",
                    "dateCreationUniteLegale": "2021-02-01",
                    "unitePurgeeUniteLegale": False,
                    "sigleUniteLegale": "SNCF",
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

        reponse = ReponseUnitesLegales.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 2
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 2

        assert len(reponse.unites_legales) == 2
        assert isinstance(reponse.unites_legales[0], UniteLegale)
        assert reponse.unites_legales[0].siren == "123456789"
        assert reponse.unites_legales[0].statut_diffusion_unite_legale == "O"
        assert reponse.unites_legales[0].date_creation_unite_legale == date(2020, 1, 1)
        assert reponse.unites_legales[0].unite_purgee_unite_legale is False
        assert reponse.unites_legales[0].sigle_unite_legale == "TC"

        assert isinstance(reponse.unites_legales[1], UniteLegale)
        assert reponse.unites_legales[1].siren == "987654321"
        assert reponse.unites_legales[1].statut_diffusion_unite_legale == "O"
        assert reponse.unites_legales[1].date_creation_unite_legale == date(2021, 2, 1)
        assert reponse.unites_legales[1].unite_purgee_unite_legale is False
        assert reponse.unites_legales[1].sigle_unite_legale == "SNCF"

        assert len(reponse.facettes) == 1
        assert isinstance(reponse.facettes[0], Facette)
        assert reponse.facettes[0].nom == "test_facette"
        assert reponse.facettes[0].total == 10
        assert reponse.facettes[0].modalites == 5

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}

        reponse = ReponseUnitesLegales.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.unites_legales == []
        assert reponse.facettes == []
        assert reponse.additional_properties == {}

    def test_from_dict_with_empty_lists(self):
        """Test from_dict with empty lists."""
        data = {
            "unitesLegales": [],
            "facettes": [],
        }

        reponse = ReponseUnitesLegales.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.unites_legales == []
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

        unite_legale1 = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="TC",
        )

        unite_legale2 = UniteLegale(
            siren="987654321",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2021, 2, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="SNCF",
        )

        facette = Facette(
            nom="test_facette",
            total=10,
            modalites=5,
        )

        original = ReponseUnitesLegales(
            header=header,
            unites_legales=[unite_legale1, unite_legale2],
            facettes=[facette],
        )

        # Serialize to dict
        data = original.to_dict()

        # Deserialize back to object
        restored = ReponseUnitesLegales.from_dict(data)

        # Verify all fields are preserved
        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 2
        assert restored.header.debut == 0
        assert restored.header.nombre == 2

        assert len(restored.unites_legales) == 2
        assert isinstance(restored.unites_legales[0], UniteLegale)
        assert restored.unites_legales[0].siren == "123456789"
        assert restored.unites_legales[0].statut_diffusion_unite_legale == "O"
        assert restored.unites_legales[0].date_creation_unite_legale == date(2020, 1, 1)
        assert restored.unites_legales[0].unite_purgee_unite_legale is False
        assert restored.unites_legales[0].sigle_unite_legale == "TC"

        assert isinstance(restored.unites_legales[1], UniteLegale)
        assert restored.unites_legales[1].siren == "987654321"
        assert restored.unites_legales[1].statut_diffusion_unite_legale == "O"
        assert restored.unites_legales[1].date_creation_unite_legale == date(2021, 2, 1)
        assert restored.unites_legales[1].unite_purgee_unite_legale is False
        assert restored.unites_legales[1].sigle_unite_legale == "SNCF"

        assert len(restored.facettes) == 1
        assert isinstance(restored.facettes[0], Facette)
        assert restored.facettes[0].nom == "test_facette"
        assert restored.facettes[0].total == 10
        assert restored.facettes[0].modalites == 5

    def test_additional_properties_getitem(self):
        """Test additional properties __getitem__."""
        reponse = ReponseUnitesLegales()
        reponse.additional_properties["extraField"] = "extraValue"

        assert reponse["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test additional properties __setitem__."""
        reponse = ReponseUnitesLegales()
        reponse["extraField"] = "extraValue"

        assert reponse.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test additional properties __delitem__."""
        reponse = ReponseUnitesLegales()
        reponse.additional_properties["extraField"] = "extraValue"

        del reponse["extraField"]

        assert "extraField" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test additional properties __contains__."""
        reponse = ReponseUnitesLegales()
        reponse.additional_properties["extraField"] = "extraValue"

        assert "extraField" in reponse
        assert "nonexistentField" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseUnitesLegales()
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

        unite_legale1 = UniteLegale(
            siren="123456789",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2020, 1, 1),
            date_dernier_traitement_unite_legale="2020-01-02",
            unite_purgee_unite_legale=False,
            sigle_unite_legale="TC",
            nombre_periodes_unite_legale=1,
        )

        unite_legale2 = UniteLegale(
            siren="987654321",
            statut_diffusion_unite_legale="O",
            date_creation_unite_legale=date(2021, 2, 1),
            unite_purgee_unite_legale=False,
            sigle_unite_legale="SNCF",
            nombre_periodes_unite_legale=2,
        )

        unite_legale3 = UniteLegale(
            siren="555666777",
            statut_diffusion_unite_legale="N",
            date_creation_unite_legale=date(2022, 3, 1),
            unite_purgee_unite_legale=True,
            sigle_unite_legale="RATP",
            nombre_periodes_unite_legale=1,
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

        reponse = ReponseUnitesLegales(
            header=header,
            unites_legales=[unite_legale1, unite_legale2, unite_legale3],
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

        # Verify all unites_legales
        assert len(result["unitesLegales"]) == 3

        # First legal unit
        assert result["unitesLegales"][0]["siren"] == "123456789"
        assert result["unitesLegales"][0]["statutDiffusionUniteLegale"] == "O"
        assert result["unitesLegales"][0]["dateCreationUniteLegale"] == "2020-01-01"
        assert (
            result["unitesLegales"][0]["dateDernierTraitementUniteLegale"]
            == "2020-01-02"
        )
        assert result["unitesLegales"][0]["unitePurgeeUniteLegale"] is False
        assert result["unitesLegales"][0]["sigleUniteLegale"] == "TC"
        assert result["unitesLegales"][0]["nombrePeriodesUniteLegale"] == 1

        # Second legal unit
        assert result["unitesLegales"][1]["siren"] == "987654321"
        assert result["unitesLegales"][1]["statutDiffusionUniteLegale"] == "O"
        assert result["unitesLegales"][1]["dateCreationUniteLegale"] == "2021-02-01"
        assert result["unitesLegales"][1]["unitePurgeeUniteLegale"] is False
        assert result["unitesLegales"][1]["sigleUniteLegale"] == "SNCF"
        assert result["unitesLegales"][1]["nombrePeriodesUniteLegale"] == 2

        # Third legal unit
        assert result["unitesLegales"][2]["siren"] == "555666777"
        assert result["unitesLegales"][2]["statutDiffusionUniteLegale"] == "N"
        assert result["unitesLegales"][2]["dateCreationUniteLegale"] == "2022-03-01"
        assert result["unitesLegales"][2]["unitePurgeeUniteLegale"] is True
        assert result["unitesLegales"][2]["sigleUniteLegale"] == "RATP"
        assert result["unitesLegales"][2]["nombrePeriodesUniteLegale"] == 1

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
        restored = ReponseUnitesLegales.from_dict(result)

        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 3
        assert restored.header.debut == 0
        assert restored.header.nombre == 3
        assert restored.header.curseur == "start"
        assert restored.header.curseur_suivant == "next"

        assert len(restored.unites_legales) == 3
        assert isinstance(restored.unites_legales[0], UniteLegale)
        assert restored.unites_legales[0].siren == "123456789"
        assert restored.unites_legales[0].statut_diffusion_unite_legale == "O"
        assert restored.unites_legales[0].date_creation_unite_legale == date(2020, 1, 1)
        assert (
            restored.unites_legales[0].date_dernier_traitement_unite_legale
            == "2020-01-02"
        )
        assert restored.unites_legales[0].unite_purgee_unite_legale is False
        assert restored.unites_legales[0].sigle_unite_legale == "TC"
        assert restored.unites_legales[0].nombre_periodes_unite_legale == 1

        assert isinstance(restored.unites_legales[1], UniteLegale)
        assert restored.unites_legales[1].siren == "987654321"
        assert restored.unites_legales[1].statut_diffusion_unite_legale == "O"
        assert restored.unites_legales[1].date_creation_unite_legale == date(2021, 2, 1)
        assert restored.unites_legales[1].unite_purgee_unite_legale is False
        assert restored.unites_legales[1].sigle_unite_legale == "SNCF"
        assert restored.unites_legales[1].nombre_periodes_unite_legale == 2

        assert isinstance(restored.unites_legales[2], UniteLegale)
        assert restored.unites_legales[2].siren == "555666777"
        assert restored.unites_legales[2].statut_diffusion_unite_legale == "N"
        assert restored.unites_legales[2].date_creation_unite_legale == date(2022, 3, 1)
        assert restored.unites_legales[2].unite_purgee_unite_legale is True
        assert restored.unites_legales[2].sigle_unite_legale == "RATP"
        assert restored.unites_legales[2].nombre_periodes_unite_legale == 1

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
