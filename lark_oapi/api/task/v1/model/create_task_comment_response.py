# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_task_comment_response_body import CreateTaskCommentResponseBody


class CreateTaskCommentResponse(BaseResponse):
    _types = {
        "data": CreateTaskCommentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateTaskCommentResponseBody] = None
        init(self, d, self._types)
