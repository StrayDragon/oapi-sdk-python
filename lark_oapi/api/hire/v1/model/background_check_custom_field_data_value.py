# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BackgroundCheckCustomFieldDataValue(object):
    _types = {
        "key": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BackgroundCheckCustomFieldDataValueBuilder":
        return BackgroundCheckCustomFieldDataValueBuilder()


class BackgroundCheckCustomFieldDataValueBuilder(object):
    def __init__(self) -> None:
        self._background_check_custom_field_data_value = BackgroundCheckCustomFieldDataValue()

    def key(self, key: str) -> "BackgroundCheckCustomFieldDataValueBuilder":
        self._background_check_custom_field_data_value.key = key
        return self

    def value(self, value: str) -> "BackgroundCheckCustomFieldDataValueBuilder":
        self._background_check_custom_field_data_value.value = value
        return self

    def build(self) -> "BackgroundCheckCustomFieldDataValue":
        return self._background_check_custom_field_data_value
