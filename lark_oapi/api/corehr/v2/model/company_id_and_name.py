# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .i18n import I18n


class CompanyIdAndName(object):
    _types = {
        "company_id": str,
        "company_name": List[I18n],
    }

    def __init__(self, d=None):
        self.company_id: Optional[str] = None
        self.company_name: Optional[List[I18n]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompanyIdAndNameBuilder":
        return CompanyIdAndNameBuilder()


class CompanyIdAndNameBuilder(object):
    def __init__(self) -> None:
        self._company_id_and_name = CompanyIdAndName()

    def company_id(self, company_id: str) -> "CompanyIdAndNameBuilder":
        self._company_id_and_name.company_id = company_id
        return self

    def company_name(self, company_name: List[I18n]) -> "CompanyIdAndNameBuilder":
        self._company_id_and_name.company_name = company_name
        return self

    def build(self) -> "CompanyIdAndName":
        return self._company_id_and_name
