"""Tests for api_types module."""

from http import HTTPStatus
from unittest.mock import Mock

import pytest

from sirene_api_client.api_types import UNSET, File, Response, Unset


@pytest.mark.requirement("REQ-API-TYPES-001")
class TestUnset:
    """Test Unset class functionality."""

    def test_unset_bool_method(self):
        """Test Unset.__bool__ method returns False."""
        assert bool(UNSET) is False
        assert bool(Unset()) is False

    def test_unset_singleton_behavior(self):
        """Test UNSET singleton behavior."""
        unset1 = UNSET
        unset2 = UNSET
        assert unset1 is unset2
        # UNSET is a singleton instance, but Unset() creates new instances
        assert unset1 is not Unset()

    def test_unset_equality(self):
        """Test Unset equality."""
        # Unset instances are not equal by default (no __eq__ implemented)
        assert Unset() != UNSET
        assert UNSET == UNSET

    def test_unset_not_equal_to_other_values(self):
        """Test Unset is not equal to other values."""
        assert UNSET is not None
        assert UNSET != ""
        assert UNSET != 0
        assert UNSET is not False

    def test_unset_repr(self):
        """Test Unset string representation."""
        # Unset doesn't implement __repr__, so it uses default object repr
        repr_str = repr(UNSET)
        assert "Unset" in repr_str
        assert "object at" in repr_str
        # str() also uses default object representation
        str_str = str(UNSET)
        assert "Unset" in str_str
        assert "object at" in str_str


@pytest.mark.requirement("REQ-API-TYPES-002")
class TestFile:
    """Test File class functionality."""

    def test_file_initialization_with_all_parameters(self):
        """Test File initialization with all parameters."""
        mock_payload = Mock()
        file_obj = File(
            payload=mock_payload, file_name="test.txt", mime_type="text/plain"
        )

        assert file_obj.payload is mock_payload
        assert file_obj.file_name == "test.txt"
        assert file_obj.mime_type == "text/plain"

    def test_file_initialization_with_minimal_parameters(self):
        """Test File initialization with minimal parameters."""
        mock_payload = Mock()
        file_obj = File(payload=mock_payload)

        assert file_obj.payload is mock_payload
        assert file_obj.file_name is None
        assert file_obj.mime_type is None

    def test_file_to_tuple_with_all_parameters(self):
        """Test File.to_tuple() with all parameters."""
        mock_payload = Mock()
        file_obj = File(
            payload=mock_payload, file_name="test.txt", mime_type="text/plain"
        )

        result = file_obj.to_tuple()
        expected = ("test.txt", mock_payload, "text/plain")
        assert result == expected

    def test_file_to_tuple_with_none_parameters(self):
        """Test File.to_tuple() with None parameters."""
        mock_payload = Mock()
        file_obj = File(payload=mock_payload)

        result = file_obj.to_tuple()
        expected = (None, mock_payload, None)
        assert result == expected

    def test_file_to_tuple_with_empty_strings(self):
        """Test File.to_tuple() with empty strings."""
        mock_payload = Mock()
        file_obj = File(payload=mock_payload, file_name="", mime_type="")

        result = file_obj.to_tuple()
        expected = ("", mock_payload, "")
        assert result == expected

    def test_file_repr(self):
        """Test File string representation."""
        mock_payload = Mock()
        file_obj = File(
            payload=mock_payload, file_name="test.txt", mime_type="text/plain"
        )

        repr_str = repr(file_obj)
        assert "File" in repr_str
        assert "test.txt" in repr_str
        assert "text/plain" in repr_str


@pytest.mark.requirement("REQ-API-TYPES-003")
class TestResponse:
    """Test Response class functionality."""

    def test_response_initialization_with_all_fields(self):
        """Test Response initialization with all fields."""
        mock_parsed = Mock()
        headers = {"Content-Type": "application/json", "X-Custom": "value"}
        content = b'{"test": "data"}'

        response = Response(
            status_code=HTTPStatus.OK,
            content=content,
            headers=headers,
            parsed=mock_parsed,
        )

        assert response.status_code == HTTPStatus.OK
        assert response.content == content
        assert response.headers == headers
        assert response.parsed is mock_parsed

    def test_response_initialization_with_none_parsed(self):
        """Test Response initialization with None parsed."""
        headers = {"Content-Type": "application/json"}
        content = b'{"error": "not found"}'

        response = Response(
            status_code=HTTPStatus.NOT_FOUND,
            content=content,
            headers=headers,
            parsed=None,
        )

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.content == content
        assert response.headers == headers
        assert response.parsed is None

    def test_response_initialization_with_empty_headers(self):
        """Test Response initialization with empty headers."""
        content = b""

        response = Response(
            status_code=HTTPStatus.NO_CONTENT, content=content, headers={}, parsed=None
        )

        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.content == content
        assert response.headers == {}
        assert response.parsed is None

    def test_response_initialization_with_empty_content(self):
        """Test Response initialization with empty content."""
        headers = {"Content-Length": "0"}

        response = Response(
            status_code=HTTPStatus.OK, content=b"", headers=headers, parsed=None
        )

        assert response.status_code == HTTPStatus.OK
        assert response.content == b""
        assert response.headers == headers
        assert response.parsed is None

    def test_response_with_different_status_codes(self):
        """Test Response with different HTTP status codes."""
        status_codes = [
            HTTPStatus.OK,
            HTTPStatus.CREATED,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
            HTTPStatus.INTERNAL_SERVER_ERROR,
            HTTPStatus.SERVICE_UNAVAILABLE,
        ]

        for status_code in status_codes:
            response = Response(
                status_code=status_code,
                content=b"test content",
                headers={"Content-Type": "text/plain"},
                parsed=None,
            )
            assert response.status_code == status_code

    def test_response_headers_mutable(self):
        """Test Response headers are mutable."""
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"test",
            headers={"Content-Type": "text/plain"},
            parsed=None,
        )

        # Test that headers can be modified
        response.headers["X-Custom"] = "value"
        assert response.headers["X-Custom"] == "value"

        # Test that headers can be updated
        response.headers.update({"X-Another": "another_value"})
        assert response.headers["X-Another"] == "another_value"

    def test_response_with_binary_content(self):
        """Test Response with binary content."""
        binary_content = b"\x00\x01\x02\x03\xff\xfe\xfd"

        response = Response(
            status_code=HTTPStatus.OK,
            content=binary_content,
            headers={"Content-Type": "application/octet-stream"},
            parsed=None,
        )

        assert response.content == binary_content

    def test_response_with_unicode_content(self):
        """Test Response with Unicode content."""
        unicode_content = "Hello, 世界! 🌍".encode()

        response = Response(
            status_code=HTTPStatus.OK,
            content=unicode_content,
            headers={"Content-Type": "text/plain; charset=utf-8"},
            parsed=None,
        )

        assert response.content == unicode_content

    def test_response_repr(self):
        """Test Response string representation."""
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"test",
            headers={"Content-Type": "text/plain"},
            parsed=None,
        )

        repr_str = repr(response)
        assert "Response" in repr_str
        assert "200" in repr_str or "OK" in repr_str

    def test_response_generic_type_handling(self):
        """Test Response generic type handling."""
        # Test with string type
        response_str = Response[str](
            status_code=HTTPStatus.OK,
            content=b'"hello"',
            headers={"Content-Type": "application/json"},
            parsed="hello",
        )
        assert response_str.parsed == "hello"

        # Test with dict type
        response_dict = Response[dict](
            status_code=HTTPStatus.OK,
            content=b'{"key": "value"}',
            headers={"Content-Type": "application/json"},
            parsed={"key": "value"},
        )
        assert response_dict.parsed == {"key": "value"}

        # Test with None type
        response_none = Response[None](
            status_code=HTTPStatus.NO_CONTENT, content=b"", headers={}, parsed=None
        )
        assert response_none.parsed is None
