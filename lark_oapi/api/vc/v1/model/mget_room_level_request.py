# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .mget_room_level_request_body import MgetRoomLevelRequestBody


class MgetRoomLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[MgetRoomLevelRequestBody] = None

    @staticmethod
    def builder() -> "MgetRoomLevelRequestBuilder":
        return MgetRoomLevelRequestBuilder()


class MgetRoomLevelRequestBuilder(object):

    def __init__(self) -> None:
        mget_room_level_request = MgetRoomLevelRequest()
        mget_room_level_request.http_method = HttpMethod.POST
        mget_room_level_request.uri = "/open-apis/vc/v1/room_levels/mget"
        mget_room_level_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._mget_room_level_request: MgetRoomLevelRequest = mget_room_level_request

    def request_body(self, request_body: MgetRoomLevelRequestBody) -> "MgetRoomLevelRequestBuilder":
        self._mget_room_level_request.request_body = request_body
        self._mget_room_level_request.body = request_body
        return self

    def build(self) -> MgetRoomLevelRequest:
        return self._mget_room_level_request
