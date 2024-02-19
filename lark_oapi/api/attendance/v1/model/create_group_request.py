# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_group_request_body import CreateGroupRequestBody


class CreateGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.dept_type: Optional[str] = None
        self.request_body: Optional[CreateGroupRequestBody] = None

    @staticmethod
    def builder() -> "CreateGroupRequestBuilder":
        return CreateGroupRequestBuilder()


class CreateGroupRequestBuilder(object):

    def __init__(self) -> None:
        create_group_request = CreateGroupRequest()
        create_group_request.http_method = HttpMethod.POST
        create_group_request.uri = "/open-apis/attendance/v1/groups"
        create_group_request.token_types = {AccessTokenType.TENANT}
        self._create_group_request: CreateGroupRequest = create_group_request

    def employee_type(self, employee_type: str) -> "CreateGroupRequestBuilder":
        self._create_group_request.employee_type = employee_type
        self._create_group_request.add_query("employee_type", employee_type)
        return self

    def dept_type(self, dept_type: str) -> "CreateGroupRequestBuilder":
        self._create_group_request.dept_type = dept_type
        self._create_group_request.add_query("dept_type", dept_type)
        return self

    def request_body(self, request_body: CreateGroupRequestBody) -> "CreateGroupRequestBuilder":
        self._create_group_request.request_body = request_body
        self._create_group_request.body = request_body
        return self

    def build(self) -> CreateGroupRequest:
        return self._create_group_request
