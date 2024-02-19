# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class PreHireProbationInfo(object):
    _types = {
        "probation_start_date": str,
        "probation_end_date": str,
        "probation_period": int,
    }

    def __init__(self, d=None):
        self.probation_start_date: Optional[str] = None
        self.probation_end_date: Optional[str] = None
        self.probation_period: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreHireProbationInfoBuilder":
        return PreHireProbationInfoBuilder()


class PreHireProbationInfoBuilder(object):
    def __init__(self) -> None:
        self._pre_hire_probation_info = PreHireProbationInfo()

    def probation_start_date(self, probation_start_date: str) -> "PreHireProbationInfoBuilder":
        self._pre_hire_probation_info.probation_start_date = probation_start_date
        return self

    def probation_end_date(self, probation_end_date: str) -> "PreHireProbationInfoBuilder":
        self._pre_hire_probation_info.probation_end_date = probation_end_date
        return self

    def probation_period(self, probation_period: int) -> "PreHireProbationInfoBuilder":
        self._pre_hire_probation_info.probation_period = probation_period
        return self

    def build(self) -> "PreHireProbationInfo":
        return self._pre_hire_probation_info
