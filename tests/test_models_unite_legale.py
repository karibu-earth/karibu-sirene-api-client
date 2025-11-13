"""Tests for sirene_api_client.models.unite_legale module."""

import datetime
from unittest.mock import Mock

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.unite_legale import UniteLegale
from sirene_api_client.models.unite_legale_categorie_entreprise import (
    UniteLegaleCategorieEntreprise,
)
from sirene_api_client.models.unite_legale_sexe_unite_legale import (
    UniteLegaleSexeUniteLegale,
)


@pytest.mark.requirement("REQ-MODEL-002")
class TestUniteLegale:
    """Test UniteLegale model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        unite_legale = UniteLegale(
            score=0.95,
            siren="123456789",
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
            nombre_periodes_unite_legale=1,
            categorie_entreprise=UniteLegaleCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
        )

        assert unite_legale.score == 0.95
        assert unite_legale.siren == "123456789"
        assert unite_legale.statut_diffusion_unite_legale == "O"
        assert unite_legale.unite_purgee_unite_legale is False
        assert unite_legale.date_creation_unite_legale == datetime.date(2020, 1, 1)
        assert unite_legale.date_naissance_unite_legale == "1990-01-01"
        assert unite_legale.code_commune_naissance_unite_legale == "75001"
        assert unite_legale.code_pays_naissance_unite_legale == "FR"
        assert unite_legale.libelle_nationalite_unite_legale == "Française"
        assert unite_legale.identifiant_association_unite_legale == "W123456789"
        assert unite_legale.tranche_effectifs_unite_legale == "00"
        assert unite_legale.annee_effectifs_unite_legale == "2020"
        assert unite_legale.date_dernier_traitement_unite_legale == "2023-01-01"
        assert unite_legale.nombre_periodes_unite_legale == 1
        assert unite_legale.categorie_entreprise == UniteLegaleCategorieEntreprise.GE
        assert unite_legale.annee_categorie_entreprise == "2020"
        assert unite_legale.sigle_unite_legale == "SNCF"
        assert unite_legale.sexe_unite_legale == UniteLegaleSexeUniteLegale.M
        assert unite_legale.prenom_1_unite_legale == "Jean"
        assert unite_legale.prenom_2_unite_legale == "Pierre"
        assert unite_legale.prenom_3_unite_legale == "Marie"
        assert unite_legale.prenom_4_unite_legale == "Anne"
        assert unite_legale.prenom_usuel_unite_legale == "Jean"
        assert unite_legale.pseudonyme_unite_legale == "JP"

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        unite_legale = UniteLegale()

        assert unite_legale.score is UNSET
        assert unite_legale.siren is UNSET
        assert unite_legale.statut_diffusion_unite_legale is UNSET
        assert unite_legale.unite_purgee_unite_legale is UNSET
        assert unite_legale.date_creation_unite_legale is UNSET
        assert unite_legale.date_naissance_unite_legale is UNSET
        assert unite_legale.code_commune_naissance_unite_legale is UNSET
        assert unite_legale.code_pays_naissance_unite_legale is UNSET
        assert unite_legale.libelle_nationalite_unite_legale is UNSET
        assert unite_legale.identifiant_association_unite_legale is UNSET
        assert unite_legale.tranche_effectifs_unite_legale is UNSET
        assert unite_legale.annee_effectifs_unite_legale is UNSET
        assert unite_legale.date_dernier_traitement_unite_legale is UNSET
        assert unite_legale.nombre_periodes_unite_legale is UNSET
        assert unite_legale.categorie_entreprise is UNSET
        assert unite_legale.annee_categorie_entreprise is UNSET
        assert unite_legale.sigle_unite_legale is UNSET
        assert unite_legale.sexe_unite_legale is UNSET
        assert unite_legale.prenom_1_unite_legale is UNSET
        assert unite_legale.prenom_2_unite_legale is UNSET
        assert unite_legale.prenom_3_unite_legale is UNSET
        assert unite_legale.prenom_4_unite_legale is UNSET
        assert unite_legale.prenom_usuel_unite_legale is UNSET
        assert unite_legale.pseudonyme_unite_legale is UNSET
        assert unite_legale.periodes_unite_legale is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        unite_legale = UniteLegale(
            score=0.95,
            siren="123456789",
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
            nombre_periodes_unite_legale=1,
            categorie_entreprise=UniteLegaleCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
        )

        result = unite_legale.to_dict()

        assert result["score"] == 0.95
        assert result["siren"] == "123456789"
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
        assert result["nombrePeriodesUniteLegale"] == 1
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

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        unite_legale = UniteLegale(
            siren="123456789",  # Only set one field
        )

        result = unite_legale.to_dict()

        assert result["siren"] == "123456789"
        assert "score" not in result
        assert "statutDiffusionUniteLegale" not in result
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
        assert "nombrePeriodesUniteLegale" not in result
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
        assert "periodesUniteLegale" not in result

    def test_to_dict_with_nested_objects(self):
        """Test to_dict with nested objects."""
        # Mock nested objects
        mock_periode = Mock()
        mock_periode.to_dict.return_value = {"dateDebut": "2020-01-01"}

        unite_legale = UniteLegale(
            siren="123456789",
            periodes_unite_legale=[mock_periode],
        )

        result = unite_legale.to_dict()

        assert result["siren"] == "123456789"
        assert result["periodesUniteLegale"] == [{"dateDebut": "2020-01-01"}]

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "score": 0.95,
            "siren": "123456789",
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
            "nombrePeriodesUniteLegale": 1,
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
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.score == 0.95
        assert unite_legale.siren == "123456789"
        assert unite_legale.statut_diffusion_unite_legale == "O"
        assert unite_legale.unite_purgee_unite_legale is False
        assert unite_legale.date_creation_unite_legale == datetime.date(2020, 1, 1)
        assert unite_legale.date_naissance_unite_legale == "1990-01-01"
        assert unite_legale.code_commune_naissance_unite_legale == "75001"
        assert unite_legale.code_pays_naissance_unite_legale == "FR"
        assert unite_legale.libelle_nationalite_unite_legale == "Française"
        assert unite_legale.identifiant_association_unite_legale == "W123456789"
        assert unite_legale.tranche_effectifs_unite_legale == "00"
        assert unite_legale.annee_effectifs_unite_legale == "2020"
        assert unite_legale.date_dernier_traitement_unite_legale == "2023-01-01"
        assert unite_legale.nombre_periodes_unite_legale == 1
        assert unite_legale.categorie_entreprise == UniteLegaleCategorieEntreprise.GE
        assert unite_legale.annee_categorie_entreprise == "2020"
        assert unite_legale.sigle_unite_legale == "SNCF"
        assert unite_legale.sexe_unite_legale == UniteLegaleSexeUniteLegale.M
        assert unite_legale.prenom_1_unite_legale == "Jean"
        assert unite_legale.prenom_2_unite_legale == "Pierre"
        assert unite_legale.prenom_3_unite_legale == "Marie"
        assert unite_legale.prenom_4_unite_legale == "Anne"
        assert unite_legale.prenom_usuel_unite_legale == "Jean"
        assert unite_legale.pseudonyme_unite_legale == "JP"

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "siren": "123456789",  # Only required field
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.siren == "123456789"
        assert unite_legale.score is UNSET
        assert unite_legale.statut_diffusion_unite_legale is UNSET
        assert unite_legale.unite_purgee_unite_legale is UNSET
        assert unite_legale.date_creation_unite_legale is UNSET
        assert unite_legale.date_naissance_unite_legale is UNSET
        assert unite_legale.code_commune_naissance_unite_legale is UNSET
        assert unite_legale.code_pays_naissance_unite_legale is UNSET
        assert unite_legale.libelle_nationalite_unite_legale is UNSET
        assert unite_legale.identifiant_association_unite_legale is UNSET
        assert unite_legale.tranche_effectifs_unite_legale is UNSET
        assert unite_legale.annee_effectifs_unite_legale is UNSET
        assert unite_legale.date_dernier_traitement_unite_legale is UNSET
        assert unite_legale.nombre_periodes_unite_legale is UNSET
        assert unite_legale.categorie_entreprise is UNSET
        assert unite_legale.annee_categorie_entreprise is UNSET
        assert unite_legale.sigle_unite_legale is UNSET
        assert unite_legale.sexe_unite_legale is UNSET
        assert unite_legale.prenom_1_unite_legale is UNSET
        assert unite_legale.prenom_2_unite_legale is UNSET
        assert unite_legale.prenom_3_unite_legale is UNSET
        assert unite_legale.prenom_4_unite_legale is UNSET
        assert unite_legale.prenom_usuel_unite_legale is UNSET
        assert unite_legale.pseudonyme_unite_legale is UNSET
        assert unite_legale.periodes_unite_legale == []

    def test_from_dict_with_null_values(self):
        """Test from_dict with null values."""
        data = {
            "siren": "123456789",
            "dateCreationUniteLegale": None,
            "dateNaissanceUniteLegale": None,
            "identifiantAssociationUniteLegale": None,
            "prenom1UniteLegale": None,
            "prenom2UniteLegale": None,
            "prenom3UniteLegale": None,
            "prenom4UniteLegale": None,
            "prenomUsuelUniteLegale": None,
            "pseudonymeUniteLegale": None,
            "categorieEntreprise": None,
            "sexeUniteLegale": None,
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.siren == "123456789"
        assert unite_legale.date_creation_unite_legale is UNSET
        assert unite_legale.date_naissance_unite_legale is UNSET
        assert unite_legale.identifiant_association_unite_legale is UNSET
        assert unite_legale.prenom_1_unite_legale is UNSET
        assert unite_legale.prenom_2_unite_legale is UNSET
        assert unite_legale.prenom_3_unite_legale is UNSET
        assert unite_legale.prenom_4_unite_legale is UNSET
        assert unite_legale.prenom_usuel_unite_legale is UNSET
        assert unite_legale.pseudonyme_unite_legale is UNSET
        assert unite_legale.categorie_entreprise is UNSET
        assert unite_legale.sexe_unite_legale is UNSET

    def test_from_dict_with_nested_objects(self):
        """Test from_dict with nested objects."""
        data = {
            "siren": "123456789",
            "periodesUniteLegale": [{"dateDebut": "2020-01-01"}],
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.siren == "123456789"
        assert len(unite_legale.periodes_unite_legale) == 1

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = UniteLegale(
            score=0.95,
            siren="123456789",
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
            nombre_periodes_unite_legale=1,
            categorie_entreprise=UniteLegaleCategorieEntreprise.GE,
            annee_categorie_entreprise="2020",
            sigle_unite_legale="SNCF",
            sexe_unite_legale=UniteLegaleSexeUniteLegale.M,
            prenom_1_unite_legale="Jean",
            prenom_2_unite_legale="Pierre",
            prenom_3_unite_legale="Marie",
            prenom_4_unite_legale="Anne",
            prenom_usuel_unite_legale="Jean",
            pseudonyme_unite_legale="JP",
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = UniteLegale.from_dict(data)

        # Verify all fields are preserved
        assert restored.score == original.score
        assert restored.siren == original.siren
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
        assert (
            restored.nombre_periodes_unite_legale
            == original.nombre_periodes_unite_legale
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
        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        unite_legale = UniteLegale()
        unite_legale["custom_field"] = "custom_value"

        assert unite_legale["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        unite_legale = UniteLegale()
        unite_legale["custom_field"] = "custom_value"

        assert unite_legale.additional_properties["custom_field"] == "custom_value"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        unite_legale = UniteLegale()
        unite_legale["custom_field"] = "custom_value"

        del unite_legale["custom_field"]

        assert "custom_field" not in unite_legale.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        unite_legale = UniteLegale()
        unite_legale["custom_field"] = "custom_value"

        assert "custom_field" in unite_legale
        assert "nonexistent_field" not in unite_legale

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        unite_legale = UniteLegale()
        unite_legale["field1"] = "value1"
        unite_legale["field2"] = "value2"

        keys = unite_legale.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        unite_legale = UniteLegale(
            siren="123456789",
            libelle_nationalite_unite_legale="Française",
            prenom_1_unite_legale="José",
        )
        unite_legale["unicode_field"] = "Café & Société 🏢"

        result = unite_legale.to_dict()
        assert result["libelleNationaliteUniteLegale"] == "Française"
        assert result["prenom1UniteLegale"] == "José"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = UniteLegale.from_dict(result)
        assert restored.libelle_nationalite_unite_legale == "Française"
        assert restored.prenom_1_unite_legale == "José"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        unite_legale = UniteLegale(
            siren="123456789",
            sigle_unite_legale="",  # Empty string
            prenom_1_unite_legale=UNSET,  # UNSET
        )

        result = unite_legale.to_dict()
        assert result["siren"] == "123456789"
        assert result["sigleUniteLegale"] == ""
        assert "prenom1UniteLegale" not in result  # UNSET should be excluded

    def test_boolean_field_handling(self):
        """Test boolean field handling."""
        unite_legale = UniteLegale(
            siren="123456789",
            unite_purgee_unite_legale=True,
        )

        result = unite_legale.to_dict()
        assert result["unitePurgeeUniteLegale"] is True

        # Test False
        unite_legale.unite_purgee_unite_legale = False
        result = unite_legale.to_dict()
        assert result["unitePurgeeUniteLegale"] is False

    def test_numeric_field_handling(self):
        """Test numeric field handling."""
        unite_legale = UniteLegale(
            siren="123456789",
            score=0.95,
            nombre_periodes_unite_legale=5,
        )

        result = unite_legale.to_dict()
        assert result["score"] == 0.95
        assert result["nombrePeriodesUniteLegale"] == 5

    def test_date_field_parsing(self):
        """Test date field parsing."""
        data = {
            "siren": "123456789",
            "dateCreationUniteLegale": "2020-01-01",
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.date_creation_unite_legale == datetime.date(2020, 1, 1)

    def test_enum_field_handling(self):
        """Test enum field handling."""
        unite_legale = UniteLegale(
            siren="123456789",
            categorie_entreprise=UniteLegaleCategorieEntreprise.GE,
            sexe_unite_legale=UniteLegaleSexeUniteLegale.M,
        )

        result = unite_legale.to_dict()
        assert result["categorieEntreprise"] == "GE"
        assert result["sexeUniteLegale"] == "M"

        # Test deserialization
        data = {
            "siren": "123456789",
            "categorieEntreprise": "GE",
            "sexeUniteLegale": "M",
        }

        restored = UniteLegale.from_dict(data)
        assert restored.categorie_entreprise == UniteLegaleCategorieEntreprise.GE
        assert restored.sexe_unite_legale == UniteLegaleSexeUniteLegale.M

    def test_periodes_unite_legale_empty_list(self):
        """Test periodes_unite_legale with empty list."""
        data = {
            "siren": "123456789",
            "periodesUniteLegale": [],
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.periodes_unite_legale == []

    def test_periodes_unite_legale_none(self):
        """Test periodes_unite_legale with None."""
        data = {
            "siren": "123456789",
            "periodesUniteLegale": None,
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.periodes_unite_legale == []

    def test_periodes_unite_legale_missing(self):
        """Test periodes_unite_legale when missing from data."""
        data = {
            "siren": "123456789",
        }

        unite_legale = UniteLegale.from_dict(data)

        assert unite_legale.periodes_unite_legale == []

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("score", "score", 0.95),
            ("siren", "siren", "123456789"),
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
            ("nombre_periodes_unite_legale", "nombrePeriodesUniteLegale", 1),
            ("annee_categorie_entreprise", "anneeCategorieEntreprise", "2020"),
            ("sigle_unite_legale", "sigleUniteLegale", "SNCF"),
            ("prenom_1_unite_legale", "prenom1UniteLegale", "Jean"),
            ("prenom_2_unite_legale", "prenom2UniteLegale", "Pierre"),
            ("prenom_3_unite_legale", "prenom3UniteLegale", "Marie"),
            ("prenom_4_unite_legale", "prenom4UniteLegale", "Anne"),
            ("prenom_usuel_unite_legale", "prenomUsuelUniteLegale", "Jean"),
            ("pseudonyme_unite_legale", "pseudonymeUniteLegale", "JP"),
        ],
    )
    def test_field_serialization(self, field_name, api_key, value):
        """Test individual field serialization."""
        unite_legale = UniteLegale(**{field_name: value})

        result = unite_legale.to_dict()
        assert result[api_key] == value

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("score", "score", 0.95),
            ("siren", "siren", "123456789"),
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
            ("nombre_periodes_unite_legale", "nombrePeriodesUniteLegale", 1),
            ("annee_categorie_entreprise", "anneeCategorieEntreprise", "2020"),
            ("sigle_unite_legale", "sigleUniteLegale", "SNCF"),
            ("prenom_1_unite_legale", "prenom1UniteLegale", "Jean"),
            ("prenom_2_unite_legale", "prenom2UniteLegale", "Pierre"),
            ("prenom_3_unite_legale", "prenom3UniteLegale", "Marie"),
            ("prenom_4_unite_legale", "prenom4UniteLegale", "Anne"),
            ("prenom_usuel_unite_legale", "prenomUsuelUniteLegale", "Jean"),
            ("pseudonyme_unite_legale", "pseudonymeUniteLegale", "JP"),
        ],
    )
    def test_field_deserialization(self, field_name, api_key, value):
        """Test individual field deserialization."""
        data = {api_key: value}

        unite_legale = UniteLegale.from_dict(data)
        assert getattr(unite_legale, field_name) == value
