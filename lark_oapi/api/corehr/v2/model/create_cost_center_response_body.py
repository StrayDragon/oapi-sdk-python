# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .cost_center import CostCenter


class CreateCostCenterResponseBody(object):
    _types = {
        "cost_center": CostCenter,
    }

    def __init__(self, d=None):
        self.cost_center: Optional[CostCenter] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCostCenterResponseBodyBuilder":
        return CreateCostCenterResponseBodyBuilder()


class CreateCostCenterResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_cost_center_response_body = CreateCostCenterResponseBody()

    def cost_center(self, cost_center: CostCenter) -> "CreateCostCenterResponseBodyBuilder":
        self._create_cost_center_response_body.cost_center = cost_center
        return self

    def build(self) -> "CreateCostCenterResponseBody":
        return self._create_cost_center_response_body
