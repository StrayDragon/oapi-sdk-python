# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetProgressBatchMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.batch_message_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetProgressBatchMessageRequestBuilder":
        return GetProgressBatchMessageRequestBuilder()


class GetProgressBatchMessageRequestBuilder(object):

    def __init__(self) -> None:
        get_progress_batch_message_request = GetProgressBatchMessageRequest()
        get_progress_batch_message_request.http_method = HttpMethod.GET
        get_progress_batch_message_request.uri = "/open-apis/im/v1/batch_messages/:batch_message_id/get_progress"
        get_progress_batch_message_request.token_types = {AccessTokenType.TENANT}
        self._get_progress_batch_message_request: GetProgressBatchMessageRequest = get_progress_batch_message_request

    def batch_message_id(self, batch_message_id: str) -> "GetProgressBatchMessageRequestBuilder":
        self._get_progress_batch_message_request.batch_message_id = batch_message_id
        self._get_progress_batch_message_request.paths["batch_message_id"] = str(batch_message_id)
        return self

    def build(self) -> GetProgressBatchMessageRequest:
        return self._get_progress_batch_message_request
