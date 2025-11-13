"""Tests for informations module."""

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from sirene_api_client.api.informations.informations import (
    _build_response,
    _get_kwargs,
    _parse_response,
    asyncio,
    asyncio_detailed,
    sync,
    sync_detailed,
)
from sirene_api_client.errors import UnexpectedStatusError
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_informations import ReponseInformations


@pytest.mark.requirement("REQ-API-050")
class TestGetKwargs:
    """Test _get_kwargs function."""

    def test_get_kwargs_no_parameters(self):
        """Test _get_kwargs with no parameters."""
        kwargs = _get_kwargs()

        assert kwargs["method"] == "get"
        assert kwargs["url"] == "/informations"


@pytest.mark.requirement("REQ-API-051")
class TestParseResponse:
    """Test _parse_response function."""

    def test_parse_response_200_success(self):
        """Test parsing successful response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"version": "1.0", "etatService": "UP"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseInformations)
        mock_response.json.assert_called_once()

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


@pytest.mark.requirement("REQ-API-052")
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
            "sirene_api_client.api.informations.informations._parse_response"
        ) as mock_parse:
            mock_parse.return_value = ReponseInformations.from_dict(
                {"version": "1.0", "etatService": "UP"}
            )

            result = _build_response(client=mock_client, response=mock_response)

            assert result.status_code == HTTPStatus.OK
            assert result.content == b"test content"
            assert result.headers == {"Content-Type": "application/json"}
            assert result.parsed is not None


@pytest.mark.requirement("REQ-API-053")
class TestSyncDetailed:
    """Test sync_detailed function."""

    def test_sync_detailed_success(self):
        """Test successful sync_detailed call."""
        mock_client = Mock()
        mock_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"version": "1.0", "etatService": "UP"}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        mock_client.get_httpx_client.return_value = mock_httpx_client
        mock_httpx_client.request.return_value = mock_response

        result = sync_detailed(client=mock_client)

        assert result.status_code == HTTPStatus.OK
        mock_httpx_client.request.assert_called_once()


@pytest.mark.requirement("REQ-API-054")
class TestSync:
    """Test sync function."""

    def test_sync_success(self):
        """Test successful sync call."""
        mock_client = Mock()

        with patch(
            "sirene_api_client.api.informations.informations.sync_detailed"
        ) as mock_sync_detailed:
            mock_sync_detailed.return_value.parsed = ReponseInformations.from_dict(
                {"version": "1.0", "etatService": "UP"}
            )

            result = sync(client=mock_client)

            assert result is not None
            mock_sync_detailed.assert_called_once()


@pytest.mark.requirement("REQ-API-055")
class TestAsyncioDetailed:
    """Test asyncio_detailed function."""

    @pytest.mark.asyncio
    async def test_asyncio_detailed_success(self):
        """Test successful asyncio_detailed call."""
        mock_client = Mock()
        mock_async_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"version": "1.0", "etatService": "UP"}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        # Create an async mock function

        async def mock_request(**_kwargs):
            return mock_response

        mock_client.get_async_httpx_client.return_value = mock_async_httpx_client

        mock_async_httpx_client.request = mock_request

        result = await asyncio_detailed(client=mock_client)

        assert result.status_code == HTTPStatus.OK


@pytest.mark.requirement("REQ-API-056")
class TestAsyncio:
    """Test asyncio function."""

    @pytest.mark.asyncio
    async def test_asyncio_success(self):
        """Test successful asyncio call."""
        mock_client = Mock()

        with patch(
            "sirene_api_client.api.informations.informations.asyncio_detailed"
        ) as mock_asyncio_detailed:
            mock_asyncio_detailed.return_value.parsed = ReponseInformations.from_dict(
                {"version": "1.0", "etatService": "UP"}
            )

            result = await asyncio(client=mock_client)

            assert result is not None
            mock_asyncio_detailed.assert_called_once()
