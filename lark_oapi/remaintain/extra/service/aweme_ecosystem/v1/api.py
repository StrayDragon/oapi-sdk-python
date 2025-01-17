# Code generated by lark suite oapi sdk gen

from typing import *

from ....api import (
    Request as APIRequest,
    Response as APIResponse,
    set_timeout,
    set_tenant_key,
    set_user_access_token,
    set_path_params,
    set_query_params,
    set_response_stream,
    set_is_response_stream,
    FormData,
    FormDataFile,
)
from ....config import Config
from ....consts import (
    ACCESS_TOKEN_TYPE_TENANT,
    ACCESS_TOKEN_TYPE_USER,
    ACCESS_TOKEN_TYPE_APP,
)
from .model import *


class Service:
    def __init__(self, conf):
        # type: (Config) -> None
        self.conf = conf
        self.aweme_users = AwemeUserService(self)


class AwemeUserService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def get_bind_info(self, tenant_key=None, timeout=None):
        # type: (str, int) -> AwemeUserGetBindInfoReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return AwemeUserGetBindInfoReqCall(self, request_opts=request_opts)


class AwemeUserGetBindInfoReqCall:
    def __init__(self, service, request_opts=None):
        # type: (AwemeUserService, List[Any]) -> None

        self.service = service

        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_user_id_type(self, user_id_type):
        # type: (str) -> AwemeUserGetBindInfoReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def set_user_id(self, user_id):
        # type: (str) -> AwemeUserGetBindInfoReqCall
        self.query_params["user_id"] = user_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[AwemeUserGetBindInfoResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/aweme_ecosystem/v1/aweme_users/get_bind_info",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=AwemeUserGetBindInfoResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp
