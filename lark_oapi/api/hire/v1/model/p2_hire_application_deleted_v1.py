# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2HireApplicationDeletedV1Data(object):
    _types = {
        "application_ids": List[str],
    }

    def __init__(self, d=None):
        self.application_ids: Optional[List[str]] = None
        init(self, d, self._types)


class P2HireApplicationDeletedV1(EventContext):
    _types = {
        "event": P2HireApplicationDeletedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2HireApplicationDeletedV1Data] = None
        init(self, d, self._types)
