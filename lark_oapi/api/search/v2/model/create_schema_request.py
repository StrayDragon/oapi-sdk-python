# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .schema import Schema


class CreateSchemaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.validate_only: Optional[bool] = None
        self.request_body: Optional[Schema] = None

    @staticmethod
    def builder() -> "CreateSchemaRequestBuilder":
        return CreateSchemaRequestBuilder()


class CreateSchemaRequestBuilder(object):

    def __init__(self) -> None:
        create_schema_request = CreateSchemaRequest()
        create_schema_request.http_method = HttpMethod.POST
        create_schema_request.uri = "/open-apis/search/v2/schemas"
        create_schema_request.token_types = {AccessTokenType.TENANT}
        self._create_schema_request: CreateSchemaRequest = create_schema_request

    def validate_only(self, validate_only: bool) -> "CreateSchemaRequestBuilder":
        self._create_schema_request.validate_only = validate_only
        self._create_schema_request.add_query("validate_only", validate_only)
        return self

    def request_body(self, request_body: Schema) -> "CreateSchemaRequestBuilder":
        self._create_schema_request.request_body = request_body
        self._create_schema_request.body = request_body
        return self

    def build(self) -> CreateSchemaRequest:
        return self._create_schema_request
