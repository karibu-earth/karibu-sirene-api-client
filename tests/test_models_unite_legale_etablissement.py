"""Tests for sirene_api_client.models.unite_legale_etablissement module."""

import datetime

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.unite_legale_etablissement import UniteLegaleEtablissement
from sirene_api_client.models.unite_legale_etablissement_caractere_employeur_unite_legale import (
    UniteLegaleEtablissementCaractereEmployeurUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_categorie_entreprise import (
    UniteLegaleEtablissementCategorieEntreprise,
)
from sirene_api_client.models.unite_legale_etablissement_etat_administratif_unite_legale import (
    UniteLegaleEtablissementEtatAdministratifUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_nomenclature_activite_principale_unite_legale import (
    UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_sexe_unite_legale import (
    UniteLegaleEtablissementSexeUniteLegale,
)


@pytest.mark.requirement("REQ-MODEL-003")
class TestUniteLegaleEtablissement:
    """Test UniteLegaleEtablissement model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            unite_purgee_unite_legale=False,
            date_creation_unite_legale=datetime.date(2020, 1, 1),
            date_naissance_unite_legale="1990-01-01",
            code_commune_naissance_unite_legale="75001",
            code_pays_naissance_unite_legale="FR",
            libelle_nationalite_unite_legale="Française",
            identifiant_association_unite_legale="W123456789",
            tranche_effectifs_unite_legale="00",
            annee_effectifs_unite_legale="2020",
            date_dernier_traitement_unite_legale="2023-01-01",
            categorie_entreprise=UniteLegaleEtablissementCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleEtablissementSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
            etat_administratif_unite_legale=UniteLegaleEtablissementEtatAdministratifUniteLegale.A,
            nom_unite_legale="Dupont",
            denomination_unite_legale="Société Dupont",
            denomination_usuelle_1_unite_legale="Dupont SA",
            denomination_usuelle_2_unite_legale="Dupont Corp",
            denomination_usuelle_3_unite_legale="Dupont Ltd",
            activite_principale_unite_legale="6201Z",
            categorie_juridique_unite_legale="5710",
            nic_siege_unite_legale="00001",
            nomenclature_activite_principale_unite_legale=UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            nom_usage_unite_legale="Martin",
            economie_sociale_solidaire_unite_legale="O",
            societe_mission_unite_legale="N",
            caractere_employeur_unite_legale=UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI,
        )

        assert unite_legale_etablissement.statut_diffusion_unite_legale == "O"
        assert unite_legale_etablissement.unite_purgee_unite_legale is False
        assert unite_legale_etablissement.date_creation_unite_legale == datetime.date(
            2020, 1, 1
        )
        assert unite_legale_etablissement.date_naissance_unite_legale == "1990-01-01"
        assert unite_legale_etablissement.code_commune_naissance_unite_legale == "75001"
        assert unite_legale_etablissement.code_pays_naissance_unite_legale == "FR"
        assert (
            unite_legale_etablissement.libelle_nationalite_unite_legale == "Française"
        )
        assert (
            unite_legale_etablissement.identifiant_association_unite_legale
            == "W123456789"
        )
        assert unite_legale_etablissement.tranche_effectifs_unite_legale == "00"
        assert unite_legale_etablissement.annee_effectifs_unite_legale == "2020"
        assert (
            unite_legale_etablissement.date_dernier_traitement_unite_legale
            == "2023-01-01"
        )
        assert (
            unite_legale_etablissement.categorie_entreprise
            == UniteLegaleEtablissementCategorieEntreprise.GE
        )
        assert unite_legale_etablissement.annee_categorie_entreprise == "2020"
        assert unite_legale_etablissement.sigle_unite_legale == "SNCF"
        assert (
            unite_legale_etablissement.sexe_unite_legale
            == UniteLegaleEtablissementSexeUniteLegale.M
        )
        assert unite_legale_etablissement.prenom_1_unite_legale == "Jean"
        assert unite_legale_etablissement.prenom_2_unite_legale == "Pierre"
        assert unite_legale_etablissement.prenom_3_unite_legale == "Marie"
        assert unite_legale_etablissement.prenom_4_unite_legale == "Anne"
        assert unite_legale_etablissement.prenom_usuel_unite_legale == "Jean"
        assert unite_legale_etablissement.pseudonyme_unite_legale == "JP"
        assert (
            unite_legale_etablissement.etat_administratif_unite_legale
            == UniteLegaleEtablissementEtatAdministratifUniteLegale.A
        )
        assert unite_legale_etablissement.nom_unite_legale == "Dupont"
        assert unite_legale_etablissement.denomination_unite_legale == "Société Dupont"
        assert (
            unite_legale_etablissement.denomination_usuelle_1_unite_legale
            == "Dupont SA"
        )
        assert (
            unite_legale_etablissement.denomination_usuelle_2_unite_legale
            == "Dupont Corp"
        )
        assert (
            unite_legale_etablissement.denomination_usuelle_3_unite_legale
            == "Dupont Ltd"
        )
        assert unite_legale_etablissement.activite_principale_unite_legale == "6201Z"
        assert unite_legale_etablissement.categorie_juridique_unite_legale == "5710"
        assert unite_legale_etablissement.nic_siege_unite_legale == "00001"
        assert (
            unite_legale_etablissement.nomenclature_activite_principale_unite_legale
            == UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2
        )
        assert unite_legale_etablissement.nom_usage_unite_legale == "Martin"
        assert unite_legale_etablissement.economie_sociale_solidaire_unite_legale == "O"
        assert unite_legale_etablissement.societe_mission_unite_legale == "N"
        assert (
            unite_legale_etablissement.caractere_employeur_unite_legale
            == UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI
        )

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        unite_legale_etablissement = UniteLegaleEtablissement()

        assert unite_legale_etablissement.statut_diffusion_unite_legale is UNSET
        assert unite_legale_etablissement.unite_purgee_unite_legale is UNSET
        assert unite_legale_etablissement.date_creation_unite_legale is UNSET
        assert unite_legale_etablissement.date_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.code_commune_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.code_pays_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.libelle_nationalite_unite_legale is UNSET
        assert unite_legale_etablissement.identifiant_association_unite_legale is UNSET
        assert unite_legale_etablissement.tranche_effectifs_unite_legale is UNSET
        assert unite_legale_etablissement.annee_effectifs_unite_legale is UNSET
        assert unite_legale_etablissement.date_dernier_traitement_unite_legale is UNSET
        assert unite_legale_etablissement.categorie_entreprise is UNSET
        assert unite_legale_etablissement.annee_categorie_entreprise is UNSET
        assert unite_legale_etablissement.sigle_unite_legale is UNSET
        assert unite_legale_etablissement.sexe_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_1_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_2_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_3_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_4_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_usuel_unite_legale is UNSET
        assert unite_legale_etablissement.pseudonyme_unite_legale is UNSET
        assert unite_legale_etablissement.etat_administratif_unite_legale is UNSET
        assert unite_legale_etablissement.nom_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_1_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_2_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_3_unite_legale is UNSET
        assert unite_legale_etablissement.activite_principale_unite_legale is UNSET
        assert unite_legale_etablissement.categorie_juridique_unite_legale is UNSET
        assert unite_legale_etablissement.nic_siege_unite_legale is UNSET
        assert (
            unite_legale_etablissement.nomenclature_activite_principale_unite_legale
            is UNSET
        )
        assert unite_legale_etablissement.nom_usage_unite_legale is UNSET
        assert (
            unite_legale_etablissement.economie_sociale_solidaire_unite_legale is UNSET
        )
        assert unite_legale_etablissement.societe_mission_unite_legale is UNSET
        assert unite_legale_etablissement.caractere_employeur_unite_legale is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            unite_purgee_unite_legale=False,
            date_creation_unite_legale=datetime.date(2020, 1, 1),
            date_naissance_unite_legale="1990-01-01",
            code_commune_naissance_unite_legale="75001",
            code_pays_naissance_unite_legale="FR",
            libelle_nationalite_unite_legale="Française",
            identifiant_association_unite_legale="W123456789",
            tranche_effectifs_unite_legale="00",
            annee_effectifs_unite_legale="2020",
            date_dernier_traitement_unite_legale="2023-01-01",
            categorie_entreprise=UniteLegaleEtablissementCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleEtablissementSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
            etat_administratif_unite_legale=UniteLegaleEtablissementEtatAdministratifUniteLegale.A,
            nom_unite_legale="Dupont",
            denomination_unite_legale="Société Dupont",
            denomination_usuelle_1_unite_legale="Dupont SA",
            denomination_usuelle_2_unite_legale="Dupont Corp",
            denomination_usuelle_3_unite_legale="Dupont Ltd",
            activite_principale_unite_legale="6201Z",
            categorie_juridique_unite_legale="5710",
            nic_siege_unite_legale="00001",
            nomenclature_activite_principale_unite_legale=UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            nom_usage_unite_legale="Martin",
            economie_sociale_solidaire_unite_legale="O",
            societe_mission_unite_legale="N",
            caractere_employeur_unite_legale=UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI,
        )

        result = unite_legale_etablissement.to_dict()

        assert result["statutDiffusionUniteLegale"] == "O"
        assert result["unitePurgeeUniteLegale"] is False
        assert result["dateCreationUniteLegale"] == "2020-01-01"
        assert result["dateNaissanceUniteLegale"] == "1990-01-01"
        assert result["codeCommuneNaissanceUniteLegale"] == "75001"
        assert result["codePaysNaissanceUniteLegale"] == "FR"
        assert result["libelleNationaliteUniteLegale"] == "Française"
        assert result["identifiantAssociationUniteLegale"] == "W123456789"
        assert result["trancheEffectifsUniteLegale"] == "00"
        assert result["anneeEffectifsUniteLegale"] == "2020"
        assert result["dateDernierTraitementUniteLegale"] == "2023-01-01"
        assert result["categorieEntreprise"] == "GE"
        assert result["anneeCategorieEntreprise"] == "2020"
        assert result["sigleUniteLegale"] == "SNCF"
        assert result["sexeUniteLegale"] == "M"
        assert result["prenom1UniteLegale"] == "Jean"
        assert result["prenom2UniteLegale"] == "Pierre"
        assert result["prenom3UniteLegale"] == "Marie"
        assert result["prenom4UniteLegale"] == "Anne"
        assert result["prenomUsuelUniteLegale"] == "Jean"
        assert result["pseudonymeUniteLegale"] == "JP"
        assert result["etatAdministratifUniteLegale"] == "A"
        assert result["nomUniteLegale"] == "Dupont"
        assert result["denominationUniteLegale"] == "Société Dupont"
        assert result["denominationUsuelle1UniteLegale"] == "Dupont SA"
        assert result["denominationUsuelle2UniteLegale"] == "Dupont Corp"
        assert result["denominationUsuelle3UniteLegale"] == "Dupont Ltd"
        assert result["activitePrincipaleUniteLegale"] == "6201Z"
        assert result["categorieJuridiqueUniteLegale"] == "5710"
        assert result["nicSiegeUniteLegale"] == "00001"
        assert result["nomenclatureActivitePrincipaleUniteLegale"] == "NAFRev2"
        assert result["nomUsageUniteLegale"] == "Martin"
        assert result["economieSocialeSolidaireUniteLegale"] == "O"
        assert result["societeMissionUniteLegale"] == "N"
        assert result["caractereEmployeurUniteLegale"] == "O"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",  # Only set one field
        )

        result = unite_legale_etablissement.to_dict()

        assert result["statutDiffusionUniteLegale"] == "O"
        assert "unitePurgeeUniteLegale" not in result
        assert "dateCreationUniteLegale" not in result
        assert "dateNaissanceUniteLegale" not in result
        assert "codeCommuneNaissanceUniteLegale" not in result
        assert "codePaysNaissanceUniteLegale" not in result
        assert "libelleNationaliteUniteLegale" not in result
        assert "identifiantAssociationUniteLegale" not in result
        assert "trancheEffectifsUniteLegale" not in result
        assert "anneeEffectifsUniteLegale" not in result
        assert "dateDernierTraitementUniteLegale" not in result
        assert "categorieEntreprise" not in result
        assert "anneeCategorieEntreprise" not in result
        assert "sigleUniteLegale" not in result
        assert "sexeUniteLegale" not in result
        assert "prenom1UniteLegale" not in result
        assert "prenom2UniteLegale" not in result
        assert "prenom3UniteLegale" not in result
        assert "prenom4UniteLegale" not in result
        assert "prenomUsuelUniteLegale" not in result
        assert "pseudonymeUniteLegale" not in result
        assert "etatAdministratifUniteLegale" not in result
        assert "nomUniteLegale" not in result
        assert "denominationUniteLegale" not in result
        assert "denominationUsuelle1UniteLegale" not in result
        assert "denominationUsuelle2UniteLegale" not in result
        assert "denominationUsuelle3UniteLegale" not in result
        assert "activitePrincipaleUniteLegale" not in result
        assert "categorieJuridiqueUniteLegale" not in result
        assert "nicSiegeUniteLegale" not in result
        assert "nomenclatureActivitePrincipaleUniteLegale" not in result
        assert "nomUsageUniteLegale" not in result
        assert "economieSocialeSolidaireUniteLegale" not in result
        assert "societeMissionUniteLegale" not in result
        assert "caractereEmployeurUniteLegale" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "statutDiffusionUniteLegale": "O",
            "unitePurgeeUniteLegale": False,
            "dateCreationUniteLegale": "2020-01-01",
            "dateNaissanceUniteLegale": "1990-01-01",
            "codeCommuneNaissanceUniteLegale": "75001",
            "codePaysNaissanceUniteLegale": "FR",
            "libelleNationaliteUniteLegale": "Française",
            "identifiantAssociationUniteLegale": "W123456789",
            "trancheEffectifsUniteLegale": "00",
            "anneeEffectifsUniteLegale": "2020",
            "dateDernierTraitementUniteLegale": "2023-01-01",
            "categorieEntreprise": "GE",
            "anneeCategorieEntreprise": "2020",
            "sigleUniteLegale": "SNCF",
            "sexeUniteLegale": "M",
            "prenom1UniteLegale": "Jean",
            "prenom2UniteLegale": "Pierre",
            "prenom3UniteLegale": "Marie",
            "prenom4UniteLegale": "Anne",
            "prenomUsuelUniteLegale": "Jean",
            "pseudonymeUniteLegale": "JP",
            "etatAdministratifUniteLegale": "A",
            "nomUniteLegale": "Dupont",
            "denominationUniteLegale": "Société Dupont",
            "denominationUsuelle1UniteLegale": "Dupont SA",
            "denominationUsuelle2UniteLegale": "Dupont Corp",
            "denominationUsuelle3UniteLegale": "Dupont Ltd",
            "activitePrincipaleUniteLegale": "6201Z",
            "categorieJuridiqueUniteLegale": "5710",
            "nicSiegeUniteLegale": "00001",
            "nomenclatureActivitePrincipaleUniteLegale": "NAFRev2",
            "nomUsageUniteLegale": "Martin",
            "economieSocialeSolidaireUniteLegale": "O",
            "societeMissionUniteLegale": "N",
            "caractereEmployeurUniteLegale": "O",
        }

        unite_legale_etablissement = UniteLegaleEtablissement.from_dict(data)

        assert unite_legale_etablissement.statut_diffusion_unite_legale == "O"
        assert unite_legale_etablissement.unite_purgee_unite_legale is False
        assert unite_legale_etablissement.date_creation_unite_legale == datetime.date(
            2020, 1, 1
        )
        assert unite_legale_etablissement.date_naissance_unite_legale == "1990-01-01"
        assert unite_legale_etablissement.code_commune_naissance_unite_legale == "75001"
        assert unite_legale_etablissement.code_pays_naissance_unite_legale == "FR"
        assert (
            unite_legale_etablissement.libelle_nationalite_unite_legale == "Française"
        )
        assert (
            unite_legale_etablissement.identifiant_association_unite_legale
            == "W123456789"
        )
        assert unite_legale_etablissement.tranche_effectifs_unite_legale == "00"
        assert unite_legale_etablissement.annee_effectifs_unite_legale == "2020"
        assert (
            unite_legale_etablissement.date_dernier_traitement_unite_legale
            == "2023-01-01"
        )
        assert (
            unite_legale_etablissement.categorie_entreprise
            == UniteLegaleEtablissementCategorieEntreprise.GE
        )
        assert unite_legale_etablissement.annee_categorie_entreprise == "2020"
        assert unite_legale_etablissement.sigle_unite_legale == "SNCF"
        assert (
            unite_legale_etablissement.sexe_unite_legale
            == UniteLegaleEtablissementSexeUniteLegale.M
        )
        assert unite_legale_etablissement.prenom_1_unite_legale == "Jean"
        assert unite_legale_etablissement.prenom_2_unite_legale == "Pierre"
        assert unite_legale_etablissement.prenom_3_unite_legale == "Marie"
        assert unite_legale_etablissement.prenom_4_unite_legale == "Anne"
        assert unite_legale_etablissement.prenom_usuel_unite_legale == "Jean"
        assert unite_legale_etablissement.pseudonyme_unite_legale == "JP"
        assert (
            unite_legale_etablissement.etat_administratif_unite_legale
            == UniteLegaleEtablissementEtatAdministratifUniteLegale.A
        )
        assert unite_legale_etablissement.nom_unite_legale == "Dupont"
        assert unite_legale_etablissement.denomination_unite_legale == "Société Dupont"
        assert (
            unite_legale_etablissement.denomination_usuelle_1_unite_legale
            == "Dupont SA"
        )
        assert (
            unite_legale_etablissement.denomination_usuelle_2_unite_legale
            == "Dupont Corp"
        )
        assert (
            unite_legale_etablissement.denomination_usuelle_3_unite_legale
            == "Dupont Ltd"
        )
        assert unite_legale_etablissement.activite_principale_unite_legale == "6201Z"
        assert unite_legale_etablissement.categorie_juridique_unite_legale == "5710"
        assert unite_legale_etablissement.nic_siege_unite_legale == "00001"
        assert (
            unite_legale_etablissement.nomenclature_activite_principale_unite_legale
            == UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2
        )
        assert unite_legale_etablissement.nom_usage_unite_legale == "Martin"
        assert unite_legale_etablissement.economie_sociale_solidaire_unite_legale == "O"
        assert unite_legale_etablissement.societe_mission_unite_legale == "N"
        assert (
            unite_legale_etablissement.caractere_employeur_unite_legale
            == UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI
        )

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "statutDiffusionUniteLegale": "O",  # Only required field
        }

        unite_legale_etablissement = UniteLegaleEtablissement.from_dict(data)

        assert unite_legale_etablissement.statut_diffusion_unite_legale == "O"
        assert unite_legale_etablissement.unite_purgee_unite_legale is UNSET
        assert unite_legale_etablissement.date_creation_unite_legale is UNSET
        assert unite_legale_etablissement.date_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.code_commune_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.code_pays_naissance_unite_legale is UNSET
        assert unite_legale_etablissement.libelle_nationalite_unite_legale is UNSET
        assert unite_legale_etablissement.identifiant_association_unite_legale is UNSET
        assert unite_legale_etablissement.tranche_effectifs_unite_legale is UNSET
        assert unite_legale_etablissement.annee_effectifs_unite_legale is UNSET
        assert unite_legale_etablissement.date_dernier_traitement_unite_legale is UNSET
        assert unite_legale_etablissement.categorie_entreprise is UNSET
        assert unite_legale_etablissement.annee_categorie_entreprise is UNSET
        assert unite_legale_etablissement.sigle_unite_legale is UNSET
        assert unite_legale_etablissement.sexe_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_1_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_2_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_3_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_4_unite_legale is UNSET
        assert unite_legale_etablissement.prenom_usuel_unite_legale is UNSET
        assert unite_legale_etablissement.pseudonyme_unite_legale is UNSET
        assert unite_legale_etablissement.etat_administratif_unite_legale is UNSET
        assert unite_legale_etablissement.nom_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_1_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_2_unite_legale is UNSET
        assert unite_legale_etablissement.denomination_usuelle_3_unite_legale is UNSET
        assert unite_legale_etablissement.activite_principale_unite_legale is UNSET
        assert unite_legale_etablissement.categorie_juridique_unite_legale is UNSET
        assert unite_legale_etablissement.nic_siege_unite_legale is UNSET
        assert (
            unite_legale_etablissement.nomenclature_activite_principale_unite_legale
            is UNSET
        )
        assert unite_legale_etablissement.nom_usage_unite_legale is UNSET
        assert (
            unite_legale_etablissement.economie_sociale_solidaire_unite_legale is UNSET
        )
        assert unite_legale_etablissement.societe_mission_unite_legale is UNSET
        assert unite_legale_etablissement.caractere_employeur_unite_legale is UNSET

    def test_from_dict_with_null_values(self):
        """Test from_dict with null values."""
        data = {
            "statutDiffusionUniteLegale": "O",
            "dateNaissanceUniteLegale": None,
            "identifiantAssociationUniteLegale": None,
            "prenom1UniteLegale": None,
            "prenom2UniteLegale": None,
            "prenom3UniteLegale": None,
            "prenom4UniteLegale": None,
            "prenomUsuelUniteLegale": None,
            "pseudonymeUniteLegale": None,
        }

        unite_legale_etablissement = UniteLegaleEtablissement.from_dict(data)

        assert unite_legale_etablissement.statut_diffusion_unite_legale == "O"
        assert unite_legale_etablissement.date_creation_unite_legale is UNSET
        assert unite_legale_etablissement.date_naissance_unite_legale is None
        assert unite_legale_etablissement.identifiant_association_unite_legale is None
        assert unite_legale_etablissement.prenom_1_unite_legale is None
        assert unite_legale_etablissement.prenom_2_unite_legale is None
        assert unite_legale_etablissement.prenom_3_unite_legale is None
        assert unite_legale_etablissement.prenom_4_unite_legale is None
        assert unite_legale_etablissement.prenom_usuel_unite_legale is None
        assert unite_legale_etablissement.pseudonyme_unite_legale is None

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            unite_purgee_unite_legale=False,
            date_creation_unite_legale=datetime.date(2020, 1, 1),
            date_naissance_unite_legale="1990-01-01",
            code_commune_naissance_unite_legale="75001",
            code_pays_naissance_unite_legale="FR",
            libelle_nationalite_unite_legale="Française",
            identifiant_association_unite_legale="W123456789",
            tranche_effectifs_unite_legale="00",
            annee_effectifs_unite_legale="2020",
            date_dernier_traitement_unite_legale="2023-01-01",
            categorie_entreprise=UniteLegaleEtablissementCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleEtablissementSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
            etat_administratif_unite_legale=UniteLegaleEtablissementEtatAdministratifUniteLegale.A,
            nom_unite_legale="Dupont",
            denomination_unite_legale="Société Dupont",
            denomination_usuelle_1_unite_legale="Dupont SA",
            denomination_usuelle_2_unite_legale="Dupont Corp",
            denomination_usuelle_3_unite_legale="Dupont Ltd",
            activite_principale_unite_legale="6201Z",
            categorie_juridique_unite_legale="5710",
            nic_siege_unite_legale="00001",
            nomenclature_activite_principale_unite_legale=UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
            nom_usage_unite_legale="Martin",
            economie_sociale_solidaire_unite_legale="O",
            societe_mission_unite_legale="N",
            caractere_employeur_unite_legale=UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI,
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = UniteLegaleEtablissement.from_dict(data)

        # Verify all fields are preserved
        assert (
            restored.statut_diffusion_unite_legale
            == original.statut_diffusion_unite_legale
        )
        assert restored.unite_purgee_unite_legale == original.unite_purgee_unite_legale
        assert (
            restored.date_creation_unite_legale == original.date_creation_unite_legale
        )
        assert (
            restored.date_naissance_unite_legale == original.date_naissance_unite_legale
        )
        assert (
            restored.code_commune_naissance_unite_legale
            == original.code_commune_naissance_unite_legale
        )
        assert (
            restored.code_pays_naissance_unite_legale
            == original.code_pays_naissance_unite_legale
        )
        assert (
            restored.libelle_nationalite_unite_legale
            == original.libelle_nationalite_unite_legale
        )
        assert (
            restored.identifiant_association_unite_legale
            == original.identifiant_association_unite_legale
        )
        assert (
            restored.tranche_effectifs_unite_legale
            == original.tranche_effectifs_unite_legale
        )
        assert (
            restored.annee_effectifs_unite_legale
            == original.annee_effectifs_unite_legale
        )
        assert (
            restored.date_dernier_traitement_unite_legale
            == original.date_dernier_traitement_unite_legale
        )
        assert restored.categorie_entreprise == original.categorie_entreprise
        assert (
            restored.annee_categorie_entreprise == original.annee_categorie_entreprise
        )
        assert restored.sigle_unite_legale == original.sigle_unite_legale
        assert restored.sexe_unite_legale == original.sexe_unite_legale
        assert restored.prenom_1_unite_legale == original.prenom_1_unite_legale
        assert restored.prenom_2_unite_legale == original.prenom_2_unite_legale
        assert restored.prenom_3_unite_legale == original.prenom_3_unite_legale
        assert restored.prenom_4_unite_legale == original.prenom_4_unite_legale
        assert restored.prenom_usuel_unite_legale == original.prenom_usuel_unite_legale
        assert restored.pseudonyme_unite_legale == original.pseudonyme_unite_legale
        assert (
            restored.etat_administratif_unite_legale
            == original.etat_administratif_unite_legale
        )
        assert restored.nom_unite_legale == original.nom_unite_legale
        assert restored.denomination_unite_legale == original.denomination_unite_legale
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
            restored.activite_principale_unite_legale
            == original.activite_principale_unite_legale
        )
        assert (
            restored.categorie_juridique_unite_legale
            == original.categorie_juridique_unite_legale
        )
        assert restored.nic_siege_unite_legale == original.nic_siege_unite_legale
        assert (
            restored.nomenclature_activite_principale_unite_legale
            == original.nomenclature_activite_principale_unite_legale
        )
        assert restored.nom_usage_unite_legale == original.nom_usage_unite_legale
        assert (
            restored.economie_sociale_solidaire_unite_legale
            == original.economie_sociale_solidaire_unite_legale
        )
        assert (
            restored.societe_mission_unite_legale
            == original.societe_mission_unite_legale
        )
        assert (
            restored.caractere_employeur_unite_legale
            == original.caractere_employeur_unite_legale
        )
        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        unite_legale_etablissement = UniteLegaleEtablissement()
        unite_legale_etablissement["custom_field"] = "custom_value"

        assert unite_legale_etablissement["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        unite_legale_etablissement = UniteLegaleEtablissement()
        unite_legale_etablissement["custom_field"] = "custom_value"

        assert (
            unite_legale_etablissement.additional_properties["custom_field"]
            == "custom_value"
        )

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        unite_legale_etablissement = UniteLegaleEtablissement()
        unite_legale_etablissement["custom_field"] = "custom_value"

        del unite_legale_etablissement["custom_field"]

        assert "custom_field" not in unite_legale_etablissement.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        unite_legale_etablissement = UniteLegaleEtablissement()
        unite_legale_etablissement["custom_field"] = "custom_value"

        assert "custom_field" in unite_legale_etablissement
        assert "nonexistent_field" not in unite_legale_etablissement

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        unite_legale_etablissement = UniteLegaleEtablissement()
        unite_legale_etablissement["field1"] = "value1"
        unite_legale_etablissement["field2"] = "value2"

        keys = unite_legale_etablissement.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            libelle_nationalite_unite_legale="Française",
            prenom_1_unite_legale="José",
            denomination_unite_legale="Société & Cie",
        )
        unite_legale_etablissement["unicode_field"] = "Café & Société 🏢"

        result = unite_legale_etablissement.to_dict()
        assert result["libelleNationaliteUniteLegale"] == "Française"
        assert result["prenom1UniteLegale"] == "José"
        assert result["denominationUniteLegale"] == "Société & Cie"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = UniteLegaleEtablissement.from_dict(result)
        assert restored.libelle_nationalite_unite_legale == "Française"
        assert restored.prenom_1_unite_legale == "José"
        assert restored.denomination_unite_legale == "Société & Cie"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            sigle_unite_legale="",  # Empty string
            prenom_1_unite_legale=UNSET,  # UNSET
        )

        result = unite_legale_etablissement.to_dict()
        assert result["statutDiffusionUniteLegale"] == "O"
        assert result["sigleUniteLegale"] == ""
        assert "prenom1UniteLegale" not in result  # UNSET should be excluded

    def test_boolean_field_handling(self):
        """Test boolean field handling."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            unite_purgee_unite_legale=True,
        )

        result = unite_legale_etablissement.to_dict()
        assert result["unitePurgeeUniteLegale"] is True

        # Test False
        unite_legale_etablissement.unite_purgee_unite_legale = False
        result = unite_legale_etablissement.to_dict()
        assert result["unitePurgeeUniteLegale"] is False

    def test_date_field_parsing(self):
        """Test date field parsing."""
        data = {
            "statutDiffusionUniteLegale": "O",
            "dateCreationUniteLegale": "2020-01-01",
        }

        unite_legale_etablissement = UniteLegaleEtablissement.from_dict(data)

        assert unite_legale_etablissement.date_creation_unite_legale == datetime.date(
            2020, 1, 1
        )

    def test_enum_field_handling(self):
        """Test enum field handling."""
        unite_legale_etablissement = UniteLegaleEtablissement(
            statut_diffusion_unite_legale="O",
            categorie_entreprise=UniteLegaleEtablissementCategorieEntreprise.GE,
            sexe_unite_legale=UniteLegaleEtablissementSexeUniteLegale.M,
            etat_administratif_unite_legale=UniteLegaleEtablissementEtatAdministratifUniteLegale.A,
            caractere_employeur_unite_legale=UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI,
            nomenclature_activite_principale_unite_legale=UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2,
        )

        result = unite_legale_etablissement.to_dict()
        assert result["categorieEntreprise"] == "GE"
        assert result["sexeUniteLegale"] == "M"
        assert result["etatAdministratifUniteLegale"] == "A"
        assert result["caractereEmployeurUniteLegale"] == "O"
        assert result["nomenclatureActivitePrincipaleUniteLegale"] == "NAFRev2"

        # Test deserialization
        data = {
            "statutDiffusionUniteLegale": "O",
            "categorieEntreprise": "GE",
            "sexeUniteLegale": "M",
            "etatAdministratifUniteLegale": "A",
            "caractereEmployeurUniteLegale": "O",
            "nomenclatureActivitePrincipaleUniteLegale": "NAFRev2",
        }

        restored = UniteLegaleEtablissement.from_dict(data)
        assert (
            restored.categorie_entreprise
            == UniteLegaleEtablissementCategorieEntreprise.GE
        )
        assert restored.sexe_unite_legale == UniteLegaleEtablissementSexeUniteLegale.M
        assert (
            restored.etat_administratif_unite_legale
            == UniteLegaleEtablissementEtatAdministratifUniteLegale.A
        )
        assert (
            restored.caractere_employeur_unite_legale
            == UniteLegaleEtablissementCaractereEmployeurUniteLegale.OUI
        )
        assert (
            restored.nomenclature_activite_principale_unite_legale
            == UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale.NAFREV2
        )

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("statut_diffusion_unite_legale", "statutDiffusionUniteLegale", "O"),
            ("unite_purgee_unite_legale", "unitePurgeeUniteLegale", True),
            ("date_naissance_unite_legale", "dateNaissanceUniteLegale", "1990-01-01"),
            (
                "code_commune_naissance_unite_legale",
                "codeCommuneNaissanceUniteLegale",
                "75001",
            ),
            ("code_pays_naissance_unite_legale", "codePaysNaissanceUniteLegale", "FR"),
            (
                "libelle_nationalite_unite_legale",
                "libelleNationaliteUniteLegale",
                "Française",
            ),
            (
                "identifiant_association_unite_legale",
                "identifiantAssociationUniteLegale",
                "W123456789",
            ),
            ("tranche_effectifs_unite_legale", "trancheEffectifsUniteLegale", "00"),
            ("annee_effectifs_unite_legale", "anneeEffectifsUniteLegale", "2020"),
            (
                "date_dernier_traitement_unite_legale",
                "dateDernierTraitementUniteLegale",
                "2023-01-01",
            ),
            ("annee_categorie_entreprise", "anneeCategorieEntreprise", "2020"),
            ("sigle_unite_legale", "sigleUniteLegale", "SNCF"),
            ("prenom_1_unite_legale", "prenom1UniteLegale", "Jean"),
            ("prenom_2_unite_legale", "prenom2UniteLegale", "Pierre"),
            ("prenom_3_unite_legale", "prenom3UniteLegale", "Marie"),
            ("prenom_4_unite_legale", "prenom4UniteLegale", "Anne"),
            ("prenom_usuel_unite_legale", "prenomUsuelUniteLegale", "Jean"),
            ("pseudonyme_unite_legale", "pseudonymeUniteLegale", "JP"),
            ("nom_unite_legale", "nomUniteLegale", "Dupont"),
            ("denomination_unite_legale", "denominationUniteLegale", "Société Dupont"),
            (
                "denomination_usuelle_1_unite_legale",
                "denominationUsuelle1UniteLegale",
                "Dupont SA",
            ),
            (
                "denomination_usuelle_2_unite_legale",
                "denominationUsuelle2UniteLegale",
                "Dupont Corp",
            ),
            (
                "denomination_usuelle_3_unite_legale",
                "denominationUsuelle3UniteLegale",
                "Dupont Ltd",
            ),
            (
                "activite_principale_unite_legale",
                "activitePrincipaleUniteLegale",
                "6201Z",
            ),
            (
                "categorie_juridique_unite_legale",
                "categorieJuridiqueUniteLegale",
                "5710",
            ),
            ("nic_siege_unite_legale", "nicSiegeUniteLegale", "00001"),
            ("nom_usage_unite_legale", "nomUsageUniteLegale", "Martin"),
            (
                "economie_sociale_solidaire_unite_legale",
                "economieSocialeSolidaireUniteLegale",
                "O",
            ),
            ("societe_mission_unite_legale", "societeMissionUniteLegale", "N"),
        ],
    )
    def test_field_serialization(self, field_name, api_key, value):
        """Test individual field serialization."""
        unite_legale_etablissement = UniteLegaleEtablissement(**{field_name: value})

        result = unite_legale_etablissement.to_dict()
        assert result[api_key] == value

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("statut_diffusion_unite_legale", "statutDiffusionUniteLegale", "O"),
            ("unite_purgee_unite_legale", "unitePurgeeUniteLegale", True),
            ("date_naissance_unite_legale", "dateNaissanceUniteLegale", "1990-01-01"),
            (
                "code_commune_naissance_unite_legale",
                "codeCommuneNaissanceUniteLegale",
                "75001",
            ),
            ("code_pays_naissance_unite_legale", "codePaysNaissanceUniteLegale", "FR"),
            (
                "libelle_nationalite_unite_legale",
                "libelleNationaliteUniteLegale",
                "Française",
            ),
            (
                "identifiant_association_unite_legale",
                "identifiantAssociationUniteLegale",
                "W123456789",
            ),
            ("tranche_effectifs_unite_legale", "trancheEffectifsUniteLegale", "00"),
            ("annee_effectifs_unite_legale", "anneeEffectifsUniteLegale", "2020"),
            (
                "date_dernier_traitement_unite_legale",
                "dateDernierTraitementUniteLegale",
                "2023-01-01",
            ),
            ("annee_categorie_entreprise", "anneeCategorieEntreprise", "2020"),
            ("sigle_unite_legale", "sigleUniteLegale", "SNCF"),
            ("prenom_1_unite_legale", "prenom1UniteLegale", "Jean"),
            ("prenom_2_unite_legale", "prenom2UniteLegale", "Pierre"),
            ("prenom_3_unite_legale", "prenom3UniteLegale", "Marie"),
            ("prenom_4_unite_legale", "prenom4UniteLegale", "Anne"),
            ("prenom_usuel_unite_legale", "prenomUsuelUniteLegale", "Jean"),
            ("pseudonyme_unite_legale", "pseudonymeUniteLegale", "JP"),
            ("nom_unite_legale", "nomUniteLegale", "Dupont"),
            ("denomination_unite_legale", "denominationUniteLegale", "Société Dupont"),
            (
                "denomination_usuelle_1_unite_legale",
                "denominationUsuelle1UniteLegale",
                "Dupont SA",
            ),
            (
                "denomination_usuelle_2_unite_legale",
                "denominationUsuelle2UniteLegale",
                "Dupont Corp",
            ),
            (
                "denomination_usuelle_3_unite_legale",
                "denominationUsuelle3UniteLegale",
                "Dupont Ltd",
            ),
            (
                "activite_principale_unite_legale",
                "activitePrincipaleUniteLegale",
                "6201Z",
            ),
            (
                "categorie_juridique_unite_legale",
                "categorieJuridiqueUniteLegale",
                "5710",
            ),
            ("nic_siege_unite_legale", "nicSiegeUniteLegale", "00001"),
            ("nom_usage_unite_legale", "nomUsageUniteLegale", "Martin"),
            (
                "economie_sociale_solidaire_unite_legale",
                "economieSocialeSolidaireUniteLegale",
                "O",
            ),
            ("societe_mission_unite_legale", "societeMissionUniteLegale", "N"),
        ],
    )
    def test_field_deserialization(self, field_name, api_key, value):
        """Test individual field deserialization."""
        data = {api_key: value}

        unite_legale_etablissement = UniteLegaleEtablissement.from_dict(data)
        assert getattr(unite_legale_etablissement, field_name) == value
