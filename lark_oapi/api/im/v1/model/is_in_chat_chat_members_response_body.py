# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class IsInChatChatMembersResponseBody(object):
    _types = {
        "is_in_chat": bool,
    }

    def __init__(self, d=None):
        self.is_in_chat: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "IsInChatChatMembersResponseBodyBuilder":
        return IsInChatChatMembersResponseBodyBuilder()


class IsInChatChatMembersResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._is_in_chat_chat_members_response_body = IsInChatChatMembersResponseBody()

    def is_in_chat(self, is_in_chat: bool) -> "IsInChatChatMembersResponseBodyBuilder":
        self._is_in_chat_chat_members_response_body.is_in_chat = is_in_chat
        return self

    def build(self) -> "IsInChatChatMembersResponseBody":
        return self._is_in_chat_chat_members_response_body
