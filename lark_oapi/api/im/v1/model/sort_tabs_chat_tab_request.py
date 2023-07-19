# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .sort_tabs_chat_tab_request_body import SortTabsChatTabRequestBody


class SortTabsChatTabRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None
        self.request_body: Optional[SortTabsChatTabRequestBody] = None

    @staticmethod
    def builder() -> "SortTabsChatTabRequestBuilder":
        return SortTabsChatTabRequestBuilder()


class SortTabsChatTabRequestBuilder(object):

    def __init__(self, sort_tabs_chat_tab_request: SortTabsChatTabRequest = SortTabsChatTabRequest()) -> None:
        sort_tabs_chat_tab_request.http_method = HttpMethod.POST
        sort_tabs_chat_tab_request.uri = "/open-apis/im/v1/chats/:chat_id/chat_tabs/sort_tabs"
        sort_tabs_chat_tab_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._sort_tabs_chat_tab_request: SortTabsChatTabRequest = sort_tabs_chat_tab_request

    def chat_id(self, chat_id: str) -> "SortTabsChatTabRequestBuilder":
        self._sort_tabs_chat_tab_request.chat_id = chat_id
        self._sort_tabs_chat_tab_request.paths["chat_id"] = chat_id
        return self

    def request_body(self, request_body: SortTabsChatTabRequestBody) -> "SortTabsChatTabRequestBuilder":
        self._sort_tabs_chat_tab_request.request_body = request_body
        self._sort_tabs_chat_tab_request.body = request_body
        return self

    def build(self) -> SortTabsChatTabRequest:
        return self._sort_tabs_chat_tab_request