# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .progress_item import ProgressItem
from .progress_rate import ProgressRate
from .upsert_objective_kr import UpsertObjectiveKr


class UpsertObjective(object):
    _types = {
        "content": str,
        "mention_list": List[str],
        "kr_list": List[UpsertObjectiveKr],
        "progress_rate": ProgressRate,
        "progress_list": List[ProgressItem],
        "weight": float,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.mention_list: Optional[List[str]] = None
        self.kr_list: Optional[List[UpsertObjectiveKr]] = None
        self.progress_rate: Optional[ProgressRate] = None
        self.progress_list: Optional[List[ProgressItem]] = None
        self.weight: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpsertObjectiveBuilder":
        return UpsertObjectiveBuilder()


class UpsertObjectiveBuilder(object):
    def __init__(self) -> None:
        self._upsert_objective = UpsertObjective()

    def content(self, content: str) -> "UpsertObjectiveBuilder":
        self._upsert_objective.content = content
        return self

    def mention_list(self, mention_list: List[str]) -> "UpsertObjectiveBuilder":
        self._upsert_objective.mention_list = mention_list
        return self

    def kr_list(self, kr_list: List[UpsertObjectiveKr]) -> "UpsertObjectiveBuilder":
        self._upsert_objective.kr_list = kr_list
        return self

    def progress_rate(self, progress_rate: ProgressRate) -> "UpsertObjectiveBuilder":
        self._upsert_objective.progress_rate = progress_rate
        return self

    def progress_list(self, progress_list: List[ProgressItem]) -> "UpsertObjectiveBuilder":
        self._upsert_objective.progress_list = progress_list
        return self

    def weight(self, weight: float) -> "UpsertObjectiveBuilder":
        self._upsert_objective.weight = weight
        return self

    def build(self) -> "UpsertObjective":
        return self._upsert_objective
