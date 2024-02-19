# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Administrator(object):
    _types = {
        "user_id": int,
        "is_super_administrator": bool,
        "is_administrator": bool,
    }

    def __init__(self, d=None):
        self.user_id: Optional[int] = None
        self.is_super_administrator: Optional[bool] = None
        self.is_administrator: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AdministratorBuilder":
        return AdministratorBuilder()


class AdministratorBuilder(object):
    def __init__(self) -> None:
        self._administrator = Administrator()

    def user_id(self, user_id: int) -> "AdministratorBuilder":
        self._administrator.user_id = user_id
        return self

    def is_super_administrator(self, is_super_administrator: bool) -> "AdministratorBuilder":
        self._administrator.is_super_administrator = is_super_administrator
        return self

    def is_administrator(self, is_administrator: bool) -> "AdministratorBuilder":
        self._administrator.is_administrator = is_administrator
        return self

    def build(self) -> "Administrator":
        return self._administrator
