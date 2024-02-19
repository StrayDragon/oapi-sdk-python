# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .participant_quality_list_export_response_body import ParticipantQualityListExportResponseBody


class ParticipantQualityListExportResponse(BaseResponse):
    _types = {
        "data": ParticipantQualityListExportResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ParticipantQualityListExportResponseBody] = None
        init(self, d, self._types)
