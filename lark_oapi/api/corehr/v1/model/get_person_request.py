# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetPersonRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.person_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetPersonRequestBuilder":
        return GetPersonRequestBuilder()


class GetPersonRequestBuilder(object):

    def __init__(self, get_person_request: GetPersonRequest = GetPersonRequest()) -> None:
        get_person_request.http_method = HttpMethod.GET
        get_person_request.uri = "/open-apis/corehr/v1/persons/:person_id"
        get_person_request.token_types = {AccessTokenType.TENANT}
        self._get_person_request: GetPersonRequest = get_person_request

    def user_id_type(self, user_id_type: str) -> "GetPersonRequestBuilder":
        self._get_person_request.user_id_type = user_id_type
        self._get_person_request.queries["user_id_type"] = str(user_id_type)
        return self

    def person_id(self, person_id: str) -> "GetPersonRequestBuilder":
        self._get_person_request.person_id = person_id
        self._get_person_request.paths["person_id"] = person_id
        return self

    def build(self) -> GetPersonRequest:
        return self._get_person_request