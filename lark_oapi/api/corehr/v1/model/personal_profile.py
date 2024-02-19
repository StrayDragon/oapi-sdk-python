# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .enum import Enum
from .file import File


class PersonalProfile(object):
    _types = {
        "personal_profile_id": str,
        "personal_profile_type": Enum,
        "files": List[File],
    }

    def __init__(self, d=None):
        self.personal_profile_id: Optional[str] = None
        self.personal_profile_type: Optional[Enum] = None
        self.files: Optional[List[File]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PersonalProfileBuilder":
        return PersonalProfileBuilder()


class PersonalProfileBuilder(object):
    def __init__(self) -> None:
        self._personal_profile = PersonalProfile()

    def personal_profile_id(self, personal_profile_id: str) -> "PersonalProfileBuilder":
        self._personal_profile.personal_profile_id = personal_profile_id
        return self

    def personal_profile_type(self, personal_profile_type: Enum) -> "PersonalProfileBuilder":
        self._personal_profile.personal_profile_type = personal_profile_type
        return self

    def files(self, files: List[File]) -> "PersonalProfileBuilder":
        self._personal_profile.files = files
        return self

    def build(self) -> "PersonalProfile":
        return self._personal_profile
