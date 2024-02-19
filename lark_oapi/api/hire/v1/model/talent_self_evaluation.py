# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentSelfEvaluation(object):
    _types = {
        "id": str,
        "content": str,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.content: Optional[str] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentSelfEvaluationBuilder":
        return TalentSelfEvaluationBuilder()


class TalentSelfEvaluationBuilder(object):
    def __init__(self) -> None:
        self._talent_self_evaluation = TalentSelfEvaluation()

    def id(self, id: str) -> "TalentSelfEvaluationBuilder":
        self._talent_self_evaluation.id = id
        return self

    def content(self, content: str) -> "TalentSelfEvaluationBuilder":
        self._talent_self_evaluation.content = content
        return self

    def customized_data(self, customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentSelfEvaluationBuilder":
        self._talent_self_evaluation.customized_data = customized_data
        return self

    def build(self) -> "TalentSelfEvaluation":
        return self._talent_self_evaluation
