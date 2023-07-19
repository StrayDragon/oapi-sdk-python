# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.workplace.v1.model.search_workplace_block_access_data_request import \
    SearchWorkplaceBlockAccessDataRequest
from lark_oapi.api.workplace.v1.model.search_workplace_block_access_data_response import \
    SearchWorkplaceBlockAccessDataResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class WorkplaceBlockAccessData(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def search(self, request: SearchWorkplaceBlockAccessDataRequest,
               option: RequestOption = RequestOption()) -> SearchWorkplaceBlockAccessDataResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchWorkplaceBlockAccessDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          SearchWorkplaceBlockAccessDataResponse)
        response.raw = resp

        return response