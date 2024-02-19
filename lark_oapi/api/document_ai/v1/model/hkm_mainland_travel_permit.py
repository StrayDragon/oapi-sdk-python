# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .hkm_mainland_travel_permit_entity import HkmMainlandTravelPermitEntity


class HkmMainlandTravelPermit(object):
    _types = {
        "entities": List[HkmMainlandTravelPermitEntity],
    }

    def __init__(self, d=None):
        self.entities: Optional[List[HkmMainlandTravelPermitEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "HkmMainlandTravelPermitBuilder":
        return HkmMainlandTravelPermitBuilder()


class HkmMainlandTravelPermitBuilder(object):
    def __init__(self) -> None:
        self._hkm_mainland_travel_permit = HkmMainlandTravelPermit()

    def entities(self, entities: List[HkmMainlandTravelPermitEntity]) -> "HkmMainlandTravelPermitBuilder":
        self._hkm_mainland_travel_permit.entities = entities
        return self

    def build(self) -> "HkmMainlandTravelPermit":
        return self._hkm_mainland_travel_permit
