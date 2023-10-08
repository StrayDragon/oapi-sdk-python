# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_department_request import BatchDepartmentRequest
from ..model.batch_department_response import BatchDepartmentResponse
from ..model.children_department_request import ChildrenDepartmentRequest
from ..model.children_department_response import ChildrenDepartmentResponse
from ..model.create_department_request import CreateDepartmentRequest
from ..model.create_department_response import CreateDepartmentResponse
from ..model.delete_department_request import DeleteDepartmentRequest
from ..model.delete_department_response import DeleteDepartmentResponse
from ..model.get_department_request import GetDepartmentRequest
from ..model.get_department_response import GetDepartmentResponse
from ..model.list_department_request import ListDepartmentRequest
from ..model.list_department_response import ListDepartmentResponse
from ..model.parent_department_request import ParentDepartmentRequest
from ..model.parent_department_response import ParentDepartmentResponse
from ..model.patch_department_request import PatchDepartmentRequest
from ..model.patch_department_response import PatchDepartmentResponse
from ..model.search_department_request import SearchDepartmentRequest
from ..model.search_department_response import SearchDepartmentResponse
from ..model.unbind_department_chat_department_request import UnbindDepartmentChatDepartmentRequest
from ..model.unbind_department_chat_department_response import UnbindDepartmentChatDepartmentResponse
from ..model.update_department_request import UpdateDepartmentRequest
from ..model.update_department_response import UpdateDepartmentResponse


class Department(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch(self, request: BatchDepartmentRequest, option: Optional[RequestOption] = None) -> BatchDepartmentResponse:
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
        response: BatchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchDepartmentResponse)
        response.raw = resp

        return response

    def children(self, request: ChildrenDepartmentRequest,
                 option: Optional[RequestOption] = None) -> ChildrenDepartmentResponse:
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
        response: ChildrenDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ChildrenDepartmentResponse)
        response.raw = resp

        return response

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

    def parent(self, request: ParentDepartmentRequest,
               option: Optional[RequestOption] = None) -> ParentDepartmentResponse:
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
        response: ParentDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), ParentDepartmentResponse)
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

    def search(self, request: SearchDepartmentRequest,
               option: Optional[RequestOption] = None) -> SearchDepartmentResponse:
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
        response: SearchDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchDepartmentResponse)
        response.raw = resp

        return response

    def unbind_department_chat(self, request: UnbindDepartmentChatDepartmentRequest,
                               option: Optional[RequestOption] = None) -> UnbindDepartmentChatDepartmentResponse:
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
        response: UnbindDepartmentChatDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                          UnbindDepartmentChatDepartmentResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateDepartmentRequest,
               option: Optional[RequestOption] = None) -> UpdateDepartmentResponse:
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
        response: UpdateDepartmentResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateDepartmentResponse)
        response.raw = resp

        return response
