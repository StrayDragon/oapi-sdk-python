# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_app_response_body import UpdateAppResponseBody


class UpdateAppResponse(BaseResponse):
    _types = {
        "data": UpdateAppResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateAppResponseBody] = None
        init(self, d, self._types)
