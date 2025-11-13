"""Tests for sirene_api_client.models.periode_unite_legale module."""

from datetime import date

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.periode_unite_legale import PeriodeUniteLegale
from sirene_api_client.models.periode_unite_legale_caractere_employeur_unite_legale import (
    PeriodeUniteLegaleCaractereEmployeurUniteLegale,
)
from sirene_api_client.models.periode_unite_legale_etat_administratif_unite_legale import (
    PeriodeUniteLegaleEtatAdministratifUniteLegale,
)
from sirene_api_client.models.periode_unite_legale_nomenclature_activite_principale_unite_legale import (
    PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale,
)


class TestPeriodeUniteLegale:
    """Test PeriodeUniteLegale model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        periode = PeriodeUniteLegale(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_unite_legale=PeriodeUniteLegaleEtatAdministratifUniteLegale.A,
            changement_etat_administratif_unite_legale=False,
            nom_unite_legale="DUPONT",
            changement_nom_unite_legale=False,
            nom_usage_unite_legale="MARTIN",
            changement_nom_usage_unite_legale=True,
            denomination_unite_legale="SOCIETE DUPONT",
            changement_denomination_unite_legale=False,
            denomination_usuelle_1_unite_legale="DUPONT SARL",
            denomination_usuelle_2_unite_legale="DUPONT COMPANY",
            denomination_usuelle_3_unite_legale="DUPONT ENTREPRISE",
            categorie_juridique_unite_legale="5710",
            changement_categorie_juridique_unite_legale=False,
            activite_principale_unite_legale="6201Z",
            nomenclature_activite_principale_unite_legale=PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            changement_activite_principale_unite_legale=True,
            nic_siege_unite_legale="00001",
            changement_nic_siege_unite_legale=False,
            economie_sociale_solidaire_unite_legale="O",
            changement_economie_sociale_solidaire_unite_legale=False,
            societe_mission_unite_legale="N",
            changement_societe_mission_unite_legale=False,
            caractere_employeur_unite_legale=PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI,
            changement_caractere_employeur_unite_legale=True,
            changement_denomination_usuelle_unite_legale=False,
        )

        assert periode.date_fin == date(2023, 12, 31)
        assert periode.date_debut == date(2023, 1, 1)
        assert (
            periode.etat_administratif_unite_legale
            == PeriodeUniteLegaleEtatAdministratifUniteLegale.A
        )
        assert periode.changement_etat_administratif_unite_legale is False
        assert periode.nom_unite_legale == "DUPONT"
        assert periode.changement_nom_unite_legale is False
        assert periode.nom_usage_unite_legale == "MARTIN"
        assert periode.changement_nom_usage_unite_legale is True
        assert periode.denomination_unite_legale == "SOCIETE DUPONT"
        assert periode.changement_denomination_unite_legale is False
        assert periode.denomination_usuelle_1_unite_legale == "DUPONT SARL"
        assert periode.denomination_usuelle_2_unite_legale == "DUPONT COMPANY"
        assert periode.denomination_usuelle_3_unite_legale == "DUPONT ENTREPRISE"
        assert periode.categorie_juridique_unite_legale == "5710"
        assert periode.changement_categorie_juridique_unite_legale is False
        assert periode.activite_principale_unite_legale == "6201Z"
        assert (
            periode.nomenclature_activite_principale_unite_legale
            == PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2
        )
        assert periode.changement_activite_principale_unite_legale is True
        assert periode.nic_siege_unite_legale == "00001"
        assert periode.changement_nic_siege_unite_legale is False
        assert periode.economie_sociale_solidaire_unite_legale == "O"
        assert periode.changement_economie_sociale_solidaire_unite_legale is False
        assert periode.societe_mission_unite_legale == "N"
        assert periode.changement_societe_mission_unite_legale is False
        assert (
            periode.caractere_employeur_unite_legale
            == PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI
        )
        assert periode.changement_caractere_employeur_unite_legale is True
        assert periode.changement_denomination_usuelle_unite_legale is False

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        periode = PeriodeUniteLegale()

        assert periode.date_fin is UNSET
        assert periode.date_debut is UNSET
        assert periode.etat_administratif_unite_legale is UNSET
        assert periode.changement_etat_administratif_unite_legale is UNSET
        assert periode.nom_unite_legale is UNSET
        assert periode.changement_nom_unite_legale is UNSET
        assert periode.nom_usage_unite_legale is UNSET
        assert periode.changement_nom_usage_unite_legale is UNSET
        assert periode.denomination_unite_legale is UNSET
        assert periode.changement_denomination_unite_legale is UNSET
        assert periode.denomination_usuelle_1_unite_legale is UNSET
        assert periode.denomination_usuelle_2_unite_legale is UNSET
        assert periode.denomination_usuelle_3_unite_legale is UNSET
        assert periode.categorie_juridique_unite_legale is UNSET
        assert periode.changement_categorie_juridique_unite_legale is UNSET
        assert periode.activite_principale_unite_legale is UNSET
        assert periode.nomenclature_activite_principale_unite_legale is UNSET
        assert periode.changement_activite_principale_unite_legale is UNSET
        assert periode.nic_siege_unite_legale is UNSET
        assert periode.changement_nic_siege_unite_legale is UNSET
        assert periode.economie_sociale_solidaire_unite_legale is UNSET
        assert periode.changement_economie_sociale_solidaire_unite_legale is UNSET
        assert periode.societe_mission_unite_legale is UNSET
        assert periode.changement_societe_mission_unite_legale is UNSET
        assert periode.caractere_employeur_unite_legale is UNSET
        assert periode.changement_caractere_employeur_unite_legale is UNSET
        assert periode.changement_denomination_usuelle_unite_legale is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        periode = PeriodeUniteLegale(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_unite_legale=PeriodeUniteLegaleEtatAdministratifUniteLegale.A,
            changement_etat_administratif_unite_legale=False,
            nom_unite_legale="DUPONT",
            changement_nom_unite_legale=False,
            nom_usage_unite_legale="MARTIN",
            changement_nom_usage_unite_legale=True,
            denomination_unite_legale="SOCIETE DUPONT",
            changement_denomination_unite_legale=False,
            denomination_usuelle_1_unite_legale="DUPONT SARL",
            denomination_usuelle_2_unite_legale="DUPONT COMPANY",
            denomination_usuelle_3_unite_legale="DUPONT ENTREPRISE",
            categorie_juridique_unite_legale="5710",
            changement_categorie_juridique_unite_legale=False,
            activite_principale_unite_legale="6201Z",
            nomenclature_activite_principale_unite_legale=PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            changement_activite_principale_unite_legale=True,
            nic_siege_unite_legale="00001",
            changement_nic_siege_unite_legale=False,
            economie_sociale_solidaire_unite_legale="O",
            changement_economie_sociale_solidaire_unite_legale=False,
            societe_mission_unite_legale="N",
            changement_societe_mission_unite_legale=False,
            caractere_employeur_unite_legale=PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI,
            changement_caractere_employeur_unite_legale=True,
            changement_denomination_usuelle_unite_legale=False,
        )

        result = periode.to_dict()

        assert result["dateFin"] == "2023-12-31"
        assert result["dateDebut"] == "2023-01-01"
        assert result["etatAdministratifUniteLegale"] == "A"
        assert result["changementEtatAdministratifUniteLegale"] is False
        assert result["nomUniteLegale"] == "DUPONT"
        assert result["changementNomUniteLegale"] is False
        assert result["nomUsageUniteLegale"] == "MARTIN"
        assert result["changementNomUsageUniteLegale"] is True
        assert result["denominationUniteLegale"] == "SOCIETE DUPONT"
        assert result["changementDenominationUniteLegale"] is False
        assert result["denominationUsuelle1UniteLegale"] == "DUPONT SARL"
        assert result["denominationUsuelle2UniteLegale"] == "DUPONT COMPANY"
        assert result["denominationUsuelle3UniteLegale"] == "DUPONT ENTREPRISE"
        assert result["categorieJuridiqueUniteLegale"] == "5710"
        assert result["changementCategorieJuridiqueUniteLegale"] is False
        assert result["activitePrincipaleUniteLegale"] == "6201Z"
        assert result["nomenclatureActivitePrincipaleUniteLegale"] == "NAFRev2"
        assert result["changementActivitePrincipaleUniteLegale"] is True
        assert result["nicSiegeUniteLegale"] == "00001"
        assert result["changementNicSiegeUniteLegale"] is False
        assert result["economieSocialeSolidaireUniteLegale"] == "O"
        assert result["changementEconomieSocialeSolidaireUniteLegale"] is False
        assert result["societeMissionUniteLegale"] == "N"
        assert result["changementSocieteMissionUniteLegale"] is False
        assert result["caractereEmployeurUniteLegale"] == "O"
        assert result["changementCaractereEmployeurUniteLegale"] is True
        assert result["changementDenominationUsuelleUniteLegale"] is False

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        periode = PeriodeUniteLegale()

        result = periode.to_dict()

        assert "dateFin" not in result
        assert "dateDebut" not in result
        assert "etatAdministratifUniteLegale" not in result
        assert "changementEtatAdministratifUniteLegale" not in result
        assert "nomUniteLegale" not in result
        assert "changementNomUniteLegale" not in result
        assert "nomUsageUniteLegale" not in result
        assert "changementNomUsageUniteLegale" not in result
        assert "denominationUniteLegale" not in result
        assert "changementDenominationUniteLegale" not in result
        assert "denominationUsuelle1UniteLegale" not in result
        assert "denominationUsuelle2UniteLegale" not in result
        assert "denominationUsuelle3UniteLegale" not in result
        assert "categorieJuridiqueUniteLegale" not in result
        assert "changementCategorieJuridiqueUniteLegale" not in result
        assert "activitePrincipaleUniteLegale" not in result
        assert "nomenclatureActivitePrincipaleUniteLegale" not in result
        assert "changementActivitePrincipaleUniteLegale" not in result
        assert "nicSiegeUniteLegale" not in result
        assert "changementNicSiegeUniteLegale" not in result
        assert "economieSocialeSolidaireUniteLegale" not in result
        assert "changementEconomieSocialeSolidaireUniteLegale" not in result
        assert "societeMissionUniteLegale" not in result
        assert "changementSocieteMissionUniteLegale" not in result
        assert "caractereEmployeurUniteLegale" not in result
        assert "changementCaractereEmployeurUniteLegale" not in result
        assert "changementDenominationUsuelleUniteLegale" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "dateFin": "2023-12-31",
            "dateDebut": "2023-01-01",
            "etatAdministratifUniteLegale": "A",
            "changementEtatAdministratifUniteLegale": False,
            "nomUniteLegale": "DUPONT",
            "changementNomUniteLegale": False,
            "nomUsageUniteLegale": "MARTIN",
            "changementNomUsageUniteLegale": True,
            "denominationUniteLegale": "SOCIETE DUPONT",
            "changementDenominationUniteLegale": False,
            "denominationUsuelle1UniteLegale": "DUPONT SARL",
            "denominationUsuelle2UniteLegale": "DUPONT COMPANY",
            "denominationUsuelle3UniteLegale": "DUPONT ENTREPRISE",
            "categorieJuridiqueUniteLegale": "5710",
            "changementCategorieJuridiqueUniteLegale": False,
            "activitePrincipaleUniteLegale": "6201Z",
            "nomenclatureActivitePrincipaleUniteLegale": "NAFRev2",
            "changementActivitePrincipaleUniteLegale": True,
            "nicSiegeUniteLegale": "00001",
            "changementNicSiegeUniteLegale": False,
            "economieSocialeSolidaireUniteLegale": "O",
            "changementEconomieSocialeSolidaireUniteLegale": False,
            "societeMissionUniteLegale": "N",
            "changementSocieteMissionUniteLegale": False,
            "caractereEmployeurUniteLegale": "O",
            "changementCaractereEmployeurUniteLegale": True,
            "changementDenominationUsuelleUniteLegale": False,
        }

        periode = PeriodeUniteLegale.from_dict(data)

        assert periode.date_fin == date(2023, 12, 31)
        assert periode.date_debut == date(2023, 1, 1)
        assert (
            periode.etat_administratif_unite_legale
            == PeriodeUniteLegaleEtatAdministratifUniteLegale.A
        )
        assert periode.changement_etat_administratif_unite_legale is False
        assert periode.nom_unite_legale == "DUPONT"
        assert periode.changement_nom_unite_legale is False
        assert periode.nom_usage_unite_legale == "MARTIN"
        assert periode.changement_nom_usage_unite_legale is True
        assert periode.denomination_unite_legale == "SOCIETE DUPONT"
        assert periode.changement_denomination_unite_legale is False
        assert periode.denomination_usuelle_1_unite_legale == "DUPONT SARL"
        assert periode.denomination_usuelle_2_unite_legale == "DUPONT COMPANY"
        assert periode.denomination_usuelle_3_unite_legale == "DUPONT ENTREPRISE"
        assert periode.categorie_juridique_unite_legale == "5710"
        assert periode.changement_categorie_juridique_unite_legale is False
        assert periode.activite_principale_unite_legale == "6201Z"
        assert (
            periode.nomenclature_activite_principale_unite_legale
            == PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2
        )
        assert periode.changement_activite_principale_unite_legale is True
        assert periode.nic_siege_unite_legale == "00001"
        assert periode.changement_nic_siege_unite_legale is False
        assert periode.economie_sociale_solidaire_unite_legale == "O"
        assert periode.changement_economie_sociale_solidaire_unite_legale is False
        assert periode.societe_mission_unite_legale == "N"
        assert periode.changement_societe_mission_unite_legale is False
        assert (
            periode.caractere_employeur_unite_legale
            == PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI
        )
        assert periode.changement_caractere_employeur_unite_legale is True
        assert periode.changement_denomination_usuelle_unite_legale is False

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "dateDebut": "2023-01-01",
            "etatAdministratifUniteLegale": "A",
        }

        periode = PeriodeUniteLegale.from_dict(data)

        assert periode.date_fin is UNSET
        assert periode.date_debut == date(2023, 1, 1)
        assert (
            periode.etat_administratif_unite_legale
            == PeriodeUniteLegaleEtatAdministratifUniteLegale.A
        )
        assert periode.changement_etat_administratif_unite_legale is UNSET
        assert periode.nom_unite_legale is UNSET
        assert periode.changement_nom_unite_legale is UNSET
        assert periode.nom_usage_unite_legale is UNSET
        assert periode.changement_nom_usage_unite_legale is UNSET
        assert periode.denomination_unite_legale is UNSET
        assert periode.changement_denomination_unite_legale is UNSET
        assert periode.denomination_usuelle_1_unite_legale is UNSET
        assert periode.denomination_usuelle_2_unite_legale is UNSET
        assert periode.denomination_usuelle_3_unite_legale is UNSET
        assert periode.categorie_juridique_unite_legale is UNSET
        assert periode.changement_categorie_juridique_unite_legale is UNSET
        assert periode.activite_principale_unite_legale is UNSET
        assert periode.nomenclature_activite_principale_unite_legale is UNSET
        assert periode.changement_activite_principale_unite_legale is UNSET
        assert periode.nic_siege_unite_legale is UNSET
        assert periode.changement_nic_siege_unite_legale is UNSET
        assert periode.economie_sociale_solidaire_unite_legale is UNSET
        assert periode.changement_economie_sociale_solidaire_unite_legale is UNSET
        assert periode.societe_mission_unite_legale is UNSET
        assert periode.changement_societe_mission_unite_legale is UNSET
        assert periode.caractere_employeur_unite_legale is UNSET
        assert periode.changement_caractere_employeur_unite_legale is UNSET
        assert periode.changement_denomination_usuelle_unite_legale is UNSET

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = PeriodeUniteLegale(
            date_fin=date(2023, 12, 31),
            date_debut=date(2023, 1, 1),
            etat_administratif_unite_legale=PeriodeUniteLegaleEtatAdministratifUniteLegale.A,
            changement_etat_administratif_unite_legale=False,
            nom_unite_legale="DUPONT",
            changement_nom_unite_legale=False,
            nom_usage_unite_legale="MARTIN",
            changement_nom_usage_unite_legale=True,
            denomination_unite_legale="SOCIETE DUPONT",
            changement_denomination_unite_legale=False,
            denomination_usuelle_1_unite_legale="DUPONT SARL",
            denomination_usuelle_2_unite_legale="DUPONT COMPANY",
            denomination_usuelle_3_unite_legale="DUPONT ENTREPRISE",
            categorie_juridique_unite_legale="5710",
            changement_categorie_juridique_unite_legale=False,
            activite_principale_unite_legale="6201Z",
            nomenclature_activite_principale_unite_legale=PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            changement_activite_principale_unite_legale=True,
            nic_siege_unite_legale="00001",
            changement_nic_siege_unite_legale=False,
            economie_sociale_solidaire_unite_legale="O",
            changement_economie_sociale_solidaire_unite_legale=False,
            societe_mission_unite_legale="N",
            changement_societe_mission_unite_legale=False,
            caractere_employeur_unite_legale=PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI,
            changement_caractere_employeur_unite_legale=True,
            changement_denomination_usuelle_unite_legale=False,
        )

        data = original.to_dict()
        restored = PeriodeUniteLegale.from_dict(data)

        assert restored.date_fin == original.date_fin
        assert restored.date_debut == original.date_debut
        assert (
            restored.etat_administratif_unite_legale
            == original.etat_administratif_unite_legale
        )
        assert (
            restored.changement_etat_administratif_unite_legale
            == original.changement_etat_administratif_unite_legale
        )
        assert restored.nom_unite_legale == original.nom_unite_legale
        assert (
            restored.changement_nom_unite_legale == original.changement_nom_unite_legale
        )
        assert restored.nom_usage_unite_legale == original.nom_usage_unite_legale
        assert (
            restored.changement_nom_usage_unite_legale
            == original.changement_nom_usage_unite_legale
        )
        assert restored.denomination_unite_legale == original.denomination_unite_legale
        assert (
            restored.changement_denomination_unite_legale
            == original.changement_denomination_unite_legale
        )
        assert (
            restored.denomination_usuelle_1_unite_legale
            == original.denomination_usuelle_1_unite_legale
        )
        assert (
            restored.denomination_usuelle_2_unite_legale
            == original.denomination_usuelle_2_unite_legale
        )
        assert (
            restored.denomination_usuelle_3_unite_legale
            == original.denomination_usuelle_3_unite_legale
        )
        assert (
            restored.categorie_juridique_unite_legale
            == original.categorie_juridique_unite_legale
        )
        assert (
            restored.changement_categorie_juridique_unite_legale
            == original.changement_categorie_juridique_unite_legale
        )
        assert (
            restored.activite_principale_unite_legale
            == original.activite_principale_unite_legale
        )
        assert (
            restored.nomenclature_activite_principale_unite_legale
            == original.nomenclature_activite_principale_unite_legale
        )
        assert (
            restored.changement_activite_principale_unite_legale
            == original.changement_activite_principale_unite_legale
        )
        assert restored.nic_siege_unite_legale == original.nic_siege_unite_legale
        assert (
            restored.changement_nic_siege_unite_legale
            == original.changement_nic_siege_unite_legale
        )
        assert (
            restored.economie_sociale_solidaire_unite_legale
            == original.economie_sociale_solidaire_unite_legale
        )
        assert (
            restored.changement_economie_sociale_solidaire_unite_legale
            == original.changement_economie_sociale_solidaire_unite_legale
        )
        assert (
            restored.societe_mission_unite_legale
            == original.societe_mission_unite_legale
        )
        assert (
            restored.changement_societe_mission_unite_legale
            == original.changement_societe_mission_unite_legale
        )
        assert (
            restored.caractere_employeur_unite_legale
            == original.caractere_employeur_unite_legale
        )
        assert (
            restored.changement_caractere_employeur_unite_legale
            == original.changement_caractere_employeur_unite_legale
        )
        assert (
            restored.changement_denomination_usuelle_unite_legale
            == original.changement_denomination_usuelle_unite_legale
        )

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        periode = PeriodeUniteLegale()
        periode.additional_properties["extraField"] = "extraValue"

        assert periode["extraField"] == "extraValue"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        periode = PeriodeUniteLegale()
        periode["extraField"] = "extraValue"

        assert periode.additional_properties["extraField"] == "extraValue"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        periode = PeriodeUniteLegale()
        periode.additional_properties["extraField"] = "extraValue"

        del periode["extraField"]

        assert "extraField" not in periode.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        periode = PeriodeUniteLegale()
        periode.additional_properties["extraField"] = "extraValue"

        assert "extraField" in periode
        assert "nonexistentField" not in periode

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        periode = PeriodeUniteLegale()
        periode.additional_properties["field1"] = "value1"
        periode.additional_properties["field2"] = "value2"

        keys = periode.additional_keys
        assert len(keys) == 2
        assert "field1" in keys
        assert "field2" in keys

    def test_enum_field_handling(self):
        """Test handling of enum fields."""
        # Test etat_administratif_unite_legale enum
        etat_values = [
            PeriodeUniteLegaleEtatAdministratifUniteLegale.A,
            PeriodeUniteLegaleEtatAdministratifUniteLegale.C,
        ]

        for enum_value in etat_values:
            periode = PeriodeUniteLegale(etat_administratif_unite_legale=enum_value)

            result = periode.to_dict()
            assert result["etatAdministratifUniteLegale"] == enum_value.value

            # Test deserialization
            restored = PeriodeUniteLegale.from_dict(result)
            assert restored.etat_administratif_unite_legale == enum_value

        # Test caractere_employeur_unite_legale enum
        caractere_values = [
            PeriodeUniteLegaleCaractereEmployeurUniteLegale.OUI,
            PeriodeUniteLegaleCaractereEmployeurUniteLegale.NON,
            PeriodeUniteLegaleCaractereEmployeurUniteLegale.NULL,
        ]

        for enum_value in caractere_values:
            periode = PeriodeUniteLegale(caractere_employeur_unite_legale=enum_value)

            result = periode.to_dict()
            assert result["caractereEmployeurUniteLegale"] == enum_value.value

            # Test deserialization
            restored = PeriodeUniteLegale.from_dict(result)
            assert restored.caractere_employeur_unite_legale == enum_value

        # Test nomenclature_activite_principale_unite_legale enum
        nomenclature_values = [
            PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAP,
            PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV1,
            PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale.NAF1993,
        ]

        for enum_value in nomenclature_values:
            periode = PeriodeUniteLegale(
                nomenclature_activite_principale_unite_legale=enum_value
            )

            result = periode.to_dict()
            assert (
                result["nomenclatureActivitePrincipaleUniteLegale"] == enum_value.value
            )

            # Test deserialization
            restored = PeriodeUniteLegale.from_dict(result)
            assert restored.nomenclature_activite_principale_unite_legale == enum_value

    def test_boolean_field_handling(self):
        """Test handling of boolean fields."""
        periode = PeriodeUniteLegale(
            changement_etat_administratif_unite_legale=True,
            changement_nom_unite_legale=False,
            changement_nom_usage_unite_legale=True,
            changement_denomination_unite_legale=False,
            changement_categorie_juridique_unite_legale=True,
            changement_activite_principale_unite_legale=False,
            changement_nic_siege_unite_legale=True,
            changement_economie_sociale_solidaire_unite_legale=False,
            changement_societe_mission_unite_legale=True,
            changement_caractere_employeur_unite_legale=False,
            changement_denomination_usuelle_unite_legale=True,
        )

        result = periode.to_dict()

        assert result["changementEtatAdministratifUniteLegale"] is True
        assert result["changementNomUniteLegale"] is False
        assert result["changementNomUsageUniteLegale"] is True
        assert result["changementDenominationUniteLegale"] is False
        assert result["changementCategorieJuridiqueUniteLegale"] is True
        assert result["changementActivitePrincipaleUniteLegale"] is False
        assert result["changementNicSiegeUniteLegale"] is True
        assert result["changementEconomieSocialeSolidaireUniteLegale"] is False
        assert result["changementSocieteMissionUniteLegale"] is True
        assert result["changementCaractereEmployeurUniteLegale"] is False
        assert result["changementDenominationUsuelleUniteLegale"] is True

        # Test deserialization
        restored = PeriodeUniteLegale.from_dict(result)

        assert restored.changement_etat_administratif_unite_legale is True
        assert restored.changement_nom_unite_legale is False
        assert restored.changement_nom_usage_unite_legale is True
        assert restored.changement_denomination_unite_legale is False
        assert restored.changement_categorie_juridique_unite_legale is True
        assert restored.changement_activite_principale_unite_legale is False
        assert restored.changement_nic_siege_unite_legale is True
        assert restored.changement_economie_sociale_solidaire_unite_legale is False
        assert restored.changement_societe_mission_unite_legale is True
        assert restored.changement_caractere_employeur_unite_legale is False
        assert restored.changement_denomination_usuelle_unite_legale is True

    def test_date_field_handling(self):
        """Test handling of date fields."""
        periode = PeriodeUniteLegale(
            date_debut=date(2023, 1, 1),
            date_fin=date(2023, 12, 31),
        )

        result = periode.to_dict()

        assert result["dateDebut"] == "2023-01-01"
        assert result["dateFin"] == "2023-12-31"

        # Test deserialization
        restored = PeriodeUniteLegale.from_dict(result)

        assert restored.date_debut == date(2023, 1, 1)
        assert restored.date_fin == date(2023, 12, 31)

    def test_string_field_handling(self):
        """Test handling of string fields."""
        periode = PeriodeUniteLegale(
            nom_unite_legale="DUPONT",
            nom_usage_unite_legale="MARTIN",
            denomination_unite_legale="SOCIETE DUPONT",
            denomination_usuelle_1_unite_legale="DUPONT SARL",
            denomination_usuelle_2_unite_legale="DUPONT COMPANY",
            denomination_usuelle_3_unite_legale="DUPONT ENTREPRISE",
            categorie_juridique_unite_legale="5710",
            activite_principale_unite_legale="6201Z",
            nic_siege_unite_legale="00001",
            economie_sociale_solidaire_unite_legale="O",
            societe_mission_unite_legale="N",
        )

        result = periode.to_dict()

        assert result["nomUniteLegale"] == "DUPONT"
        assert result["nomUsageUniteLegale"] == "MARTIN"
        assert result["denominationUniteLegale"] == "SOCIETE DUPONT"
        assert result["denominationUsuelle1UniteLegale"] == "DUPONT SARL"
        assert result["denominationUsuelle2UniteLegale"] == "DUPONT COMPANY"
        assert result["denominationUsuelle3UniteLegale"] == "DUPONT ENTREPRISE"
        assert result["categorieJuridiqueUniteLegale"] == "5710"
        assert result["activitePrincipaleUniteLegale"] == "6201Z"
        assert result["nicSiegeUniteLegale"] == "00001"
        assert result["economieSocialeSolidaireUniteLegale"] == "O"
        assert result["societeMissionUniteLegale"] == "N"

        # Test deserialization
        restored = PeriodeUniteLegale.from_dict(result)

        assert restored.nom_unite_legale == "DUPONT"
        assert restored.nom_usage_unite_legale == "MARTIN"
        assert restored.denomination_unite_legale == "SOCIETE DUPONT"
        assert restored.denomination_usuelle_1_unite_legale == "DUPONT SARL"
        assert restored.denomination_usuelle_2_unite_legale == "DUPONT COMPANY"
        assert restored.denomination_usuelle_3_unite_legale == "DUPONT ENTREPRISE"
        assert restored.categorie_juridique_unite_legale == "5710"
        assert restored.activite_principale_unite_legale == "6201Z"
        assert restored.nic_siege_unite_legale == "00001"
        assert restored.economie_sociale_solidaire_unite_legale == "O"
        assert restored.societe_mission_unite_legale == "N"

    def test_unicode_handling(self):
        """Test handling of unicode characters in string fields."""
        periode = PeriodeUniteLegale(
            nom_unite_legale="DUPONT",
            nom_usage_unite_legale="MARTIN",
            denomination_unite_legale="Société Française",
            denomination_usuelle_1_unite_legale="Café & Restaurant",
            denomination_usuelle_2_unite_legale="Établissement Français",
            denomination_usuelle_3_unite_legale="Société à Responsabilité Limitée",
        )

        result = periode.to_dict()

        assert result["nomUniteLegale"] == "DUPONT"
        assert result["nomUsageUniteLegale"] == "MARTIN"
        assert result["denominationUniteLegale"] == "Société Française"
        assert result["denominationUsuelle1UniteLegale"] == "Café & Restaurant"
        assert result["denominationUsuelle2UniteLegale"] == "Établissement Français"
        assert (
            result["denominationUsuelle3UniteLegale"]
            == "Société à Responsabilité Limitée"
        )

        # Test deserialization
        restored = PeriodeUniteLegale.from_dict(result)

        assert restored.nom_unite_legale == "DUPONT"
        assert restored.nom_usage_unite_legale == "MARTIN"
        assert restored.denomination_unite_legale == "Société Française"
        assert restored.denomination_usuelle_1_unite_legale == "Café & Restaurant"
        assert restored.denomination_usuelle_2_unite_legale == "Établissement Français"
        assert (
            restored.denomination_usuelle_3_unite_legale
            == "Société à Responsabilité Limitée"
        )

    def test_empty_strings_vs_unset(self):
        """Test distinction between empty strings and UNSET."""
        periode = PeriodeUniteLegale(
            nom_unite_legale="",
            nom_usage_unite_legale="NON_UNSET",
        )

        result = periode.to_dict()

        assert result["nomUniteLegale"] == ""
        assert result["nomUsageUniteLegale"] == "NON_UNSET"
        assert "denominationUniteLegale" not in result  # UNSET field

        # Test deserialization
        restored = PeriodeUniteLegale.from_dict(result)

        assert restored.nom_unite_legale == ""
        assert restored.nom_usage_unite_legale == "NON_UNSET"
        assert restored.denomination_unite_legale is UNSET
