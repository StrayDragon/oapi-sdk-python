# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MailContact(object):
    _types = {
        "id": str,
        "name": str,
        "company": str,
        "phone": str,
        "mail_address": str,
        "tag": str,
        "remark": str,
        "avatar": str,
        "position": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.company: Optional[str] = None
        self.phone: Optional[str] = None
        self.mail_address: Optional[str] = None
        self.tag: Optional[str] = None
        self.remark: Optional[str] = None
        self.avatar: Optional[str] = None
        self.position: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MailContactBuilder":
        return MailContactBuilder()


class MailContactBuilder(object):
    def __init__(self) -> None:
        self._mail_contact = MailContact()

    def id(self, id: str) -> "MailContactBuilder":
        self._mail_contact.id = id
        return self

    def name(self, name: str) -> "MailContactBuilder":
        self._mail_contact.name = name
        return self

    def company(self, company: str) -> "MailContactBuilder":
        self._mail_contact.company = company
        return self

    def phone(self, phone: str) -> "MailContactBuilder":
        self._mail_contact.phone = phone
        return self

    def mail_address(self, mail_address: str) -> "MailContactBuilder":
        self._mail_contact.mail_address = mail_address
        return self

    def tag(self, tag: str) -> "MailContactBuilder":
        self._mail_contact.tag = tag
        return self

    def remark(self, remark: str) -> "MailContactBuilder":
        self._mail_contact.remark = remark
        return self

    def avatar(self, avatar: str) -> "MailContactBuilder":
        self._mail_contact.avatar = avatar
        return self

    def position(self, position: str) -> "MailContactBuilder":
        self._mail_contact.position = position
        return self

    def build(self) -> "MailContact":
        return self._mail_contact
