# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .file import File


class CopyFileResponseBody(object):
    _types = {
        "file": File,
    }

    def __init__(self, d=None):
        self.file: Optional[File] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopyFileResponseBodyBuilder":
        return CopyFileResponseBodyBuilder()


class CopyFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._copy_file_response_body = CopyFileResponseBody()

    def file(self, file: File) -> "CopyFileResponseBodyBuilder":
        self._copy_file_response_body.file = file
        return self

    def build(self) -> "CopyFileResponseBody":
        return self._copy_file_response_body
