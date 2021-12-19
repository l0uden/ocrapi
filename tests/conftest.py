import pytest

from ocrapi_qa.data.parse_image_data import parse_image_body, parse_image_headers


@pytest.fixture
def parse_image_body_fixture():
    return parse_image_body()


@pytest.fixture
def parse_image_headers_fixture():
    return parse_image_headers()
