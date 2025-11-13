"""Tests for unite_legale find_by_siren module."""

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from sirene_api_client.api.unite_legale.find_by_siren import (
    _build_response,
    _get_kwargs,
    _parse_response,
    asyncio,
    asyncio_detailed,
    sync,
    sync_detailed,
)
from sirene_api_client.api_types import UNSET
from sirene_api_client.errors import UnexpectedStatusError
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_unite_legale import ReponseUniteLegale


@pytest.mark.requirement("REQ-API-043")
class TestGetKwargs:
    """Test _get_kwargs function."""

    def test_get_kwargs_with_siren_and_params(self):
        """Test _get_kwargs with siren and all parameters."""
        kwargs = _get_kwargs(
            siren="123456789",
            date="2023-01-01",
            champs="siren,denominationUniteLegale",
            masquer_valeurs_nulles=True,
        )

        assert kwargs["method"] == "get"
        assert kwargs["url"] == "/siren/123456789"
        assert kwargs["params"]["date"] == "2023-01-01"
        assert kwargs["params"]["champs"] == "siren,denominationUniteLegale"
        assert kwargs["params"]["masquerValeursNulles"] is True

    def test_get_kwargs_with_siren_only(self):
        """Test _get_kwargs with siren only."""
        kwargs = _get_kwargs(siren="123456789")

        assert kwargs["method"] == "get"
        assert kwargs["url"] == "/siren/123456789"
        assert "params" not in kwargs or not kwargs["params"]

    def test_get_kwargs_filters_unset_values(self):
        """Test _get_kwargs filters out UNSET values."""
        kwargs = _get_kwargs(
            siren="123456789",
            date=UNSET,
            champs="siren",
            masquer_valeurs_nulles=UNSET,
        )

        assert kwargs["params"]["champs"] == "siren"
        assert "date" not in kwargs["params"]
        assert "masquerValeursNulles" not in kwargs["params"]


@pytest.mark.requirement("REQ-API-044")
class TestParseResponse:
    """Test _parse_response function."""

    def test_parse_response_200_success(self):
        """Test parsing successful response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"uniteLegale": {}}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseUniteLegale)
        mock_response.json.assert_called_once()

    def test_parse_response_301_redirect(self):
        """Test parsing 301 redirect response."""
        mock_response = Mock()
        mock_response.status_code = 301
        mock_response.json.return_value = "redirect_url"

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result == "redirect_url"

    def test_parse_response_404_error(self):
        """Test parsing 404 error response."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Not found"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseErreur)

    def test_parse_response_500_error(self):
        """Test parsing 500 error response."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"message": "Internal server error"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseErreur)

    def test_parse_response_503_error(self):
        """Test parsing 503 error response."""
        mock_response = Mock()
        mock_response.status_code = 503
        mock_response.json.return_value = {"message": "Service unavailable"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseErreur)

    def test_parse_response_unexpected_status_with_raise_enabled(self):
        """Test parsing unexpected status with raise enabled."""
        mock_response = Mock()
        mock_response.status_code = 999
        mock_response.content = b"Unexpected response"

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = True

        with pytest.raises(UnexpectedStatusError):  # Should raise UnexpectedStatusError
            _parse_response(client=mock_client, response=mock_response)

    def test_parse_response_unexpected_status_with_raise_disabled(self):
        """Test parsing unexpected status with raise disabled."""
        mock_response = Mock()
        mock_response.status_code = 999
        mock_response.content = b"Unexpected response"

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None

    def test_parse_response_400_returns_none(self):
        """Test parsing 400 response returns None."""
        mock_response = Mock()
        mock_response.status_code = 400

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None

    def test_parse_response_401_returns_none(self):
        """Test parsing 401 response returns None."""
        mock_response = Mock()
        mock_response.status_code = 401

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None

    def test_parse_response_403_returns_none(self):
        """Test parsing 403 response returns None."""
        mock_response = Mock()
        mock_response.status_code = 403

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None

    def test_parse_response_406_returns_none(self):
        """Test parsing 406 response returns None."""
        mock_response = Mock()
        mock_response.status_code = 406

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None

    def test_parse_response_429_returns_none(self):
        """Test parsing 429 response returns None."""
        mock_response = Mock()
        mock_response.status_code = 429

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert result is None


@pytest.mark.requirement("REQ-API-045")
class TestBuildResponse:
    """Test _build_response function."""

    def test_build_response_success(self):
        """Test building response object."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        with patch(
            "sirene_api_client.api.unite_legale.find_by_siren._parse_response"
        ) as mock_parse:
            mock_parse.return_value = ReponseUniteLegale.from_dict({"uniteLegale": {}})

            result = _build_response(client=mock_client, response=mock_response)

            assert result.status_code == HTTPStatus.OK
            assert result.content == b"test content"
            assert result.headers == {"Content-Type": "application/json"}
            assert result.parsed is not None


@pytest.mark.requirement("REQ-API-046")
class TestSyncDetailed:
    """Test sync_detailed function."""

    def test_sync_detailed_success(self):
        """Test successful sync_detailed call."""
        mock_client = Mock()
        mock_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"uniteLegale": {}}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        mock_client.get_httpx_client.return_value = mock_httpx_client
        mock_httpx_client.request.return_value = mock_response

        result = sync_detailed(
            siren="123456789",
            client=mock_client,
            date="2023-01-01",
            champs="siren",
            masquer_valeurs_nulles=True,
        )

        assert result.status_code == HTTPStatus.OK
        mock_httpx_client.request.assert_called_once()

    def test_sync_detailed_with_minimal_params(self):
        """Test sync_detailed with minimal parameters."""
        mock_client = Mock()
        mock_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"uniteLegale": {}}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        mock_client.get_httpx_client.return_value = mock_httpx_client
        mock_httpx_client.request.return_value = mock_response

        result = sync_detailed(siren="123456789", client=mock_client)

        assert result.status_code == HTTPStatus.OK
        mock_httpx_client.request.assert_called_once()


@pytest.mark.requirement("REQ-API-047")
class TestSync:
    """Test sync function."""

    def test_sync_success(self):
        """Test successful sync call."""
        mock_client = Mock()

        with patch(
            "sirene_api_client.api.unite_legale.find_by_siren.sync_detailed"
        ) as mock_sync_detailed:
            mock_sync_detailed.return_value.parsed = ReponseUniteLegale.from_dict(
                {"uniteLegale": {}}
            )

            result = sync(
                siren="123456789",
                client=mock_client,
                date="2023-01-01",
            )

            assert result is not None
            mock_sync_detailed.assert_called_once()


@pytest.mark.requirement("REQ-API-048")
class TestAsyncioDetailed:
    """Test asyncio_detailed function."""

    @pytest.mark.asyncio
    async def test_asyncio_detailed_success(self):
        """Test successful asyncio_detailed call."""
        mock_client = Mock()
        mock_async_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"uniteLegale": {}}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        # Create an async mock function

        async def mock_request(**_kwargs):
            return mock_response

        mock_client.get_async_httpx_client.return_value = mock_async_httpx_client

        mock_async_httpx_client.request = mock_request

        result = await asyncio_detailed(
            siren="123456789",
            client=mock_client,
            date="2023-01-01",
        )

        assert result.status_code == HTTPStatus.OK


@pytest.mark.requirement("REQ-API-049")
class TestAsyncio:
    """Test asyncio function."""

    @pytest.mark.asyncio
    async def test_asyncio_success(self):
        """Test successful asyncio call."""
        mock_client = Mock()

        with patch(
            "sirene_api_client.api.unite_legale.find_by_siren.asyncio_detailed"
        ) as mock_asyncio_detailed:
            mock_asyncio_detailed.return_value.parsed = ReponseUniteLegale.from_dict(
                {"uniteLegale": {}}
            )

            result = await asyncio(
                siren="123456789",
                client=mock_client,
                date="2023-01-01",
            )

            assert result is not None
            mock_asyncio_detailed.assert_called_once()
