# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class QueryOffboardingRequestBody(object):
    _types = {
        "active": bool,
        "offboarding_reason_unique_identifier": List[str],
    }

    def __init__(self, d=None):
        self.active: Optional[bool] = None
        self.offboarding_reason_unique_identifier: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryOffboardingRequestBodyBuilder":
        return QueryOffboardingRequestBodyBuilder()


class QueryOffboardingRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_offboarding_request_body = QueryOffboardingRequestBody()

    def active(self, active: bool) -> "QueryOffboardingRequestBodyBuilder":
        self._query_offboarding_request_body.active = active
        return self

    def offboarding_reason_unique_identifier(self, offboarding_reason_unique_identifier: List[
        str]) -> "QueryOffboardingRequestBodyBuilder":
        self._query_offboarding_request_body.offboarding_reason_unique_identifier = offboarding_reason_unique_identifier
        return self

    def build(self) -> "QueryOffboardingRequestBody":
        return self._query_offboarding_request_body
