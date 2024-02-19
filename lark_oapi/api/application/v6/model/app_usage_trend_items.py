# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .usage_trend_item import UsageTrendItem


class AppUsageTrendItems(object):
    _types = {
        "id": str,
        "trend": List[UsageTrendItem],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.trend: Optional[List[UsageTrendItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppUsageTrendItemsBuilder":
        return AppUsageTrendItemsBuilder()


class AppUsageTrendItemsBuilder(object):
    def __init__(self) -> None:
        self._app_usage_trend_items = AppUsageTrendItems()

    def id(self, id: str) -> "AppUsageTrendItemsBuilder":
        self._app_usage_trend_items.id = id
        return self

    def trend(self, trend: List[UsageTrendItem]) -> "AppUsageTrendItemsBuilder":
        self._app_usage_trend_items.trend = trend
        return self

    def build(self) -> "AppUsageTrendItems":
        return self._app_usage_trend_items
