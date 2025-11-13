"""Tests for sirene_api_client.models.periode_etablissement module."""

from datetime import date

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.periode_etablissement import PeriodeEtablissement
from sirene_api_client.models.periode_etablissement_nomenclature_activite_principale_etablissement import (
    PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement,
)


class TestPeriodeEtablissement:
    """Test PeriodeEtablissement model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        periode = PeriodeEtablissement(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_etablissement="A",
            changement_etat_administratif_etablissement=False,
            enseigne_1_etablissement="ENSEIGNE 1",
            enseigne_2_etablissement="ENSEIGNE 2",
            enseigne_3_etablissement="ENSEIGNE 3",
            changement_enseigne_etablissement=True,
            denomination_usuelle_etablissement="DENOMINATION USUELLE",
            changement_denomination_usuelle_etablissement=False,
            activite_principale_etablissement="6201Z",
            nomenclature_activite_principale_etablissement=PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2,
            changement_activite_principale_etablissement=True,
            caractere_employeur_etablissement="O",
            changement_caractere_employeur_etablissement=False,
        )

        assert periode.date_fin == date(2023, 12, 31)
        assert periode.date_debut == date(2023, 1, 1)
        assert periode.etat_administratif_etablissement == "A"
        assert periode.changement_etat_administratif_etablissement is False
        assert periode.enseigne_1_etablissement == "ENSEIGNE 1"
        assert periode.enseigne_2_etablissement == "ENSEIGNE 2"
        assert periode.enseigne_3_etablissement == "ENSEIGNE 3"
        assert periode.changement_enseigne_etablissement is True
        assert periode.denomination_usuelle_etablissement == "DENOMINATION USUELLE"
        assert periode.changement_denomination_usuelle_etablissement is False
        assert periode.activite_principale_etablissement == "6201Z"
        assert (
            periode.nomenclature_activite_principale_etablissement
            == PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2
        )
        assert periode.changement_activite_principale_etablissement is True
        assert periode.caractere_employeur_etablissement == "O"
        assert periode.changement_caractere_employeur_etablissement is False

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        periode = PeriodeEtablissement()

        assert periode.date_fin is UNSET
        assert periode.date_debut is UNSET
        assert periode.etat_administratif_etablissement is UNSET
        assert periode.changement_etat_administratif_etablissement is UNSET
        assert periode.enseigne_1_etablissement is UNSET
        assert periode.enseigne_2_etablissement is UNSET
        assert periode.enseigne_3_etablissement is UNSET
        assert periode.changement_enseigne_etablissement is UNSET
        assert periode.denomination_usuelle_etablissement is UNSET
        assert periode.changement_denomination_usuelle_etablissement is UNSET
        assert periode.activite_principale_etablissement is UNSET
        assert periode.nomenclature_activite_principale_etablissement is UNSET
        assert periode.changement_activite_principale_etablissement is UNSET
        assert periode.caractere_employeur_etablissement is UNSET
        assert periode.changement_caractere_employeur_etablissement is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        periode = PeriodeEtablissement(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_etablissement="A",
            changement_etat_administratif_etablissement=False,
            enseigne_1_etablissement="ENSEIGNE 1",
            enseigne_2_etablissement="ENSEIGNE 2",
            enseigne_3_etablissement="ENSEIGNE 3",
            changement_enseigne_etablissement=True,
            denomination_usuelle_etablissement="DENOMINATION USUELLE",
            changement_denomination_usuelle_etablissement=False,
            activite_principale_etablissement="6201Z",
            nomenclature_activite_principale_etablissement=PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2,
            changement_activite_principale_etablissement=True,
            caractere_employeur_etablissement="O",
            changement_caractere_employeur_etablissement=False,
        )

        result = periode.to_dict()

        assert result["dateFin"] == "2023-12-31"
        assert result["dateDebut"] == "2023-01-01"
        assert result["etatAdministratifEtablissement"] == "A"
        assert result["changementEtatAdministratifEtablissement"] is False
        assert result["enseigne1Etablissement"] == "ENSEIGNE 1"
        assert result["enseigne2Etablissement"] == "ENSEIGNE 2"
        assert result["enseigne3Etablissement"] == "ENSEIGNE 3"
        assert result["changementEnseigneEtablissement"] is True
        assert result["denominationUsuelleEtablissement"] == "DENOMINATION USUELLE"
        assert result["changementDenominationUsuelleEtablissement"] is False
        assert result["activitePrincipaleEtablissement"] == "6201Z"
        assert result["nomenclatureActivitePrincipaleEtablissement"] == "NAFRev2"
        assert result["changementActivitePrincipaleEtablissement"] is True
        assert result["caractereEmployeurEtablissement"] == "O"
        assert result["changementCaractereEmployeurEtablissement"] is False

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        periode = PeriodeEtablissement()

        result = periode.to_dict()

        assert "dateFin" not in result
        assert "dateDebut" not in result
        assert "etatAdministratifEtablissement" not in result
        assert "changementEtatAdministratifEtablissement" not in result
        assert "enseigne1Etablissement" not in result
        assert "enseigne2Etablissement" not in result
        assert "enseigne3Etablissement" not in result
        assert "changementEnseigneEtablissement" not in result
        assert "denominationUsuelleEtablissement" not in result
        assert "changementDenominationUsuelleEtablissement" not in result
        assert "activitePrincipaleEtablissement" not in result
        assert "nomenclatureActivitePrincipaleEtablissement" not in result
        assert "changementActivitePrincipaleEtablissement" not in result
        assert "caractereEmployeurEtablissement" not in result
        assert "changementCaractereEmployeurEtablissement" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "dateFin": "2023-12-31",
            "dateDebut": "2023-01-01",
            "etatAdministratifEtablissement": "A",
            "changementEtatAdministratifEtablissement": False,
            "enseigne1Etablissement": "ENSEIGNE 1",
            "enseigne2Etablissement": "ENSEIGNE 2",
            "enseigne3Etablissement": "ENSEIGNE 3",
            "changementEnseigneEtablissement": True,
            "denominationUsuelleEtablissement": "DENOMINATION USUELLE",
            "changementDenominationUsuelleEtablissement": False,
            "activitePrincipaleEtablissement": "6201Z",
            "nomenclatureActivitePrincipaleEtablissement": "NAFRev2",
            "changementActivitePrincipaleEtablissement": True,
            "caractereEmployeurEtablissement": "O",
            "changementCaractereEmployeurEtablissement": False,
        }

        periode = PeriodeEtablissement.from_dict(data)

        assert periode.date_fin == date(2023, 12, 31)
        assert periode.date_debut == date(2023, 1, 1)
        assert periode.etat_administratif_etablissement == "A"
        assert periode.changement_etat_administratif_etablissement is False
        assert periode.enseigne_1_etablissement == "ENSEIGNE 1"
        assert periode.enseigne_2_etablissement == "ENSEIGNE 2"
        assert periode.enseigne_3_etablissement == "ENSEIGNE 3"
        assert periode.changement_enseigne_etablissement is True
        assert periode.denomination_usuelle_etablissement == "DENOMINATION USUELLE"
        assert periode.changement_denomination_usuelle_etablissement is False
        assert periode.activite_principale_etablissement == "6201Z"
        assert (
            periode.nomenclature_activite_principale_etablissement
            == PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2
        )
        assert periode.changement_activite_principale_etablissement is True
        assert periode.caractere_employeur_etablissement == "O"
        assert periode.changement_caractere_employeur_etablissement is False

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "dateDebut": "2023-01-01",
            "etatAdministratifEtablissement": "A",
        }

        periode = PeriodeEtablissement.from_dict(data)

        assert periode.date_fin is UNSET
        assert periode.date_debut == date(2023, 1, 1)
        assert periode.etat_administratif_etablissement == "A"
        assert periode.changement_etat_administratif_etablissement is UNSET
        assert periode.enseigne_1_etablissement is UNSET
        assert periode.enseigne_2_etablissement is UNSET
        assert periode.enseigne_3_etablissement is UNSET
        assert periode.changement_enseigne_etablissement is UNSET
        assert periode.denomination_usuelle_etablissement is UNSET
        assert periode.changement_denomination_usuelle_etablissement is UNSET
        assert periode.activite_principale_etablissement is UNSET
        assert periode.nomenclature_activite_principale_etablissement is UNSET
        assert periode.changement_activite_principale_etablissement is UNSET
        assert periode.caractere_employeur_etablissement is UNSET
        assert periode.changement_caractere_employeur_etablissement is UNSET

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = PeriodeEtablissement(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_etablissement="A",
            changement_etat_administratif_etablissement=False,
            enseigne_1_etablissement="ENSEIGNE 1",
            enseigne_2_etablissement="ENSEIGNE 2",
            enseigne_3_etablissement="ENSEIGNE 3",
            changement_enseigne_etablissement=True,
            denomination_usuelle_etablissement="DENOMINATION USUELLE",
            changement_denomination_usuelle_etablissement=False,
            activite_principale_etablissement="6201Z",
            nomenclature_activite_principale_etablissement=PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2,
            changement_activite_principale_etablissement=True,
            caractere_employeur_etablissement="O",
            changement_caractere_employeur_etablissement=False,
        )

        data = original.to_dict()
        restored = PeriodeEtablissement.from_dict(data)

        assert restored.date_fin == original.date_fin
        assert restored.date_debut == original.date_debut
        assert (
            restored.etat_administratif_etablissement
            == original.etat_administratif_etablissement
        )
        assert (
            restored.changement_etat_administratif_etablissement
            == original.changement_etat_administratif_etablissement
        )
        assert restored.enseigne_1_etablissement == original.enseigne_1_etablissement
        assert restored.enseigne_2_etablissement == original.enseigne_2_etablissement
        assert restored.enseigne_3_etablissement == original.enseigne_3_etablissement
        assert (
            restored.changement_enseigne_etablissement
            == original.changement_enseigne_etablissement
        )
        assert (
            restored.denomination_usuelle_etablissement
            == original.denomination_usuelle_etablissement
        )
        assert (
            restored.changement_denomination_usuelle_etablissement
            == original.changement_denomination_usuelle_etablissement
        )
        assert (
            restored.activite_principale_etablissement
            == original.activite_principale_etablissement
        )
        assert (
            restored.nomenclature_activite_principale_etablissement
            == original.nomenclature_activite_principale_etablissement
        )
        assert (
            restored.changement_activite_principale_etablissement
            == original.changement_activite_principale_etablissement
        )
        assert (
            restored.caractere_employeur_etablissement
            == original.caractere_employeur_etablissement
        )
        assert (
            restored.changement_caractere_employeur_etablissement
            == original.changement_caractere_employeur_etablissement
        )

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        periode = PeriodeEtablissement()
        periode.additional_properties["extraField"] = "extraValue"

        assert periode["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        periode = PeriodeEtablissement()
        periode["extraField"] = "extraValue"

        assert periode.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        periode = PeriodeEtablissement()
        periode.additional_properties["extraField"] = "extraValue"

        del periode["extraField"]

        assert "extraField" not in periode.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        periode = PeriodeEtablissement()
        periode.additional_properties["extraField"] = "extraValue"

        assert "extraField" in periode
        assert "nonexistentField" not in periode

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        periode = PeriodeEtablissement()
        periode.additional_properties["field1"] = "value1"
        periode.additional_properties["field2"] = "value2"

        keys = periode.additional_keys
        assert len(keys) == 2
        assert "field1" in keys
        assert "field2" in keys

    def test_enum_field_handling(self):
        """Test handling of enum fields."""
        # Test all enum values
        enum_values = [
            PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAP,
            PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV1,
            PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAFREV2,
            PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement.NAF1993,
        ]

        for enum_value in enum_values:
            periode = PeriodeEtablissement(
                nomenclature_activite_principale_etablissement=enum_value
            )

            result = periode.to_dict()
            assert (
                result["nomenclatureActivitePrincipaleEtablissement"]
                == enum_value.value
            )

            # Test deserialization
            restored = PeriodeEtablissement.from_dict(result)
            assert restored.nomenclature_activite_principale_etablissement == enum_value

    def test_boolean_field_handling(self):
        """Test handling of boolean fields."""
        periode = PeriodeEtablissement(
            changement_etat_administratif_etablissement=True,
            changement_enseigne_etablissement=False,
            changement_denomination_usuelle_etablissement=True,
            changement_activite_principale_etablissement=False,
            changement_caractere_employeur_etablissement=True,
        )

        result = periode.to_dict()

        assert result["changementEtatAdministratifEtablissement"] is True
        assert result["changementEnseigneEtablissement"] is False
        assert result["changementDenominationUsuelleEtablissement"] is True
        assert result["changementActivitePrincipaleEtablissement"] is False
        assert result["changementCaractereEmployeurEtablissement"] is True

        # Test deserialization
        restored = PeriodeEtablissement.from_dict(result)

        assert restored.changement_etat_administratif_etablissement is True
        assert restored.changement_enseigne_etablissement is False
        assert restored.changement_denomination_usuelle_etablissement is True
        assert restored.changement_activite_principale_etablissement is False
        assert restored.changement_caractere_employeur_etablissement is True

    def test_date_field_handling(self):
        """Test handling of date fields."""
        periode = PeriodeEtablissement(
            date_debut=date(2023, 1, 1),
            date_fin=date(2023, 12, 31),
        )

        result = periode.to_dict()

        assert result["dateDebut"] == "2023-01-01"
        assert result["dateFin"] == "2023-12-31"

        # Test deserialization
        restored = PeriodeEtablissement.from_dict(result)

        assert restored.date_debut == date(2023, 1, 1)
        assert restored.date_fin == date(2023, 12, 31)

    def test_string_field_handling(self):
        """Test handling of string fields."""
        periode = PeriodeEtablissement(
            etat_administratif_etablissement="A",
            enseigne_1_etablissement="ENSEIGNE 1",
            enseigne_2_etablissement="ENSEIGNE 2",
            enseigne_3_etablissement="ENSEIGNE 3",
            denomination_usuelle_etablissement="DENOMINATION USUELLE",
            activite_principale_etablissement="6201Z",
            caractere_employeur_etablissement="O",
        )

        result = periode.to_dict()

        assert result["etatAdministratifEtablissement"] == "A"
        assert result["enseigne1Etablissement"] == "ENSEIGNE 1"
        assert result["enseigne2Etablissement"] == "ENSEIGNE 2"
        assert result["enseigne3Etablissement"] == "ENSEIGNE 3"
        assert result["denominationUsuelleEtablissement"] == "DENOMINATION USUELLE"
        assert result["activitePrincipaleEtablissement"] == "6201Z"
        assert result["caractereEmployeurEtablissement"] == "O"

        # Test deserialization
        restored = PeriodeEtablissement.from_dict(result)

        assert restored.etat_administratif_etablissement == "A"
        assert restored.enseigne_1_etablissement == "ENSEIGNE 1"
        assert restored.enseigne_2_etablissement == "ENSEIGNE 2"
        assert restored.enseigne_3_etablissement == "ENSEIGNE 3"
        assert restored.denomination_usuelle_etablissement == "DENOMINATION USUELLE"
        assert restored.activite_principale_etablissement == "6201Z"
        assert restored.caractere_employeur_etablissement == "O"

    def test_unicode_handling(self):
        """Test handling of unicode characters in string fields."""
        periode = PeriodeEtablissement(
            enseigne_1_etablissement="Café & Restaurant",
            enseigne_2_etablissement="Établissement Français",
            enseigne_3_etablissement="Société à Responsabilité Limitée",
            denomination_usuelle_etablissement="Société Française",
        )

        result = periode.to_dict()

        assert result["enseigne1Etablissement"] == "Café & Restaurant"
        assert result["enseigne2Etablissement"] == "Établissement Français"
        assert result["enseigne3Etablissement"] == "Société à Responsabilité Limitée"
        assert result["denominationUsuelleEtablissement"] == "Société Française"

        # Test deserialization
        restored = PeriodeEtablissement.from_dict(result)

        assert restored.enseigne_1_etablissement == "Café & Restaurant"
        assert restored.enseigne_2_etablissement == "Établissement Français"
        assert restored.enseigne_3_etablissement == "Société à Responsabilité Limitée"
        assert restored.denomination_usuelle_etablissement == "Société Française"

    def test_empty_strings_vs_unset(self):
        """Test distinction between empty strings and UNSET."""
        periode = PeriodeEtablissement(
            enseigne_1_etablissement="",
            enseigne_2_etablissement="NON_UNSET",
        )

        result = periode.to_dict()

        assert result["enseigne1Etablissement"] == ""
        assert result["enseigne2Etablissement"] == "NON_UNSET"
        assert "enseigne3Etablissement" not in result  # UNSET field

        # Test deserialization
        restored = PeriodeEtablissement.from_dict(result)

        assert restored.enseigne_1_etablissement == ""
        assert restored.enseigne_2_etablissement == "NON_UNSET"
        assert restored.enseigne_3_etablissement is UNSET
