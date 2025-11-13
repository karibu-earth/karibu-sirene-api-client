"""Tests for sirene_api_client.models.adresse_complementaire module."""

import pytest

from sirene_api_client.api_types import UNSET
from sirene_api_client.models.adresse_complementaire import AdresseComplementaire


@pytest.mark.requirement("REQ-MODEL-005")
class TestAdresseComplementaire:
    """Test AdresseComplementaire model."""

    def test_initialization_with_all_fields(self):
        """Test initialization with all fields populated."""
        adresse_complementaire = AdresseComplementaire(
            complement_adresse_2_etablissement="Bâtiment B",
            numero_voie_2_etablissement="456",
            indice_repetition_2_etablissement="C",
            type_voie_2_etablissement="AVENUE",
            libelle_voie_2_etablissement="des Champs-Élysées",
            code_postal_2_etablissement="75008",
            libelle_commune_2_etablissement="Paris",
            libelle_commune_etranger_2_etablissement="Berlin",
            distribution_speciale_2_etablissement="BP 456",
            code_commune_2_etablissement="75108",
            code_cedex_2_etablissement="54321",
            libelle_cedex_2_etablissement="PARIS CEDEX 08",
            code_pays_etranger_2_etablissement="DE",
            libelle_pays_etranger_2_etablissement="Allemagne",
        )

        assert adresse_complementaire.complement_adresse_2_etablissement == "Bâtiment B"
        assert adresse_complementaire.numero_voie_2_etablissement == "456"
        assert adresse_complementaire.indice_repetition_2_etablissement == "C"
        assert adresse_complementaire.type_voie_2_etablissement == "AVENUE"
        assert (
            adresse_complementaire.libelle_voie_2_etablissement == "des Champs-Élysées"
        )
        assert adresse_complementaire.code_postal_2_etablissement == "75008"
        assert adresse_complementaire.libelle_commune_2_etablissement == "Paris"
        assert (
            adresse_complementaire.libelle_commune_etranger_2_etablissement == "Berlin"
        )
        assert adresse_complementaire.distribution_speciale_2_etablissement == "BP 456"
        assert adresse_complementaire.code_commune_2_etablissement == "75108"
        assert adresse_complementaire.code_cedex_2_etablissement == "54321"
        assert adresse_complementaire.libelle_cedex_2_etablissement == "PARIS CEDEX 08"
        assert adresse_complementaire.code_pays_etranger_2_etablissement == "DE"
        assert (
            adresse_complementaire.libelle_pays_etranger_2_etablissement == "Allemagne"
        )

    def test_initialization_with_minimal_fields(self):
        """Test initialization with minimal required fields."""
        adresse_complementaire = AdresseComplementaire()

        assert adresse_complementaire.complement_adresse_2_etablissement is UNSET
        assert adresse_complementaire.numero_voie_2_etablissement is UNSET
        assert adresse_complementaire.indice_repetition_2_etablissement is UNSET
        assert adresse_complementaire.type_voie_2_etablissement is UNSET
        assert adresse_complementaire.libelle_voie_2_etablissement is UNSET
        assert adresse_complementaire.code_postal_2_etablissement is UNSET
        assert adresse_complementaire.libelle_commune_2_etablissement is UNSET
        assert adresse_complementaire.libelle_commune_etranger_2_etablissement is UNSET
        assert adresse_complementaire.distribution_speciale_2_etablissement is UNSET
        assert adresse_complementaire.code_commune_2_etablissement is UNSET
        assert adresse_complementaire.code_cedex_2_etablissement is UNSET
        assert adresse_complementaire.libelle_cedex_2_etablissement is UNSET
        assert adresse_complementaire.code_pays_etranger_2_etablissement is UNSET
        assert adresse_complementaire.libelle_pays_etranger_2_etablissement is UNSET

    def test_to_dict_with_all_fields(self):
        """Test to_dict with all fields populated."""
        adresse_complementaire = AdresseComplementaire(
            complement_adresse_2_etablissement="Bâtiment B",
            numero_voie_2_etablissement="456",
            indice_repetition_2_etablissement="C",
            type_voie_2_etablissement="AVENUE",
            libelle_voie_2_etablissement="des Champs-Élysées",
            code_postal_2_etablissement="75008",
            libelle_commune_2_etablissement="Paris",
            libelle_commune_etranger_2_etablissement="Berlin",
            distribution_speciale_2_etablissement="BP 456",
            code_commune_2_etablissement="75108",
            code_cedex_2_etablissement="54321",
            libelle_cedex_2_etablissement="PARIS CEDEX 08",
            code_pays_etranger_2_etablissement="DE",
            libelle_pays_etranger_2_etablissement="Allemagne",
        )

        result = adresse_complementaire.to_dict()

        assert result["complementAdresse2Etablissement"] == "Bâtiment B"
        assert result["numeroVoie2Etablissement"] == "456"
        assert result["indiceRepetition2Etablissement"] == "C"
        assert result["typeVoie2Etablissement"] == "AVENUE"
        assert result["libelleVoie2Etablissement"] == "des Champs-Élysées"
        assert result["codePostal2Etablissement"] == "75008"
        assert result["libelleCommune2Etablissement"] == "Paris"
        assert result["libelleCommuneEtranger2Etablissement"] == "Berlin"
        assert result["distributionSpeciale2Etablissement"] == "BP 456"
        assert result["codeCommune2Etablissement"] == "75108"
        assert result["codeCedex2Etablissement"] == "54321"
        assert result["libelleCedex2Etablissement"] == "PARIS CEDEX 08"
        assert result["codePaysEtranger2Etablissement"] == "DE"
        assert result["libellePaysEtranger2Etablissement"] == "Allemagne"

    def test_to_dict_with_unset_fields(self):
        """Test to_dict excludes UNSET fields."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="456",  # Only set one field
        )

        result = adresse_complementaire.to_dict()

        assert result["numeroVoie2Etablissement"] == "456"
        assert "complementAdresse2Etablissement" not in result
        assert "indiceRepetition2Etablissement" not in result
        assert "typeVoie2Etablissement" not in result
        assert "libelleVoie2Etablissement" not in result
        assert "codePostal2Etablissement" not in result
        assert "libelleCommune2Etablissement" not in result
        assert "libelleCommuneEtranger2Etablissement" not in result
        assert "distributionSpeciale2Etablissement" not in result
        assert "codeCommune2Etablissement" not in result
        assert "codeCedex2Etablissement" not in result
        assert "libelleCedex2Etablissement" not in result
        assert "codePaysEtranger2Etablissement" not in result
        assert "libellePaysEtranger2Etablissement" not in result

    def test_from_dict_with_complete_data(self):
        """Test from_dict with complete data."""
        data = {
            "complementAdresse2Etablissement": "Bâtiment B",
            "numeroVoie2Etablissement": "456",
            "indiceRepetition2Etablissement": "C",
            "typeVoie2Etablissement": "AVENUE",
            "libelleVoie2Etablissement": "des Champs-Élysées",
            "codePostal2Etablissement": "75008",
            "libelleCommune2Etablissement": "Paris",
            "libelleCommuneEtranger2Etablissement": "Berlin",
            "distributionSpeciale2Etablissement": "BP 456",
            "codeCommune2Etablissement": "75108",
            "codeCedex2Etablissement": "54321",
            "libelleCedex2Etablissement": "PARIS CEDEX 08",
            "codePaysEtranger2Etablissement": "DE",
            "libellePaysEtranger2Etablissement": "Allemagne",
        }

        adresse_complementaire = AdresseComplementaire.from_dict(data)

        assert adresse_complementaire.complement_adresse_2_etablissement == "Bâtiment B"
        assert adresse_complementaire.numero_voie_2_etablissement == "456"
        assert adresse_complementaire.indice_repetition_2_etablissement == "C"
        assert adresse_complementaire.type_voie_2_etablissement == "AVENUE"
        assert (
            adresse_complementaire.libelle_voie_2_etablissement == "des Champs-Élysées"
        )
        assert adresse_complementaire.code_postal_2_etablissement == "75008"
        assert adresse_complementaire.libelle_commune_2_etablissement == "Paris"
        assert (
            adresse_complementaire.libelle_commune_etranger_2_etablissement == "Berlin"
        )
        assert adresse_complementaire.distribution_speciale_2_etablissement == "BP 456"
        assert adresse_complementaire.code_commune_2_etablissement == "75108"
        assert adresse_complementaire.code_cedex_2_etablissement == "54321"
        assert adresse_complementaire.libelle_cedex_2_etablissement == "PARIS CEDEX 08"
        assert adresse_complementaire.code_pays_etranger_2_etablissement == "DE"
        assert (
            adresse_complementaire.libelle_pays_etranger_2_etablissement == "Allemagne"
        )

    def test_from_dict_with_missing_optional_fields(self):
        """Test from_dict with missing optional fields."""
        data = {
            "numeroVoie2Etablissement": "456",  # Only required field
        }

        adresse_complementaire = AdresseComplementaire.from_dict(data)

        assert adresse_complementaire.numero_voie_2_etablissement == "456"
        assert adresse_complementaire.complement_adresse_2_etablissement is UNSET
        assert adresse_complementaire.indice_repetition_2_etablissement is UNSET
        assert adresse_complementaire.type_voie_2_etablissement is UNSET
        assert adresse_complementaire.libelle_voie_2_etablissement is UNSET
        assert adresse_complementaire.code_postal_2_etablissement is UNSET
        assert adresse_complementaire.libelle_commune_2_etablissement is UNSET
        assert adresse_complementaire.libelle_commune_etranger_2_etablissement is UNSET
        assert adresse_complementaire.distribution_speciale_2_etablissement is UNSET
        assert adresse_complementaire.code_commune_2_etablissement is UNSET
        assert adresse_complementaire.code_cedex_2_etablissement is UNSET
        assert adresse_complementaire.libelle_cedex_2_etablissement is UNSET
        assert adresse_complementaire.code_pays_etranger_2_etablissement is UNSET
        assert adresse_complementaire.libelle_pays_etranger_2_etablissement is UNSET

    def test_from_dict_with_null_values(self):
        """Test from_dict with null values."""
        data = {
            "numeroVoie2Etablissement": "456",
            "complementAdresse2Etablissement": None,
            "indiceRepetition2Etablissement": None,
            "typeVoie2Etablissement": None,
            "libelleVoie2Etablissement": None,
            "codePostal2Etablissement": None,
            "libelleCommune2Etablissement": None,
            "libelleCommuneEtranger2Etablissement": None,
            "distributionSpeciale2Etablissement": None,
            "codeCommune2Etablissement": None,
            "codeCedex2Etablissement": None,
            "libelleCedex2Etablissement": None,
            "codePaysEtranger2Etablissement": None,
            "libellePaysEtranger2Etablissement": None,
        }

        adresse_complementaire = AdresseComplementaire.from_dict(data)

        assert adresse_complementaire.numero_voie_2_etablissement == "456"
        assert adresse_complementaire.complement_adresse_2_etablissement is None
        assert adresse_complementaire.indice_repetition_2_etablissement is None
        assert adresse_complementaire.type_voie_2_etablissement is None
        assert adresse_complementaire.libelle_voie_2_etablissement is None
        assert adresse_complementaire.code_postal_2_etablissement is None
        assert adresse_complementaire.libelle_commune_2_etablissement is None
        assert adresse_complementaire.libelle_commune_etranger_2_etablissement is None
        assert adresse_complementaire.distribution_speciale_2_etablissement is None
        assert adresse_complementaire.code_commune_2_etablissement is None
        assert adresse_complementaire.code_cedex_2_etablissement is None
        assert adresse_complementaire.libelle_cedex_2_etablissement is None
        assert adresse_complementaire.code_pays_etranger_2_etablissement is None
        assert adresse_complementaire.libelle_pays_etranger_2_etablissement is None

    def test_roundtrip_serialization(self):
        """Test that to_dict -> from_dict preserves data."""
        original = AdresseComplementaire(
            complement_adresse_2_etablissement="Bâtiment B",
            numero_voie_2_etablissement="456",
            indice_repetition_2_etablissement="C",
            type_voie_2_etablissement="AVENUE",
            libelle_voie_2_etablissement="des Champs-Élysées",
            code_postal_2_etablissement="75008",
            libelle_commune_2_etablissement="Paris",
            libelle_commune_etranger_2_etablissement="Berlin",
            distribution_speciale_2_etablissement="BP 456",
            code_commune_2_etablissement="75108",
            code_cedex_2_etablissement="54321",
            libelle_cedex_2_etablissement="PARIS CEDEX 08",
            code_pays_etranger_2_etablissement="DE",
            libelle_pays_etranger_2_etablissement="Allemagne",
        )

        # Add some additional properties
        original["custom_field"] = "custom_value"

        # Serialize and deserialize
        data = original.to_dict()
        restored = AdresseComplementaire.from_dict(data)

        # Verify all fields are preserved
        assert (
            restored.complement_adresse_2_etablissement
            == original.complement_adresse_2_etablissement
        )
        assert (
            restored.numero_voie_2_etablissement == original.numero_voie_2_etablissement
        )
        assert (
            restored.indice_repetition_2_etablissement
            == original.indice_repetition_2_etablissement
        )
        assert restored.type_voie_2_etablissement == original.type_voie_2_etablissement
        assert (
            restored.libelle_voie_2_etablissement
            == original.libelle_voie_2_etablissement
        )
        assert (
            restored.code_postal_2_etablissement == original.code_postal_2_etablissement
        )
        assert (
            restored.libelle_commune_2_etablissement
            == original.libelle_commune_2_etablissement
        )
        assert (
            restored.libelle_commune_etranger_2_etablissement
            == original.libelle_commune_etranger_2_etablissement
        )
        assert (
            restored.distribution_speciale_2_etablissement
            == original.distribution_speciale_2_etablissement
        )
        assert (
            restored.code_commune_2_etablissement
            == original.code_commune_2_etablissement
        )
        assert (
            restored.code_cedex_2_etablissement == original.code_cedex_2_etablissement
        )
        assert (
            restored.libelle_cedex_2_etablissement
            == original.libelle_cedex_2_etablissement
        )
        assert (
            restored.code_pays_etranger_2_etablissement
            == original.code_pays_etranger_2_etablissement
        )
        assert (
            restored.libelle_pays_etranger_2_etablissement
            == original.libelle_pays_etranger_2_etablissement
        )
        assert restored["custom_field"] == "custom_value"

    def test_additional_properties_getitem(self):
        """Test __getitem__ for additional properties."""
        adresse_complementaire = AdresseComplementaire()
        adresse_complementaire["custom_field"] = "custom_value"

        assert adresse_complementaire["custom_field"] == "custom_value"

    def test_additional_properties_setitem(self):
        """Test __setitem__ for additional properties."""
        adresse_complementaire = AdresseComplementaire()
        adresse_complementaire["custom_field"] = "custom_value"

        assert (
            adresse_complementaire.additional_properties["custom_field"]
            == "custom_value"
        )

    def test_additional_properties_delitem(self):
        """Test __delitem__ for additional properties."""
        adresse_complementaire = AdresseComplementaire()
        adresse_complementaire["custom_field"] = "custom_value"

        del adresse_complementaire["custom_field"]

        assert "custom_field" not in adresse_complementaire.additional_properties

    def test_additional_properties_contains(self):
        """Test __contains__ for additional properties."""
        adresse_complementaire = AdresseComplementaire()
        adresse_complementaire["custom_field"] = "custom_value"

        assert "custom_field" in adresse_complementaire
        assert "nonexistent_field" not in adresse_complementaire

    def test_additional_keys_property(self):
        """Test additional_keys property."""
        adresse_complementaire = AdresseComplementaire()
        adresse_complementaire["field1"] = "value1"
        adresse_complementaire["field2"] = "value2"

        keys = adresse_complementaire.additional_keys
        assert "field1" in keys
        assert "field2" in keys
        assert len(keys) == 2

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="456",
            libelle_voie_2_etablissement="Rue de l'Église",
            libelle_commune_2_etablissement="Saint-Étienne",
            libelle_pays_etranger_2_etablissement="Côte d'Ivoire",
        )
        adresse_complementaire["unicode_field"] = "Café & Société 🏢"

        result = adresse_complementaire.to_dict()
        assert result["libelleVoie2Etablissement"] == "Rue de l'Église"
        assert result["libelleCommune2Etablissement"] == "Saint-Étienne"
        assert result["libellePaysEtranger2Etablissement"] == "Côte d'Ivoire"
        assert result["unicode_field"] == "Café & Société 🏢"

        # Test roundtrip with Unicode
        restored = AdresseComplementaire.from_dict(result)
        assert restored.libelle_voie_2_etablissement == "Rue de l'Église"
        assert restored.libelle_commune_2_etablissement == "Saint-Étienne"
        assert restored.libelle_pays_etranger_2_etablissement == "Côte d'Ivoire"
        assert restored["unicode_field"] == "Café & Société 🏢"

    def test_empty_strings_vs_unset(self):
        """Test empty strings vs UNSET handling."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="456",
            libelle_voie_2_etablissement="",  # Empty string
            code_postal_2_etablissement=UNSET,  # UNSET
        )

        result = adresse_complementaire.to_dict()
        assert result["numeroVoie2Etablissement"] == "456"
        assert result["libelleVoie2Etablissement"] == ""
        assert "codePostal2Etablissement" not in result  # UNSET should be excluded

    def test_french_address_handling(self):
        """Test French address handling."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="456",
            indice_repetition_2_etablissement="C",
            type_voie_2_etablissement="AVENUE",
            libelle_voie_2_etablissement="des Champs-Élysées",
            code_postal_2_etablissement="75008",
            libelle_commune_2_etablissement="Paris",
            code_commune_2_etablissement="75108",
            code_cedex_2_etablissement="54321",
            libelle_cedex_2_etablissement="PARIS CEDEX 08",
        )

        result = adresse_complementaire.to_dict()
        assert result["numeroVoie2Etablissement"] == "456"
        assert result["indiceRepetition2Etablissement"] == "C"
        assert result["typeVoie2Etablissement"] == "AVENUE"
        assert result["libelleVoie2Etablissement"] == "des Champs-Élysées"
        assert result["codePostal2Etablissement"] == "75008"
        assert result["libelleCommune2Etablissement"] == "Paris"
        assert result["codeCommune2Etablissement"] == "75108"
        assert result["codeCedex2Etablissement"] == "54321"
        assert result["libelleCedex2Etablissement"] == "PARIS CEDEX 08"

    def test_foreign_address_handling(self):
        """Test foreign address handling."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="789",
            type_voie_2_etablissement="STREET",
            libelle_voie_2_etablissement="Baker Street",
            libelle_commune_etranger_2_etablissement="London",
            code_pays_etranger_2_etablissement="GB",
            libelle_pays_etranger_2_etablissement="United Kingdom",
        )

        result = adresse_complementaire.to_dict()
        assert result["numeroVoie2Etablissement"] == "789"
        assert result["typeVoie2Etablissement"] == "STREET"
        assert result["libelleVoie2Etablissement"] == "Baker Street"
        assert result["libelleCommuneEtranger2Etablissement"] == "London"
        assert result["codePaysEtranger2Etablissement"] == "GB"
        assert result["libellePaysEtranger2Etablissement"] == "United Kingdom"

    def test_special_distribution_handling(self):
        """Test special distribution handling."""
        adresse_complementaire = AdresseComplementaire(
            numero_voie_2_etablissement="000",
            distribution_speciale_2_etablissement="BP 456",
        )

        result = adresse_complementaire.to_dict()
        assert result["numeroVoie2Etablissement"] == "000"
        assert result["distributionSpeciale2Etablissement"] == "BP 456"

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            (
                "complement_adresse_2_etablissement",
                "complementAdresse2Etablissement",
                "Bâtiment B",
            ),
            ("numero_voie_2_etablissement", "numeroVoie2Etablissement", "456"),
            (
                "indice_repetition_2_etablissement",
                "indiceRepetition2Etablissement",
                "C",
            ),
            ("type_voie_2_etablissement", "typeVoie2Etablissement", "AVENUE"),
            (
                "libelle_voie_2_etablissement",
                "libelleVoie2Etablissement",
                "des Champs-Élysées",
            ),
            ("code_postal_2_etablissement", "codePostal2Etablissement", "75008"),
            (
                "libelle_commune_2_etablissement",
                "libelleCommune2Etablissement",
                "Paris",
            ),
            (
                "libelle_commune_etranger_2_etablissement",
                "libelleCommuneEtranger2Etablissement",
                "Berlin",
            ),
            (
                "distribution_speciale_2_etablissement",
                "distributionSpeciale2Etablissement",
                "BP 456",
            ),
            ("code_commune_2_etablissement", "codeCommune2Etablissement", "75108"),
            ("code_cedex_2_etablissement", "codeCedex2Etablissement", "54321"),
            (
                "libelle_cedex_2_etablissement",
                "libelleCedex2Etablissement",
                "PARIS CEDEX 08",
            ),
            (
                "code_pays_etranger_2_etablissement",
                "codePaysEtranger2Etablissement",
                "DE",
            ),
            (
                "libelle_pays_etranger_2_etablissement",
                "libellePaysEtranger2Etablissement",
                "Allemagne",
            ),
        ],
    )
    def test_field_serialization(self, field_name, api_key, value):
        """Test individual field serialization."""
        adresse_complementaire = AdresseComplementaire(**{field_name: value})

        result = adresse_complementaire.to_dict()
        assert result[api_key] == value

    @pytest.mark.parametrize(
        ("field_name", "api_key", "value"),
        [
            (
                "complement_adresse_2_etablissement",
                "complementAdresse2Etablissement",
                "Bâtiment B",
            ),
            ("numero_voie_2_etablissement", "numeroVoie2Etablissement", "456"),
            (
                "indice_repetition_2_etablissement",
                "indiceRepetition2Etablissement",
                "C",
            ),
            ("type_voie_2_etablissement", "typeVoie2Etablissement", "AVENUE"),
            (
                "libelle_voie_2_etablissement",
                "libelleVoie2Etablissement",
                "des Champs-Élysées",
            ),
            ("code_postal_2_etablissement", "codePostal2Etablissement", "75008"),
            (
                "libelle_commune_2_etablissement",
                "libelleCommune2Etablissement",
                "Paris",
            ),
            (
                "libelle_commune_etranger_2_etablissement",
                "libelleCommuneEtranger2Etablissement",
                "Berlin",
            ),
            (
                "distribution_speciale_2_etablissement",
                "distributionSpeciale2Etablissement",
                "BP 456",
            ),
            ("code_commune_2_etablissement", "codeCommune2Etablissement", "75108"),
            ("code_cedex_2_etablissement", "codeCedex2Etablissement", "54321"),
            (
                "libelle_cedex_2_etablissement",
                "libelleCedex2Etablissement",
                "PARIS CEDEX 08",
            ),
            (
                "code_pays_etranger_2_etablissement",
                "codePaysEtranger2Etablissement",
                "DE",
            ),
            (
                "libelle_pays_etranger_2_etablissement",
                "libellePaysEtranger2Etablissement",
                "Allemagne",
            ),
        ],
    )
    def test_field_deserialization(self, field_name, api_key, value):
        """Test individual field deserialization."""
        data = {api_key: value}

        adresse_complementaire = AdresseComplementaire.from_dict(data)
        assert getattr(adresse_complementaire, field_name) == value
