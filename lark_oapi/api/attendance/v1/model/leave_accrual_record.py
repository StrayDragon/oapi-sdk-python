# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .lang_text import LangText


class LeaveAccrualRecord(object):
    _types = {
        "id": str,
        "employment_id": str,
        "leave_type_id": str,
        "granting_quantity": str,
        "granting_unit": int,
        "effective_date": str,
        "expiration_date": str,
        "granted_by": int,
        "reason": List[LangText],
        "created_at": str,
        "created_by": str,
        "updated_at": str,
        "updated_by": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.leave_type_id: Optional[str] = None
        self.granting_quantity: Optional[str] = None
        self.granting_unit: Optional[int] = None
        self.effective_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.granted_by: Optional[int] = None
        self.reason: Optional[List[LangText]] = None
        self.created_at: Optional[str] = None
        self.created_by: Optional[str] = None
        self.updated_at: Optional[str] = None
        self.updated_by: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveAccrualRecordBuilder":
        return LeaveAccrualRecordBuilder()


class LeaveAccrualRecordBuilder(object):
    def __init__(self, leave_accrual_record: LeaveAccrualRecord = LeaveAccrualRecord({})) -> None:
        self._leave_accrual_record: LeaveAccrualRecord = leave_accrual_record

    def id(self, id: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.id = id
        return self

    def employment_id(self, employment_id: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.employment_id = employment_id
        return self

    def leave_type_id(self, leave_type_id: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.leave_type_id = leave_type_id
        return self

    def granting_quantity(self, granting_quantity: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.granting_quantity = granting_quantity
        return self

    def granting_unit(self, granting_unit: int) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.granting_unit = granting_unit
        return self

    def effective_date(self, effective_date: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.effective_date = effective_date
        return self

    def expiration_date(self, expiration_date: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.expiration_date = expiration_date
        return self

    def granted_by(self, granted_by: int) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.granted_by = granted_by
        return self

    def reason(self, reason: List[LangText]) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.reason = reason
        return self

    def created_at(self, created_at: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.created_at = created_at
        return self

    def created_by(self, created_by: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.created_by = created_by
        return self

    def updated_at(self, updated_at: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.updated_at = updated_at
        return self

    def updated_by(self, updated_by: str) -> "LeaveAccrualRecordBuilder":
        self._leave_accrual_record.updated_by = updated_by
        return self

    def build(self) -> "LeaveAccrualRecord":
        return self._leave_accrual_record