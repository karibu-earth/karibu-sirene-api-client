#!/usr/bin/env python3
"""
Test suite for null value handling in SIRENE API client models.

This test suite verifies that all model classes properly handle null values
from the API when masquer_valeurs_nulles=False.
"""

import datetime

import pytest

from sirene_api_client import AuthenticatedClient
from sirene_api_client.api.unite_legale.find_by_siren import sync
from sirene_api_client.api_types import UNSET
from sirene_api_client.models.dates_mise_a_jour_donnees import DatesMiseAJourDonnees
from sirene_api_client.models.etablissement import Etablissement
from sirene_api_client.models.periode_unite_legale import PeriodeUniteLegale
from sirene_api_client.models.unite_legale import UniteLegale


class TestNullValueHandling:
    """Test null value handling in model parsing."""

    @pytest.mark.requirement("REQ-NULL-001")
    def test_unite_legale_enum_fields_with_null_values(self):
        """Test that UniteLegale handles null enum values correctly."""
        # Test data with null enum values (what API returns when masquer_valeurs_nulles=False)
        test_data = {
            "siren": "552049447",
            "statutDiffusionUniteLegale": "O",
            "sexeUniteLegale": None,  # This should be handled as UNSET
            "categorieEntreprise": None,  # This should be handled as UNSET
            "denominationUniteLegale": "SOCIETE NATIONALE SNCF",
        }

        # This should NOT raise an exception
        unite_legale = UniteLegale.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert unite_legale.siren == "552049447"
        assert unite_legale.sexe_unite_legale is UNSET
        assert unite_legale.categorie_entreprise is UNSET

    @pytest.mark.requirement("REQ-NULL-002")
    def test_unite_legale_date_fields_with_null_values(self):
        """Test that UniteLegale handles null date values correctly."""
        test_data = {
            "siren": "552049447",
            "dateCreationUniteLegale": None,  # This should be handled as UNSET
            "dateNaissanceUniteLegale": None,  # This should be handled as UNSET
        }

        # This should NOT raise an exception
        unite_legale = UniteLegale.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert unite_legale.date_creation_unite_legale is UNSET
        assert unite_legale.date_naissance_unite_legale is UNSET

    @pytest.mark.requirement("REQ-NULL-003")
    def test_periode_unite_legale_enum_fields_with_null_values(self):
        """Test that PeriodeUniteLegale handles null enum values correctly."""
        test_data = {
            "dateDebut": "2025-10-15",
            "etatAdministratifUniteLegale": "A",
            "nomenclatureActivitePrincipaleUniteLegale": None,  # This should be handled as UNSET
            "caractereEmployeurUniteLegale": None,  # This should be handled as UNSET
        }

        # This should NOT raise an exception
        periode = PeriodeUniteLegale.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert periode.date_debut == datetime.date(2025, 10, 15)
        assert periode.nomenclature_activite_principale_unite_legale is UNSET
        assert periode.caractere_employeur_unite_legale is UNSET

    @pytest.mark.requirement("REQ-NULL-004")
    def test_periode_unite_legale_date_fields_with_null_values(self):
        """Test that PeriodeUniteLegale handles null date values correctly."""
        test_data = {
            "dateDebut": "2025-10-15",
            "dateFin": None,  # This should be handled as UNSET
            "etatAdministratifUniteLegale": "A",
        }

        # This should NOT raise an exception
        periode = PeriodeUniteLegale.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert periode.date_debut == datetime.date(2025, 10, 15)
        assert periode.date_fin is UNSET

    @pytest.mark.requirement("REQ-NULL-005")
    def test_etablissement_date_fields_with_null_values(self):
        """Test that Etablissement handles null date values correctly."""
        test_data = {
            "siret": "55204944776279",
            "dateCreationEtablissement": None,  # This should be handled as UNSET
            "dateDernierTraitementEtablissement": None,  # This should be handled as UNSET
        }

        # This should NOT raise an exception
        etablissement = Etablissement.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert etablissement.date_creation_etablissement is UNSET
        assert etablissement.date_dernier_traitement_etablissement is UNSET

    @pytest.mark.requirement("REQ-NULL-006")
    def test_dates_mise_a_jour_donnees_datetime_fields_with_null_values(self):
        """Test that DatesMiseAJourDonnees handles null datetime values correctly."""
        test_data = {
            "collection": "Unités Légales",  # Valid enum value
            "dateDerniereMiseADisposition": None,  # This should be handled as UNSET
            "dateDernierTraitementMaximum": None,  # This should be handled as UNSET
            "dateDernierTraitementDeMasse": None,  # This should be handled as UNSET
        }

        # This should NOT raise an exception
        dates = DatesMiseAJourDonnees.from_dict(test_data)

        # Verify null values are converted to UNSET
        assert dates.date_derniere_mise_a_disposition is UNSET
        assert dates.date_dernier_traitement_maximum is UNSET
        assert dates.date_dernier_traitement_de_masse is UNSET

    @pytest.mark.requirement("REQ-NULL-007")
    def test_mixed_null_and_valid_values(self):
        """Test handling of mixed null and valid values."""
        test_data = {
            "siren": "552049447",
            "statutDiffusionUniteLegale": "O",
            "sexeUniteLegale": None,  # null
            "categorieEntreprise": "GE",  # valid
            "dateCreationUniteLegale": "1955-01-01",  # valid
            "dateNaissanceUniteLegale": None,  # null
        }

        # This should NOT raise an exception
        unite_legale = UniteLegale.from_dict(test_data)

        # Verify mixed handling
        assert unite_legale.siren == "552049447"
        assert unite_legale.statut_diffusion_unite_legale == "O"
        assert unite_legale.sexe_unite_legale is UNSET  # null -> UNSET
        assert unite_legale.categorie_entreprise.value == "GE"  # valid -> enum
        assert unite_legale.date_creation_unite_legale == datetime.date(
            1955, 1, 1
        )  # valid -> date
        assert unite_legale.date_naissance_unite_legale is UNSET  # null -> UNSET


class TestIntegrationNullValueHandling:
    """Integration tests for null value handling with actual API."""

    @pytest.mark.requirement("REQ-NULL-008")
    def test_api_call_with_masquer_valeurs_nulles_false(self):
        """Test that API calls work with masquer_valeurs_nulles=False."""
        client = AuthenticatedClient(
            base_url="https://api.insee.fr/api-sirene/3.11",
            token="33cf9797-9541-4bd4-8aee-5354bec491ca",
            prefix="",
            auth_header_name="X-INSEE-Api-Key-Integration",
        )

        # This should NOT raise an exception
        result = sync(siren="552049447", client=client, masquer_valeurs_nulles=False)

        # Verify we get a valid response
        assert result is not None
        assert hasattr(result, "unite_legale")
        assert result.unite_legale is not None
        assert result.unite_legale.siren == "552049447"

        # Verify null fields are handled as UNSET
        assert result.unite_legale.sexe_unite_legale is UNSET
        assert result.unite_legale.prenom_1_unite_legale is UNSET

    @pytest.mark.requirement("REQ-NULL-009")
    def test_api_call_with_masquer_valeurs_nulles_true(self):
        """Test that API calls still work with masquer_valeurs_nulles=True (regression test)."""
        client = AuthenticatedClient(
            base_url="https://api.insee.fr/api-sirene/3.11",
            token="33cf9797-9541-4bd4-8aee-5354bec491ca",
            prefix="",
            auth_header_name="X-INSEE-Api-Key-Integration",
        )

        # This should NOT raise an exception
        result = sync(siren="552049447", client=client, masquer_valeurs_nulles=True)

        # Verify we get a valid response
        assert result is not None
        assert hasattr(result, "unite_legale")
        assert result.unite_legale is not None
        assert result.unite_legale.siren == "552049447"

        # Verify null fields are handled as UNSET (excluded from API response)
        assert result.unite_legale.sexe_unite_legale is UNSET
        assert result.unite_legale.prenom_1_unite_legale is UNSET
