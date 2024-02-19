# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class FreePunchCfg(object):
    _types = {
        "free_start_time": str,
        "free_end_time": str,
        "punch_day": int,
        "work_day_no_punch_as_lack": bool,
        "work_hours_demand": bool,
        "work_hours": int,
    }

    def __init__(self, d=None):
        self.free_start_time: Optional[str] = None
        self.free_end_time: Optional[str] = None
        self.punch_day: Optional[int] = None
        self.work_day_no_punch_as_lack: Optional[bool] = None
        self.work_hours_demand: Optional[bool] = None
        self.work_hours: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FreePunchCfgBuilder":
        return FreePunchCfgBuilder()


class FreePunchCfgBuilder(object):
    def __init__(self) -> None:
        self._free_punch_cfg = FreePunchCfg()

    def free_start_time(self, free_start_time: str) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.free_start_time = free_start_time
        return self

    def free_end_time(self, free_end_time: str) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.free_end_time = free_end_time
        return self

    def punch_day(self, punch_day: int) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.punch_day = punch_day
        return self

    def work_day_no_punch_as_lack(self, work_day_no_punch_as_lack: bool) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.work_day_no_punch_as_lack = work_day_no_punch_as_lack
        return self

    def work_hours_demand(self, work_hours_demand: bool) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.work_hours_demand = work_hours_demand
        return self

    def work_hours(self, work_hours: int) -> "FreePunchCfgBuilder":
        self._free_punch_cfg.work_hours = work_hours
        return self

    def build(self) -> "FreePunchCfg":
        return self._free_punch_cfg
