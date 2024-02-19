# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_chat_moderation_request_body import UpdateChatModerationRequestBody


class UpdateChatModerationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.request_body: Optional[UpdateChatModerationRequestBody] = None

    @staticmethod
    def builder() -> "UpdateChatModerationRequestBuilder":
        return UpdateChatModerationRequestBuilder()


class UpdateChatModerationRequestBuilder(object):

    def __init__(self) -> None:
        update_chat_moderation_request = UpdateChatModerationRequest()
        update_chat_moderation_request.http_method = HttpMethod.PUT
        update_chat_moderation_request.uri = "/open-apis/im/v1/chats/:chat_id/moderation"
        update_chat_moderation_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._update_chat_moderation_request: UpdateChatModerationRequest = update_chat_moderation_request

    def user_id_type(self, user_id_type: str) -> "UpdateChatModerationRequestBuilder":
        self._update_chat_moderation_request.user_id_type = user_id_type
        self._update_chat_moderation_request.add_query("user_id_type", user_id_type)
        return self

    def chat_id(self, chat_id: str) -> "UpdateChatModerationRequestBuilder":
        self._update_chat_moderation_request.chat_id = chat_id
        self._update_chat_moderation_request.paths["chat_id"] = str(chat_id)
        return self

    def request_body(self, request_body: UpdateChatModerationRequestBody) -> "UpdateChatModerationRequestBuilder":
        self._update_chat_moderation_request.request_body = request_body
        self._update_chat_moderation_request.body = request_body
        return self

    def build(self) -> UpdateChatModerationRequest:
        return self._update_chat_moderation_request
