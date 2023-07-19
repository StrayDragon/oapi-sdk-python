# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateMessageResponseBody(object):
    _types = {
        "items": List[str],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d):
        self.items: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateMessageResponseBodyBuilder":
        return CreateMessageResponseBodyBuilder()


class CreateMessageResponseBodyBuilder(object):
    def __init__(self, create_message_response_body: CreateMessageResponseBody = CreateMessageResponseBody({})) -> None:
        self._create_message_response_body: CreateMessageResponseBody = create_message_response_body

    def items(self, items: List[str]) -> "CreateMessageResponseBodyBuilder":
        self._create_message_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "CreateMessageResponseBodyBuilder":
        self._create_message_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "CreateMessageResponseBodyBuilder":
        self._create_message_response_body.has_more = has_more
        return self

    def build(self) -> "CreateMessageResponseBody":
        return self._create_message_response_body