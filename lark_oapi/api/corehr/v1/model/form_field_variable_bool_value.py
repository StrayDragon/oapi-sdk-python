# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FormFieldVariableBoolValue(object):
    _types = {
        "value": bool,
    }

    def __init__(self, d):
        self.value: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableBoolValueBuilder":
        return FormFieldVariableBoolValueBuilder()


class FormFieldVariableBoolValueBuilder(object):
    def __init__(self,
                 form_field_variable_bool_value: FormFieldVariableBoolValue = FormFieldVariableBoolValue({})) -> None:
        self._form_field_variable_bool_value: FormFieldVariableBoolValue = form_field_variable_bool_value

    def value(self, value: bool) -> "FormFieldVariableBoolValueBuilder":
        self._form_field_variable_bool_value.value = value
        return self

    def build(self) -> "FormFieldVariableBoolValue":
        return self._form_field_variable_bool_value