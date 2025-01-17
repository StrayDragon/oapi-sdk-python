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
        self.data_sources = DataSourceService(self)
        self.data_source_items = DataSourceItemService(self)


class DataSourceService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (DataSource, str, int) -> DataSourceCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DataSourceDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceDeleteReqCall(self, request_opts=request_opts)

    def get(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DataSourceGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceGetReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DataSourceListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceListReqCall(self, request_opts=request_opts)

    def patch(self, body, tenant_key=None, timeout=None):
        # type: (DataSourcePatchReqBody, str, int) -> DataSourcePatchReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourcePatchReqCall(self, body, request_opts=request_opts)


class DataSourceItemService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Item, str, int) -> DataSourceItemCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceItemCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DataSourceItemDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceItemDeleteReqCall(self, request_opts=request_opts)

    def get(self, tenant_key=None, timeout=None):
        # type: (str, int) -> DataSourceItemGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return DataSourceItemGetReqCall(self, request_opts=request_opts)


class DataSourceCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DataSourceService, DataSource, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> APIResponse[Type[DataSourceCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        req = APIRequest(
            "/open-apis/search/v2/data_sources",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=DataSourceCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DataSourceService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourceDeleteReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DataSourceService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourceGetReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[DataSourceGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=DataSourceGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DataSourceService, List[Any]) -> None

        self.service = service

        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_view(self, view):
        # type: (int) -> DataSourceListReqCall
        self.query_params["view"] = view
        return self

    def set_page_token(self, page_token):
        # type: (str) -> DataSourceListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_page_size(self, page_size):
        # type: (int) -> DataSourceListReqCall
        self.query_params["page_size"] = page_size
        return self

    def do(self):
        # type: () -> APIResponse[Type[DataSourceListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=DataSourceListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourcePatchReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DataSourceService, DataSourcePatchReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourcePatchReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[DataSourcePatchResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id",
            "PATCH",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=DataSourcePatchResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceItemCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DataSourceItemService, Item, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourceItemCreateReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id/items",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceItemDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DataSourceItemService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourceItemDeleteReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def set_item_id(self, item_id):
        # type: (str) -> DataSourceItemDeleteReqCall
        self.path_params["item_id"] = item_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id/items/:item_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DataSourceItemGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DataSourceItemService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_data_source_id(self, data_source_id):
        # type: (str) -> DataSourceItemGetReqCall
        self.path_params["data_source_id"] = data_source_id
        return self

    def set_item_id(self, item_id):
        # type: (str) -> DataSourceItemGetReqCall
        self.path_params["item_id"] = item_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[DataSourceItemGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/search/v2/data_sources/:data_source_id/items/:item_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=DataSourceItemGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp
