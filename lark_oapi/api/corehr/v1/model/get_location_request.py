# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.location_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetLocationRequestBuilder":
        return GetLocationRequestBuilder()


class GetLocationRequestBuilder(object):

    def __init__(self) -> None:
        get_location_request = GetLocationRequest()
        get_location_request.http_method = HttpMethod.GET
        get_location_request.uri = "/open-apis/corehr/v1/locations/:location_id"
        get_location_request.token_types = {AccessTokenType.TENANT}
        self._get_location_request: GetLocationRequest = get_location_request

    def location_id(self, location_id: str) -> "GetLocationRequestBuilder":
        self._get_location_request.location_id = location_id
        self._get_location_request.paths["location_id"] = str(location_id)
        return self

    def build(self) -> GetLocationRequest:
        return self._get_location_request
