"""Tests for sirene_api_client.models.find_lien_succession_tri module."""

import pytest

from sirene_api_client.models.find_lien_succession_tri import FindLienSuccessionTri


@pytest.mark.requirement("REQ-MODEL-005")
class TestFindLienSuccessionTri:
    """Test FindLienSuccessionTri enum."""

    def test_enum_values(self):
        """Test enum values."""
        assert FindLienSuccessionTri.SUCCESSEUR == "successeur"

    def test_enum_membership(self):
        """Test enum membership."""
        assert "successeur" in FindLienSuccessionTri

    def test_enum_iteration(self):
        """Test enum iteration."""
        values = list(FindLienSuccessionTri)
        assert len(values) == 1
        assert FindLienSuccessionTri.SUCCESSEUR in values

    def test_enum_str_method(self):
        """Test __str__ method."""
        assert str(FindLienSuccessionTri.SUCCESSEUR) == "successeur"

    def test_enum_inheritance(self):
        """Test enum inheritance from str."""
        assert isinstance(FindLienSuccessionTri.SUCCESSEUR, str)

    def test_enum_comparison(self):
        """Test enum comparison."""
        assert FindLienSuccessionTri.SUCCESSEUR == "successeur"

    def test_enum_name_access(self):
        """Test enum name access."""
        assert FindLienSuccessionTri.SUCCESSEUR.name == "SUCCESSEUR"

    def test_enum_value_access(self):
        """Test enum value access."""
        assert FindLienSuccessionTri.SUCCESSEUR.value == "successeur"
