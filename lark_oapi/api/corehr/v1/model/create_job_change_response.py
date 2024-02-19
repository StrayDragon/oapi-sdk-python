# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_job_change_response_body import CreateJobChangeResponseBody


class CreateJobChangeResponse(BaseResponse):
    _types = {
        "data": CreateJobChangeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateJobChangeResponseBody] = None
        init(self, d, self._types)
