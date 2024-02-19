# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_meeting_recording_response_body import GetMeetingRecordingResponseBody


class GetMeetingRecordingResponse(BaseResponse):
    _types = {
        "data": GetMeetingRecordingResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetMeetingRecordingResponseBody] = None
        init(self, d, self._types)
