# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_create_app_table_record_response_body import BatchCreateAppTableRecordResponseBody


class BatchCreateAppTableRecordResponse(BaseResponse):
    _types = {
        "data": BatchCreateAppTableRecordResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchCreateAppTableRecordResponseBody] = None
        init(self, d, self._types)