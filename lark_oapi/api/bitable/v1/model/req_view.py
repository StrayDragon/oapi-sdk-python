# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ReqView(object):
    _types = {
        "view_name": str,
        "view_type": str,
    }

    def __init__(self, d):
        self.view_name: Optional[str] = None
        self.view_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReqViewBuilder":
        return ReqViewBuilder()


class ReqViewBuilder(object):
    def __init__(self, req_view: ReqView = ReqView({})) -> None:
        self._req_view: ReqView = req_view

    def view_name(self, view_name: str) -> "ReqViewBuilder":
        self._req_view.view_name = view_name
        return self

    def view_type(self, view_type: str) -> "ReqViewBuilder":
        self._req_view.view_type = view_type
        return self

    def build(self) -> "ReqView":
        return self._req_view