"""Tests for sirene_api_client.models.reponse_informations_etat_service module."""

import pytest

from sirene_api_client.models.reponse_informations_etat_service import (
    ReponseInformationsEtatService,
)


@pytest.mark.requirement("REQ-MODEL-006")
class TestReponseInformationsEtatService:
    """Test ReponseInformationsEtatService enum."""

    def test_enum_values(self):
        """Test enum values."""
        assert ReponseInformationsEtatService.UP == "UP"
        assert ReponseInformationsEtatService.DOWN == "DOWN"

    def test_enum_membership(self):
        """Test enum membership."""
        assert "UP" in ReponseInformationsEtatService
        assert "DOWN" in ReponseInformationsEtatService

    def test_enum_iteration(self):
        """Test enum iteration."""
        values = list(ReponseInformationsEtatService)
        assert len(values) == 2
        assert ReponseInformationsEtatService.UP in values
        assert ReponseInformationsEtatService.DOWN in values

    def test_enum_str_method(self):
        """Test __str__ method."""
        assert str(ReponseInformationsEtatService.UP) == "UP"
        assert str(ReponseInformationsEtatService.DOWN) == "DOWN"

    def test_enum_inheritance(self):
        """Test enum inheritance from str."""
        assert isinstance(ReponseInformationsEtatService.UP, str)
        assert isinstance(ReponseInformationsEtatService.DOWN, str)

    def test_enum_comparison(self):
        """Test enum comparison."""
        assert ReponseInformationsEtatService.UP == "UP"
        assert ReponseInformationsEtatService.DOWN == "DOWN"

    def test_enum_name_access(self):
        """Test enum name access."""
        assert ReponseInformationsEtatService.UP.name == "UP"
        assert ReponseInformationsEtatService.DOWN.name == "DOWN"

    def test_enum_value_access(self):
        """Test enum value access."""
        assert ReponseInformationsEtatService.UP.value == "UP"
        assert ReponseInformationsEtatService.DOWN.value == "DOWN"
