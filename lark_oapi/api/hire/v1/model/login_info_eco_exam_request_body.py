# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .eco_exam_login_info import EcoExamLoginInfo


class LoginInfoEcoExamRequestBody(object):
    _types = {
        "result": int,
        "msg": str,
        "exam_login_info": EcoExamLoginInfo,
    }

    def __init__(self, d=None):
        self.result: Optional[int] = None
        self.msg: Optional[str] = None
        self.exam_login_info: Optional[EcoExamLoginInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LoginInfoEcoExamRequestBodyBuilder":
        return LoginInfoEcoExamRequestBodyBuilder()


class LoginInfoEcoExamRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._login_info_eco_exam_request_body = LoginInfoEcoExamRequestBody()

    def result(self, result: int) -> "LoginInfoEcoExamRequestBodyBuilder":
        self._login_info_eco_exam_request_body.result = result
        return self

    def msg(self, msg: str) -> "LoginInfoEcoExamRequestBodyBuilder":
        self._login_info_eco_exam_request_body.msg = msg
        return self

    def exam_login_info(self, exam_login_info: EcoExamLoginInfo) -> "LoginInfoEcoExamRequestBodyBuilder":
        self._login_info_eco_exam_request_body.exam_login_info = exam_login_info
        return self

    def build(self) -> "LoginInfoEcoExamRequestBody":
        return self._login_info_eco_exam_request_body