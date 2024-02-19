# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListContractRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListContractRequestBuilder":
        return ListContractRequestBuilder()


class ListContractRequestBuilder(object):

    def __init__(self) -> None:
        list_contract_request = ListContractRequest()
        list_contract_request.http_method = HttpMethod.GET
        list_contract_request.uri = "/open-apis/corehr/v1/contracts"
        list_contract_request.token_types = {AccessTokenType.TENANT}
        self._list_contract_request: ListContractRequest = list_contract_request

    def page_token(self, page_token: str) -> "ListContractRequestBuilder":
        self._list_contract_request.page_token = page_token
        self._list_contract_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListContractRequestBuilder":
        self._list_contract_request.page_size = page_size
        self._list_contract_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListContractRequest:
        return self._list_contract_request
