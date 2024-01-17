# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .device_bind_rule_external_request_body import DeviceBindRuleExternalRequestBody


class DeviceBindRuleExternalRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[DeviceBindRuleExternalRequestBody] = None

    @staticmethod
    def builder() -> "DeviceBindRuleExternalRequestBuilder":
        return DeviceBindRuleExternalRequestBuilder()


class DeviceBindRuleExternalRequestBuilder(object):

    def __init__(self) -> None:
        device_bind_rule_external_request = DeviceBindRuleExternalRequest()
        device_bind_rule_external_request.http_method = HttpMethod.POST
        device_bind_rule_external_request.uri = "/open-apis/acs/v1/rule_external/device_bind"
        device_bind_rule_external_request.token_types = {AccessTokenType.USER}
        self._device_bind_rule_external_request: DeviceBindRuleExternalRequest = device_bind_rule_external_request

    def request_body(self, request_body: DeviceBindRuleExternalRequestBody) -> "DeviceBindRuleExternalRequestBuilder":
        self._device_bind_rule_external_request.request_body = request_body
        self._device_bind_rule_external_request.body = request_body
        return self

    def build(self) -> DeviceBindRuleExternalRequest:
        return self._device_bind_rule_external_request