import requests
from hamcrest import assert_that, equal_to

from ocrapi_qa.constants import OCRAPI_URL
from ocrapi_qa.data.parse_image_data import parse_image_body, parse_image_headers


def parse_image(status_code=200, body=parse_image_body(), headers=parse_image_headers()):
    response = requests.post(url=OCRAPI_URL, data=body, headers=headers)
    assert_that(response.status_code, equal_to(status_code))
    return response.json()
