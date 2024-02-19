# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Mobile(object):
    _types = {
        "code": str,
        "number": str,
    }

    def __init__(self, d=None):
        self.code: Optional[str] = None
        self.number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MobileBuilder":
        return MobileBuilder()


class MobileBuilder(object):
    def __init__(self) -> None:
        self._mobile = Mobile()

    def code(self, code: str) -> "MobileBuilder":
        self._mobile.code = code
        return self

    def number(self, number: str) -> "MobileBuilder":
        self._mobile.number = number
        return self

    def build(self) -> "Mobile":
        return self._mobile
