# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class RemedyGroup(object):
    _types = {
        "type": str,
        "instance_code": str,
        "employee_id": str,
        "start_time": int,
        "end_time": int,
        "remedy_time": int,
        "remedy_reason": str,
        "status": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.instance_code: Optional[str] = None
        self.employee_id: Optional[str] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.remedy_time: Optional[int] = None
        self.remedy_reason: Optional[str] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemedyGroupBuilder":
        return RemedyGroupBuilder()


class RemedyGroupBuilder(object):
    def __init__(self) -> None:
        self._remedy_group = RemedyGroup()

    def type(self, type: str) -> "RemedyGroupBuilder":
        self._remedy_group.type = type
        return self

    def instance_code(self, instance_code: str) -> "RemedyGroupBuilder":
        self._remedy_group.instance_code = instance_code
        return self

    def employee_id(self, employee_id: str) -> "RemedyGroupBuilder":
        self._remedy_group.employee_id = employee_id
        return self

    def start_time(self, start_time: int) -> "RemedyGroupBuilder":
        self._remedy_group.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "RemedyGroupBuilder":
        self._remedy_group.end_time = end_time
        return self

    def remedy_time(self, remedy_time: int) -> "RemedyGroupBuilder":
        self._remedy_group.remedy_time = remedy_time
        return self

    def remedy_reason(self, remedy_reason: str) -> "RemedyGroupBuilder":
        self._remedy_group.remedy_reason = remedy_reason
        return self

    def status(self, status: str) -> "RemedyGroupBuilder":
        self._remedy_group.status = status
        return self

    def build(self) -> "RemedyGroup":
        return self._remedy_group
