# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class EcoBackgroundCheckReportFile(object):
    _types = {
        "report_name": str,
        "report_url": str,
        "report_url_type": int,
    }

    def __init__(self, d=None):
        self.report_name: Optional[str] = None
        self.report_url: Optional[str] = None
        self.report_url_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckReportFileBuilder":
        return EcoBackgroundCheckReportFileBuilder()


class EcoBackgroundCheckReportFileBuilder(object):
    def __init__(self) -> None:
        self._eco_background_check_report_file = EcoBackgroundCheckReportFile()

    def report_name(self, report_name: str) -> "EcoBackgroundCheckReportFileBuilder":
        self._eco_background_check_report_file.report_name = report_name
        return self

    def report_url(self, report_url: str) -> "EcoBackgroundCheckReportFileBuilder":
        self._eco_background_check_report_file.report_url = report_url
        return self

    def report_url_type(self, report_url_type: int) -> "EcoBackgroundCheckReportFileBuilder":
        self._eco_background_check_report_file.report_url_type = report_url_type
        return self

    def build(self) -> "EcoBackgroundCheckReportFile":
        return self._eco_background_check_report_file
