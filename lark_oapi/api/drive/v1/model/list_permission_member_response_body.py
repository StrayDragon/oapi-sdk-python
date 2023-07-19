# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .member import Member


class ListPermissionMemberResponseBody(object):
    _types = {
        "items": List[Member],
    }

    def __init__(self, d):
        self.items: Optional[List[Member]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListPermissionMemberResponseBodyBuilder":
        return ListPermissionMemberResponseBodyBuilder()


class ListPermissionMemberResponseBodyBuilder(object):
    def __init__(self,
                 list_permission_member_response_body: ListPermissionMemberResponseBody = ListPermissionMemberResponseBody(
                     {})) -> None:
        self._list_permission_member_response_body: ListPermissionMemberResponseBody = list_permission_member_response_body

    def items(self, items: List[Member]) -> "ListPermissionMemberResponseBodyBuilder":
        self._list_permission_member_response_body.items = items
        return self

    def build(self) -> "ListPermissionMemberResponseBody":
        return self._list_permission_member_response_body