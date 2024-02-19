# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .translate_text_request_body import TranslateTextRequestBody


class TranslateTextRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[TranslateTextRequestBody] = None

    @staticmethod
    def builder() -> "TranslateTextRequestBuilder":
        return TranslateTextRequestBuilder()


class TranslateTextRequestBuilder(object):

    def __init__(self) -> None:
        translate_text_request = TranslateTextRequest()
        translate_text_request.http_method = HttpMethod.POST
        translate_text_request.uri = "/open-apis/translation/v1/text/translate"
        translate_text_request.token_types = {AccessTokenType.TENANT}
        self._translate_text_request: TranslateTextRequest = translate_text_request

    def request_body(self, request_body: TranslateTextRequestBody) -> "TranslateTextRequestBuilder":
        self._translate_text_request.request_body = request_body
        self._translate_text_request.body = request_body
        return self

    def build(self) -> TranslateTextRequest:
        return self._translate_text_request
