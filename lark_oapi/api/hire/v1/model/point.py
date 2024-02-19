# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Point(object):
    _types = {
        "amount": int,
    }

    def __init__(self, d=None):
        self.amount: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PointBuilder":
        return PointBuilder()


class PointBuilder(object):
    def __init__(self) -> None:
        self._point = Point()

    def amount(self, amount: int) -> "PointBuilder":
        self._point.amount = amount
        return self

    def build(self) -> "Point":
        return self._point
