# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EmailAlias(object):
    _types = {
        "primary_email": str,
        "email_alias": str,
    }

    def __init__(self, d):
        self.primary_email: Optional[str] = None
        self.email_alias: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmailAliasBuilder":
        return EmailAliasBuilder()


class EmailAliasBuilder(object):
    def __init__(self, email_alias: EmailAlias = EmailAlias({})) -> None:
        self._email_alias: EmailAlias = email_alias

    def primary_email(self, primary_email: str) -> "EmailAliasBuilder":
        self._email_alias.primary_email = primary_email
        return self

    def email_alias(self, email_alias: str) -> "EmailAliasBuilder":
        self._email_alias.email_alias = email_alias
        return self

    def build(self) -> "EmailAlias":
        return self._email_alias