# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteMailgroupAliasRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None
        self.alias_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteMailgroupAliasRequestBuilder":
        return DeleteMailgroupAliasRequestBuilder()


class DeleteMailgroupAliasRequestBuilder(object):

    def __init__(self) -> None:
        delete_mailgroup_alias_request = DeleteMailgroupAliasRequest()
        delete_mailgroup_alias_request.http_method = HttpMethod.DELETE
        delete_mailgroup_alias_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/aliases/:alias_id"
        delete_mailgroup_alias_request.token_types = {AccessTokenType.TENANT}
        self._delete_mailgroup_alias_request: DeleteMailgroupAliasRequest = delete_mailgroup_alias_request

    def mailgroup_id(self, mailgroup_id: str) -> "DeleteMailgroupAliasRequestBuilder":
        self._delete_mailgroup_alias_request.mailgroup_id = mailgroup_id
        self._delete_mailgroup_alias_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def alias_id(self, alias_id: str) -> "DeleteMailgroupAliasRequestBuilder":
        self._delete_mailgroup_alias_request.alias_id = alias_id
        self._delete_mailgroup_alias_request.paths["alias_id"] = str(alias_id)
        return self

    def build(self) -> DeleteMailgroupAliasRequest:
        return self._delete_mailgroup_alias_request
