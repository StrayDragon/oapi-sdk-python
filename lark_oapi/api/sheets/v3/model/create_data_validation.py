# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .data_validation import DataValidation


class CreateDataValidation(object):
    _types = {
        "range": str,
        "rule": DataValidation,
    }

    def __init__(self, d=None):
        self.range: Optional[str] = None
        self.rule: Optional[DataValidation] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateDataValidationBuilder":
        return CreateDataValidationBuilder()


class CreateDataValidationBuilder(object):
    def __init__(self) -> None:
        self._create_data_validation = CreateDataValidation()

    def range(self, range: str) -> "CreateDataValidationBuilder":
        self._create_data_validation.range = range
        return self

    def rule(self, rule: DataValidation) -> "CreateDataValidationBuilder":
        self._create_data_validation.rule = rule
        return self

    def build(self) -> "CreateDataValidation":
        return self._create_data_validation
