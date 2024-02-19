# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class WebsiteChannelInfo(object):
    _types = {
        "id": str,
        "name": str,
        "link": str,
        "code": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.link: Optional[str] = None
        self.code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteChannelInfoBuilder":
        return WebsiteChannelInfoBuilder()


class WebsiteChannelInfoBuilder(object):
    def __init__(self) -> None:
        self._website_channel_info = WebsiteChannelInfo()

    def id(self, id: str) -> "WebsiteChannelInfoBuilder":
        self._website_channel_info.id = id
        return self

    def name(self, name: str) -> "WebsiteChannelInfoBuilder":
        self._website_channel_info.name = name
        return self

    def link(self, link: str) -> "WebsiteChannelInfoBuilder":
        self._website_channel_info.link = link
        return self

    def code(self, code: str) -> "WebsiteChannelInfoBuilder":
        self._website_channel_info.code = code
        return self

    def build(self) -> "WebsiteChannelInfo":
        return self._website_channel_info
