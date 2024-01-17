# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiPresent(object):
    _types = {
        "type": str,
        "body": str,
        "callback_url": str,
        "callback_info": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.body: Optional[str] = None
        self.callback_url: Optional[str] = None
        self.callback_info: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiPresentBuilder":
        return MyAiPresentBuilder()


class MyAiPresentBuilder(object):
    def __init__(self) -> None:
        self._my_ai_present = MyAiPresent()

    def type(self, type: str) -> "MyAiPresentBuilder":
        self._my_ai_present.type = type
        return self

    def body(self, body: str) -> "MyAiPresentBuilder":
        self._my_ai_present.body = body
        return self

    def callback_url(self, callback_url: str) -> "MyAiPresentBuilder":
        self._my_ai_present.callback_url = callback_url
        return self

    def callback_info(self, callback_info: str) -> "MyAiPresentBuilder":
        self._my_ai_present.callback_info = callback_info
        return self

    def build(self) -> "MyAiPresent":
        return self._my_ai_present