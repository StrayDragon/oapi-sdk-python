# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n


class JobCustomizedOption(object):
    _types = {
        "key": str,
        "name": I18n,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.name: Optional[I18n] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobCustomizedOptionBuilder":
        return JobCustomizedOptionBuilder()


class JobCustomizedOptionBuilder(object):
    def __init__(self) -> None:
        self._job_customized_option = JobCustomizedOption()

    def key(self, key: str) -> "JobCustomizedOptionBuilder":
        self._job_customized_option.key = key
        return self

    def name(self, name: I18n) -> "JobCustomizedOptionBuilder":
        self._job_customized_option.name = name
        return self

    def build(self) -> "JobCustomizedOption":
        return self._job_customized_option
