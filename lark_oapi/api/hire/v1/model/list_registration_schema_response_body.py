# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .registration_schema import RegistrationSchema


class ListRegistrationSchemaResponseBody(object):
    _types = {
        "items": List[RegistrationSchema],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[RegistrationSchema]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListRegistrationSchemaResponseBodyBuilder":
        return ListRegistrationSchemaResponseBodyBuilder()


class ListRegistrationSchemaResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_registration_schema_response_body = ListRegistrationSchemaResponseBody()

    def items(self, items: List[RegistrationSchema]) -> "ListRegistrationSchemaResponseBodyBuilder":
        self._list_registration_schema_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListRegistrationSchemaResponseBodyBuilder":
        self._list_registration_schema_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListRegistrationSchemaResponseBodyBuilder":
        self._list_registration_schema_response_body.has_more = has_more
        return self

    def build(self) -> "ListRegistrationSchemaResponseBody":
        return self._list_registration_schema_response_body
