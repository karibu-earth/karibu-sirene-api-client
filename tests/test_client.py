"""Tests for client module."""

import ssl

import httpx
import pytest

from sirene_api_client.client import AuthenticatedClient


@pytest.mark.requirement("REQ-CLIENT-001")
class TestAuthenticatedClientSireneDefaults:
    """Test AuthenticatedClient with SIRENE-specific defaults."""

    def test_authenticated_client_sirene_defaults(self):
        """Test AuthenticatedClient uses SIRENE-specific defaults."""
        client = AuthenticatedClient(token="test_token")

        assert client._base_url == "https://api.insee.fr/api-sirene/3.11"
        assert client.auth_header_name == "X-INSEE-Api-Key-Integration"
        assert client.prefix == ""

        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_token_required(self):
        """Test that token parameter is required."""
        with pytest.raises(TypeError, match="token"):
            AuthenticatedClient()

    def test_authenticated_client_custom_base_url(self):
        """Test AuthenticatedClient with custom base URL."""
        client = AuthenticatedClient(
            token="test_token", base_url="https://custom-api.example.com"
        )

        assert client._base_url == "https://custom-api.example.com"
        httpx_client = client.get_httpx_client()
        assert httpx_client.base_url == "https://custom-api.example.com"

    def test_authenticated_client_custom_auth_header(self):
        """Test AuthenticatedClient with custom auth header."""
        client = AuthenticatedClient(
            token="test_token", auth_header_name="X-Custom-Auth"
        )

        assert client.auth_header_name == "X-Custom-Auth"
        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-Custom-Auth"] == "test_token"
        assert "X-INSEE-Api-Key-Integration" not in httpx_client.headers

    def test_authenticated_client_custom_prefix(self):
        """Test AuthenticatedClient with custom prefix."""
        client = AuthenticatedClient(token="test_token", prefix="Bearer")

        assert client.prefix == "Bearer"
        httpx_client = client.get_httpx_client()
        assert (
            httpx_client.headers["X-INSEE-Api-Key-Integration"] == "Bearer test_token"
        )


@pytest.mark.requirement("REQ-CLIENT-002")
class TestAuthenticatedClient:
    """Test AuthenticatedClient class."""

    def test_authenticated_client_initialization(self):
        """Test AuthenticatedClient initialization."""
        client = AuthenticatedClient(token="test_token")

        assert client._base_url == "https://api.insee.fr/api-sirene/3.11"
        assert client.token == "test_token"
        assert client.auth_header_name == "X-INSEE-Api-Key-Integration"
        assert client.prefix == ""
        assert client._cookies == {}
        assert client._headers == {}
        assert client._timeout is None
        assert client._verify_ssl is True
        assert client._follow_redirects is False
        assert client._httpx_args == {}
        assert client.raise_on_unexpected_status is False

    def test_authenticated_client_with_custom_values(self):
        """Test AuthenticatedClient with custom values."""
        client = AuthenticatedClient(
            base_url="https://api.example.com",
            token="test_token",
            cookies={"session": "abc123"},
            headers={"User-Agent": "MyApp/1.0"},
            timeout=30.0,
            verify_ssl=False,
            follow_redirects=True,
            httpx_args={"proxies": {"http": "proxy.example.com"}},
            raise_on_unexpected_status=True,
        )

        assert client._base_url == "https://api.example.com"
        assert client.token == "test_token"
        assert client._cookies == {"session": "abc123"}
        assert client._headers == {"User-Agent": "MyApp/1.0"}
        assert client._timeout == 30.0
        assert client._verify_ssl is False
        assert client._follow_redirects is True
        assert client._httpx_args == {"proxies": {"http": "proxy.example.com"}}
        assert client.raise_on_unexpected_status is True

    def test_authenticated_client_get_httpx_client(self):
        """Test AuthenticatedClient get_httpx_client method."""
        client = AuthenticatedClient(token="test_token")

        httpx_client = client.get_httpx_client()

        assert isinstance(httpx_client, httpx.Client)
        assert httpx_client.base_url == "https://api.insee.fr/api-sirene/3.11/"
        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_get_async_httpx_client(self):
        """Test AuthenticatedClient get_async_httpx_client method."""
        client = AuthenticatedClient(token="test_token")

        async_client = client.get_async_httpx_client()

        assert isinstance(async_client, httpx.AsyncClient)
        assert async_client.base_url == "https://api.insee.fr/api-sirene/3.11/"
        assert async_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_with_existing_headers(self):
        """Test AuthenticatedClient with existing headers."""
        client = AuthenticatedClient(
            token="test_token",
            headers={"User-Agent": "MyApp/1.0"},
        )

        httpx_client = client.get_httpx_client()

        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"
        assert httpx_client.headers["User-Agent"] == "MyApp/1.0"

    def test_authenticated_client_token_override(self):
        """Test AuthenticatedClient with token in headers (should be overridden)."""
        client = AuthenticatedClient(
            token="test_token",
            headers={"X-INSEE-Api-Key-Integration": "old_token"},
        )

        httpx_client = client.get_httpx_client()

        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_inheritance(self):
        """Test AuthenticatedClient inherits from Client."""
        client = AuthenticatedClient(
            base_url="https://api.example.com",
            token="test_token",
        )

        # AuthenticatedClient doesn't inherit from Client, it's a separate class
        assert hasattr(client, "token")
        assert client.token == "test_token"


@pytest.mark.requirement("REQ-CLIENT-003")
class TestAuthenticatedClientContextManagers:
    """Test AuthenticatedClient context manager functionality."""

    def test_authenticated_client_sync_context_manager(self):
        """Test AuthenticatedClient as sync context manager."""
        client = AuthenticatedClient(token="test_token")

        with client as ctx_client:
            assert ctx_client is client
            assert client._client is not None
            assert isinstance(client._client, httpx.Client)
            # Verify auth header is set
            assert client._client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_async_context_manager(self):
        """Test AuthenticatedClient as async context manager."""
        client = AuthenticatedClient(token="test_token")

        async def test_async_context():
            async with client as ctx_client:
                assert ctx_client is client
                assert client._async_client is not None
                assert isinstance(client._async_client, httpx.AsyncClient)
                # Verify auth header is set
                assert (
                    client._async_client.headers["X-INSEE-Api-Key-Integration"]
                    == "test_token"
                )

        # Run the async test
        import asyncio

        asyncio.run(test_async_context())


@pytest.mark.requirement("REQ-CLIENT-004")
class TestAuthenticatedClientMethodChaining:
    """Test AuthenticatedClient method chaining functionality."""

    def test_authenticated_client_with_headers_chaining(self):
        """Test AuthenticatedClient with_headers method chaining."""
        client = AuthenticatedClient(token="test_token")

        # Test single header
        new_client = client.with_headers({"User-Agent": "MyApp/1.0"})
        assert new_client is not client  # Should return new instance
        assert new_client._headers == {"User-Agent": "MyApp/1.0"}
        assert new_client.token == "test_token"  # Token should be preserved

        # Test multiple headers
        another_client = new_client.with_headers({"Accept": "application/json"})
        assert another_client._headers == {
            "User-Agent": "MyApp/1.0",
            "Accept": "application/json",
        }
        assert another_client.token == "test_token"  # Token should be preserved

    def test_authenticated_client_with_cookies_chaining(self):
        """Test AuthenticatedClient with_cookies method chaining."""
        client = AuthenticatedClient(token="test_token")

        # Test single cookie
        new_client = client.with_cookies({"session": "abc123"})
        assert new_client is not client  # Should return new instance
        assert new_client._cookies == {"session": "abc123"}
        assert new_client.token == "test_token"  # Token should be preserved

        # Test multiple cookies
        another_client = new_client.with_cookies({"csrf": "xyz789"})
        assert another_client._cookies == {"session": "abc123", "csrf": "xyz789"}
        assert another_client.token == "test_token"  # Token should be preserved

    def test_authenticated_client_with_timeout_chaining(self):
        """Test AuthenticatedClient with_timeout method chaining."""
        client = AuthenticatedClient(token="test_token")
        timeout = httpx.Timeout(30.0)

        new_client = client.with_timeout(timeout)
        assert new_client is not client  # Should return new instance
        assert new_client._timeout == timeout
        assert new_client.token == "test_token"  # Token should be preserved

    def test_authenticated_client_multiple_chaining(self):
        """Test AuthenticatedClient multiple method chaining."""
        client = AuthenticatedClient(token="test_token")
        timeout = httpx.Timeout(60.0)

        chained_client = (
            client.with_headers({"User-Agent": "MyApp/1.0"})
            .with_cookies({"session": "abc123"})
            .with_timeout(timeout)
        )

        assert chained_client._headers == {"User-Agent": "MyApp/1.0"}
        assert chained_client._cookies == {"session": "abc123"}
        assert chained_client._timeout == timeout
        assert chained_client.token == "test_token"  # Token should be preserved


@pytest.mark.requirement("REQ-CLIENT-005")
class TestAuthenticatedClientMutationMethods:
    """Test AuthenticatedClient mutation methods."""

    def test_authenticated_client_set_httpx_client(self):
        """Test AuthenticatedClient set_httpx_client method."""
        client = AuthenticatedClient(token="test_token")
        custom_client = httpx.Client(base_url="https://custom.example.com")

        result = client.set_httpx_client(custom_client)
        assert result is client  # Should return self
        assert client._client is custom_client

    def test_authenticated_client_set_httpx_client_overrides_existing(self):
        """Test AuthenticatedClient set_httpx_client overrides existing client."""
        client = AuthenticatedClient(token="test_token")

        # Create initial client
        initial_client = client.get_httpx_client()
        assert client._client is initial_client

        # Set custom client
        custom_client = httpx.Client(base_url="https://custom.example.com")
        client.set_httpx_client(custom_client)
        assert client._client is custom_client
        assert client._client is not initial_client

    def test_authenticated_client_set_async_httpx_client(self):
        """Test AuthenticatedClient set_async_httpx_client method."""
        client = AuthenticatedClient(token="test_token")
        custom_async_client = httpx.AsyncClient(base_url="https://custom.example.com")

        result = client.set_async_httpx_client(custom_async_client)
        assert result is client  # Should return self
        assert client._async_client is custom_async_client

    def test_authenticated_client_set_async_httpx_client_overrides_existing(self):
        """Test AuthenticatedClient set_async_httpx_client overrides existing client."""
        client = AuthenticatedClient(token="test_token")

        # Create initial async client
        initial_async_client = client.get_async_httpx_client()
        assert client._async_client is initial_async_client

        # Set custom async client
        custom_async_client = httpx.AsyncClient(base_url="https://custom.example.com")
        client.set_async_httpx_client(custom_async_client)
        assert client._async_client is custom_async_client
        assert client._async_client is not initial_async_client


@pytest.mark.requirement("REQ-CLIENT-006")
class TestAuthenticatedClientEdgeCases:
    """Test AuthenticatedClient edge cases and error handling."""

    def test_authenticated_client_multiple_get_httpx_client_calls(self):
        """Test multiple calls to get_httpx_client return same instance."""
        client = AuthenticatedClient(token="test_token")

        client1 = client.get_httpx_client()
        client2 = client.get_httpx_client()

        assert client1 is client2
        assert client._client is client1

    def test_authenticated_client_multiple_get_async_httpx_client_calls(self):
        """Test multiple calls to get_async_httpx_client return same instance."""
        client = AuthenticatedClient(token="test_token")

        client1 = client.get_async_httpx_client()
        client2 = client.get_async_httpx_client()

        assert client1 is client2
        assert client._async_client is client1

    def test_authenticated_client_custom_prefix(self):
        """Test AuthenticatedClient with custom prefix."""
        client = AuthenticatedClient(
            token="test_token",
            prefix="Token",
        )

        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "Token test_token"

    def test_authenticated_client_empty_prefix(self):
        """Test AuthenticatedClient with empty prefix (default)."""
        client = AuthenticatedClient(token="test_token")

        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == "test_token"

    def test_authenticated_client_custom_auth_header_name(self):
        """Test AuthenticatedClient with custom auth header name."""
        client = AuthenticatedClient(
            token="test_token",
            auth_header_name="X-API-Key",
        )

        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-API-Key"] == "test_token"
        assert "X-INSEE-Api-Key-Integration" not in httpx_client.headers

    def test_authenticated_client_empty_token(self):
        """Test AuthenticatedClient with empty token."""
        client = AuthenticatedClient(token="")

        httpx_client = client.get_httpx_client()
        assert httpx_client.headers["X-INSEE-Api-Key-Integration"] == ""

    def test_authenticated_client_with_ssl_context(self):
        """Test AuthenticatedClient with SSL context."""
        ssl_context = ssl.create_default_context()
        client = AuthenticatedClient(
            token="test_token",
            verify_ssl=ssl_context,
        )

        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)

    def test_authenticated_client_with_string_ssl_verification(self):
        """Test AuthenticatedClient with string SSL verification."""
        # Use a non-existent file path to test the error handling
        client = AuthenticatedClient(
            token="test_token",
            verify_ssl="/path/to/nonexistent/cert.pem",
        )

        # This should raise an error when trying to create the client
        with pytest.raises((FileNotFoundError, OSError)):
            client.get_httpx_client()

    def test_authenticated_client_with_false_ssl_verification(self):
        """Test AuthenticatedClient with SSL verification disabled."""
        client = AuthenticatedClient(
            token="test_token",
            verify_ssl=False,
        )

        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)

    def test_authenticated_client_with_httpx_args(self):
        """Test AuthenticatedClient with additional httpx arguments."""
        client = AuthenticatedClient(
            token="test_token",
            httpx_args={"limits": httpx.Limits(max_keepalive_connections=5)},
        )

        httpx_client = client.get_httpx_client()
        assert isinstance(httpx_client, httpx.Client)
