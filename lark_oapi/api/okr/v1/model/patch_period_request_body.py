# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class PatchPeriodRequestBody(object):
    _types = {
        "status": int,
    }

    def __init__(self, d=None):
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPeriodRequestBodyBuilder":
        return PatchPeriodRequestBodyBuilder()


class PatchPeriodRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_period_request_body = PatchPeriodRequestBody()

    def status(self, status: int) -> "PatchPeriodRequestBodyBuilder":
        self._patch_period_request_body.status = status
        return self

    def build(self) -> "PatchPeriodRequestBody":
        return self._patch_period_request_body
