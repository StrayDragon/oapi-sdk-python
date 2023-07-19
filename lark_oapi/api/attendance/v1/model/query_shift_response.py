# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_shift_response_body import QueryShiftResponseBody


class QueryShiftResponse(BaseResponse):
    _types = {
        "data": QueryShiftResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[QueryShiftResponseBody] = None
        init(self, d, self._types)