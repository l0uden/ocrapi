def parse_image_body(**kwargs):
    data = dict(
        language="eng",
        isOverlayRequired=False,
        url="http://dl.a9t9.com/ocrbenchmark/eng.png",
        iscreatesearchablepdf=False,
        issearchablepdfhidetextlayer=False,
        filetype="PNG",
        detectOrientation=True,
        scale=False,
        isTable=False,
        OCREngine=1,
    )
    data.update(**kwargs)
    return data


def parse_image_headers(**kwargs):
    data = dict(
        apikey="helloworld"
    )
    data.update(**kwargs)
    return data
