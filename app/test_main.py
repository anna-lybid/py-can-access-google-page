import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_url, expected",
    [
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(has_internet_connection, valid_url, expected):
    with (
        mock.patch("app.main.has_internet_connection", return_value=has_internet_connection),
        mock.patch("app.main.valid_google_url", return_value=valid_url)
    ):
        assert can_access_google_page("http://google.com") == expected
