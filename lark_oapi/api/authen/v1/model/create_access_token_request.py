# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_access_token_request_body import CreateAccessTokenRequestBody


class CreateAccessTokenRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateAccessTokenRequestBody] = None

    @staticmethod
    def builder() -> "CreateAccessTokenRequestBuilder":
        return CreateAccessTokenRequestBuilder()


class CreateAccessTokenRequestBuilder(object):

    def __init__(self) -> None:
        create_access_token_request = CreateAccessTokenRequest()
        create_access_token_request.http_method = HttpMethod.POST
        create_access_token_request.uri = "/open-apis/authen/v1/access_token"
        create_access_token_request.token_types = {AccessTokenType.APP}
        self._create_access_token_request: CreateAccessTokenRequest = create_access_token_request

    def request_body(self, request_body: CreateAccessTokenRequestBody) -> "CreateAccessTokenRequestBuilder":
        self._create_access_token_request.request_body = request_body
        self._create_access_token_request.body = request_body
        return self

    def build(self) -> CreateAccessTokenRequest:
        return self._create_access_token_request
