from hamcrest import assert_that, has_entries, anything, equal_to, starts_with, ends_with

from ocrapi_qa.constants import PARSED_TEXT, TEXT_OVERLAY_LINES


def verify_parse_image_response(response, pdf=False):
    assert_that(response, has_entries(
        ParsedResults=anything(),
        OCRExitCode=1,
        IsErroredOnProcessing=False,
        ProcessingTimeInMilliseconds=anything(),
    ))
    assert_that(response["ParsedResults"][0], has_entries(
        TextOverlay=anything(),
        TextOrientation="0",
        FileParseExitCode=1,
        ParsedText=PARSED_TEXT,
        ErrorMessage="",
        ErrorDetails="",
    ))
    if pdf:
        assert_that(response["ParsedResults"][0]["TextOverlay"], has_entries(
            Lines=TEXT_OVERLAY_LINES,
            HasOverlay=True,
            Message="Total lines: 19",
        ))
        assert_that(response["SearchablePDFURL"], starts_with("https://api.ocr.space/SearchablePDF/"))
        assert_that(response["SearchablePDFURL"], ends_with(".pdf"))
    else:
        assert_that(response["ParsedResults"][0]["TextOverlay"], has_entries(
            Lines=[],
            HasOverlay=False,
            Message="Text overlay is not provided as it is not requested",
        ))
        assert_that(response, has_entries(
            SearchablePDFURL="Searchable PDF not generated as it was not requested.",
        ))


def verify_parse_image_invalid_apikey(response):
    assert_that(response, equal_to("The API key is invalid"))


def verify_parse_image_invalid_params(response, param):
    assert_that(response, has_entries(
        OCRExitCode=99,
        IsErroredOnProcessing=True,
        ProcessingTimeInMilliseconds=anything(),
        ErrorMessage=["Value for parameter '{}' is invalid".format(param)]
    ))


def verify_parse_image_without_mandatory_param(response):
    assert_that(response, has_entries(
        OCRExitCode=99,
        IsErroredOnProcessing=True,
        ProcessingTimeInMilliseconds=anything(),
        ErrorMessage=["No file uploaded or URL or base64 provided"],
        ErrorDetails=""
    ))
