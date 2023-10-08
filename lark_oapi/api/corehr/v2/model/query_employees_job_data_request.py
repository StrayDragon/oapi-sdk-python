# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .query_employees_job_data_request_body import QueryEmployeesJobDataRequestBody


class QueryEmployeesJobDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.request_body: Optional[QueryEmployeesJobDataRequestBody] = None

    @staticmethod
    def builder() -> "QueryEmployeesJobDataRequestBuilder":
        return QueryEmployeesJobDataRequestBuilder()


class QueryEmployeesJobDataRequestBuilder(object):

    def __init__(self) -> None:
        query_employees_job_data_request = QueryEmployeesJobDataRequest()
        query_employees_job_data_request.http_method = HttpMethod.POST
        query_employees_job_data_request.uri = "/open-apis/corehr/v2/employees/job_datas/query"
        query_employees_job_data_request.token_types = {AccessTokenType.TENANT}
        self._query_employees_job_data_request: QueryEmployeesJobDataRequest = query_employees_job_data_request

    def page_size(self, page_size: int) -> "QueryEmployeesJobDataRequestBuilder":
        self._query_employees_job_data_request.page_size = page_size
        self._query_employees_job_data_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "QueryEmployeesJobDataRequestBuilder":
        self._query_employees_job_data_request.page_token = page_token
        self._query_employees_job_data_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "QueryEmployeesJobDataRequestBuilder":
        self._query_employees_job_data_request.user_id_type = user_id_type
        self._query_employees_job_data_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "QueryEmployeesJobDataRequestBuilder":
        self._query_employees_job_data_request.department_id_type = department_id_type
        self._query_employees_job_data_request.add_query("department_id_type", department_id_type)
        return self

    def request_body(self, request_body: QueryEmployeesJobDataRequestBody) -> "QueryEmployeesJobDataRequestBuilder":
        self._query_employees_job_data_request.request_body = request_body
        self._query_employees_job_data_request.body = request_body
        return self

    def build(self) -> QueryEmployeesJobDataRequest:
        return self._query_employees_job_data_request
