# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiVcMeetingExtra(object):
    _types = {
        "vc_meeting_id": str,
        "vc_locale": str,
        "vc_applink_host": str,
        "vc_app_version": str,
        "vc_feature_config": str,
    }

    def __init__(self, d=None):
        self.vc_meeting_id: Optional[str] = None
        self.vc_locale: Optional[str] = None
        self.vc_applink_host: Optional[str] = None
        self.vc_app_version: Optional[str] = None
        self.vc_feature_config: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiVcMeetingExtraBuilder":
        return MyAiVcMeetingExtraBuilder()


class MyAiVcMeetingExtraBuilder(object):
    def __init__(self) -> None:
        self._my_ai_vc_meeting_extra = MyAiVcMeetingExtra()

    def vc_meeting_id(self, vc_meeting_id: str) -> "MyAiVcMeetingExtraBuilder":
        self._my_ai_vc_meeting_extra.vc_meeting_id = vc_meeting_id
        return self

    def vc_locale(self, vc_locale: str) -> "MyAiVcMeetingExtraBuilder":
        self._my_ai_vc_meeting_extra.vc_locale = vc_locale
        return self

    def vc_applink_host(self, vc_applink_host: str) -> "MyAiVcMeetingExtraBuilder":
        self._my_ai_vc_meeting_extra.vc_applink_host = vc_applink_host
        return self

    def vc_app_version(self, vc_app_version: str) -> "MyAiVcMeetingExtraBuilder":
        self._my_ai_vc_meeting_extra.vc_app_version = vc_app_version
        return self

    def vc_feature_config(self, vc_feature_config: str) -> "MyAiVcMeetingExtraBuilder":
        self._my_ai_vc_meeting_extra.vc_feature_config = vc_feature_config
        return self

    def build(self) -> "MyAiVcMeetingExtra":
        return self._my_ai_vc_meeting_extra
