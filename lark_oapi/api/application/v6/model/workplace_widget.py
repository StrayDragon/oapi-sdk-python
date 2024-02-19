# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class WorkplaceWidget(object):
    _types = {
        "min_lark_version": str,
    }

    def __init__(self, d=None):
        self.min_lark_version: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkplaceWidgetBuilder":
        return WorkplaceWidgetBuilder()


class WorkplaceWidgetBuilder(object):
    def __init__(self) -> None:
        self._workplace_widget = WorkplaceWidget()

    def min_lark_version(self, min_lark_version: str) -> "WorkplaceWidgetBuilder":
        self._workplace_widget.min_lark_version = min_lark_version
        return self

    def build(self) -> "WorkplaceWidget":
        return self._workplace_widget
