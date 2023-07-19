# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.mail.v1.model.create_mailgroup_alias_request import CreateMailgroupAliasRequest
from lark_oapi.api.mail.v1.model.create_mailgroup_alias_response import CreateMailgroupAliasResponse
from lark_oapi.api.mail.v1.model.delete_mailgroup_alias_request import DeleteMailgroupAliasRequest
from lark_oapi.api.mail.v1.model.delete_mailgroup_alias_response import DeleteMailgroupAliasResponse
from lark_oapi.api.mail.v1.model.list_mailgroup_alias_request import ListMailgroupAliasRequest
from lark_oapi.api.mail.v1.model.list_mailgroup_alias_response import ListMailgroupAliasResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class MailgroupAlias(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateMailgroupAliasRequest,
               option: RequestOption = RequestOption()) -> CreateMailgroupAliasResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateMailgroupAliasResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMailgroupAliasRequest,
               option: RequestOption = RequestOption()) -> DeleteMailgroupAliasResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteMailgroupAliasResponse)
        response.raw = resp

        return response

    def list(self, request: ListMailgroupAliasRequest,
             option: RequestOption = RequestOption()) -> ListMailgroupAliasResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMailgroupAliasResponse = JSON.unmarshal(str(resp.content, UTF_8), ListMailgroupAliasResponse)
        response.raw = resp

        return response