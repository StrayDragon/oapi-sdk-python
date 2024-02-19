# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BackgroundCheckReportObject(object):
    _types = {
        "url": str,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckReportObjectBuilder":
        return BackgroundCheckReportObjectBuilder()


class BackgroundCheckReportObjectBuilder(object):
    def __init__(self) -> None:
        self._background_check_report_object = BackgroundCheckReportObject()

    def url(self, url: str) -> "BackgroundCheckReportObjectBuilder":
        self._background_check_report_object.url = url
        return self

    def build(self) -> "BackgroundCheckReportObject":
        return self._background_check_report_object
