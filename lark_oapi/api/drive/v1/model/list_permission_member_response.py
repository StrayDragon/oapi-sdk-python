# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_permission_member_response_body import ListPermissionMemberResponseBody


class ListPermissionMemberResponse(BaseResponse):
    _types = {
        "data": ListPermissionMemberResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListPermissionMemberResponseBody] = None
        init(self, d, self._types)
