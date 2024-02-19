# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .user_daily_shift import UserDailyShift


class BatchCreateUserDailyShiftRequestBody(object):
    _types = {
        "user_daily_shifts": List[UserDailyShift],
        "operator_id": str,
    }

    def __init__(self, d=None):
        self.user_daily_shifts: Optional[List[UserDailyShift]] = None
        self.operator_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateUserDailyShiftRequestBodyBuilder":
        return BatchCreateUserDailyShiftRequestBodyBuilder()


class BatchCreateUserDailyShiftRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_user_daily_shift_request_body = BatchCreateUserDailyShiftRequestBody()

    def user_daily_shifts(self,
                          user_daily_shifts: List[UserDailyShift]) -> "BatchCreateUserDailyShiftRequestBodyBuilder":
        self._batch_create_user_daily_shift_request_body.user_daily_shifts = user_daily_shifts
        return self

    def operator_id(self, operator_id: str) -> "BatchCreateUserDailyShiftRequestBodyBuilder":
        self._batch_create_user_daily_shift_request_body.operator_id = operator_id
        return self

    def build(self) -> "BatchCreateUserDailyShiftRequestBody":
        return self._batch_create_user_daily_shift_request_body
