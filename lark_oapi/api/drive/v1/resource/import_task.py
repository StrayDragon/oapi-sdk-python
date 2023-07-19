# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.drive.v1.model.create_import_task_request import CreateImportTaskRequest
from lark_oapi.api.drive.v1.model.create_import_task_response import CreateImportTaskResponse
from lark_oapi.api.drive.v1.model.get_import_task_request import GetImportTaskRequest
from lark_oapi.api.drive.v1.model.get_import_task_response import GetImportTaskResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class ImportTask(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateImportTaskRequest,
               option: RequestOption = RequestOption()) -> CreateImportTaskResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateImportTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateImportTaskResponse)
        response.raw = resp

        return response

    def get(self, request: GetImportTaskRequest, option: RequestOption = RequestOption()) -> GetImportTaskResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetImportTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), GetImportTaskResponse)
        response.raw = resp

        return response