# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class JobRequirementCustomizedTimeRange(object):
    _types = {
        "start_time": str,
        "end_time": str,
    }

    def __init__(self, d=None):
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementCustomizedTimeRangeBuilder":
        return JobRequirementCustomizedTimeRangeBuilder()


class JobRequirementCustomizedTimeRangeBuilder(object):
    def __init__(self) -> None:
        self._job_requirement_customized_time_range = JobRequirementCustomizedTimeRange()

    def start_time(self, start_time: str) -> "JobRequirementCustomizedTimeRangeBuilder":
        self._job_requirement_customized_time_range.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "JobRequirementCustomizedTimeRangeBuilder":
        self._job_requirement_customized_time_range.end_time = end_time
        return self

    def build(self) -> "JobRequirementCustomizedTimeRange":
        return self._job_requirement_customized_time_range
