# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .file import File


class UploadFileResponseBody(object):
    _types = {
        "file": File,
    }

    def __init__(self, d=None):
        self.file: Optional[File] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadFileResponseBodyBuilder":
        return UploadFileResponseBodyBuilder()


class UploadFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._upload_file_response_body = UploadFileResponseBody()

    def file(self, file: File) -> "UploadFileResponseBodyBuilder":
        self._upload_file_response_body.file = file
        return self

    def build(self) -> "UploadFileResponseBody":
        return self._upload_file_response_body
