# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.patch_reserve_config_request import PatchReserveConfigRequest
from ..model.patch_reserve_config_response import PatchReserveConfigResponse
from ..model.reserve_scope_reserve_config_request import ReserveScopeReserveConfigRequest
from ..model.reserve_scope_reserve_config_response import ReserveScopeReserveConfigResponse


class ReserveConfig(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def patch(self, request: PatchReserveConfigRequest,
              option: Optional[RequestOption] = None) -> PatchReserveConfigResponse:
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
        response: PatchReserveConfigResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchReserveConfigResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchReserveConfigRequest,
                     option: Optional[RequestOption] = None) -> PatchReserveConfigResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchReserveConfigResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchReserveConfigResponse)
        response.raw = resp

        return response

    def reserve_scope(self, request: ReserveScopeReserveConfigRequest,
                      option: Optional[RequestOption] = None) -> ReserveScopeReserveConfigResponse:
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
        response: ReserveScopeReserveConfigResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     ReserveScopeReserveConfigResponse)
        response.raw = resp

        return response

    async def areserve_scope(self, request: ReserveScopeReserveConfigRequest,
                             option: Optional[RequestOption] = None) -> ReserveScopeReserveConfigResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ReserveScopeReserveConfigResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     ReserveScopeReserveConfigResponse)
        response.raw = resp

        return response
