# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .custom_attr_generic_user import CustomAttrGenericUser


class UserCustomAttrValue(object):
    _types = {
        "text": str,
        "url": str,
        "pc_url": str,
        "option_id": str,
        "option_value": str,
        "name": str,
        "picture_url": str,
        "generic_user": CustomAttrGenericUser,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.url: Optional[str] = None
        self.pc_url: Optional[str] = None
        self.option_id: Optional[str] = None
        self.option_value: Optional[str] = None
        self.name: Optional[str] = None
        self.picture_url: Optional[str] = None
        self.generic_user: Optional[CustomAttrGenericUser] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserCustomAttrValueBuilder":
        return UserCustomAttrValueBuilder()


class UserCustomAttrValueBuilder(object):
    def __init__(self) -> None:
        self._user_custom_attr_value = UserCustomAttrValue()

    def text(self, text: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.text = text
        return self

    def url(self, url: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.url = url
        return self

    def pc_url(self, pc_url: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.pc_url = pc_url
        return self

    def option_id(self, option_id: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.option_id = option_id
        return self

    def option_value(self, option_value: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.option_value = option_value
        return self

    def name(self, name: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.name = name
        return self

    def picture_url(self, picture_url: str) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.picture_url = picture_url
        return self

    def generic_user(self, generic_user: CustomAttrGenericUser) -> "UserCustomAttrValueBuilder":
        self._user_custom_attr_value.generic_user = generic_user
        return self

    def build(self) -> "UserCustomAttrValue":
        return self._user_custom_attr_value
