# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .ticket import Ticket


class GetTicketResponseBody(object):
    _types = {
        "ticket": Ticket,
    }

    def __init__(self, d=None):
        self.ticket: Optional[Ticket] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetTicketResponseBodyBuilder":
        return GetTicketResponseBodyBuilder()


class GetTicketResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_ticket_response_body = GetTicketResponseBody()

    def ticket(self, ticket: Ticket) -> "GetTicketResponseBodyBuilder":
        self._get_ticket_response_body.ticket = ticket
        return self

    def build(self) -> "GetTicketResponseBody":
        return self._get_ticket_response_body
