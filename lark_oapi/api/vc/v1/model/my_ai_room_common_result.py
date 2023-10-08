# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiRoomCommonResult(object):
    _types = {
        "room_reply": str,
    }

    def __init__(self, d=None):
        self.room_reply: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiRoomCommonResultBuilder":
        return MyAiRoomCommonResultBuilder()


class MyAiRoomCommonResultBuilder(object):
    def __init__(self) -> None:
        self._my_ai_room_common_result = MyAiRoomCommonResult()

    def room_reply(self, room_reply: str) -> "MyAiRoomCommonResultBuilder":
        self._my_ai_room_common_result.room_reply = room_reply
        return self

    def build(self) -> "MyAiRoomCommonResult":
        return self._my_ai_room_common_result
