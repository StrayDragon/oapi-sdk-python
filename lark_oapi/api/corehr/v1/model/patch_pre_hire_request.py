# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .pre_hire import PreHire


class PatchPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.pre_hire_id: Optional[str] = None
        self.request_body: Optional[PreHire] = None

    @staticmethod
    def builder() -> "PatchPreHireRequestBuilder":
        return PatchPreHireRequestBuilder()


class PatchPreHireRequestBuilder(object):

    def __init__(self) -> None:
        patch_pre_hire_request = PatchPreHireRequest()
        patch_pre_hire_request.http_method = HttpMethod.PATCH
        patch_pre_hire_request.uri = "/open-apis/corehr/v1/pre_hires/:pre_hire_id"
        patch_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._patch_pre_hire_request: PatchPreHireRequest = patch_pre_hire_request

    def client_token(self, client_token: str) -> "PatchPreHireRequestBuilder":
        self._patch_pre_hire_request.client_token = client_token
        self._patch_pre_hire_request.add_query("client_token", client_token)
        return self

    def pre_hire_id(self, pre_hire_id: str) -> "PatchPreHireRequestBuilder":
        self._patch_pre_hire_request.pre_hire_id = pre_hire_id
        self._patch_pre_hire_request.paths["pre_hire_id"] = str(pre_hire_id)
        return self

    def request_body(self, request_body: PreHire) -> "PatchPreHireRequestBuilder":
        self._patch_pre_hire_request.request_body = request_body
        self._patch_pre_hire_request.body = request_body
        return self

    def build(self) -> PatchPreHireRequest:
        return self._patch_pre_hire_request
