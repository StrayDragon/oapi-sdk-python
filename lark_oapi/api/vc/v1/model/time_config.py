# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TimeConfig(object):
    _types = {
        "if_cover_child_scope": bool,
        "time_switch": int,
        "days_in_advance": int,
        "opening_hour": int,
        "start_time": int,
        "end_time": int,
        "max_duration": int,
    }

    def __init__(self, d=None):
        self.if_cover_child_scope: Optional[bool] = None
        self.time_switch: Optional[int] = None
        self.days_in_advance: Optional[int] = None
        self.opening_hour: Optional[int] = None
        self.start_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.max_duration: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TimeConfigBuilder":
        return TimeConfigBuilder()


class TimeConfigBuilder(object):
    def __init__(self) -> None:
        self._time_config = TimeConfig()

    def if_cover_child_scope(self, if_cover_child_scope: bool) -> "TimeConfigBuilder":
        self._time_config.if_cover_child_scope = if_cover_child_scope
        return self

    def time_switch(self, time_switch: int) -> "TimeConfigBuilder":
        self._time_config.time_switch = time_switch
        return self

    def days_in_advance(self, days_in_advance: int) -> "TimeConfigBuilder":
        self._time_config.days_in_advance = days_in_advance
        return self

    def opening_hour(self, opening_hour: int) -> "TimeConfigBuilder":
        self._time_config.opening_hour = opening_hour
        return self

    def start_time(self, start_time: int) -> "TimeConfigBuilder":
        self._time_config.start_time = start_time
        return self

    def end_time(self, end_time: int) -> "TimeConfigBuilder":
        self._time_config.end_time = end_time
        return self

    def max_duration(self, max_duration: int) -> "TimeConfigBuilder":
        self._time_config.max_duration = max_duration
        return self

    def build(self) -> "TimeConfig":
        return self._time_config
