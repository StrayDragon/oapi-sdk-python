# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class SearchProbationRequestBody(object):
    _types = {
        "employment_ids": List[str],
        "department_ids": List[str],
        "probation_start_date_start": str,
        "probation_start_date_end": str,
        "probation_expected_end_date_start": str,
        "probation_expected_end_date_end": str,
        "actual_probation_end_date_start": str,
        "actual_probation_end_date_end": str,
        "initiating_time_start": str,
        "initiating_time_end": str,
        "probation_status": str,
        "final_assessment_result": str,
        "final_assessment_grade": str,
    }

    def __init__(self, d=None):
        self.employment_ids: Optional[List[str]] = None
        self.department_ids: Optional[List[str]] = None
        self.probation_start_date_start: Optional[str] = None
        self.probation_start_date_end: Optional[str] = None
        self.probation_expected_end_date_start: Optional[str] = None
        self.probation_expected_end_date_end: Optional[str] = None
        self.actual_probation_end_date_start: Optional[str] = None
        self.actual_probation_end_date_end: Optional[str] = None
        self.initiating_time_start: Optional[str] = None
        self.initiating_time_end: Optional[str] = None
        self.probation_status: Optional[str] = None
        self.final_assessment_result: Optional[str] = None
        self.final_assessment_grade: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchProbationRequestBodyBuilder":
        return SearchProbationRequestBodyBuilder()


class SearchProbationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_probation_request_body = SearchProbationRequestBody()

    def employment_ids(self, employment_ids: List[str]) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.employment_ids = employment_ids
        return self

    def department_ids(self, department_ids: List[str]) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.department_ids = department_ids
        return self

    def probation_start_date_start(self, probation_start_date_start: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.probation_start_date_start = probation_start_date_start
        return self

    def probation_start_date_end(self, probation_start_date_end: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.probation_start_date_end = probation_start_date_end
        return self

    def probation_expected_end_date_start(self,
                                          probation_expected_end_date_start: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.probation_expected_end_date_start = probation_expected_end_date_start
        return self

    def probation_expected_end_date_end(self,
                                        probation_expected_end_date_end: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.probation_expected_end_date_end = probation_expected_end_date_end
        return self

    def actual_probation_end_date_start(self,
                                        actual_probation_end_date_start: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.actual_probation_end_date_start = actual_probation_end_date_start
        return self

    def actual_probation_end_date_end(self, actual_probation_end_date_end: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.actual_probation_end_date_end = actual_probation_end_date_end
        return self

    def initiating_time_start(self, initiating_time_start: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.initiating_time_start = initiating_time_start
        return self

    def initiating_time_end(self, initiating_time_end: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.initiating_time_end = initiating_time_end
        return self

    def probation_status(self, probation_status: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.probation_status = probation_status
        return self

    def final_assessment_result(self, final_assessment_result: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.final_assessment_result = final_assessment_result
        return self

    def final_assessment_grade(self, final_assessment_grade: str) -> "SearchProbationRequestBodyBuilder":
        self._search_probation_request_body.final_assessment_grade = final_assessment_grade
        return self

    def build(self) -> "SearchProbationRequestBody":
        return self._search_probation_request_body
