# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .ability import Ability
from .i18n import I18n


class InterviewQuestion(object):
    _types = {
        "id": str,
        "title": I18n,
        "description": I18n,
        "content": str,
        "ability_list": List[Ability],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.title: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.content: Optional[str] = None
        self.ability_list: Optional[List[Ability]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewQuestionBuilder":
        return InterviewQuestionBuilder()


class InterviewQuestionBuilder(object):
    def __init__(self) -> None:
        self._interview_question = InterviewQuestion()

    def id(self, id: str) -> "InterviewQuestionBuilder":
        self._interview_question.id = id
        return self

    def title(self, title: I18n) -> "InterviewQuestionBuilder":
        self._interview_question.title = title
        return self

    def description(self, description: I18n) -> "InterviewQuestionBuilder":
        self._interview_question.description = description
        return self

    def content(self, content: str) -> "InterviewQuestionBuilder":
        self._interview_question.content = content
        return self

    def ability_list(self, ability_list: List[Ability]) -> "InterviewQuestionBuilder":
        self._interview_question.ability_list = ability_list
        return self

    def build(self) -> "InterviewQuestion":
        return self._interview_question
