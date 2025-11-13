from datetime import datetime

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.dates_mise_a_jour_donnees import DatesMiseAJourDonnees
from sirene_api_client.models.dates_mise_a_jour_donnees_collection import (
    DatesMiseAJourDonneesCollection,
)
from sirene_api_client.models.etat_collection import EtatCollection
from sirene_api_client.models.etat_collection_etat_collection import (
    EtatCollectionEtatCollection,
)
from sirene_api_client.models.header import Header
from sirene_api_client.models.reponse_informations import ReponseInformations
from sirene_api_client.models.reponse_informations_etat_service import (
    ReponseInformationsEtatService,
)


class TestReponseInformations:
    """Test ReponseInformations model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
        )

        etat_service = ReponseInformationsEtatService.UP

        etat_collection = EtatCollection(
            collection="test_collection",
            etat_collection=EtatCollectionEtatCollection.UP,
        )

        dates_mise_a_jour = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.UNITÉS_LÉGALES,
            date_derniere_mise_a_disposition=datetime(2023, 1, 1, 12, 0, 0),
        )

        reponse = ReponseInformations(
            header=header,
            etat_service=etat_service,
            etats_des_services=[etat_collection],
            version_service="1.0.0",
            journal_des_modifications="Version 1.0.0 - Initial release",
            dates_dernieres_mises_a_jour_des_donnees=[dates_mise_a_jour],
        )

        assert reponse.header == header
        assert reponse.etat_service == etat_service
        assert reponse.etats_des_services == [etat_collection]
        assert reponse.version_service == "1.0.0"
        assert reponse.journal_des_modifications == "Version 1.0.0 - Initial release"
        assert reponse.dates_dernieres_mises_a_jour_des_donnees == [dates_mise_a_jour]
        assert reponse.additional_properties == {}

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal fields."""
        reponse = ReponseInformations()

        assert reponse.header is UNSET
        assert reponse.etat_service is UNSET
        assert reponse.etats_des_services is UNSET
        assert reponse.version_service is UNSET
        assert reponse.journal_des_modifications is UNSET
        assert reponse.dates_dernieres_mises_a_jour_des_donnees is UNSET
        assert reponse.additional_properties == {}

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
        )

        etat_service = ReponseInformationsEtatService.UP

        etat_collection = EtatCollection(
            collection="test_collection",
            etat_collection=EtatCollectionEtatCollection.UP,
        )

        dates_mise_a_jour = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.UNITÉS_LÉGALES,
            date_derniere_mise_a_disposition=datetime(2023, 1, 1, 12, 0, 0),
        )

        reponse = ReponseInformations(
            header=header,
            etat_service=etat_service,
            etats_des_services=[etat_collection],
            version_service="1.0.0",
            journal_des_modifications="Version 1.0.0 - Initial release",
            dates_dernieres_mises_a_jour_des_donnees=[dates_mise_a_jour],
        )

        result = reponse.to_dict()

        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 1
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 1

        assert result["etatService"] == "UP"

        assert len(result["etatsDesServices"]) == 1
        assert result["etatsDesServices"][0]["Collection"] == "test_collection"
        assert result["etatsDesServices"][0]["etatCollection"] == "UP"

        assert result["versionService"] == "1.0.0"
        assert result["journalDesModifications"] == "Version 1.0.0 - Initial release"

        assert len(result["datesDernieresMisesAJourDesDonnees"]) == 1
        assert (
            result["datesDernieresMisesAJourDesDonnees"][0]["collection"]
            == "Unités Légales"
        )
        assert (
            result["datesDernieresMisesAJourDesDonnees"][0][
                "dateDerniereMiseADisposition"
            ]
            == "2023-01-01T12:00:00"
        )

    def test_to_dict_with_unset_fields(self):
        """Test to_dict with unset fields."""
        reponse = ReponseInformations()

        result = reponse.to_dict()

        assert "header" not in result
        assert "etatService" not in result
        assert "etatsDesServices" not in result
        assert "versionService" not in result
        assert "journalDesModifications" not in result
        assert "datesDernieresMisesAJourDesDonnees" not in result
        assert result == {}

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "header": {
                "statut": 200,
                "message": "OK",
                "total": 1,
                "debut": 0,
                "nombre": 1,
            },
            "etatService": "UP",
            "etatsDesServices": [
                {
                    "Collection": "test_collection",
                    "etatCollection": "UP",
                },
            ],
            "versionService": "1.0.0",
            "journalDesModifications": "Version 1.0.0 - Initial release",
            "datesDernieresMisesAJourDesDonnees": [
                {
                    "collection": "Unités Légales",
                    "dateDerniereMiseADisposition": "2023-01-01T12:00:00",
                },
            ],
        }

        reponse = ReponseInformations.from_dict(data)

        assert isinstance(reponse.header, Header)
        assert reponse.header.statut == 200
        assert reponse.header.message == "OK"
        assert reponse.header.total == 1
        assert reponse.header.debut == 0
        assert reponse.header.nombre == 1

        assert reponse.etat_service == ReponseInformationsEtatService.UP

        assert len(reponse.etats_des_services) == 1
        assert isinstance(reponse.etats_des_services[0], EtatCollection)
        assert reponse.etats_des_services[0].collection == "test_collection"
        assert (
            reponse.etats_des_services[0].etat_collection
            == EtatCollectionEtatCollection.UP
        )

        assert reponse.version_service == "1.0.0"
        assert reponse.journal_des_modifications == "Version 1.0.0 - Initial release"

        assert len(reponse.dates_dernieres_mises_a_jour_des_donnees) == 1
        assert isinstance(
            reponse.dates_dernieres_mises_a_jour_des_donnees[0], DatesMiseAJourDonnees
        )
        assert (
            reponse.dates_dernieres_mises_a_jour_des_donnees[0].collection
            == "Unités Légales"
        )
        assert reponse.dates_dernieres_mises_a_jour_des_donnees[
            0
        ].date_derniere_mise_a_disposition == datetime(2023, 1, 1, 12, 0, 0)

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {}

        reponse = ReponseInformations.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etat_service is UNSET
        assert reponse.etats_des_services == []
        assert reponse.version_service is UNSET
        assert reponse.journal_des_modifications is UNSET
        assert reponse.dates_dernieres_mises_a_jour_des_donnees == []
        assert reponse.additional_properties == {}

    def test_from_dict_with_empty_lists(self):
        """Test from_dict with empty lists."""
        data = {
            "etatsDesServices": [],
            "datesDernieresMisesAJourDesDonnees": [],
        }

        reponse = ReponseInformations.from_dict(data)

        assert reponse.header is UNSET
        assert reponse.etat_service is UNSET
        assert reponse.etats_des_services == []
        assert reponse.version_service is UNSET
        assert reponse.journal_des_modifications is UNSET
        assert reponse.dates_dernieres_mises_a_jour_des_donnees == []
        assert reponse.additional_properties == {}

    def test_roundtrip_serialization(self):
        """Test round-trip serialization."""
        header = Header(
            statut=200,
            message="OK",
            total=1,
            debut=0,
            nombre=1,
        )

        etat_service = ReponseInformationsEtatService.UP

        etat_collection = EtatCollection(
            collection="test_collection",
            etat_collection=EtatCollectionEtatCollection.UP,
        )

        dates_mise_a_jour = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.UNITÉS_LÉGALES,
            date_derniere_mise_a_disposition=datetime(2023, 1, 1, 12, 0, 0),
        )

        original = ReponseInformations(
            header=header,
            etat_service=etat_service,
            etats_des_services=[etat_collection],
            version_service="1.0.0",
            journal_des_modifications="Version 1.0.0 - Initial release",
            dates_dernieres_mises_a_jour_des_donnees=[dates_mise_a_jour],
        )

        # Serialize to dict
        data = original.to_dict()

        # Deserialize back to object
        restored = ReponseInformations.from_dict(data)

        # Verify all fields are preserved
        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 1
        assert restored.header.debut == 0
        assert restored.header.nombre == 1

        assert restored.etat_service == ReponseInformationsEtatService.UP

        assert len(restored.etats_des_services) == 1
        assert isinstance(restored.etats_des_services[0], EtatCollection)
        assert restored.etats_des_services[0].collection == "test_collection"
        assert (
            restored.etats_des_services[0].etat_collection
            == EtatCollectionEtatCollection.UP
        )

        assert restored.version_service == "1.0.0"
        assert restored.journal_des_modifications == "Version 1.0.0 - Initial release"

        assert len(restored.dates_dernieres_mises_a_jour_des_donnees) == 1
        assert isinstance(
            restored.dates_dernieres_mises_a_jour_des_donnees[0], DatesMiseAJourDonnees
        )
        assert (
            restored.dates_dernieres_mises_a_jour_des_donnees[0].collection
            == "Unités Légales"
        )
        assert restored.dates_dernieres_mises_a_jour_des_donnees[
            0
        ].date_derniere_mise_a_disposition == datetime(2023, 1, 1, 12, 0, 0)

    def test_additional_properties_getitem(self):
        """Test additional properties __getitem__."""
        reponse = ReponseInformations()
        reponse.additional_properties["extraField"] = "extraValue"

        assert reponse["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test additional properties __setitem__."""
        reponse = ReponseInformations()
        reponse["extraField"] = "extraValue"

        assert reponse.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test additional properties __delitem__."""
        reponse = ReponseInformations()
        reponse.additional_properties["extraField"] = "extraValue"

        del reponse["extraField"]

        assert "extraField" not in reponse.additional_properties

    def test_additional_properties_contains(self):
        """Test additional properties __contains__."""
        reponse = ReponseInformations()
        reponse.additional_properties["extraField"] = "extraValue"

        assert "extraField" in reponse
        assert "nonexistentField" not in reponse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        reponse = ReponseInformations()
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

        etat_service = ReponseInformationsEtatService.UP

        etat_collection1 = EtatCollection(
            collection="collection1",
            etat_collection=EtatCollectionEtatCollection.UP,
        )

        etat_collection2 = EtatCollection(
            collection="collection2",
            etat_collection=EtatCollectionEtatCollection.DOWN,
        )

        etat_collection3 = EtatCollection(
            collection="collection3",
            etat_collection=EtatCollectionEtatCollection.UP,
        )

        dates_mise_a_jour1 = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.UNITÉS_LÉGALES,
            date_derniere_mise_a_disposition=datetime(2023, 1, 1, 12, 0, 0),
        )

        dates_mise_a_jour2 = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.ÉTABLISSEMENTS,
            date_derniere_mise_a_disposition=datetime(2023, 1, 2, 14, 30, 0),
        )

        dates_mise_a_jour3 = DatesMiseAJourDonnees(
            collection=DatesMiseAJourDonneesCollection.LIENS_DE_SUCCESSION,
            date_derniere_mise_a_disposition=datetime(2023, 1, 3, 16, 45, 0),
        )

        reponse = ReponseInformations(
            header=header,
            etat_service=etat_service,
            etats_des_services=[etat_collection1, etat_collection2, etat_collection3],
            version_service="2.0.0",
            journal_des_modifications="Version 2.0.0 - Major update with new features",
            dates_dernieres_mises_a_jour_des_donnees=[
                dates_mise_a_jour1,
                dates_mise_a_jour2,
                dates_mise_a_jour3,
            ],
        )

        # Add additional properties to the top-level response
        reponse.additional_properties["extraField"] = "extraValue"
        reponse.additional_properties["metadata"] = {"version": "2.0.0"}

        result = reponse.to_dict()

        # Verify header serialization
        assert result["header"]["statut"] == 200
        assert result["header"]["message"] == "OK"
        assert result["header"]["total"] == 3
        assert result["header"]["debut"] == 0
        assert result["header"]["nombre"] == 3
        assert result["header"]["curseur"] == "start"
        assert result["header"]["curseurSuivant"] == "next"

        # Verify etat_service
        assert result["etatService"] == "UP"

        # Verify all etats_des_services
        assert len(result["etatsDesServices"]) == 3

        # First collection
        assert result["etatsDesServices"][0]["Collection"] == "collection1"
        assert result["etatsDesServices"][0]["etatCollection"] == "UP"

        # Second collection
        assert result["etatsDesServices"][1]["Collection"] == "collection2"
        assert result["etatsDesServices"][1]["etatCollection"] == "DOWN"

        # Third collection
        assert result["etatsDesServices"][2]["Collection"] == "collection3"
        assert result["etatsDesServices"][2]["etatCollection"] == "UP"

        # Verify version and journal
        assert result["versionService"] == "2.0.0"
        assert (
            result["journalDesModifications"]
            == "Version 2.0.0 - Major update with new features"
        )

        # Verify all dates_dernieres_mises_a_jour_des_donnees
        assert len(result["datesDernieresMisesAJourDesDonnees"]) == 3

        # First date
        assert (
            result["datesDernieresMisesAJourDesDonnees"][0]["collection"]
            == "Unités Légales"
        )
        assert (
            result["datesDernieresMisesAJourDesDonnees"][0][
                "dateDerniereMiseADisposition"
            ]
            == "2023-01-01T12:00:00"
        )

        # Second date
        assert (
            result["datesDernieresMisesAJourDesDonnees"][1]["collection"]
            == "Établissements"
        )
        assert (
            result["datesDernieresMisesAJourDesDonnees"][1][
                "dateDerniereMiseADisposition"
            ]
            == "2023-01-02T14:30:00"
        )

        # Third date
        assert (
            result["datesDernieresMisesAJourDesDonnees"][2]["collection"]
            == "Liens de succession"
        )
        assert (
            result["datesDernieresMisesAJourDesDonnees"][2][
                "dateDerniereMiseADisposition"
            ]
            == "2023-01-03T16:45:00"
        )

        # Verify additional properties
        assert result["extraField"] == "extraValue"
        assert result["metadata"] == {"version": "2.0.0"}

        # Test deserialization
        restored = ReponseInformations.from_dict(result)

        assert isinstance(restored.header, Header)
        assert restored.header.statut == 200
        assert restored.header.message == "OK"
        assert restored.header.total == 3
        assert restored.header.debut == 0
        assert restored.header.nombre == 3
        assert restored.header.curseur == "start"
        assert restored.header.curseur_suivant == "next"

        assert restored.etat_service == ReponseInformationsEtatService.UP

        assert len(restored.etats_des_services) == 3
        assert isinstance(restored.etats_des_services[0], EtatCollection)
        assert restored.etats_des_services[0].collection == "collection1"
        assert (
            restored.etats_des_services[0].etat_collection
            == EtatCollectionEtatCollection.UP
        )

        assert isinstance(restored.etats_des_services[1], EtatCollection)
        assert restored.etats_des_services[1].collection == "collection2"
        assert (
            restored.etats_des_services[1].etat_collection
            == EtatCollectionEtatCollection.DOWN
        )

        assert isinstance(restored.etats_des_services[2], EtatCollection)
        assert restored.etats_des_services[2].collection == "collection3"
        assert (
            restored.etats_des_services[2].etat_collection
            == EtatCollectionEtatCollection.UP
        )

        assert restored.version_service == "2.0.0"
        assert (
            restored.journal_des_modifications
            == "Version 2.0.0 - Major update with new features"
        )

        assert len(restored.dates_dernieres_mises_a_jour_des_donnees) == 3
        assert isinstance(
            restored.dates_dernieres_mises_a_jour_des_donnees[0], DatesMiseAJourDonnees
        )
        assert (
            restored.dates_dernieres_mises_a_jour_des_donnees[0].collection
            == DatesMiseAJourDonneesCollection.UNITÉS_LÉGALES
        )
        assert restored.dates_dernieres_mises_a_jour_des_donnees[
            0
        ].date_derniere_mise_a_disposition == datetime(2023, 1, 1, 12, 0, 0)

        assert isinstance(
            restored.dates_dernieres_mises_a_jour_des_donnees[1], DatesMiseAJourDonnees
        )
        assert (
            restored.dates_dernieres_mises_a_jour_des_donnees[1].collection
            == DatesMiseAJourDonneesCollection.ÉTABLISSEMENTS
        )
        assert restored.dates_dernieres_mises_a_jour_des_donnees[
            1
        ].date_derniere_mise_a_disposition == datetime(2023, 1, 2, 14, 30, 0)

        assert isinstance(
            restored.dates_dernieres_mises_a_jour_des_donnees[2], DatesMiseAJourDonnees
        )
        assert (
            restored.dates_dernieres_mises_a_jour_des_donnees[2].collection
            == DatesMiseAJourDonneesCollection.LIENS_DE_SUCCESSION
        )
        assert restored.dates_dernieres_mises_a_jour_des_donnees[
            2
        ].date_derniere_mise_a_disposition == datetime(2023, 1, 3, 16, 45, 0)

        assert restored.additional_properties["extraField"] == "extraValue"
        assert restored.additional_properties["metadata"] == {"version": "2.0.0"}
