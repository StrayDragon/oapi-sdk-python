# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetFileVersionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.obj_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.file_token: Optional[str] = None
        self.version_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetFileVersionRequestBuilder":
        return GetFileVersionRequestBuilder()


class GetFileVersionRequestBuilder(object):

    def __init__(self) -> None:
        get_file_version_request = GetFileVersionRequest()
        get_file_version_request.http_method = HttpMethod.GET
        get_file_version_request.uri = "/open-apis/drive/v1/files/:file_token/versions/:version_id"
        get_file_version_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_file_version_request: GetFileVersionRequest = get_file_version_request

    def obj_type(self, obj_type: str) -> "GetFileVersionRequestBuilder":
        self._get_file_version_request.obj_type = obj_type
        self._get_file_version_request.add_query("obj_type", obj_type)
        return self

    def user_id_type(self, user_id_type: str) -> "GetFileVersionRequestBuilder":
        self._get_file_version_request.user_id_type = user_id_type
        self._get_file_version_request.add_query("user_id_type", user_id_type)
        return self

    def file_token(self, file_token: str) -> "GetFileVersionRequestBuilder":
        self._get_file_version_request.file_token = file_token
        self._get_file_version_request.paths["file_token"] = str(file_token)
        return self

    def version_id(self, version_id: str) -> "GetFileVersionRequestBuilder":
        self._get_file_version_request.version_id = version_id
        self._get_file_version_request.paths["version_id"] = str(version_id)
        return self

    def build(self) -> GetFileVersionRequest:
        return self._get_file_version_request
