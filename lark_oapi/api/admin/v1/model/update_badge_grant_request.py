# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .grant import Grant


class UpdateBadgeGrantRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.badge_id: Optional[str] = None
        self.grant_id: Optional[str] = None
        self.request_body: Optional[Grant] = None

    @staticmethod
    def builder() -> "UpdateBadgeGrantRequestBuilder":
        return UpdateBadgeGrantRequestBuilder()


class UpdateBadgeGrantRequestBuilder(object):

    def __init__(self) -> None:
        update_badge_grant_request = UpdateBadgeGrantRequest()
        update_badge_grant_request.http_method = HttpMethod.PUT
        update_badge_grant_request.uri = "/open-apis/admin/v1/badges/:badge_id/grants/:grant_id"
        update_badge_grant_request.token_types = {AccessTokenType.TENANT}
        self._update_badge_grant_request: UpdateBadgeGrantRequest = update_badge_grant_request

    def user_id_type(self, user_id_type: str) -> "UpdateBadgeGrantRequestBuilder":
        self._update_badge_grant_request.user_id_type = user_id_type
        self._update_badge_grant_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "UpdateBadgeGrantRequestBuilder":
        self._update_badge_grant_request.department_id_type = department_id_type
        self._update_badge_grant_request.add_query("department_id_type", department_id_type)
        return self

    def badge_id(self, badge_id: str) -> "UpdateBadgeGrantRequestBuilder":
        self._update_badge_grant_request.badge_id = badge_id
        self._update_badge_grant_request.paths["badge_id"] = str(badge_id)
        return self

    def grant_id(self, grant_id: str) -> "UpdateBadgeGrantRequestBuilder":
        self._update_badge_grant_request.grant_id = grant_id
        self._update_badge_grant_request.paths["grant_id"] = str(grant_id)
        return self

    def request_body(self, request_body: Grant) -> "UpdateBadgeGrantRequestBuilder":
        self._update_badge_grant_request.request_body = request_body
        self._update_badge_grant_request.body = request_body
        return self

    def build(self) -> UpdateBadgeGrantRequest:
        return self._update_badge_grant_request
