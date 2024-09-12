import requests
from unittest import mock

from exemple import get_all_titles


def test_get_all_titles_works(monkeypatch):
    def mock_requests_get(url, timeout):
        class MockResponse:
            status_code = 200
            content = ""

        return MockResponse()

    monkeypatch("requests.get", mock_requests_get)

    results = get_all_titles("https://python.developpez.com")

    assert results == []
