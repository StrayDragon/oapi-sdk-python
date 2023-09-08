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
        self.access_records = AccessRecordService(self)
        self.users = UserService(self)
        self.devices = DeviceService(self)
        self.access_record_access_photos = AccessRecordAccessPhotoService(self)
        self.user_faces = UserFaceService(self)


class AccessRecordService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> AccessRecordListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return AccessRecordListReqCall(self, request_opts=request_opts)


class UserService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def patch(self, body, tenant_key=None, timeout=None):
        # type: (User, str, int) -> UserPatchReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return UserPatchReqCall(self, body, request_opts=request_opts)

    def get(self, tenant_key=None, timeout=None):
        # type: (str, int) -> UserGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return UserGetReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> UserListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return UserListReqCall(self, request_opts=request_opts)


class DeviceService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DeviceListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DeviceListReqCall(self, request_opts=request_opts)


class AccessRecordAccessPhotoService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def get(self, tenant_key=None, response_stream=None, timeout=None):
        # type: (str, Union[None, IO], int) -> AccessRecordAccessPhotoGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if response_stream is not None:
            request_opts += [set_response_stream(response_stream)]

        return AccessRecordAccessPhotoGetReqCall(self, request_opts=request_opts)


class UserFaceService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def get(self, tenant_key=None, response_stream=None, timeout=None):
        # type: (str, Union[None, IO], int) -> UserFaceGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if response_stream is not None:
            request_opts += [set_response_stream(response_stream)]

        return UserFaceGetReqCall(self, request_opts=request_opts)

    def update(self, tenant_key=None, timeout=None):
        # type: (str, int) -> UserFaceUpdateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return UserFaceUpdateReqCall(self, request_opts=request_opts)


class AccessRecordListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (AccessRecordService, List[Any]) -> None

        self.service = service

        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_page_size(self, page_size):
        # type: (int) -> AccessRecordListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> AccessRecordListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_from(self, from_):
        # type: (int) -> AccessRecordListReqCall
        self.query_params["from"] = from_
        return self

    def set_to(self, to):
        # type: (int) -> AccessRecordListReqCall
        self.query_params["to"] = to
        return self

    def set_device_id(self, device_id):
        # type: (int) -> AccessRecordListReqCall
        self.query_params["device_id"] = device_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> AccessRecordListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[AccessRecordListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/acs/v1/access_records",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=AccessRecordListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class AccessRecordAccessPhotoGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (AccessRecordAccessPhotoService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_access_record_id(self, access_record_id):
        # type: (int) -> AccessRecordAccessPhotoGetReqCall
        self.path_params["access_record_id"] = access_record_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_is_response_stream()]
        req = APIRequest(
            "/open-apis/acs/v1/access_records/:access_record_id/access_photo",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DeviceListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DeviceService, List[Any]) -> None

        self.service = service

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> APIResponse[Type[DeviceListResult]]
        root_service = self.service.service

        conf = root_service.conf
        req = APIRequest(
            "/open-apis/acs/v1/devices",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=DeviceListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class UserPatchReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (UserService, User, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_user_id(self, user_id):
        # type: (str) -> UserPatchReqCall
        self.path_params["user_id"] = user_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> UserPatchReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/acs/v1/users/:user_id",
            "PATCH",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class UserGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (UserService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_user_id(self, user_id):
        # type: (str) -> UserGetReqCall
        self.path_params["user_id"] = user_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> UserGetReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[UserGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/acs/v1/users/:user_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=UserGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class UserListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (UserService, List[Any]) -> None

        self.service = service

        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_page_size(self, page_size):
        # type: (int) -> UserListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> UserListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> UserListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[UserListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/acs/v1/users",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=UserListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class UserFaceGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (UserFaceService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_user_id(self, user_id):
        # type: (str) -> UserFaceGetReqCall
        self.path_params["user_id"] = user_id
        return self

    def set_is_cropped(self, is_cropped):
        # type: (bool) -> UserFaceGetReqCall
        self.query_params["is_cropped"] = is_cropped
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> UserFaceGetReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        self.request_opts += [set_is_response_stream()]
        req = APIRequest(
            "/open-apis/acs/v1/users/:user_id/face",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class UserFaceUpdateReqCall:
    def __init__(self, service, request_opts=None):
        # type: (UserFaceService, List[Any]) -> None

        self.service = service
        self.body = FormData()
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_files(self, files):
        # type: (IO[Any]) -> UserFaceUpdateReqCall
        self.body.add_file("files", FormDataFile(files))
        return self

    def set_file_type(self, file_type):
        # type: (str) -> UserFaceUpdateReqCall
        self.body.add_param("file_type", file_type)
        return self

    def set_file_name(self, file_name):
        # type: (str) -> UserFaceUpdateReqCall
        self.body.add_param("file_name", file_name)
        return self

    def set_user_id(self, user_id):
        # type: (str) -> UserFaceUpdateReqCall
        self.path_params["user_id"] = user_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> UserFaceUpdateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/acs/v1/users/:user_id/face",
            "PUT",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp