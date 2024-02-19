# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .faq import Faq


class SearchFaqResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[Faq],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[Faq]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchFaqResponseBodyBuilder":
        return SearchFaqResponseBodyBuilder()


class SearchFaqResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_faq_response_body = SearchFaqResponseBody()

    def has_more(self, has_more: bool) -> "SearchFaqResponseBodyBuilder":
        self._search_faq_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchFaqResponseBodyBuilder":
        self._search_faq_response_body.page_token = page_token
        return self

    def items(self, items: List[Faq]) -> "SearchFaqResponseBodyBuilder":
        self._search_faq_response_body.items = items
        return self

    def build(self) -> "SearchFaqResponseBody":
        return self._search_faq_response_body
