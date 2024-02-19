# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .search_department_request_body import SearchDepartmentRequestBody


class SearchDepartmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.request_body: Optional[SearchDepartmentRequestBody] = None

    @staticmethod
    def builder() -> "SearchDepartmentRequestBuilder":
        return SearchDepartmentRequestBuilder()


class SearchDepartmentRequestBuilder(object):

    def __init__(self) -> None:
        search_department_request = SearchDepartmentRequest()
        search_department_request.http_method = HttpMethod.POST
        search_department_request.uri = "/open-apis/contact/v3/departments/search"
        search_department_request.token_types = {AccessTokenType.USER}
        self._search_department_request: SearchDepartmentRequest = search_department_request

    def user_id_type(self, user_id_type: str) -> "SearchDepartmentRequestBuilder":
        self._search_department_request.user_id_type = user_id_type
        self._search_department_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "SearchDepartmentRequestBuilder":
        self._search_department_request.department_id_type = department_id_type
        self._search_department_request.add_query("department_id_type", department_id_type)
        return self

    def page_token(self, page_token: str) -> "SearchDepartmentRequestBuilder":
        self._search_department_request.page_token = page_token
        self._search_department_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "SearchDepartmentRequestBuilder":
        self._search_department_request.page_size = page_size
        self._search_department_request.add_query("page_size", page_size)
        return self

    def request_body(self, request_body: SearchDepartmentRequestBody) -> "SearchDepartmentRequestBuilder":
        self._search_department_request.request_body = request_body
        self._search_department_request.body = request_body
        return self

    def build(self) -> SearchDepartmentRequest:
        return self._search_department_request
