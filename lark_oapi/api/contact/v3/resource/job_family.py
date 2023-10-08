# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_job_family_request import CreateJobFamilyRequest
from ..model.create_job_family_response import CreateJobFamilyResponse
from ..model.delete_job_family_request import DeleteJobFamilyRequest
from ..model.delete_job_family_response import DeleteJobFamilyResponse
from ..model.get_job_family_request import GetJobFamilyRequest
from ..model.get_job_family_response import GetJobFamilyResponse
from ..model.list_job_family_request import ListJobFamilyRequest
from ..model.list_job_family_response import ListJobFamilyResponse
from ..model.update_job_family_request import UpdateJobFamilyRequest
from ..model.update_job_family_response import UpdateJobFamilyResponse


class JobFamily(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateJobFamilyRequest,
               option: Optional[RequestOption] = None) -> CreateJobFamilyResponse:
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
        response: CreateJobFamilyResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateJobFamilyResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteJobFamilyRequest,
               option: Optional[RequestOption] = None) -> DeleteJobFamilyResponse:
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
        response: DeleteJobFamilyResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteJobFamilyResponse)
        response.raw = resp

        return response

    def get(self, request: GetJobFamilyRequest, option: Optional[RequestOption] = None) -> GetJobFamilyResponse:
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
        response: GetJobFamilyResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobFamilyResponse)
        response.raw = resp

        return response

    def list(self, request: ListJobFamilyRequest, option: Optional[RequestOption] = None) -> ListJobFamilyResponse:
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
        response: ListJobFamilyResponse = JSON.unmarshal(str(resp.content, UTF_8), ListJobFamilyResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateJobFamilyRequest,
               option: Optional[RequestOption] = None) -> UpdateJobFamilyResponse:
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
        response: UpdateJobFamilyResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateJobFamilyResponse)
        response.raw = resp

        return response
