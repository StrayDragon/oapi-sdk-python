# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class OfferCustomizedInfo(object):
    _types = {
        "id": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferCustomizedInfoBuilder":
        return OfferCustomizedInfoBuilder()


class OfferCustomizedInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_customized_info = OfferCustomizedInfo()

    def id(self, id: str) -> "OfferCustomizedInfoBuilder":
        self._offer_customized_info.id = id
        return self

    def value(self, value: str) -> "OfferCustomizedInfoBuilder":
        self._offer_customized_info.value = value
        return self

    def build(self) -> "OfferCustomizedInfo":
        return self._offer_customized_info
