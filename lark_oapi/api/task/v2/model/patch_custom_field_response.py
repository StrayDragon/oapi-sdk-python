# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_custom_field_response_body import PatchCustomFieldResponseBody


class PatchCustomFieldResponse(BaseResponse):
    _types = {
        "data": PatchCustomFieldResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchCustomFieldResponseBody] = None
        init(self, d, self._types)
