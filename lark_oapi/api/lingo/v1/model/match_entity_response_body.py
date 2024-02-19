# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .match_info import MatchInfo


class MatchEntityResponseBody(object):
    _types = {
        "results": List[MatchInfo],
    }

    def __init__(self, d=None):
        self.results: Optional[List[MatchInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MatchEntityResponseBodyBuilder":
        return MatchEntityResponseBodyBuilder()


class MatchEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._match_entity_response_body = MatchEntityResponseBody()

    def results(self, results: List[MatchInfo]) -> "MatchEntityResponseBodyBuilder":
        self._match_entity_response_body.results = results
        return self

    def build(self) -> "MatchEntityResponseBody":
        return self._match_entity_response_body
