"""Tests for sirene_api_client.models.adresse module."""

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.adresse import Adresse


@pytest.mark.requirement("REQ-MODEL-004")
class TestAdresse:
    """Test Adresse model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        adresse = Adresse(
            complement_adresse_etablissement="Bâtiment A",
            numero_voie_etablissement="123",
            indice_repetition_etablissement="B",
            dernier_numero_voie_etablissement="125",
            indice_repetition_dernier_numero_voie_etablissement="C",
            type_voie_etablissement="RUE",
            libelle_voie_etablissement="de la Paix",
            code_postal_etablissement="75001",
            libelle_commune_etablissement="Paris",
            libelle_commune_etranger_etablissement="London",
            distribution_speciale_etablissement="BP 123",
            code_commune_etablissement="75101",
            code_cedex_etablissement="12345",
            libelle_cedex_etablissement="PARIS CEDEX 01",
            code_pays_etranger_etablissement="GB",
            libelle_pays_etranger_etablissement="Royaume-Uni",
            identifiant_adresse_etablissement="AD123456",
            coordonnee_lambert_abscisse_etablissement="123456.78",
            coordonnee_lambert_ordonnee_etablissement="234567.89",
        )

        assert adresse.complement_adresse_etablissement == "Bâtiment A"
        assert adresse.numero_voie_etablissement == "123"
        assert adresse.indice_repetition_etablissement == "B"
        assert adresse.dernier_numero_voie_etablissement == "125"
        assert adresse.indice_repetition_dernier_numero_voie_etablissement == "C"
        assert adresse.type_voie_etablissement == "RUE"
        assert adresse.libelle_voie_etablissement == "de la Paix"
        assert adresse.code_postal_etablissement == "75001"
        assert adresse.libelle_commune_etablissement == "Paris"
        assert adresse.libelle_commune_etranger_etablissement == "London"
        assert adresse.distribution_speciale_etablissement == "BP 123"
        assert adresse.code_commune_etablissement == "75101"
        assert adresse.code_cedex_etablissement == "12345"
        assert adresse.libelle_cedex_etablissement == "PARIS CEDEX 01"
        assert adresse.code_pays_etranger_etablissement == "GB"
        assert adresse.libelle_pays_etranger_etablissement == "Royaume-Uni"
        assert adresse.identifiant_adresse_etablissement == "AD123456"
        assert adresse.coordonnee_lambert_abscisse_etablissement == "123456.78"
        assert adresse.coordonnee_lambert_ordonnee_etablissement == "234567.89"

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        adresse = Adresse()

        assert adresse.complement_adresse_etablissement is UNSET
        assert adresse.numero_voie_etablissement is UNSET
        assert adresse.indice_repetition_etablissement is UNSET
        assert adresse.dernier_numero_voie_etablissement is UNSET
        assert adresse.indice_repetition_dernier_numero_voie_etablissement is UNSET
        assert adresse.type_voie_etablissement is UNSET
        assert adresse.libelle_voie_etablissement is UNSET
        assert adresse.code_postal_etablissement is UNSET
        assert adresse.libelle_commune_etablissement is UNSET
        assert adresse.libelle_commune_etranger_etablissement is UNSET
        assert adresse.distribution_speciale_etablissement is UNSET
        assert adresse.code_commune_etablissement is UNSET
        assert adresse.code_cedex_etablissement is UNSET
        assert adresse.libelle_cedex_etablissement is UNSET
        assert adresse.code_pays_etranger_etablissement is UNSET
        assert adresse.libelle_pays_etranger_etablissement is UNSET
        assert adresse.identifiant_adresse_etablissement is UNSET
        assert adresse.coordonnee_lambert_abscisse_etablissement is UNSET
        assert adresse.coordonnee_lambert_ordonnee_etablissement is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        adresse = Adresse(
            complement_adresse_etablissement="Bâtiment A",
            numero_voie_etablissement="123",
            indice_repetition_etablissement="B",
            dernier_numero_voie_etablissement="125",
            indice_repetition_dernier_numero_voie_etablissement="C",
            type_voie_etablissement="RUE",
            libelle_voie_etablissement="de la Paix",
            code_postal_etablissement="75001",
            libelle_commune_etablissement="Paris",
            libelle_commune_etranger_etablissement="London",
            distribution_speciale_etablissement="BP 123",
            code_commune_etablissement="75101",
            code_cedex_etablissement="12345",
            libelle_cedex_etablissement="PARIS CEDEX 01",
            code_pays_etranger_etablissement="GB",
            libelle_pays_etranger_etablissement="Royaume-Uni",
            identifiant_adresse_etablissement="AD123456",
            coordonnee_lambert_abscisse_etablissement="123456.78",
            coordonnee_lambert_ordonnee_etablissement="234567.89",
        )

        result = adresse.to_dict()

        assert result["complementAdresseEtablissement"] == "Bâtiment A"
        assert result["numeroVoieEtablissement"] == "123"
        assert result["indiceRepetitionEtablissement"] == "B"
        assert result["dernierNumeroVoieEtablissement"] == "125"
        assert result["indiceRepetitionDernierNumeroVoieEtablissement"] == "C"
        assert result["typeVoieEtablissement"] == "RUE"
        assert result["libelleVoieEtablissement"] == "de la Paix"
        assert result["codePostalEtablissement"] == "75001"
        assert result["libelleCommuneEtablissement"] == "Paris"
        assert result["libelleCommuneEtrangerEtablissement"] == "London"
        assert result["distributionSpecialeEtablissement"] == "BP 123"
        assert result["codeCommuneEtablissement"] == "75101"
        assert result["codeCedexEtablissement"] == "12345"
        assert result["libelleCedexEtablissement"] == "PARIS CEDEX 01"
        assert result["codePaysEtrangerEtablissement"] == "GB"
        assert result["libellePaysEtrangerEtablissement"] == "Royaume-Uni"
        assert result["identifiantAdresseEtablissement"] == "AD123456"
        assert result["coordonneeLambertAbscisseEtablissement"] == "123456.78"
        assert result["coordonneeLambertOrdonneeEtablissement"] == "234567.89"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        adresse = Adresse(
            numero_voie_etablissement="123",  # Only set one field
        )

        result = adresse.to_dict()

        assert result["numeroVoieEtablissement"] == "123"
        assert "complementAdresseEtablissement" not in result
        assert "indiceRepetitionEtablissement" not in result
        assert "dernierNumeroVoieEtablissement" not in result
        assert "indiceRepetitionDernierNumeroVoieEtablissement" not in result
        assert "typeVoieEtablissement" not in result
        assert "libelleVoieEtablissement" not in result
        assert "codePostalEtablissement" not in result
        assert "libelleCommuneEtablissement" not in result
        assert "libelleCommuneEtrangerEtablissement" not in result
        assert "distributionSpecialeEtablissement" not in result
        assert "codeCommuneEtablissement" not in result
        assert "codeCedexEtablissement" not in result
        assert "libelleCedexEtablissement" not in result
        assert "codePaysEtrangerEtablissement" not in result
        assert "libellePaysEtrangerEtablissement" not in result
        assert "identifiantAdresseEtablissement" not in result
        assert "coordonneeLambertAbscisseEtablissement" not in result
        assert "coordonneeLambertOrdonneeEtablissement" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "complementAdresseEtablissement": "Bâtiment A",
            "numeroVoieEtablissement": "123",
            "indiceRepetitionEtablissement": "B",
            "dernierNumeroVoieEtablissement": "125",
            "indiceRepetitionDernierNumeroVoieEtablissement": "C",
            "typeVoieEtablissement": "RUE",
            "libelleVoieEtablissement": "de la Paix",
            "codePostalEtablissement": "75001",
            "libelleCommuneEtablissement": "Paris",
            "libelleCommuneEtrangerEtablissement": "London",
            "distributionSpecialeEtablissement": "BP 123",
            "codeCommuneEtablissement": "75101",
            "codeCedexEtablissement": "12345",
            "libelleCedexEtablissement": "PARIS CEDEX 01",
            "codePaysEtrangerEtablissement": "GB",
            "libellePaysEtrangerEtablissement": "Royaume-Uni",
            "identifiantAdresseEtablissement": "AD123456",
            "coordonneeLambertAbscisseEtablissement": "123456.78",
            "coordonneeLambertOrdonneeEtablissement": "234567.89",
        }

        adresse = Adresse.from_dict(data)

        assert adresse.complement_adresse_etablissement == "Bâtiment A"
        assert adresse.numero_voie_etablissement == "123"
        assert adresse.indice_repetition_etablissement == "B"
        assert adresse.dernier_numero_voie_etablissement == "125"
        assert adresse.indice_repetition_dernier_numero_voie_etablissement == "C"
        assert adresse.type_voie_etablissement == "RUE"
        assert adresse.libelle_voie_etablissement == "de la Paix"
        assert adresse.code_postal_etablissement == "75001"
        assert adresse.libelle_commune_etablissement == "Paris"
        assert adresse.libelle_commune_etranger_etablissement == "London"
        assert adresse.distribution_speciale_etablissement == "BP 123"
        assert adresse.code_commune_etablissement == "75101"
        assert adresse.code_cedex_etablissement == "12345"
        assert adresse.libelle_cedex_etablissement == "PARIS CEDEX 01"
        assert adresse.code_pays_etranger_etablissement == "GB"
        assert adresse.libelle_pays_etranger_etablissement == "Royaume-Uni"
        assert adresse.identifiant_adresse_etablissement == "AD123456"
        assert adresse.coordonnee_lambert_abscisse_etablissement == "123456.78"
        assert adresse.coordonnee_lambert_ordonnee_etablissement == "234567.89"

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "numeroVoieEtablissement": "123",  # Only required field
        }

        adresse = Adresse.from_dict(data)

        assert adresse.numero_voie_etablissement == "123"
        assert adresse.complement_adresse_etablissement is UNSET
        assert adresse.indice_repetition_etablissement is UNSET
        assert adresse.dernier_numero_voie_etablissement is UNSET
        assert adresse.indice_repetition_dernier_numero_voie_etablissement is UNSET
        assert adresse.type_voie_etablissement is UNSET
        assert adresse.libelle_voie_etablissement is UNSET
        assert adresse.code_postal_etablissement is UNSET
        assert adresse.libelle_commune_etablissement is UNSET
        assert adresse.libelle_commune_etranger_etablissement is UNSET
        assert adresse.distribution_speciale_etablissement is UNSET
        assert adresse.code_commune_etablissement is UNSET
        assert adresse.code_cedex_etablissement is UNSET
        assert adresse.libelle_cedex_etablissement is UNSET
        assert adresse.code_pays_etranger_etablissement is UNSET
        assert adresse.libelle_pays_etranger_etablissement is UNSET
        assert adresse.identifiant_adresse_etablissement is UNSET
        assert adresse.coordonnee_lambert_abscisse_etablissement is UNSET
        assert adresse.coordonnee_lambert_ordonnee_etablissement is UNSET

    def test_from_dict_with_null_values(self):
        """Test from_dict with null values."""
        data = {
            "numeroVoieEtablissement": "123",
            "complementAdresseEtablissement": None,
            "indiceRepetitionEtablissement": None,
            "dernierNumeroVoieEtablissement": None,
            "indiceRepetitionDernierNumeroVoieEtablissement": None,
            "typeVoieEtablissement": None,
            "libelleVoieEtablissement": None,
            "codePostalEtablissement": None,
            "libelleCommuneEtablissement": None,
            "libelleCommuneEtrangerEtablissement": None,
            "distributionSpecialeEtablissement": None,
            "codeCommuneEtablissement": None,
            "codeCedexEtablissement": None,
            "libelleCedexEtablissement": None,
            "codePaysEtrangerEtablissement": None,
            "libellePaysEtrangerEtablissement": None,
            "identifiantAdresseEtablissement": None,
            "coordonneeLambertAbscisseEtablissement": None,
            "coordonneeLambertOrdonneeEtablissement": None,
        }

        adresse = Adresse.from_dict(data)

        assert adresse.numero_voie_etablissement == "123"
        assert adresse.complement_adresse_etablissement is None
        assert adresse.indice_repetition_etablissement is None
        assert adresse.dernier_numero_voie_etablissement is None
        assert adresse.indice_repetition_dernier_numero_voie_etablissement is None
        assert adresse.type_voie_etablissement is None
        assert adresse.libelle_voie_etablissement is None
        assert adresse.code_postal_etablissement is None
        assert adresse.libelle_commune_etablissement is None
        assert adresse.libelle_commune_etranger_etablissement is None
        assert adresse.distribution_speciale_etablissement is None
        assert adresse.code_commune_etablissement is None
        assert adresse.code_cedex_etablissement is None
        assert adresse.libelle_cedex_etablissement is None
        assert adresse.code_pays_etranger_etablissement is None
        assert adresse.libelle_pays_etranger_etablissement is None
        assert adresse.identifiant_adresse_etablissement is None
        assert adresse.coordonnee_lambert_abscisse_etablissement is None
        assert adresse.coordonnee_lambert_ordonnee_etablissement is None

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = Adresse(
            complement_adresse_etablissement="Bâtiment A",
            numero_voie_etablissement="123",
            indice_repetition_etablissement="B",
            dernier_numero_voie_etablissement="125",
            indice_repetition_dernier_numero_voie_etablissement="C",
            type_voie_etablissement="RUE",
            libelle_voie_etablissement="de la Paix",
            code_postal_etablissement="75001",
            libelle_commune_etablissement="Paris",
            libelle_commune_etranger_etablissement="London",
            distribution_speciale_etablissement="BP 123",
            code_commune_etablissement="75101",
            code_cedex_etablissement="12345",
            libelle_cedex_etablissement="PARIS CEDEX 01",
            code_pays_etranger_etablissement="GB",
            libelle_pays_etranger_etablissement="Royaume-Uni",
            identifiant_adresse_etablissement="AD123456",
            coordonnee_lambert_abscisse_etablissement="123456.78",
            coordonnee_lambert_ordonnee_etablissement="234567.89",
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = Adresse.from_dict(data)

        # Verify all fields are preserved
        assert (
            restored.complement_adresse_etablissement
            == original.complement_adresse_etablissement
        )
        assert restored.numero_voie_etablissement == original.numero_voie_etablissement
        assert (
            restored.indice_repetition_etablissement
            == original.indice_repetition_etablissement
        )
        assert (
            restored.dernier_numero_voie_etablissement
            == original.dernier_numero_voie_etablissement
        )
        assert (
            restored.indice_repetition_dernier_numero_voie_etablissement
            == original.indice_repetition_dernier_numero_voie_etablissement
        )
        assert restored.type_voie_etablissement == original.type_voie_etablissement
        assert (
            restored.libelle_voie_etablissement == original.libelle_voie_etablissement
        )
        assert restored.code_postal_etablissement == original.code_postal_etablissement
        assert (
            restored.libelle_commune_etablissement
            == original.libelle_commune_etablissement
        )
        assert (
            restored.libelle_commune_etranger_etablissement
            == original.libelle_commune_etranger_etablissement
        )
        assert (
            restored.distribution_speciale_etablissement
            == original.distribution_speciale_etablissement
        )
        assert (
            restored.code_commune_etablissement == original.code_commune_etablissement
        )
        assert restored.code_cedex_etablissement == original.code_cedex_etablissement
        assert (
            restored.libelle_cedex_etablissement == original.libelle_cedex_etablissement
        )
        assert (
            restored.code_pays_etranger_etablissement
            == original.code_pays_etranger_etablissement
        )
        assert (
            restored.libelle_pays_etranger_etablissement
            == original.libelle_pays_etranger_etablissement
        )
        assert (
            restored.identifiant_adresse_etablissement
            == original.identifiant_adresse_etablissement
        )
        assert (
            restored.coordonnee_lambert_abscisse_etablissement
            == original.coordonnee_lambert_abscisse_etablissement
        )
        assert (
            restored.coordonnee_lambert_ordonnee_etablissement
            == original.coordonnee_lambert_ordonnee_etablissement
        )
        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        adresse = Adresse()
        adresse["custom_field"] = "custom_value"

        assert adresse["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        adresse = Adresse()
        adresse["custom_field"] = "custom_value"

        assert adresse.additional_properties["custom_field"] == "custom_value"

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        adresse = Adresse()
        adresse["custom_field"] = "custom_value"

        del adresse["custom_field"]

        assert "custom_field" not in adresse.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        adresse = Adresse()
        adresse["custom_field"] = "custom_value"

        assert "custom_field" in adresse
        assert "nonexistent_field" not in adresse

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        adresse = Adresse()
        adresse["field1"] = "value1"
        adresse["field2"] = "value2"

        keys = adresse.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        adresse = Adresse(
            numero_voie_etablissement="123",
            libelle_voie_etablissement="Rue de l'Église",
            libelle_commune_etablissement="Saint-Étienne",
            libelle_pays_etranger_etablissement="Côte d'Ivoire",
        )
        adresse["unicode_field"] = "Café & Société 🏢"

        result = adresse.to_dict()
        assert result["libelleVoieEtablissement"] == "Rue de l'Église"
        assert result["libelleCommuneEtablissement"] == "Saint-Étienne"
        assert result["libellePaysEtrangerEtablissement"] == "Côte d'Ivoire"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = Adresse.from_dict(result)
        assert restored.libelle_voie_etablissement == "Rue de l'Église"
        assert restored.libelle_commune_etablissement == "Saint-Étienne"
        assert restored.libelle_pays_etranger_etablissement == "Côte d'Ivoire"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        adresse = Adresse(
            numero_voie_etablissement="123",
            libelle_voie_etablissement="",  # Empty string
            code_postal_etablissement=UNSET,  # UNSET
        )

        result = adresse.to_dict()
        assert result["numeroVoieEtablissement"] == "123"
        assert result["libelleVoieEtablissement"] == ""
        assert "codePostalEtablissement" not in result  # UNSET should be excluded

    def test_french_address_handling(self):
        """Test French address handling."""
        adresse = Adresse(
            numero_voie_etablissement="123",
            indice_repetition_etablissement="B",
            type_voie_etablissement="RUE",
            libelle_voie_etablissement="de la Paix",
            code_postal_etablissement="75001",
            libelle_commune_etablissement="Paris",
            code_commune_etablissement="75101",
            code_cedex_etablissement="12345",
            libelle_cedex_etablissement="PARIS CEDEX 01",
        )

        result = adresse.to_dict()
        assert result["numeroVoieEtablissement"] == "123"
        assert result["indiceRepetitionEtablissement"] == "B"
        assert result["typeVoieEtablissement"] == "RUE"
        assert result["libelleVoieEtablissement"] == "de la Paix"
        assert result["codePostalEtablissement"] == "75001"
        assert result["libelleCommuneEtablissement"] == "Paris"
        assert result["codeCommuneEtablissement"] == "75101"
        assert result["codeCedexEtablissement"] == "12345"
        assert result["libelleCedexEtablissement"] == "PARIS CEDEX 01"

    def test_foreign_address_handling(self):
        """Test foreign address handling."""
        adresse = Adresse(
            numero_voie_etablissement="456",
            type_voie_etablissement="STREET",
            libelle_voie_etablissement="Baker Street",
            libelle_commune_etranger_etablissement="London",
            code_pays_etranger_etablissement="GB",
            libelle_pays_etranger_etablissement="United Kingdom",
        )

        result = adresse.to_dict()
        assert result["numeroVoieEtablissement"] == "456"
        assert result["typeVoieEtablissement"] == "STREET"
        assert result["libelleVoieEtablissement"] == "Baker Street"
        assert result["libelleCommuneEtrangerEtablissement"] == "London"
        assert result["codePaysEtrangerEtablissement"] == "GB"
        assert result["libellePaysEtrangerEtablissement"] == "United Kingdom"

    def test_lambert_coordinates_handling(self):
        """Test Lambert coordinates handling."""
        adresse = Adresse(
            numero_voie_etablissement="789",
            coordonnee_lambert_abscisse_etablissement="123456.78",
            coordonnee_lambert_ordonnee_etablissement="234567.89",
        )

        result = adresse.to_dict()
        assert result["numeroVoieEtablissement"] == "789"
        assert result["coordonneeLambertAbscisseEtablissement"] == "123456.78"
        assert result["coordonneeLambertOrdonneeEtablissement"] == "234567.89"

    def test_special_distribution_handling(self):
        """Test special distribution handling."""
        adresse = Adresse(
            numero_voie_etablissement="000",
            distribution_speciale_etablissement="BP 123",
            identifiant_adresse_etablissement="AD123456",
        )

        result = adresse.to_dict()
        assert result["numeroVoieEtablissement"] == "000"
        assert result["distributionSpecialeEtablissement"] == "BP 123"
        assert result["identifiantAdresseEtablissement"] == "AD123456"

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            (
                "complement_adresse_etablissement",
                "complementAdresseEtablissement",
                "Bâtiment A",
            ),
            ("numero_voie_etablissement", "numeroVoieEtablissement", "123"),
            ("indice_repetition_etablissement", "indiceRepetitionEtablissement", "B"),
            (
                "dernier_numero_voie_etablissement",
                "dernierNumeroVoieEtablissement",
                "125",
            ),
            (
                "indice_repetition_dernier_numero_voie_etablissement",
                "indiceRepetitionDernierNumeroVoieEtablissement",
                "C",
            ),
            ("type_voie_etablissement", "typeVoieEtablissement", "RUE"),
            ("libelle_voie_etablissement", "libelleVoieEtablissement", "de la Paix"),
            ("code_postal_etablissement", "codePostalEtablissement", "75001"),
            ("libelle_commune_etablissement", "libelleCommuneEtablissement", "Paris"),
            (
                "libelle_commune_etranger_etablissement",
                "libelleCommuneEtrangerEtablissement",
                "London",
            ),
            (
                "distribution_speciale_etablissement",
                "distributionSpecialeEtablissement",
                "BP 123",
            ),
            ("code_commune_etablissement", "codeCommuneEtablissement", "75101"),
            ("code_cedex_etablissement", "codeCedexEtablissement", "12345"),
            (
                "libelle_cedex_etablissement",
                "libelleCedexEtablissement",
                "PARIS CEDEX 01",
            ),
            ("code_pays_etranger_etablissement", "codePaysEtrangerEtablissement", "GB"),
            (
                "libelle_pays_etranger_etablissement",
                "libellePaysEtrangerEtablissement",
                "Royaume-Uni",
            ),
            (
                "identifiant_adresse_etablissement",
                "identifiantAdresseEtablissement",
                "AD123456",
            ),
            (
                "coordonnee_lambert_abscisse_etablissement",
                "coordonneeLambertAbscisseEtablissement",
                "123456.78",
            ),
            (
                "coordonnee_lambert_ordonnee_etablissement",
                "coordonneeLambertOrdonneeEtablissement",
                "234567.89",
            ),
        ],
    )
    def test_field_serialization(self, field_name, api_key, value):
        """Test individual field serialization."""
        adresse = Adresse(**{field_name: value})

        result = adresse.to_dict()
        assert result[api_key] == value

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            (
                "complement_adresse_etablissement",
                "complementAdresseEtablissement",
                "Bâtiment A",
            ),
            ("numero_voie_etablissement", "numeroVoieEtablissement", "123"),
            ("indice_repetition_etablissement", "indiceRepetitionEtablissement", "B"),
            (
                "dernier_numero_voie_etablissement",
                "dernierNumeroVoieEtablissement",
                "125",
            ),
            (
                "indice_repetition_dernier_numero_voie_etablissement",
                "indiceRepetitionDernierNumeroVoieEtablissement",
                "C",
            ),
            ("type_voie_etablissement", "typeVoieEtablissement", "RUE"),
            ("libelle_voie_etablissement", "libelleVoieEtablissement", "de la Paix"),
            ("code_postal_etablissement", "codePostalEtablissement", "75001"),
            ("libelle_commune_etablissement", "libelleCommuneEtablissement", "Paris"),
            (
                "libelle_commune_etranger_etablissement",
                "libelleCommuneEtrangerEtablissement",
                "London",
            ),
            (
                "distribution_speciale_etablissement",
                "distributionSpecialeEtablissement",
                "BP 123",
            ),
            ("code_commune_etablissement", "codeCommuneEtablissement", "75101"),
            ("code_cedex_etablissement", "codeCedexEtablissement", "12345"),
            (
                "libelle_cedex_etablissement",
                "libelleCedexEtablissement",
                "PARIS CEDEX 01",
            ),
            ("code_pays_etranger_etablissement", "codePaysEtrangerEtablissement", "GB"),
            (
                "libelle_pays_etranger_etablissement",
                "libellePaysEtrangerEtablissement",
                "Royaume-Uni",
            ),
            (
                "identifiant_adresse_etablissement",
                "identifiantAdresseEtablissement",
                "AD123456",
            ),
            (
                "coordonnee_lambert_abscisse_etablissement",
                "coordonneeLambertAbscisseEtablissement",
                "123456.78",
            ),
            (
                "coordonnee_lambert_ordonnee_etablissement",
                "coordonneeLambertOrdonneeEtablissement",
                "234567.89",
            ),
        ],
    )
    def test_field_deserialization(self, field_name, api_key, value):
        """Test individual field deserialization."""
        data = {api_key: value}

        adresse = Adresse.from_dict(data)
        assert getattr(adresse, field_name) == value
