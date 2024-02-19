# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_employment_response_body import CreateEmploymentResponseBody


class CreateEmploymentResponse(BaseResponse):
    _types = {
        "data": CreateEmploymentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateEmploymentResponseBody] = None
        init(self, d, self._types)
