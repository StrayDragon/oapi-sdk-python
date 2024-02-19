# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_progress_batch_message_response_body import GetProgressBatchMessageResponseBody


class GetProgressBatchMessageResponse(BaseResponse):
    _types = {
        "data": GetProgressBatchMessageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetProgressBatchMessageResponseBody] = None
        init(self, d, self._types)
