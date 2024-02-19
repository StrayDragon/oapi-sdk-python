# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .item import Item


class UserStatsView(object):
    _types = {
        "view_id": str,
        "stats_type": str,
        "user_id": str,
        "items": List[Item],
    }

    def __init__(self, d=None):
        self.view_id: Optional[str] = None
        self.stats_type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.items: Optional[List[Item]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserStatsViewBuilder":
        return UserStatsViewBuilder()


class UserStatsViewBuilder(object):
    def __init__(self) -> None:
        self._user_stats_view = UserStatsView()

    def view_id(self, view_id: str) -> "UserStatsViewBuilder":
        self._user_stats_view.view_id = view_id
        return self

    def stats_type(self, stats_type: str) -> "UserStatsViewBuilder":
        self._user_stats_view.stats_type = stats_type
        return self

    def user_id(self, user_id: str) -> "UserStatsViewBuilder":
        self._user_stats_view.user_id = user_id
        return self

    def items(self, items: List[Item]) -> "UserStatsViewBuilder":
        self._user_stats_view.items = items
        return self

    def build(self) -> "UserStatsView":
        return self._user_stats_view
