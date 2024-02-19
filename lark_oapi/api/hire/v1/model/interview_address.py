# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .code_name_object import CodeNameObject
from .i18n import I18n


class InterviewAddress(object):
    _types = {
        "id": str,
        "name": I18n,
        "district": CodeNameObject,
        "city": CodeNameObject,
        "state": CodeNameObject,
        "country": CodeNameObject,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.district: Optional[CodeNameObject] = None
        self.city: Optional[CodeNameObject] = None
        self.state: Optional[CodeNameObject] = None
        self.country: Optional[CodeNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewAddressBuilder":
        return InterviewAddressBuilder()


class InterviewAddressBuilder(object):
    def __init__(self) -> None:
        self._interview_address = InterviewAddress()

    def id(self, id: str) -> "InterviewAddressBuilder":
        self._interview_address.id = id
        return self

    def name(self, name: I18n) -> "InterviewAddressBuilder":
        self._interview_address.name = name
        return self

    def district(self, district: CodeNameObject) -> "InterviewAddressBuilder":
        self._interview_address.district = district
        return self

    def city(self, city: CodeNameObject) -> "InterviewAddressBuilder":
        self._interview_address.city = city
        return self

    def state(self, state: CodeNameObject) -> "InterviewAddressBuilder":
        self._interview_address.state = state
        return self

    def country(self, country: CodeNameObject) -> "InterviewAddressBuilder":
        self._interview_address.country = country
        return self

    def build(self) -> "InterviewAddress":
        return self._interview_address
