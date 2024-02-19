# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class LookupFieldSetting(object):
    _types = {
        "lookup_obj_api_name": str,
        "is_multiple": bool,
    }

    def __init__(self, d=None):
        self.lookup_obj_api_name: Optional[str] = None
        self.is_multiple: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LookupFieldSettingBuilder":
        return LookupFieldSettingBuilder()


class LookupFieldSettingBuilder(object):
    def __init__(self) -> None:
        self._lookup_field_setting = LookupFieldSetting()

    def lookup_obj_api_name(self, lookup_obj_api_name: str) -> "LookupFieldSettingBuilder":
        self._lookup_field_setting.lookup_obj_api_name = lookup_obj_api_name
        return self

    def is_multiple(self, is_multiple: bool) -> "LookupFieldSettingBuilder":
        self._lookup_field_setting.is_multiple = is_multiple
        return self

    def build(self) -> "LookupFieldSetting":
        return self._lookup_field_setting
