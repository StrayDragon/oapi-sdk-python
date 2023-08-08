# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2CorehrOffboardingUpdatedV1Data(object):
    _types = {
        "employment_id": str,
        "target_user_id": UserId,
        "offboarding_id": str,
        "process_id": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.target_user_id: Optional[UserId] = None
        self.offboarding_id: Optional[str] = None
        self.process_id: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)


class P2CorehrOffboardingUpdatedV1(EventContext):
    _types = {
        "event": P2CorehrOffboardingUpdatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrOffboardingUpdatedV1Data] = None
        init(self, d, self._types)