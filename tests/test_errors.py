"""Tests for errors module."""

import pytest

from sirene_api_client.errors import UnexpectedStatusError


@pytest.mark.requirement("REQ-ERRORS-001")
class TestUnexpectedStatusError:
    """Test UnexpectedStatusError class."""

    def test_unexpected_status_error_initialization(self):
        """Test UnexpectedStatusError initialization."""
        status_code = 418
        content = b"I'm a teapot"

        error = UnexpectedStatusError(status_code, content)

        assert error.status_code == 418
        assert error.content == b"I'm a teapot"

    def test_unexpected_status_error_message(self):
        """Test UnexpectedStatusError message format."""
        status_code = 418
        content = b"I'm a teapot"

        error = UnexpectedStatusError(status_code, content)

        expected_message = (
            "Unexpected status code: 418\n\nResponse content:\nI'm a teapot"
        )
        assert str(error) == expected_message

    def test_unexpected_status_error_with_unicode_content(self):
        """Test UnexpectedStatusError with unicode content."""
        status_code = 500
        content = b"Erreur serveur"

        error = UnexpectedStatusError(status_code, content)

        expected_message = (
            "Unexpected status code: 500\n\nResponse content:\nErreur serveur"
        )
        assert str(error) == expected_message

    def test_unexpected_status_error_with_binary_content(self):
        """Test UnexpectedStatusError with binary content."""
        status_code = 200
        content = b"\x00\x01\x02\x03\xff\xfe\xfd"

        error = UnexpectedStatusError(status_code, content)

        # Should handle binary content gracefully
        assert "Unexpected status code: 200" in str(error)
        assert "Response content:" in str(error)

    def test_unexpected_status_error_inheritance(self):
        """Test UnexpectedStatusError inherits from Exception."""
        error = UnexpectedStatusError(418, b"I'm a teapot")

        assert isinstance(error, Exception)
        assert isinstance(error, UnexpectedStatusError)

    def test_unexpected_status_error_attributes(self):
        """Test UnexpectedStatusError has correct attributes."""
        status_code = 404
        content = b"Not found"

        error = UnexpectedStatusError(status_code, content)

        assert hasattr(error, "status_code")
        assert hasattr(error, "content")
        assert error.status_code == 404
        assert error.content == b"Not found"

    def test_unexpected_status_error_with_empty_content(self):
        """Test UnexpectedStatusError with empty content."""
        status_code = 204
        content = b""

        error = UnexpectedStatusError(status_code, content)

        expected_message = "Unexpected status code: 204\n\nResponse content:\n"
        assert str(error) == expected_message

    def test_unexpected_status_error_with_none_content(self):
        """Test UnexpectedStatusError with None content."""
        status_code = 500
        content = None

        # This should raise an AttributeError since None doesn't have decode method
        with pytest.raises(AttributeError):
            UnexpectedStatusError(status_code, content)
