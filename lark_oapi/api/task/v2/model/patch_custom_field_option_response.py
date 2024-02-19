# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_custom_field_option_response_body import PatchCustomFieldOptionResponseBody


class PatchCustomFieldOptionResponse(BaseResponse):
    _types = {
        "data": PatchCustomFieldOptionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchCustomFieldOptionResponseBody] = None
        init(self, d, self._types)
