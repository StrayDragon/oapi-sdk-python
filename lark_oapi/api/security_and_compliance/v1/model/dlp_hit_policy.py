# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DlpHitPolicy(object):
    _types = {
        "policy_id": int,
        "policy_name": str,
    }

    def __init__(self, d=None):
        self.policy_id: Optional[int] = None
        self.policy_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DlpHitPolicyBuilder":
        return DlpHitPolicyBuilder()


class DlpHitPolicyBuilder(object):
    def __init__(self) -> None:
        self._dlp_hit_policy = DlpHitPolicy()

    def policy_id(self, policy_id: int) -> "DlpHitPolicyBuilder":
        self._dlp_hit_policy.policy_id = policy_id
        return self

    def policy_name(self, policy_name: str) -> "DlpHitPolicyBuilder":
        self._dlp_hit_policy.policy_name = policy_name
        return self

    def build(self) -> "DlpHitPolicy":
        return self._dlp_hit_policy
