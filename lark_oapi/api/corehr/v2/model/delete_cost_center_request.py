# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .delete_cost_center_request_body import DeleteCostCenterRequestBody


class DeleteCostCenterRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.cost_center_id: Optional[str] = None
        self.request_body: Optional[DeleteCostCenterRequestBody] = None

    @staticmethod
    def builder() -> "DeleteCostCenterRequestBuilder":
        return DeleteCostCenterRequestBuilder()


class DeleteCostCenterRequestBuilder(object):

    def __init__(self) -> None:
        delete_cost_center_request = DeleteCostCenterRequest()
        delete_cost_center_request.http_method = HttpMethod.DELETE
        delete_cost_center_request.uri = "/open-apis/corehr/v2/cost_centers/:cost_center_id"
        delete_cost_center_request.token_types = {AccessTokenType.TENANT}
        self._delete_cost_center_request: DeleteCostCenterRequest = delete_cost_center_request

    def cost_center_id(self, cost_center_id: str) -> "DeleteCostCenterRequestBuilder":
        self._delete_cost_center_request.cost_center_id = cost_center_id
        self._delete_cost_center_request.paths["cost_center_id"] = str(cost_center_id)
        return self

    def request_body(self, request_body: DeleteCostCenterRequestBody) -> "DeleteCostCenterRequestBuilder":
        self._delete_cost_center_request.request_body = request_body
        self._delete_cost_center_request.body = request_body
        return self

    def build(self) -> DeleteCostCenterRequest:
        return self._delete_cost_center_request
