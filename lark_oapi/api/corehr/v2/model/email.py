# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum


class Email(object):
    _types = {
        "email": str,
        "is_primary": bool,
        "is_public": bool,
        "email_usage": Enum,
    }

    def __init__(self, d):
        self.email: Optional[str] = None
        self.is_primary: Optional[bool] = None
        self.is_public: Optional[bool] = None
        self.email_usage: Optional[Enum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmailBuilder":
        return EmailBuilder()


class EmailBuilder(object):
    def __init__(self, email: Email = Email({})) -> None:
        self._email: Email = email

    def email(self, email: str) -> "EmailBuilder":
        self._email.email = email
        return self

    def is_primary(self, is_primary: bool) -> "EmailBuilder":
        self._email.is_primary = is_primary
        return self

    def is_public(self, is_public: bool) -> "EmailBuilder":
        self._email.is_public = is_public
        return self

    def email_usage(self, email_usage: Enum) -> "EmailBuilder":
        self._email.email_usage = email_usage
        return self

    def build(self) -> "Email":
        return self._email