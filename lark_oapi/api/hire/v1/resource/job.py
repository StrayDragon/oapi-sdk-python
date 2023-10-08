# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.combined_create_job_request import CombinedCreateJobRequest
from ..model.combined_create_job_response import CombinedCreateJobResponse
from ..model.combined_update_job_request import CombinedUpdateJobRequest
from ..model.combined_update_job_response import CombinedUpdateJobResponse
from ..model.config_job_request import ConfigJobRequest
from ..model.config_job_response import ConfigJobResponse
from ..model.get_job_request import GetJobRequest
from ..model.get_job_response import GetJobResponse
from ..model.update_config_job_request import UpdateConfigJobRequest
from ..model.update_config_job_response import UpdateConfigJobResponse


class Job(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def combined_create(self, request: CombinedCreateJobRequest,
                        option: Optional[RequestOption] = None) -> CombinedCreateJobResponse:
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
        response: CombinedCreateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CombinedCreateJobResponse)
        response.raw = resp

        return response

    def combined_update(self, request: CombinedUpdateJobRequest,
                        option: Optional[RequestOption] = None) -> CombinedUpdateJobResponse:
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
        response: CombinedUpdateJobResponse = JSON.unmarshal(str(resp.content, UTF_8), CombinedUpdateJobResponse)
        response.raw = resp

        return response

    def config(self, request: ConfigJobRequest, option: Optional[RequestOption] = None) -> ConfigJobResponse:
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
        response: ConfigJobResponse = JSON.unmarshal(str(resp.content, UTF_8), ConfigJobResponse)
        response.raw = resp

        return response

    def get(self, request: GetJobRequest, option: Optional[RequestOption] = None) -> GetJobResponse:
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
        response: GetJobResponse = JSON.unmarshal(str(resp.content, UTF_8), GetJobResponse)
        response.raw = resp

        return response

    def update_config(self, request: UpdateConfigJobRequest,
                      option: Optional[RequestOption] = None) -> UpdateConfigJobResponse:
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
        response: UpdateConfigJobResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateConfigJobResponse)
        response.raw = resp

        return response
