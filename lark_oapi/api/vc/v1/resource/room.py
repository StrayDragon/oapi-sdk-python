# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_room_request import CreateRoomRequest
from ..model.create_room_response import CreateRoomResponse
from ..model.delete_room_request import DeleteRoomRequest
from ..model.delete_room_response import DeleteRoomResponse
from ..model.get_room_request import GetRoomRequest
from ..model.get_room_response import GetRoomResponse
from ..model.list_room_request import ListRoomRequest
from ..model.list_room_response import ListRoomResponse
from ..model.mget_room_request import MgetRoomRequest
from ..model.mget_room_response import MgetRoomResponse
from ..model.patch_room_request import PatchRoomRequest
from ..model.patch_room_response import PatchRoomResponse
from ..model.search_room_request import SearchRoomRequest
from ..model.search_room_response import SearchRoomResponse


class Room(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateRoomRequest, option: Optional[RequestOption] = None) -> CreateRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateRoomResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteRoomRequest, option: Optional[RequestOption] = None) -> DeleteRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteRoomResponse)
        response.raw = resp

        return response

    def get(self, request: GetRoomRequest, option: Optional[RequestOption] = None) -> GetRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), GetRoomResponse)
        response.raw = resp

        return response

    def list(self, request: ListRoomRequest, option: Optional[RequestOption] = None) -> ListRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), ListRoomResponse)
        response.raw = resp

        return response

    def mget(self, request: MgetRoomRequest, option: Optional[RequestOption] = None) -> MgetRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MgetRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), MgetRoomResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchRoomRequest, option: Optional[RequestOption] = None) -> PatchRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchRoomResponse)
        response.raw = resp

        return response

    def search(self, request: SearchRoomRequest, option: Optional[RequestOption] = None) -> SearchRoomResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchRoomResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchRoomResponse)
        response.raw = resp

        return response
