# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class SubscriptionCalendarAclRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.calendar_id: Optional[str] = None

    @staticmethod
    def builder() -> "SubscriptionCalendarAclRequestBuilder":
        return SubscriptionCalendarAclRequestBuilder()


class SubscriptionCalendarAclRequestBuilder(object):

    def __init__(self) -> None:
        subscription_calendar_acl_request = SubscriptionCalendarAclRequest()
        subscription_calendar_acl_request.http_method = HttpMethod.POST
        subscription_calendar_acl_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/acls/subscription"
        subscription_calendar_acl_request.token_types = {AccessTokenType.USER}
        self._subscription_calendar_acl_request: SubscriptionCalendarAclRequest = subscription_calendar_acl_request

    def calendar_id(self, calendar_id: str) -> "SubscriptionCalendarAclRequestBuilder":
        self._subscription_calendar_acl_request.calendar_id = calendar_id
        self._subscription_calendar_acl_request.paths["calendar_id"] = str(calendar_id)
        return self

    def build(self) -> SubscriptionCalendarAclRequest:
        return self._subscription_calendar_acl_request
