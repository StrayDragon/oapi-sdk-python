# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Attachment(object):
    _types = {
        "id": str,
        "mime_type": str,
        "name": str,
        "size": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.mime_type: Optional[str] = None
        self.name: Optional[str] = None
        self.size: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentBuilder":
        return AttachmentBuilder()


class AttachmentBuilder(object):
    def __init__(self) -> None:
        self._attachment = Attachment()

    def id(self, id: str) -> "AttachmentBuilder":
        self._attachment.id = id
        return self

    def mime_type(self, mime_type: str) -> "AttachmentBuilder":
        self._attachment.mime_type = mime_type
        return self

    def name(self, name: str) -> "AttachmentBuilder":
        self._attachment.name = name
        return self

    def size(self, size: int) -> "AttachmentBuilder":
        self._attachment.size = size
        return self

    def build(self) -> "Attachment":
        return self._attachment
