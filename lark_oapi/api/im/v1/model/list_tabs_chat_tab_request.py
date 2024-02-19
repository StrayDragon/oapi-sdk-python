# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListTabsChatTabRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListTabsChatTabRequestBuilder":
        return ListTabsChatTabRequestBuilder()


class ListTabsChatTabRequestBuilder(object):

    def __init__(self) -> None:
        list_tabs_chat_tab_request = ListTabsChatTabRequest()
        list_tabs_chat_tab_request.http_method = HttpMethod.GET
        list_tabs_chat_tab_request.uri = "/open-apis/im/v1/chats/:chat_id/chat_tabs/list_tabs"
        list_tabs_chat_tab_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_tabs_chat_tab_request: ListTabsChatTabRequest = list_tabs_chat_tab_request

    def chat_id(self, chat_id: str) -> "ListTabsChatTabRequestBuilder":
        self._list_tabs_chat_tab_request.chat_id = chat_id
        self._list_tabs_chat_tab_request.paths["chat_id"] = str(chat_id)
        return self

    def build(self) -> ListTabsChatTabRequest:
        return self._list_tabs_chat_tab_request
