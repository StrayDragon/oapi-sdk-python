# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_tab import ChatTab


class SortTabsChatTabResponseBody(object):
    _types = {
        "chat_tabs": List[ChatTab],
    }

    def __init__(self, d):
        self.chat_tabs: Optional[List[ChatTab]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SortTabsChatTabResponseBodyBuilder":
        return SortTabsChatTabResponseBodyBuilder()


class SortTabsChatTabResponseBodyBuilder(object):
    def __init__(self, sort_tabs_chat_tab_response_body: SortTabsChatTabResponseBody = SortTabsChatTabResponseBody(
        {})) -> None:
        self._sort_tabs_chat_tab_response_body: SortTabsChatTabResponseBody = sort_tabs_chat_tab_response_body

    def chat_tabs(self, chat_tabs: List[ChatTab]) -> "SortTabsChatTabResponseBodyBuilder":
        self._sort_tabs_chat_tab_response_body.chat_tabs = chat_tabs
        return self

    def build(self) -> "SortTabsChatTabResponseBody":
        return self._sort_tabs_chat_tab_response_body