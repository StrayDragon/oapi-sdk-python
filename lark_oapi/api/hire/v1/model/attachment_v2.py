# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class AttachmentV2(object):
    _types = {
        "id": str,
        "url": str,
        "name": str,
        "mime": str,
        "create_time": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.url: Optional[str] = None
        self.name: Optional[str] = None
        self.mime: Optional[str] = None
        self.create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentV2Builder":
        return AttachmentV2Builder()


class AttachmentV2Builder(object):
    def __init__(self) -> None:
        self._attachment_v2 = AttachmentV2()

    def id(self, id: str) -> "AttachmentV2Builder":
        self._attachment_v2.id = id
        return self

    def url(self, url: str) -> "AttachmentV2Builder":
        self._attachment_v2.url = url
        return self

    def name(self, name: str) -> "AttachmentV2Builder":
        self._attachment_v2.name = name
        return self

    def mime(self, mime: str) -> "AttachmentV2Builder":
        self._attachment_v2.mime = mime
        return self

    def create_time(self, create_time: str) -> "AttachmentV2Builder":
        self._attachment_v2.create_time = create_time
        return self

    def build(self) -> "AttachmentV2":
        return self._attachment_v2
