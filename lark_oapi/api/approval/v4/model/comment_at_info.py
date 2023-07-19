# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CommentAtInfo(object):
    _types = {
        "user_id": int,
        "name": str,
        "offset": int,
    }

    def __init__(self, d):
        self.user_id: Optional[int] = None
        self.name: Optional[str] = None
        self.offset: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommentAtInfoBuilder":
        return CommentAtInfoBuilder()


class CommentAtInfoBuilder(object):
    def __init__(self, comment_at_info: CommentAtInfo = CommentAtInfo({})) -> None:
        self._comment_at_info: CommentAtInfo = comment_at_info

    def user_id(self, user_id: int) -> "CommentAtInfoBuilder":
        self._comment_at_info.user_id = user_id
        return self

    def name(self, name: str) -> "CommentAtInfoBuilder":
        self._comment_at_info.name = name
        return self

    def offset(self, offset: int) -> "CommentAtInfoBuilder":
        self._comment_at_info.offset = offset
        return self

    def build(self) -> "CommentAtInfo":
        return self._comment_at_info