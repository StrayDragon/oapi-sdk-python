# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .external_interview_assessment import ExternalInterviewAssessment


class CreateExternalInterviewAssessmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExternalInterviewAssessment] = None

    @staticmethod
    def builder() -> "CreateExternalInterviewAssessmentRequestBuilder":
        return CreateExternalInterviewAssessmentRequestBuilder()


class CreateExternalInterviewAssessmentRequestBuilder(object):

    def __init__(self) -> None:
        create_external_interview_assessment_request = CreateExternalInterviewAssessmentRequest()
        create_external_interview_assessment_request.http_method = HttpMethod.POST
        create_external_interview_assessment_request.uri = "/open-apis/hire/v1/external_interview_assessments"
        create_external_interview_assessment_request.token_types = {AccessTokenType.TENANT}
        self._create_external_interview_assessment_request: CreateExternalInterviewAssessmentRequest = create_external_interview_assessment_request

    def request_body(self,
                     request_body: ExternalInterviewAssessment) -> "CreateExternalInterviewAssessmentRequestBuilder":
        self._create_external_interview_assessment_request.request_body = request_body
        self._create_external_interview_assessment_request.body = request_body
        return self

    def build(self) -> CreateExternalInterviewAssessmentRequest:
        return self._create_external_interview_assessment_request
