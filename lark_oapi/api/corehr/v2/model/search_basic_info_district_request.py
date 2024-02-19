# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .search_basic_info_district_request_body import SearchBasicInfoDistrictRequestBody


class SearchBasicInfoDistrictRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.request_body: Optional[SearchBasicInfoDistrictRequestBody] = None

    @staticmethod
    def builder() -> "SearchBasicInfoDistrictRequestBuilder":
        return SearchBasicInfoDistrictRequestBuilder()


class SearchBasicInfoDistrictRequestBuilder(object):

    def __init__(self) -> None:
        search_basic_info_district_request = SearchBasicInfoDistrictRequest()
        search_basic_info_district_request.http_method = HttpMethod.POST
        search_basic_info_district_request.uri = "/open-apis/corehr/v2/basic_info/districts/search"
        search_basic_info_district_request.token_types = {AccessTokenType.TENANT}
        self._search_basic_info_district_request: SearchBasicInfoDistrictRequest = search_basic_info_district_request

    def page_size(self, page_size: int) -> "SearchBasicInfoDistrictRequestBuilder":
        self._search_basic_info_district_request.page_size = page_size
        self._search_basic_info_district_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchBasicInfoDistrictRequestBuilder":
        self._search_basic_info_district_request.page_token = page_token
        self._search_basic_info_district_request.add_query("page_token", page_token)
        return self

    def request_body(self, request_body: SearchBasicInfoDistrictRequestBody) -> "SearchBasicInfoDistrictRequestBuilder":
        self._search_basic_info_district_request.request_body = request_body
        self._search_basic_info_district_request.body = request_body
        return self

    def build(self) -> SearchBasicInfoDistrictRequest:
        return self._search_basic_info_district_request
