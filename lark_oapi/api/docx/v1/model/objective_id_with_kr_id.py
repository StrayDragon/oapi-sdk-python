# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class ObjectiveIdWithKrId(object):
    _types = {
        "objective_id": int,
        "kr_ids": List[int],
    }

    def __init__(self, d=None):
        self.objective_id: Optional[int] = None
        self.kr_ids: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectiveIdWithKrIdBuilder":
        return ObjectiveIdWithKrIdBuilder()


class ObjectiveIdWithKrIdBuilder(object):
    def __init__(self) -> None:
        self._objective_id_with_kr_id = ObjectiveIdWithKrId()

    def objective_id(self, objective_id: int) -> "ObjectiveIdWithKrIdBuilder":
        self._objective_id_with_kr_id.objective_id = objective_id
        return self

    def kr_ids(self, kr_ids: List[int]) -> "ObjectiveIdWithKrIdBuilder":
        self._objective_id_with_kr_id.kr_ids = kr_ids
        return self

    def build(self) -> "ObjectiveIdWithKrId":
        return self._objective_id_with_kr_id
