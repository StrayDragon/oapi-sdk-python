# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .evaluation import Evaluation


class ListEvaluationResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[Evaluation],
    }

    def __init__(self, d):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[Evaluation]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListEvaluationResponseBodyBuilder":
        return ListEvaluationResponseBodyBuilder()


class ListEvaluationResponseBodyBuilder(object):
    def __init__(self,
                 list_evaluation_response_body: ListEvaluationResponseBody = ListEvaluationResponseBody({})) -> None:
        self._list_evaluation_response_body: ListEvaluationResponseBody = list_evaluation_response_body

    def has_more(self, has_more: bool) -> "ListEvaluationResponseBodyBuilder":
        self._list_evaluation_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListEvaluationResponseBodyBuilder":
        self._list_evaluation_response_body.page_token = page_token
        return self

    def items(self, items: List[Evaluation]) -> "ListEvaluationResponseBodyBuilder":
        self._list_evaluation_response_body.items = items
        return self

    def build(self) -> "ListEvaluationResponseBody":
        return self._list_evaluation_response_body