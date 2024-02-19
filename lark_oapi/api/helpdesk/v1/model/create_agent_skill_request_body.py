# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .agent_skill_rule import AgentSkillRule


class CreateAgentSkillRequestBody(object):
    _types = {
        "name": str,
        "rules": List[AgentSkillRule],
        "agent_ids": List[str],
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.rules: Optional[List[AgentSkillRule]] = None
        self.agent_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAgentSkillRequestBodyBuilder":
        return CreateAgentSkillRequestBodyBuilder()


class CreateAgentSkillRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_agent_skill_request_body = CreateAgentSkillRequestBody()

    def name(self, name: str) -> "CreateAgentSkillRequestBodyBuilder":
        self._create_agent_skill_request_body.name = name
        return self

    def rules(self, rules: List[AgentSkillRule]) -> "CreateAgentSkillRequestBodyBuilder":
        self._create_agent_skill_request_body.rules = rules
        return self

    def agent_ids(self, agent_ids: List[str]) -> "CreateAgentSkillRequestBodyBuilder":
        self._create_agent_skill_request_body.agent_ids = agent_ids
        return self

    def build(self) -> "CreateAgentSkillRequestBody":
        return self._create_agent_skill_request_body
