# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class JiraIssue(object):
    _types = {
        "id": str,
        "key": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JiraIssueBuilder":
        return JiraIssueBuilder()


class JiraIssueBuilder(object):
    def __init__(self) -> None:
        self._jira_issue = JiraIssue()

    def id(self, id: str) -> "JiraIssueBuilder":
        self._jira_issue.id = id
        return self

    def key(self, key: str) -> "JiraIssueBuilder":
        self._jira_issue.key = key
        return self

    def build(self) -> "JiraIssue":
        return self._jira_issue
