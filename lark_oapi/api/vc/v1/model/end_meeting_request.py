# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class EndMeetingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_id: Optional[int] = None

    @staticmethod
    def builder() -> "EndMeetingRequestBuilder":
        return EndMeetingRequestBuilder()


class EndMeetingRequestBuilder(object):

    def __init__(self) -> None:
        end_meeting_request = EndMeetingRequest()
        end_meeting_request.http_method = HttpMethod.PATCH
        end_meeting_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/end"
        end_meeting_request.token_types = {AccessTokenType.USER}
        self._end_meeting_request: EndMeetingRequest = end_meeting_request

    def meeting_id(self, meeting_id: int) -> "EndMeetingRequestBuilder":
        self._end_meeting_request.meeting_id = meeting_id
        self._end_meeting_request.paths["meeting_id"] = str(meeting_id)
        return self

    def build(self) -> EndMeetingRequest:
        return self._end_meeting_request
