# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiMessageCallbackRequest(object):
    _types = {
        "message_id": str,
        "callback_info": str,
    }

    def __init__(self, d=None):
        self.message_id: Optional[str] = None
        self.callback_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiMessageCallbackRequestBuilder":
        return MyAiMessageCallbackRequestBuilder()


class MyAiMessageCallbackRequestBuilder(object):
    def __init__(self) -> None:
        self._my_ai_message_callback_request = MyAiMessageCallbackRequest()

    def message_id(self, message_id: str) -> "MyAiMessageCallbackRequestBuilder":
        self._my_ai_message_callback_request.message_id = message_id
        return self

    def callback_info(self, callback_info: str) -> "MyAiMessageCallbackRequestBuilder":
        self._my_ai_message_callback_request.callback_info = callback_info
        return self

    def build(self) -> "MyAiMessageCallbackRequest":
        return self._my_ai_message_callback_request