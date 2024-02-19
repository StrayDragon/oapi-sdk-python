# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .app_table_record import AppTableRecord


class ListAppTableRecordResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "total": int,
        "items": List[AppTableRecord],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.total: Optional[int] = None
        self.items: Optional[List[AppTableRecord]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppTableRecordResponseBodyBuilder":
        return ListAppTableRecordResponseBodyBuilder()


class ListAppTableRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_app_table_record_response_body = ListAppTableRecordResponseBody()

    def has_more(self, has_more: bool) -> "ListAppTableRecordResponseBodyBuilder":
        self._list_app_table_record_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListAppTableRecordResponseBodyBuilder":
        self._list_app_table_record_response_body.page_token = page_token
        return self

    def total(self, total: int) -> "ListAppTableRecordResponseBodyBuilder":
        self._list_app_table_record_response_body.total = total
        return self

    def items(self, items: List[AppTableRecord]) -> "ListAppTableRecordResponseBodyBuilder":
        self._list_app_table_record_response_body.items = items
        return self

    def build(self) -> "ListAppTableRecordResponseBody":
        return self._list_app_table_record_response_body
