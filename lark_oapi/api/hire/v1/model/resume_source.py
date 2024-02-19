# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ResumeSource(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
        "active_status": int,
        "resume_source_type": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.active_status: Optional[int] = None
        self.resume_source_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ResumeSourceBuilder":
        return ResumeSourceBuilder()


class ResumeSourceBuilder(object):
    def __init__(self) -> None:
        self._resume_source = ResumeSource()

    def id(self, id: str) -> "ResumeSourceBuilder":
        self._resume_source.id = id
        return self

    def zh_name(self, zh_name: str) -> "ResumeSourceBuilder":
        self._resume_source.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "ResumeSourceBuilder":
        self._resume_source.en_name = en_name
        return self

    def active_status(self, active_status: int) -> "ResumeSourceBuilder":
        self._resume_source.active_status = active_status
        return self

    def resume_source_type(self, resume_source_type: int) -> "ResumeSourceBuilder":
        self._resume_source.resume_source_type = resume_source_type
        return self

    def build(self) -> "ResumeSource":
        return self._resume_source
