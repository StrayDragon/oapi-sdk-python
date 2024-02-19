# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Thread(object):
    _types = {
        "thread_id": str,
        "chat_id": str,
        "update_time": str,
    }

    def __init__(self, d=None):
        self.thread_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.update_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ThreadBuilder":
        return ThreadBuilder()


class ThreadBuilder(object):
    def __init__(self) -> None:
        self._thread = Thread()

    def thread_id(self, thread_id: str) -> "ThreadBuilder":
        self._thread.thread_id = thread_id
        return self

    def chat_id(self, chat_id: str) -> "ThreadBuilder":
        self._thread.chat_id = chat_id
        return self

    def update_time(self, update_time: str) -> "ThreadBuilder":
        self._thread.update_time = update_time
        return self

    def build(self) -> "Thread":
        return self._thread
