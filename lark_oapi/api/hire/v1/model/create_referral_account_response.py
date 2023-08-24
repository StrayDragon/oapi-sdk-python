# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_referral_account_response_body import CreateReferralAccountResponseBody


class CreateReferralAccountResponse(BaseResponse):
    _types = {
        "data": CreateReferralAccountResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateReferralAccountResponseBody] = None
        init(self, d, self._types)