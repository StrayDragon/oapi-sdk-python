# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_group_request import CreateGroupRequest
from ..model.create_group_response import CreateGroupResponse
from ..model.delete_group_request import DeleteGroupRequest
from ..model.delete_group_response import DeleteGroupResponse
from ..model.get_group_request import GetGroupRequest
from ..model.get_group_response import GetGroupResponse
from ..model.member_belong_group_request import MemberBelongGroupRequest
from ..model.member_belong_group_response import MemberBelongGroupResponse
from ..model.patch_group_request import PatchGroupRequest
from ..model.patch_group_response import PatchGroupResponse
from ..model.simplelist_group_request import SimplelistGroupRequest
from ..model.simplelist_group_response import SimplelistGroupResponse


class Group(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateGroupRequest, option: Optional[RequestOption] = None) -> CreateGroupResponse:
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
        response: CreateGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateGroupResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateGroupRequest, option: Optional[RequestOption] = None) -> CreateGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateGroupResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteGroupRequest, option: Optional[RequestOption] = None) -> DeleteGroupResponse:
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
        response: DeleteGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteGroupResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteGroupRequest, option: Optional[RequestOption] = None) -> DeleteGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteGroupResponse)
        response.raw = resp

        return response

    def get(self, request: GetGroupRequest, option: Optional[RequestOption] = None) -> GetGroupResponse:
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
        response: GetGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), GetGroupResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetGroupRequest, option: Optional[RequestOption] = None) -> GetGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), GetGroupResponse)
        response.raw = resp

        return response

    def member_belong(self, request: MemberBelongGroupRequest,
                      option: Optional[RequestOption] = None) -> MemberBelongGroupResponse:
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
        response: MemberBelongGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), MemberBelongGroupResponse)
        response.raw = resp

        return response

    async def amember_belong(self, request: MemberBelongGroupRequest,
                             option: Optional[RequestOption] = None) -> MemberBelongGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: MemberBelongGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), MemberBelongGroupResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchGroupRequest, option: Optional[RequestOption] = None) -> PatchGroupResponse:
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
        response: PatchGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchGroupResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchGroupRequest, option: Optional[RequestOption] = None) -> PatchGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchGroupResponse)
        response.raw = resp

        return response

    def simplelist(self, request: SimplelistGroupRequest,
                   option: Optional[RequestOption] = None) -> SimplelistGroupResponse:
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
        response: SimplelistGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), SimplelistGroupResponse)
        response.raw = resp

        return response

    async def asimplelist(self, request: SimplelistGroupRequest,
                          option: Optional[RequestOption] = None) -> SimplelistGroupResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: SimplelistGroupResponse = JSON.unmarshal(str(resp.content, UTF_8), SimplelistGroupResponse)
        response.raw = resp

        return response
