# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_contract_response_body import SearchContractResponseBody


class SearchContractResponse(BaseResponse):
    _types = {
        "data": SearchContractResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchContractResponseBody] = None
        init(self, d, self._types)
