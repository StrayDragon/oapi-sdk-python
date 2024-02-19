# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .member import Member


class CreateSpaceMemberResponseBody(object):
    _types = {
        "member": Member,
    }

    def __init__(self, d=None):
        self.member: Optional[Member] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSpaceMemberResponseBodyBuilder":
        return CreateSpaceMemberResponseBodyBuilder()


class CreateSpaceMemberResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_space_member_response_body = CreateSpaceMemberResponseBody()

    def member(self, member: Member) -> "CreateSpaceMemberResponseBodyBuilder":
        self._create_space_member_response_body.member = member
        return self

    def build(self) -> "CreateSpaceMemberResponseBody":
        return self._create_space_member_response_body
