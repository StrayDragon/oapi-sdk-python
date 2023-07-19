# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.group_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetGroupRequestBuilder":
        return GetGroupRequestBuilder()


class GetGroupRequestBuilder(object):

    def __init__(self, get_group_request: GetGroupRequest = GetGroupRequest()) -> None:
        get_group_request.http_method = HttpMethod.GET
        get_group_request.uri = "/open-apis/contact/v3/group/:group_id"
        get_group_request.token_types = {AccessTokenType.TENANT}
        self._get_group_request: GetGroupRequest = get_group_request

    def user_id_type(self, user_id_type: str) -> "GetGroupRequestBuilder":
        self._get_group_request.user_id_type = user_id_type
        self._get_group_request.queries["user_id_type"] = str(user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetGroupRequestBuilder":
        self._get_group_request.department_id_type = department_id_type
        self._get_group_request.queries["department_id_type"] = str(department_id_type)
        return self

    def group_id(self, group_id: str) -> "GetGroupRequestBuilder":
        self._get_group_request.group_id = group_id
        self._get_group_request.paths["group_id"] = group_id
        return self

    def build(self) -> GetGroupRequest:
        return self._get_group_request