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
        self.documents = DocumentService(self)
        self.document_blocks = DocumentBlockService(self)
        self.document_block_childrens = DocumentBlockChildrenService(self)


class DocumentService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (DocumentCreateReqBody, str, str, int) -> DocumentCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentCreateReqCall(self, body, request_opts=request_opts)

    def get(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> DocumentGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentGetReqCall(self, request_opts=request_opts)

    def raw_content(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> DocumentRawContentReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentRawContentReqCall(self, request_opts=request_opts)


class DocumentBlockService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def batch_update(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (DocumentBlockBatchUpdateReqBody, str, str, int) -> DocumentBlockBatchUpdateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockBatchUpdateReqCall(self, body, request_opts=request_opts)

    def get(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> DocumentBlockGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockGetReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> DocumentBlockListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockListReqCall(self, request_opts=request_opts)

    def patch(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (UpdateBlockRequest, str, str, int) -> DocumentBlockPatchReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockPatchReqCall(self, body, request_opts=request_opts)


class DocumentBlockChildrenService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def batch_delete(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (DocumentBlockChildrenBatchDeleteReqBody, str, str, int) -> DocumentBlockChildrenBatchDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockChildrenBatchDeleteReqCall(
            self, body, request_opts=request_opts
        )

    def create(self, body, tenant_key=None, user_access_token=None, timeout=None):
        # type: (DocumentBlockChildrenCreateReqBody, str, str, int) -> DocumentBlockChildrenCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockChildrenCreateReqCall(self, body, request_opts=request_opts)

    def get(self, tenant_key=None, user_access_token=None, timeout=None):
        # type: (str, str, int) -> DocumentBlockChildrenGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        if user_access_token is not None:
            request_opts += [set_user_access_token(user_access_token)]

        return DocumentBlockChildrenGetReqCall(self, request_opts=request_opts)


class DocumentCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DocumentService, DocumentCreateReqBody, List[Any]) -> None

        self.service = service
        self.body = body

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def do(self):
        # type: () -> APIResponse[Type[DocumentCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        req = APIRequest(
            "/open-apis/docx/v1/documents",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=DocumentCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DocumentService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentGetReqCall
        self.path_params["document_id"] = document_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=DocumentGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentRawContentReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DocumentService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentRawContentReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_lang(self, lang):
        # type: (int) -> DocumentRawContentReqCall
        self.query_params["lang"] = lang
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentRawContentResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/raw_content",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=DocumentRawContentResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockBatchUpdateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DocumentBlockService, DocumentBlockBatchUpdateReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockBatchUpdateReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockBatchUpdateReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_client_token(self, client_token):
        # type: (str) -> DocumentBlockBatchUpdateReqCall
        self.query_params["client_token"] = client_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockBatchUpdateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockBatchUpdateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/batch_update",
            "PATCH",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=DocumentBlockBatchUpdateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DocumentBlockService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockGetReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_block_id(self, block_id):
        # type: (str) -> DocumentBlockGetReqCall
        self.path_params["block_id"] = block_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockGetReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockGetReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/:block_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=DocumentBlockGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DocumentBlockService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockListReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_page_size(self, page_size):
        # type: (int) -> DocumentBlockListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> DocumentBlockListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockListReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=DocumentBlockListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockPatchReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DocumentBlockService, UpdateBlockRequest, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockPatchReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_block_id(self, block_id):
        # type: (str) -> DocumentBlockPatchReqCall
        self.path_params["block_id"] = block_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockPatchReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_client_token(self, client_token):
        # type: (str) -> DocumentBlockPatchReqCall
        self.query_params["client_token"] = client_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockPatchReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockPatchResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/:block_id",
            "PATCH",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=DocumentBlockPatchResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockChildrenBatchDeleteReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DocumentBlockChildrenService, DocumentBlockChildrenBatchDeleteReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockChildrenBatchDeleteReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_block_id(self, block_id):
        # type: (str) -> DocumentBlockChildrenBatchDeleteReqCall
        self.path_params["block_id"] = block_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockChildrenBatchDeleteReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_client_token(self, client_token):
        # type: (str) -> DocumentBlockChildrenBatchDeleteReqCall
        self.query_params["client_token"] = client_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockChildrenBatchDeleteResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/children/batch_delete",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=DocumentBlockChildrenBatchDeleteResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockChildrenCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (DocumentBlockChildrenService, DocumentBlockChildrenCreateReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockChildrenCreateReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_block_id(self, block_id):
        # type: (str) -> DocumentBlockChildrenCreateReqCall
        self.path_params["block_id"] = block_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockChildrenCreateReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_client_token(self, client_token):
        # type: (str) -> DocumentBlockChildrenCreateReqCall
        self.query_params["client_token"] = client_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockChildrenCreateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockChildrenCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/children",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            self.body,
            output_class=DocumentBlockChildrenCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class DocumentBlockChildrenGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (DocumentBlockChildrenService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_document_id(self, document_id):
        # type: (str) -> DocumentBlockChildrenGetReqCall
        self.path_params["document_id"] = document_id
        return self

    def set_block_id(self, block_id):
        # type: (str) -> DocumentBlockChildrenGetReqCall
        self.path_params["block_id"] = block_id
        return self

    def set_document_revision_id(self, document_revision_id):
        # type: (int) -> DocumentBlockChildrenGetReqCall
        self.query_params["document_revision_id"] = document_revision_id
        return self

    def set_page_token(self, page_token):
        # type: (str) -> DocumentBlockChildrenGetReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_page_size(self, page_size):
        # type: (int) -> DocumentBlockChildrenGetReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> DocumentBlockChildrenGetReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[DocumentBlockChildrenGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/docx/v1/documents/:document_id/blocks/:block_id/children",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT, ACCESS_TOKEN_TYPE_USER],
            None,
            output_class=DocumentBlockChildrenGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp