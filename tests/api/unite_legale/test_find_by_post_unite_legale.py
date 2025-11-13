"""Tests for unite_legale find_by_post_unite_legale module."""

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from sirene_api_client.api.unite_legale.find_by_post_unite_legale import (
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
from sirene_api_client.models.reponse_unites_legales import ReponseUnitesLegales
from sirene_api_client.models.unite_legale_post_multi_criteres import (
    UniteLegalePostMultiCriteres,
)


@pytest.mark.requirement("REQ-API-036")
class TestGetKwargs:
    """Test _get_kwargs function."""

    def test_get_kwargs_with_body(self):
        """Test _get_kwargs with body parameter."""
        mock_body = Mock(spec=UniteLegalePostMultiCriteres)
        mock_body.to_dict.return_value = {"q": "test query"}

        kwargs = _get_kwargs(body=mock_body)

        assert kwargs["method"] == "post"
        assert kwargs["url"] == "/siren"
        assert kwargs["data"] == {"q": "test query"}
        assert kwargs["headers"]["Content-Type"] == "application/x-www-form-urlencoded"
        mock_body.to_dict.assert_called_once()


@pytest.mark.requirement("REQ-API-037")
class TestParseResponse:
    """Test _parse_response function."""

    def test_parse_response_200_success(self):
        """Test parsing successful response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"unitesLegales": []}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseUnitesLegales)
        mock_response.json.assert_called_once()

    def test_parse_response_404_error(self):
        """Test parsing 404 error response."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Not found"}

        mock_client = Mock()
        mock_client.raise_on_unexpected_status = False

        result = _parse_response(client=mock_client, response=mock_response)

        assert isinstance(result, ReponseErreur)

    def test_parse_response_414_error(self):
        """Test parsing 414 error response."""
        mock_response = Mock()
        mock_response.status_code = 414
        mock_response.json.return_value = {"message": "URI too long"}

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


@pytest.mark.requirement("REQ-API-038")
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
            "sirene_api_client.api.unite_legale.find_by_post_unite_legale._parse_response"
        ) as mock_parse:
            mock_parse.return_value = ReponseUnitesLegales.from_dict(
                {"unitesLegales": []}
            )

            result = _build_response(client=mock_client, response=mock_response)

            assert result.status_code == HTTPStatus.OK
            assert result.content == b"test content"
            assert result.headers == {"Content-Type": "application/json"}
            assert result.parsed is not None


@pytest.mark.requirement("REQ-API-039")
class TestSyncDetailed:
    """Test sync_detailed function."""

    def test_sync_detailed_success(self):
        """Test successful sync_detailed call."""
        mock_client = Mock()
        mock_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"unitesLegales": []}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        mock_client.get_httpx_client.return_value = mock_httpx_client
        mock_httpx_client.request.return_value = mock_response

        mock_body = Mock(spec=UniteLegalePostMultiCriteres)
        mock_body.to_dict.return_value = {"q": "test query"}

        result = sync_detailed(client=mock_client, body=mock_body)

        assert result.status_code == HTTPStatus.OK
        mock_httpx_client.request.assert_called_once()


@pytest.mark.requirement("REQ-API-040")
class TestSync:
    """Test sync function."""

    def test_sync_success(self):
        """Test successful sync call."""
        mock_client = Mock()
        mock_body = Mock(spec=UniteLegalePostMultiCriteres)

        with patch(
            "sirene_api_client.api.unite_legale.find_by_post_unite_legale.sync_detailed"
        ) as mock_sync_detailed:
            mock_sync_detailed.return_value.parsed = ReponseUnitesLegales.from_dict(
                {"unitesLegales": []}
            )

            result = sync(client=mock_client, body=mock_body)

            assert result is not None
            mock_sync_detailed.assert_called_once()


@pytest.mark.requirement("REQ-API-041")
class TestAsyncioDetailed:
    """Test asyncio_detailed function."""

    @pytest.mark.asyncio
    async def test_asyncio_detailed_success(self):
        """Test successful asyncio_detailed call."""
        mock_client = Mock()
        mock_async_httpx_client = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"unitesLegales": []}
        mock_response.content = b"test content"
        mock_response.headers = {"Content-Type": "application/json"}

        # Create an async mock function

        async def mock_request(**_kwargs):
            return mock_response

        mock_client.get_async_httpx_client.return_value = mock_async_httpx_client

        mock_async_httpx_client.request = mock_request

        mock_body = Mock(spec=UniteLegalePostMultiCriteres)
        mock_body.to_dict.return_value = {"q": "test query"}

        result = await asyncio_detailed(client=mock_client, body=mock_body)

        assert result.status_code == HTTPStatus.OK


@pytest.mark.requirement("REQ-API-042")
class TestAsyncio:
    """Test asyncio function."""

    @pytest.mark.asyncio
    async def test_asyncio_success(self):
        """Test successful asyncio call."""
        mock_client = Mock()
        mock_body = Mock(spec=UniteLegalePostMultiCriteres)

        with patch(
            "sirene_api_client.api.unite_legale.find_by_post_unite_legale.asyncio_detailed"
        ) as mock_asyncio_detailed:
            mock_asyncio_detailed.return_value.parsed = ReponseUnitesLegales.from_dict(
                {"unitesLegales": []}
            )

            result = await asyncio(client=mock_client, body=mock_body)

            assert result is not None
            mock_asyncio_detailed.assert_called_once()
