# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UserInfo(object):
    _types = {
        "user_language": str,
        "timezone": str,
        "user_id": int,
        "user_open_id": str,
        "tenant_id": int,
        "locale": str,
    }

    def __init__(self, d=None):
        self.user_language: Optional[str] = None
        self.timezone: Optional[str] = None
        self.user_id: Optional[int] = None
        self.user_open_id: Optional[str] = None
        self.tenant_id: Optional[int] = None
        self.locale: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserInfoBuilder":
        return UserInfoBuilder()


class UserInfoBuilder(object):
    def __init__(self) -> None:
        self._user_info = UserInfo()

    def user_language(self, user_language: str) -> "UserInfoBuilder":
        self._user_info.user_language = user_language
        return self

    def timezone(self, timezone: str) -> "UserInfoBuilder":
        self._user_info.timezone = timezone
        return self

    def user_id(self, user_id: int) -> "UserInfoBuilder":
        self._user_info.user_id = user_id
        return self

    def user_open_id(self, user_open_id: str) -> "UserInfoBuilder":
        self._user_info.user_open_id = user_open_id
        return self

    def tenant_id(self, tenant_id: int) -> "UserInfoBuilder":
        self._user_info.tenant_id = tenant_id
        return self

    def locale(self, locale: str) -> "UserInfoBuilder":
        self._user_info.locale = locale
        return self

    def build(self) -> "UserInfo":
        return self._user_info
