# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TaxiEnitity(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaxiEnitityBuilder":
        return TaxiEnitityBuilder()


class TaxiEnitityBuilder(object):
    def __init__(self) -> None:
        self._taxi_enitity = TaxiEnitity()

    def type(self, type: str) -> "TaxiEnitityBuilder":
        self._taxi_enitity.type = type
        return self

    def value(self, value: str) -> "TaxiEnitityBuilder":
        self._taxi_enitity.value = value
        return self

    def build(self) -> "TaxiEnitity":
        return self._taxi_enitity
