# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ApprovalConfig(object):
    _types = {
        "can_update_viewer": bool,
        "can_update_form": bool,
        "can_update_process": bool,
        "can_update_revert": bool,
        "help_url": str,
    }

    def __init__(self, d=None):
        self.can_update_viewer: Optional[bool] = None
        self.can_update_form: Optional[bool] = None
        self.can_update_process: Optional[bool] = None
        self.can_update_revert: Optional[bool] = None
        self.help_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalConfigBuilder":
        return ApprovalConfigBuilder()


class ApprovalConfigBuilder(object):
    def __init__(self) -> None:
        self._approval_config = ApprovalConfig()

    def can_update_viewer(self, can_update_viewer: bool) -> "ApprovalConfigBuilder":
        self._approval_config.can_update_viewer = can_update_viewer
        return self

    def can_update_form(self, can_update_form: bool) -> "ApprovalConfigBuilder":
        self._approval_config.can_update_form = can_update_form
        return self

    def can_update_process(self, can_update_process: bool) -> "ApprovalConfigBuilder":
        self._approval_config.can_update_process = can_update_process
        return self

    def can_update_revert(self, can_update_revert: bool) -> "ApprovalConfigBuilder":
        self._approval_config.can_update_revert = can_update_revert
        return self

    def help_url(self, help_url: str) -> "ApprovalConfigBuilder":
        self._approval_config.help_url = help_url
        return self

    def build(self) -> "ApprovalConfig":
        return self._approval_config
