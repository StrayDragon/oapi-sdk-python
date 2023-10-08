# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_department_request import CreateDepartmentRequest
from ..model.create_department_response import CreateDepartmentResponse
from ..model.delete_department_request import DeleteDepartmentRequest
from ..model.delete_department_response import DeleteDepartmentResponse
from ..model.get_department_request import GetDepartmentRequest
from ..model.get_department_response import GetDepartmentResponse
from ..model.list_department_request import ListDepartmentRequest
from ..model.list_department_response import ListDepartmentResponse
from ..model.patch_department_request import PatchDepartmentRequest
from ..model.patch_department_response import PatchDepartmentResponse


class Department(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateDepartmentRequest,
               option: Optional[RequestOption] = None) -> CreateDepartmentResponse:
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
        response: CreateDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateDepartmentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteDepartmentRequest,
               option: Optional[RequestOption] = None) -> DeleteDepartmentResponse:
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
        response: DeleteDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteDepartmentResponse)
        response.raw = resp

        return response

    def get(self, request: GetDepartmentRequest, option: Optional[RequestOption] = None) -> GetDepartmentResponse:
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
        response: GetDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetDepartmentResponse)
        response.raw = resp

        return response

    def list(self, request: ListDepartmentRequest, option: Optional[RequestOption] = None) -> ListDepartmentResponse:
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
        response: ListDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListDepartmentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchDepartmentRequest, option: Optional[RequestOption] = None) -> PatchDepartmentResponse:
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
        response: PatchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchDepartmentResponse)
        response.raw = resp

        return response
