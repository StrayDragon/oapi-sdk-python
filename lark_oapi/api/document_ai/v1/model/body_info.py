# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .body_entity import BodyEntity


class BodyInfo(object):
    _types = {
        "body_type": str,
        "value": BodyEntity,
    }

    def __init__(self, d=None):
        self.body_type: Optional[str] = None
        self.value: Optional[BodyEntity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BodyInfoBuilder":
        return BodyInfoBuilder()


class BodyInfoBuilder(object):
    def __init__(self) -> None:
        self._body_info = BodyInfo()

    def body_type(self, body_type: str) -> "BodyInfoBuilder":
        self._body_info.body_type = body_type
        return self

    def value(self, value: BodyEntity) -> "BodyInfoBuilder":
        self._body_info.value = value
        return self

    def build(self) -> "BodyInfo":
        return self._body_info
