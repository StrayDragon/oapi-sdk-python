# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListShiftRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListShiftRequestBuilder":
        return ListShiftRequestBuilder()


class ListShiftRequestBuilder(object):

    def __init__(self) -> None:
        list_shift_request = ListShiftRequest()
        list_shift_request.http_method = HttpMethod.GET
        list_shift_request.uri = "/open-apis/attendance/v1/shifts"
        list_shift_request.token_types = {AccessTokenType.TENANT}
        self._list_shift_request: ListShiftRequest = list_shift_request

    def page_size(self, page_size: int) -> "ListShiftRequestBuilder":
        self._list_shift_request.page_size = page_size
        self._list_shift_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListShiftRequestBuilder":
        self._list_shift_request.page_token = page_token
        self._list_shift_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListShiftRequest:
        return self._list_shift_request
