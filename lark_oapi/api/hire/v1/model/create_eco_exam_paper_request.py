# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .eco_exam_paper import EcoExamPaper


class CreateEcoExamPaperRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[EcoExamPaper] = None

    @staticmethod
    def builder() -> "CreateEcoExamPaperRequestBuilder":
        return CreateEcoExamPaperRequestBuilder()


class CreateEcoExamPaperRequestBuilder(object):

    def __init__(self) -> None:
        create_eco_exam_paper_request = CreateEcoExamPaperRequest()
        create_eco_exam_paper_request.http_method = HttpMethod.POST
        create_eco_exam_paper_request.uri = "/open-apis/hire/v1/eco_exam_papers"
        create_eco_exam_paper_request.token_types = {AccessTokenType.TENANT}
        self._create_eco_exam_paper_request: CreateEcoExamPaperRequest = create_eco_exam_paper_request

    def request_body(self, request_body: EcoExamPaper) -> "CreateEcoExamPaperRequestBuilder":
        self._create_eco_exam_paper_request.request_body = request_body
        self._create_eco_exam_paper_request.body = request_body
        return self

    def build(self) -> CreateEcoExamPaperRequest:
        return self._create_eco_exam_paper_request
