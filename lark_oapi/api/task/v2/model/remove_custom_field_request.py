# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .remove_custom_field_request_body import RemoveCustomFieldRequestBody


class RemoveCustomFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.custom_field_guid: Optional[str] = None
        self.request_body: Optional[RemoveCustomFieldRequestBody] = None

    @staticmethod
    def builder() -> "RemoveCustomFieldRequestBuilder":
        return RemoveCustomFieldRequestBuilder()


class RemoveCustomFieldRequestBuilder(object):

    def __init__(self) -> None:
        remove_custom_field_request = RemoveCustomFieldRequest()
        remove_custom_field_request.http_method = HttpMethod.POST
        remove_custom_field_request.uri = "/open-apis/task/v2/custom_fields/:custom_field_guid/remove"
        remove_custom_field_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._remove_custom_field_request: RemoveCustomFieldRequest = remove_custom_field_request

    def custom_field_guid(self, custom_field_guid: str) -> "RemoveCustomFieldRequestBuilder":
        self._remove_custom_field_request.custom_field_guid = custom_field_guid
        self._remove_custom_field_request.paths["custom_field_guid"] = str(custom_field_guid)
        return self

    def request_body(self, request_body: RemoveCustomFieldRequestBody) -> "RemoveCustomFieldRequestBuilder":
        self._remove_custom_field_request.request_body = request_body
        self._remove_custom_field_request.body = request_body
        return self

    def build(self) -> RemoveCustomFieldRequest:
        return self._remove_custom_field_request