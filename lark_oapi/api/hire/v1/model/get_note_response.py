# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_note_response_body import GetNoteResponseBody


class GetNoteResponse(BaseResponse):
    _types = {
        "data": GetNoteResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetNoteResponseBody] = None
        init(self, d, self._types)
