# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .meeting_list_export_request_body import MeetingListExportRequestBody


class MeetingListExportRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[MeetingListExportRequestBody] = None

    @staticmethod
    def builder() -> "MeetingListExportRequestBuilder":
        return MeetingListExportRequestBuilder()


class MeetingListExportRequestBuilder(object):

    def __init__(self) -> None:
        meeting_list_export_request = MeetingListExportRequest()
        meeting_list_export_request.http_method = HttpMethod.POST
        meeting_list_export_request.uri = "/open-apis/vc/v1/exports/meeting_list"
        meeting_list_export_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._meeting_list_export_request: MeetingListExportRequest = meeting_list_export_request

    def user_id_type(self, user_id_type: str) -> "MeetingListExportRequestBuilder":
        self._meeting_list_export_request.user_id_type = user_id_type
        self._meeting_list_export_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: MeetingListExportRequestBody) -> "MeetingListExportRequestBuilder":
        self._meeting_list_export_request.request_body = request_body
        self._meeting_list_export_request.body = request_body
        return self

    def build(self) -> MeetingListExportRequest:
        return self._meeting_list_export_request
