# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Setting(object):
    _types = {
        "create_setting": str,
        "security_setting": str,
        "comment_setting": str,
    }

    def __init__(self, d=None):
        self.create_setting: Optional[str] = None
        self.security_setting: Optional[str] = None
        self.comment_setting: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SettingBuilder":
        return SettingBuilder()


class SettingBuilder(object):
    def __init__(self) -> None:
        self._setting = Setting()

    def create_setting(self, create_setting: str) -> "SettingBuilder":
        self._setting.create_setting = create_setting
        return self

    def security_setting(self, security_setting: str) -> "SettingBuilder":
        self._setting.security_setting = security_setting
        return self

    def comment_setting(self, comment_setting: str) -> "SettingBuilder":
        self._setting.comment_setting = comment_setting
        return self

    def build(self) -> "Setting":
        return self._setting
