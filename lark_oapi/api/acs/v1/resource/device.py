# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.list_device_request import ListDeviceRequest
from ..model.list_device_response import ListDeviceResponse


class Device(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list(self, request: ListDeviceRequest, option: Optional[RequestOption] = None) -> ListDeviceResponse:
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
        response: ListDeviceResponse = JSON.unmarshal(str(resp.content, UTF_8), ListDeviceResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListDeviceRequest, option: Optional[RequestOption] = None) -> ListDeviceResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListDeviceResponse = JSON.unmarshal(str(resp.content, UTF_8), ListDeviceResponse)
        response.raw = resp

        return response
