# Code generated by Lark OpenAPI.

from typing import Optional

from requests_toolbelt import MultipartEncoder

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.create_badge_image_request import CreateBadgeImageRequest
from ..model.create_badge_image_response import CreateBadgeImageResponse


class BadgeImage(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateBadgeImageRequest,
               option: Optional[RequestOption] = None) -> CreateBadgeImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            request.body = form_data
            option.headers[CONTENT_TYPE] = form_data.content_type

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateBadgeImageResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateBadgeImageResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateBadgeImageRequest,
                      option: Optional[RequestOption] = None) -> CreateBadgeImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 解析文件
        request.files = Files.extract_files(request.body)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateBadgeImageResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateBadgeImageResponse)
        response.raw = resp

        return response
