# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .job_level import JobLevel


class GetJobLevelResponseBody(object):
    _types = {
        "job_level": JobLevel,
    }

    def __init__(self, d=None):
        self.job_level: Optional[JobLevel] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetJobLevelResponseBodyBuilder":
        return GetJobLevelResponseBodyBuilder()


class GetJobLevelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_job_level_response_body = GetJobLevelResponseBody()

    def job_level(self, job_level: JobLevel) -> "GetJobLevelResponseBodyBuilder":
        self._get_job_level_response_body.job_level = job_level
        return self

    def build(self) -> "GetJobLevelResponseBody":
        return self._get_job_level_response_body
