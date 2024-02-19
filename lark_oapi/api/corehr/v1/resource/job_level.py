# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_job_level_request import CreateJobLevelRequest
from ..model.create_job_level_response import CreateJobLevelResponse
from ..model.delete_job_level_request import DeleteJobLevelRequest
from ..model.delete_job_level_response import DeleteJobLevelResponse
from ..model.get_job_level_request import GetJobLevelRequest
from ..model.get_job_level_response import GetJobLevelResponse
from ..model.list_job_level_request import ListJobLevelRequest
from ..model.list_job_level_response import ListJobLevelResponse
from ..model.patch_job_level_request import PatchJobLevelRequest
from ..model.patch_job_level_response import PatchJobLevelResponse


class JobLevel(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateJobLevelRequest, option: Optional[RequestOption] = None) -> CreateJobLevelResponse:
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
        response: CreateJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobLevelResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateJobLevelRequest,
                      option: Optional[RequestOption] = None) -> CreateJobLevelResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobLevelResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobLevelRequest, option: Optional[RequestOption] = None) -> DeleteJobLevelResponse:
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
        response: DeleteJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobLevelResponse)
        response.raw = resp

        return response

    async def adelete(self, request: DeleteJobLevelRequest,
                      option: Optional[RequestOption] = None) -> DeleteJobLevelResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: DeleteJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobLevelResponse)
        response.raw = resp

        return response

    def get(self, request: GetJobLevelRequest, option: Optional[RequestOption] = None) -> GetJobLevelResponse:
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
        response: GetJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobLevelResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetJobLevelRequest, option: Optional[RequestOption] = None) -> GetJobLevelResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobLevelResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobLevelRequest, option: Optional[RequestOption] = None) -> ListJobLevelResponse:
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
        response: ListJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobLevelResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListJobLevelRequest, option: Optional[RequestOption] = None) -> ListJobLevelResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobLevelResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchJobLevelRequest, option: Optional[RequestOption] = None) -> PatchJobLevelResponse:
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
        response: PatchJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchJobLevelResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchJobLevelRequest,
                     option: Optional[RequestOption] = None) -> PatchJobLevelResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchJobLevelResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchJobLevelResponse)
        response.raw = resp

        return response
