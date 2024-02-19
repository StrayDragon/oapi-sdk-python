# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_calendar_event_response_body import ListCalendarEventResponseBody


class ListCalendarEventResponse(BaseResponse):
    _types = {
        "data": ListCalendarEventResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListCalendarEventResponseBody] = None
        init(self, d, self._types)
