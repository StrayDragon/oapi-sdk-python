# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .classification import Classification


class ListClassificationResponseBody(object):
    _types = {
        "items": List[Classification],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Classification]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListClassificationResponseBodyBuilder":
        return ListClassificationResponseBodyBuilder()


class ListClassificationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_classification_response_body = ListClassificationResponseBody()

    def items(self, items: List[Classification]) -> "ListClassificationResponseBodyBuilder":
        self._list_classification_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListClassificationResponseBodyBuilder":
        self._list_classification_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListClassificationResponseBodyBuilder":
        self._list_classification_response_body.has_more = has_more
        return self

    def build(self) -> "ListClassificationResponseBody":
        return self._list_classification_response_body