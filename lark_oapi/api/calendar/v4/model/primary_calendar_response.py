# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .primary_calendar_response_body import PrimaryCalendarResponseBody


class PrimaryCalendarResponse(BaseResponse):
    _types = {
        "data": PrimaryCalendarResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PrimaryCalendarResponseBody] = None
        init(self, d, self._types)
