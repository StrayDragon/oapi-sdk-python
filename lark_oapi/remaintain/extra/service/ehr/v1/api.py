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
        self.attachments = AttachmentService(self)
        self.employees = EmployeeService(self)


class AttachmentService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def get(self, tenant_key=None, response_stream=None, timeout=None):
        # type: (str, Union[None, IO], int) -> AttachmentGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if response_stream is not None:
            request_opts += [set_response_stream(response_stream)]

        return AttachmentGetReqCall(self, request_opts=request_opts)


class EmployeeService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> EmployeeListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return EmployeeListReqCall(self, request_opts=request_opts)


class AttachmentGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (AttachmentService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_token(self, token):
        # type: (str) -> AttachmentGetReqCall
        self.path_params["token"] = token
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_is_response_stream()]
        req = APIRequest(
            "/open-apis/ehr/v1/attachments/:token",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class EmployeeListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (EmployeeService, List[Any]) -> None

        self.service = service

        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_view(self, view):
        # type: (str) -> EmployeeListReqCall
        self.query_params["view"] = view
        return self

    def set_status(self, status):
        # type: (List[int]) -> EmployeeListReqCall
        self.query_params["status"] = status
        return self

    def set_type(self, type):
        # type: (List[int]) -> EmployeeListReqCall
        self.query_params["type"] = type
        return self

    def set_start_time(self, start_time):
        # type: (int) -> EmployeeListReqCall
        self.query_params["start_time"] = start_time
        return self

    def set_end_time(self, end_time):
        # type: (int) -> EmployeeListReqCall
        self.query_params["end_time"] = end_time
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> EmployeeListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def set_user_ids(self, user_ids):
        # type: (List[str]) -> EmployeeListReqCall
        self.query_params["user_ids"] = user_ids
        return self

    def set_page_token(self, page_token):
        # type: (str) -> EmployeeListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_page_size(self, page_size):
        # type: (int) -> EmployeeListReqCall
        self.query_params["page_size"] = page_size
        return self

    def do(self):
        # type: () -> APIResponse[Type[EmployeeListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/ehr/v1/employees",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=EmployeeListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp
