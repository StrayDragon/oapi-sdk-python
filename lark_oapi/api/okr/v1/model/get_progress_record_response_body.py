# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .content_block import ContentBlock


class GetProgressRecordResponseBody(object):
    _types = {
        "progress_id": int,
        "modify_time": int,
        "content": ContentBlock,
    }

    def __init__(self, d):
        self.progress_id: Optional[int] = None
        self.modify_time: Optional[int] = None
        self.content: Optional[ContentBlock] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetProgressRecordResponseBodyBuilder":
        return GetProgressRecordResponseBodyBuilder()


class GetProgressRecordResponseBodyBuilder(object):
    def __init__(self, get_progress_record_response_body: GetProgressRecordResponseBody = GetProgressRecordResponseBody(
        {})) -> None:
        self._get_progress_record_response_body: GetProgressRecordResponseBody = get_progress_record_response_body

    def progress_id(self, progress_id: int) -> "GetProgressRecordResponseBodyBuilder":
        self._get_progress_record_response_body.progress_id = progress_id
        return self

    def modify_time(self, modify_time: int) -> "GetProgressRecordResponseBodyBuilder":
        self._get_progress_record_response_body.modify_time = modify_time
        return self

    def content(self, content: ContentBlock) -> "GetProgressRecordResponseBodyBuilder":
        self._get_progress_record_response_body.content = content
        return self

    def build(self) -> "GetProgressRecordResponseBody":
        return self._get_progress_record_response_body