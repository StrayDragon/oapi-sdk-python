# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class InstanceSearchLink(object):
    _types = {
        "pc_link": str,
        "mobile_link": str,
    }

    def __init__(self, d=None):
        self.pc_link: Optional[str] = None
        self.mobile_link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceSearchLinkBuilder":
        return InstanceSearchLinkBuilder()


class InstanceSearchLinkBuilder(object):
    def __init__(self) -> None:
        self._instance_search_link = InstanceSearchLink()

    def pc_link(self, pc_link: str) -> "InstanceSearchLinkBuilder":
        self._instance_search_link.pc_link = pc_link
        return self

    def mobile_link(self, mobile_link: str) -> "InstanceSearchLinkBuilder":
        self._instance_search_link.mobile_link = mobile_link
        return self

    def build(self) -> "InstanceSearchLink":
        return self._instance_search_link
