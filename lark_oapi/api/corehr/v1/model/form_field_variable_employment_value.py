# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class FormFieldVariableEmploymentValue(object):
    _types = {
        "value": str,
        "user_id": str,
    }

    def __init__(self, d=None):
        self.value: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableEmploymentValueBuilder":
        return FormFieldVariableEmploymentValueBuilder()


class FormFieldVariableEmploymentValueBuilder(object):
    def __init__(self) -> None:
        self._form_field_variable_employment_value = FormFieldVariableEmploymentValue()

    def value(self, value: str) -> "FormFieldVariableEmploymentValueBuilder":
        self._form_field_variable_employment_value.value = value
        return self

    def user_id(self, user_id: str) -> "FormFieldVariableEmploymentValueBuilder":
        self._form_field_variable_employment_value.user_id = user_id
        return self

    def build(self) -> "FormFieldVariableEmploymentValue":
        return self._form_field_variable_employment_value
