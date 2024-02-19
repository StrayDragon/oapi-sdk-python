# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class CopyAppRequestBody(object):
    _types = {
        "name": str,
        "folder_token": str,
        "without_content": bool,
        "time_zone": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.folder_token: Optional[str] = None
        self.without_content: Optional[bool] = None
        self.time_zone: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopyAppRequestBodyBuilder":
        return CopyAppRequestBodyBuilder()


class CopyAppRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._copy_app_request_body = CopyAppRequestBody()

    def name(self, name: str) -> "CopyAppRequestBodyBuilder":
        self._copy_app_request_body.name = name
        return self

    def folder_token(self, folder_token: str) -> "CopyAppRequestBodyBuilder":
        self._copy_app_request_body.folder_token = folder_token
        return self

    def without_content(self, without_content: bool) -> "CopyAppRequestBodyBuilder":
        self._copy_app_request_body.without_content = without_content
        return self

    def time_zone(self, time_zone: str) -> "CopyAppRequestBodyBuilder":
        self._copy_app_request_body.time_zone = time_zone
        return self

    def build(self) -> "CopyAppRequestBody":
        return self._copy_app_request_body
