# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_instance_comment_request import CreateInstanceCommentRequest
from ..model.create_instance_comment_response import CreateInstanceCommentResponse
from ..model.delete_instance_comment_request import DeleteInstanceCommentRequest
from ..model.delete_instance_comment_response import DeleteInstanceCommentResponse
from ..model.list_instance_comment_request import ListInstanceCommentRequest
from ..model.list_instance_comment_response import ListInstanceCommentResponse
from ..model.remove_instance_comment_request import RemoveInstanceCommentRequest
from ..model.remove_instance_comment_response import RemoveInstanceCommentResponse


class InstanceComment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateInstanceCommentRequest,
               option: Optional[RequestOption] = None) -> CreateInstanceCommentResponse:
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
        response: CreateInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateInstanceCommentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteInstanceCommentRequest,
               option: Optional[RequestOption] = None) -> DeleteInstanceCommentResponse:
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
        response: DeleteInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteInstanceCommentResponse)
        response.raw = resp

        return response

    def list(self, request: ListInstanceCommentRequest,
             option: Optional[RequestOption] = None) -> ListInstanceCommentResponse:
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
        response: ListInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListInstanceCommentResponse)
        response.raw = resp

        return response

    def remove(self, request: RemoveInstanceCommentRequest,
               option: Optional[RequestOption] = None) -> RemoveInstanceCommentResponse:
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
        response: RemoveInstanceCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 RemoveInstanceCommentResponse)
        response.raw = resp

        return response
