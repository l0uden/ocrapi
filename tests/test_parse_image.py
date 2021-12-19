import pytest

from ocrapi_qa.matchers.parse_image_matchers import verify_parse_image_response, verify_parse_image_invalid_apikey, \
    verify_parse_image_invalid_params, verify_parse_image_without_mandatory_param
from ocrapi_qa.steps.parse_image_api import parse_image


class TestOcrParseImage:
    @pytest.fixture(autouse=True)
    def setup(self, parse_image_body_fixture, parse_image_headers_fixture):
        self.body = parse_image_body_fixture
        self.headers = parse_image_headers_fixture

    @pytest.mark.parametrize("value, pdf", [
        (True, True),
        (False, False),
    ], ids=["iscreatesearchablepdf=True",
            "iscreatesearchablepdf=False",
            ])
    def test_parse_image(self, value, pdf):
        self.body.update({"iscreatesearchablepdf": value})
        response = parse_image(body=self.body)
        verify_parse_image_response(response, pdf=pdf)

    @pytest.mark.parametrize("param, value", [
        ("language", "byn"),
        ("isOverlayRequired", "12"),
        ("isCreateSearchablePDF", "13"),
        ("isSearchablePdfHideTextLayer", "14"),
        ("detectOrientation", "16"),
        ("scale", 17),
    ], ids=[
        "language=byn",
        "isOverlayRequired=12",
        "isCreateSearchablePDF=13",
        "isSearchablePdfHideTextLayer=14",
        "detectOrientation=16",
        "scale=17",
    ])
    def test_invalid_params(self, param, value):
        self.body.update({param: value})
        response = parse_image(body=self.body)
        verify_parse_image_invalid_params(response, param)

    def test_without_mandatory_params(self):
        self.body.pop("url")
        response = parse_image(body=self.body)
        verify_parse_image_without_mandatory_param(response)

    def test_invalid_apikey(self):
        self.headers.update({"apikey": "abc"})
        response = parse_image(status_code=403, headers=self.headers)
        verify_parse_image_invalid_apikey(response)
