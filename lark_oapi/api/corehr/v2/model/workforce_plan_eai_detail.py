# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class WorkforcePlanEaiDetail(object):
    _types = {
        "date": str,
        "estimated_active_individuals": str,
    }

    def __init__(self, d=None):
        self.date: Optional[str] = None
        self.estimated_active_individuals: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkforcePlanEaiDetailBuilder":
        return WorkforcePlanEaiDetailBuilder()


class WorkforcePlanEaiDetailBuilder(object):
    def __init__(self) -> None:
        self._workforce_plan_eai_detail = WorkforcePlanEaiDetail()

    def date(self, date: str) -> "WorkforcePlanEaiDetailBuilder":
        self._workforce_plan_eai_detail.date = date
        return self

    def estimated_active_individuals(self, estimated_active_individuals: str) -> "WorkforcePlanEaiDetailBuilder":
        self._workforce_plan_eai_detail.estimated_active_individuals = estimated_active_individuals
        return self

    def build(self) -> "WorkforcePlanEaiDetail":
        return self._workforce_plan_eai_detail
