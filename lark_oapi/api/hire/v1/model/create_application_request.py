# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_application_request_body import CreateApplicationRequestBody


class CreateApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateApplicationRequestBody] = None

    @staticmethod
    def builder() -> "CreateApplicationRequestBuilder":
        return CreateApplicationRequestBuilder()


class CreateApplicationRequestBuilder(object):

    def __init__(self, create_application_request: CreateApplicationRequest = CreateApplicationRequest()) -> None:
        create_application_request.http_method = HttpMethod.POST
        create_application_request.uri = "/open-apis/hire/v1/applications"
        create_application_request.token_types = {AccessTokenType.TENANT}
        self._create_application_request: CreateApplicationRequest = create_application_request

    def request_body(self, request_body: CreateApplicationRequestBody) -> "CreateApplicationRequestBuilder":
        self._create_application_request.request_body = request_body
        self._create_application_request.body = request_body
        return self

    def build(self) -> CreateApplicationRequest:
        return self._create_application_request