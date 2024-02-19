# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n


class ApplicationResumeSource(object):
    _types = {
        "id": str,
        "name": I18n,
        "resume_source_type": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.resume_source_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationResumeSourceBuilder":
        return ApplicationResumeSourceBuilder()


class ApplicationResumeSourceBuilder(object):
    def __init__(self) -> None:
        self._application_resume_source = ApplicationResumeSource()

    def id(self, id: str) -> "ApplicationResumeSourceBuilder":
        self._application_resume_source.id = id
        return self

    def name(self, name: I18n) -> "ApplicationResumeSourceBuilder":
        self._application_resume_source.name = name
        return self

    def resume_source_type(self, resume_source_type: int) -> "ApplicationResumeSourceBuilder":
        self._application_resume_source.resume_source_type = resume_source_type
        return self

    def build(self) -> "ApplicationResumeSource":
        return self._application_resume_source
