# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class CreateAppResponseBody(object):
    _types = {
        "items": List[str],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppResponseBodyBuilder":
        return CreateAppResponseBodyBuilder()


class CreateAppResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_response_body = CreateAppResponseBody()

    def items(self, items: List[str]) -> "CreateAppResponseBodyBuilder":
        self._create_app_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "CreateAppResponseBodyBuilder":
        self._create_app_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "CreateAppResponseBodyBuilder":
        self._create_app_response_body.has_more = has_more
        return self

    def build(self) -> "CreateAppResponseBody":
        return self._create_app_response_body
