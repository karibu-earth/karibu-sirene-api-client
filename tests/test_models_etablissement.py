"""Tests for sirene_api_client.models.etablissement module."""

import datetime
from unittest.mock import Mock

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.etablissement import Etablissement


@pytest.mark.requirement("REQ-MODEL-001")
class TestEtablissement:
    """Test Etablissement model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        etablissement = Etablissement(
            score=0.95,
            siren="123456789",
            nic="12345",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=datetime.date(2020, 1, 1),
            tranche_effectifs_etablissement="00",
            annee_effectifs_etablissement="2020",
            activite_principale_registre_metiers_etablissement="1234A",
            date_dernier_traitement_etablissement=datetime.datetime(
                2023, 1, 1, 12, 0, 0
            ),
            etablissement_siege=True,
            nombre_periodes_etablissement=1,
        )

        assert etablissement.score == 0.95
        assert etablissement.siren == "123456789"
        assert etablissement.nic == "12345"
        assert etablissement.siret == "12345678901234"
        assert etablissement.statut_diffusion_etablissement == "O"
        assert etablissement.date_creation_etablissement == datetime.date(2020, 1, 1)
        assert etablissement.tranche_effectifs_etablissement == "00"
        assert etablissement.annee_effectifs_etablissement == "2020"
        assert (
            etablissement.activite_principale_registre_metiers_etablissement == "1234A"
        )
        assert etablissement.date_dernier_traitement_etablissement == datetime.datetime(
            2023, 1, 1, 12, 0, 0
        )
        assert etablissement.etablissement_siege is True
        assert etablissement.nombre_periodes_etablissement == 1

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        etablissement = Etablissement()

        assert etablissement.score is UNSET
        assert etablissement.siren is UNSET
        assert etablissement.nic is UNSET
        assert etablissement.siret is UNSET
        assert etablissement.statut_diffusion_etablissement is UNSET
        assert etablissement.date_creation_etablissement is UNSET
        assert etablissement.tranche_effectifs_etablissement is UNSET
        assert etablissement.annee_effectifs_etablissement is UNSET
        assert etablissement.activite_principale_registre_metiers_etablissement is UNSET
        assert etablissement.date_dernier_traitement_etablissement is UNSET
        assert etablissement.etablissement_siege is UNSET
        assert etablissement.nombre_periodes_etablissement is UNSET
        assert etablissement.unite_legale is UNSET
        assert etablissement.adresse_etablissement is UNSET
        assert etablissement.adresse_2_etablissement is UNSET
        assert etablissement.periodes_etablissement is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        etablissement = Etablissement(
            score=0.95,
            siren="123456789",
            nic="12345",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=datetime.date(2020, 1, 1),
            tranche_effectifs_etablissement="00",
            annee_effectifs_etablissement="2020",
            activite_principale_registre_metiers_etablissement="1234A",
            date_dernier_traitement_etablissement=datetime.datetime(
                2023, 1, 1, 12, 0, 0
            ),
            etablissement_siege=True,
            nombre_periodes_etablissement=1,
        )

        result = etablissement.to_dict()

        assert result["score"] == 0.95
        assert result["siren"] == "123456789"
        assert result["nic"] == "12345"
        assert result["siret"] == "12345678901234"
        assert result["statutDiffusionEtablissement"] == "O"
        assert result["dateCreationEtablissement"] == "2020-01-01"
        assert result["trancheEffectifsEtablissement"] == "00"
        assert result["anneeEffectifsEtablissement"] == "2020"
        assert result["activitePrincipaleRegistreMetiersEtablissement"] == "1234A"
        assert result["dateDernierTraitementEtablissement"] == "2023-01-01T12:00:00"
        assert result["etablissementSiege"] is True
        assert result["nombrePeriodesEtablissement"] == 1

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        etablissement = Etablissement(
            siret="12345678901234",  # Only set one field
        )

        result = etablissement.to_dict()

        assert result["siret"] == "12345678901234"
        assert "score" not in result
        assert "siren" not in result
        assert "nic" not in result
        assert "statutDiffusionEtablissement" not in result
        assert "dateCreationEtablissement" not in result
        assert "trancheEffectifsEtablissement" not in result
        assert "anneeEffectifsEtablissement" not in result
        assert "activitePrincipaleRegistreMetiersEtablissement" not in result
        assert "dateDernierTraitementEtablissement" not in result
        assert "etablissementSiege" not in result
        assert "nombrePeriodesEtablissement" not in result
        assert "uniteLegale" not in result
        assert "adresseEtablissement" not in result
        assert "adresse2Etablissement" not in result
        assert "periodesEtablissement" not in result

    def test_to_dict_with_nested_objects(self):
        """Test to_dict with nested objects."""
        # Mock nested objects
        mock_unite_legale = Mock()
        mock_unite_legale.to_dict.return_value = {"siren": "123456789"}

        mock_adresse = Mock()
        mock_adresse.to_dict.return_value = {"codePostalEtablissement": "75001"}

        mock_adresse_2 = Mock()
        mock_adresse_2.to_dict.return_value = {
            "complementAdresseEtablissement": "Bâtiment A"
        }

        mock_periode = Mock()
        mock_periode.to_dict.return_value = {"dateDebut": "2020-01-01"}

        etablissement = Etablissement(
            siret="12345678901234",
            unite_legale=mock_unite_legale,
            adresse_etablissement=mock_adresse,
            adresse_2_etablissement=mock_adresse_2,
            periodes_etablissement=[mock_periode],
        )

        result = etablissement.to_dict()

        assert result["siret"] == "12345678901234"
        assert result["uniteLegale"] == {"siren": "123456789"}
        assert result["adresseEtablissement"] == {"codePostalEtablissement": "75001"}
        assert result["adresse2Etablissement"] == {
            "complementAdresseEtablissement": "Bâtiment A"
        }
        assert result["periodesEtablissement"] == [{"dateDebut": "2020-01-01"}]

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "score": 0.95,
            "siren": "123456789",
            "nic": "12345",
            "siret": "12345678901234",
            "statutDiffusionEtablissement": "O",
            "dateCreationEtablissement": "2020-01-01",
            "trancheEffectifsEtablissement": "00",
            "anneeEffectifsEtablissement": "2020",
            "activitePrincipaleRegistreMetiersEtablissement": "1234A",
            "dateDernierTraitementEtablissement": "2023-01-01T12:00:00",
            "etablissementSiege": True,
            "nombrePeriodesEtablissement": 1,
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.score == 0.95
        assert etablissement.siren == "123456789"
        assert etablissement.nic == "12345"
        assert etablissement.siret == "12345678901234"
        assert etablissement.statut_diffusion_etablissement == "O"
        assert etablissement.date_creation_etablissement == datetime.date(2020, 1, 1)
        assert etablissement.tranche_effectifs_etablissement == "00"
        assert etablissement.annee_effectifs_etablissement == "2020"
        assert (
            etablissement.activite_principale_registre_metiers_etablissement == "1234A"
        )
        assert etablissement.date_dernier_traitement_etablissement == datetime.datetime(
            2023, 1, 1, 12, 0, 0
        )
        assert etablissement.etablissement_siege is True
        assert etablissement.nombre_periodes_etablissement == 1

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "siret": "12345678901234",  # Only required field
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.siret == "12345678901234"
        assert etablissement.score is UNSET
        assert etablissement.siren is UNSET
        assert etablissement.nic is UNSET
        assert etablissement.statut_diffusion_etablissement is UNSET
        assert etablissement.date_creation_etablissement is UNSET
        assert etablissement.tranche_effectifs_etablissement is UNSET
        assert etablissement.annee_effectifs_etablissement is UNSET
        assert etablissement.activite_principale_registre_metiers_etablissement is UNSET
        assert etablissement.date_dernier_traitement_etablissement is UNSET
        assert etablissement.etablissement_siege is UNSET
        assert etablissement.nombre_periodes_etablissement is UNSET
        assert etablissement.unite_legale is UNSET
        assert etablissement.adresse_etablissement is UNSET
        assert etablissement.adresse_2_etablissement is UNSET
        assert etablissement.periodes_etablissement == []

    def test_from_dict_with_null_values(self):
        """Test from_dict with null values."""
        data = {
            "siret": "12345678901234",
            "dateCreationEtablissement": None,
            "dateDernierTraitementEtablissement": None,
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.siret == "12345678901234"
        assert etablissement.date_creation_etablissement is UNSET
        assert etablissement.date_dernier_traitement_etablissement is UNSET

    def test_from_dict_with_nested_objects(self):
        """Test from_dict with nested objects."""
        data = {
            "siret": "12345678901234",
            "uniteLegale": {"siren": "123456789"},
            "adresseEtablissement": {"codePostalEtablissement": "75001"},
            "adresse2Etablissement": {"complementAdresseEtablissement": "Bâtiment A"},
            "periodesEtablissement": [{"dateDebut": "2020-01-01"}],
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.siret == "12345678901234"
        assert etablissement.unite_legale is not UNSET
        assert etablissement.adresse_etablissement is not UNSET
        assert etablissement.adresse_2_etablissement is not UNSET
        assert len(etablissement.periodes_etablissement) == 1

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = Etablissement(
            score=0.95,
            siren="123456789",
            nic="12345",
            siret="12345678901234",
            statut_diffusion_etablissement="O",
            date_creation_etablissement=datetime.date(2020, 1, 1),
            tranche_effectifs_etablissement="00",
            annee_effectifs_etablissement="2020",
            activite_principale_registre_metiers_etablissement="1234A",
            date_dernier_traitement_etablissement=datetime.datetime(
                2023, 1, 1, 12, 0, 0
            ),
            etablissement_siege=True,
            nombre_periodes_etablissement=1,
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = Etablissement.from_dict(data)

        # Verify all fields are preserved
        assert restored.score == original.score
        assert restored.siren == original.siren
        assert restored.nic == original.nic
        assert restored.siret == original.siret
        assert (
            restored.statut_diffusion_etablissement
            == original.statut_diffusion_etablissement
        )
        assert (
            restored.date_creation_etablissement == original.date_creation_etablissement
        )
        assert (
            restored.tranche_effectifs_etablissement
            == original.tranche_effectifs_etablissement
        )
        assert (
            restored.annee_effectifs_etablissement
            == original.annee_effectifs_etablissement
        )
        assert (
            restored.activite_principale_registre_metiers_etablissement
            == original.activite_principale_registre_metiers_etablissement
        )
        assert (
            restored.date_dernier_traitement_etablissement
            == original.date_dernier_traitement_etablissement
        )
        assert restored.etablissement_siege == original.etablissement_siege
        assert (
            restored.nombre_periodes_etablissement
            == original.nombre_periodes_etablissement
        )
        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        etablissement = Etablissement()
        etablissement["custom_field"] = "custom_value"

        assert etablissement["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        etablissement = Etablissement()
        etablissement["custom_field"] = "custom_value"

        assert etablissement.additional_properties["custom_field"] == "custom_value"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        etablissement = Etablissement()
        etablissement["custom_field"] = "custom_value"

        del etablissement["custom_field"]

        assert "custom_field" not in etablissement.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        etablissement = Etablissement()
        etablissement["custom_field"] = "custom_value"

        assert "custom_field" in etablissement
        assert "nonexistent_field" not in etablissement

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        etablissement = Etablissement()
        etablissement["field1"] = "value1"
        etablissement["field2"] = "value2"

        keys = etablissement.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        etablissement = Etablissement(
            siret="12345678901234",
            statut_diffusion_etablissement="O",
        )
        etablissement["unicode_field"] = "Café & Société 🏢"

        result = etablissement.to_dict()
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = Etablissement.from_dict(result)
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        etablissement = Etablissement(
            siret="12345678901234",
            siren="",  # Empty string
            nic=UNSET,  # UNSET
        )

        result = etablissement.to_dict()
        assert result["siret"] == "12345678901234"
        assert result["siren"] == ""
        assert "nic" not in result  # UNSET should be excluded

    def test_boolean_field_handling(self):
        """Test boolean field handling."""
        etablissement = Etablissement(
            siret="12345678901234",
            etablissement_siege=True,
        )

        result = etablissement.to_dict()
        assert result["etablissementSiege"] is True

        # Test False
        etablissement.etablissement_siege = False
        result = etablissement.to_dict()
        assert result["etablissementSiege"] is False

    def test_numeric_field_handling(self):
        """Test numeric field handling."""
        etablissement = Etablissement(
            siret="12345678901234",
            score=0.95,
            nombre_periodes_etablissement=5,
        )

        result = etablissement.to_dict()
        assert result["score"] == 0.95
        assert result["nombrePeriodesEtablissement"] == 5

    def test_date_field_parsing(self):
        """Test date field parsing."""
        data = {
            "siret": "12345678901234",
            "dateCreationEtablissement": "2020-01-01",
            "dateDernierTraitementEtablissement": "2023-01-01T12:00:00",
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.date_creation_etablissement == datetime.date(2020, 1, 1)
        assert etablissement.date_dernier_traitement_etablissement == datetime.datetime(
            2023, 1, 1, 12, 0, 0
        )

    def test_periodes_etablissement_empty_list(self):
        """Test periodes_etablissement with empty list."""
        data = {
            "siret": "12345678901234",
            "periodesEtablissement": [],
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.periodes_etablissement == []

    def test_periodes_etablissement_none(self):
        """Test periodes_etablissement with None."""
        data = {
            "siret": "12345678901234",
            "periodesEtablissement": None,
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.periodes_etablissement == []

    def test_periodes_etablissement_missing(self):
        """Test periodes_etablissement when missing from data."""
        data = {
            "siret": "12345678901234",
        }

        etablissement = Etablissement.from_dict(data)

        assert etablissement.periodes_etablissement == []

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("score", "score", 0.95),
            ("siren", "siren", "123456789"),
            ("nic", "nic", "12345"),
            ("siret", "siret", "12345678901234"),
            ("statut_diffusion_etablissement", "statutDiffusionEtablissement", "O"),
            ("tranche_effectifs_etablissement", "trancheEffectifsEtablissement", "00"),
            ("annee_effectifs_etablissement", "anneeEffectifsEtablissement", "2020"),
            (
                "activite_principale_registre_metiers_etablissement",
                "activitePrincipaleRegistreMetiersEtablissement",
                "1234A",
            ),
            ("etablissement_siege", "etablissementSiege", True),
            ("nombre_periodes_etablissement", "nombrePeriodesEtablissement", 1),
        ],
    )
    def test_field_serialization(self, field_name, api_key, value):
        """Test individual field serialization."""
        etablissement = Etablissement(**{field_name: value})

        result = etablissement.to_dict()
        assert result[api_key] == value

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            ("score", "score", 0.95),
            ("siren", "siren", "123456789"),
            ("nic", "nic", "12345"),
            ("siret", "siret", "12345678901234"),
            ("statut_diffusion_etablissement", "statutDiffusionEtablissement", "O"),
            ("tranche_effectifs_etablissement", "trancheEffectifsEtablissement", "00"),
            ("annee_effectifs_etablissement", "anneeEffectifsEtablissement", "2020"),
            (
                "activite_principale_registre_metiers_etablissement",
                "activitePrincipaleRegistreMetiersEtablissement",
                "1234A",
            ),
            ("etablissement_siege", "etablissementSiege", True),
            ("nombre_periodes_etablissement", "nombrePeriodesEtablissement", 1),
        ],
    )
    def test_field_deserialization(self, field_name, api_key, value):
        """Test individual field deserialization."""
        data = {api_key: value}

        etablissement = Etablissement.from_dict(data)
        assert getattr(etablissement, field_name) == value
