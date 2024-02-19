# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .bitable_table_field_action_value_property import BitableTableFieldActionValueProperty


class BitableTableFieldActionValue(object):
    _types = {
        "id": str,
        "name": str,
        "type": int,
        "description": str,
        "property": BitableTableFieldActionValueProperty,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.type: Optional[int] = None
        self.description: Optional[str] = None
        self.property: Optional[BitableTableFieldActionValueProperty] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableFieldActionValueBuilder":
        return BitableTableFieldActionValueBuilder()


class BitableTableFieldActionValueBuilder(object):
    def __init__(self) -> None:
        self._bitable_table_field_action_value = BitableTableFieldActionValue()

    def id(self, id: str) -> "BitableTableFieldActionValueBuilder":
        self._bitable_table_field_action_value.id = id
        return self

    def name(self, name: str) -> "BitableTableFieldActionValueBuilder":
        self._bitable_table_field_action_value.name = name
        return self

    def type(self, type: int) -> "BitableTableFieldActionValueBuilder":
        self._bitable_table_field_action_value.type = type
        return self

    def description(self, description: str) -> "BitableTableFieldActionValueBuilder":
        self._bitable_table_field_action_value.description = description
        return self

    def property(self, property: BitableTableFieldActionValueProperty) -> "BitableTableFieldActionValueBuilder":
        self._bitable_table_field_action_value.property = property
        return self

    def build(self) -> "BitableTableFieldActionValue":
        return self._bitable_table_field_action_value
