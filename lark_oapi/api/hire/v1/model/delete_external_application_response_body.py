# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .external_application import ExternalApplication


class DeleteExternalApplicationResponseBody(object):
    _types = {
        "external_application": ExternalApplication,
    }

    def __init__(self, d=None):
        self.external_application: Optional[ExternalApplication] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteExternalApplicationResponseBodyBuilder":
        return DeleteExternalApplicationResponseBodyBuilder()


class DeleteExternalApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_external_application_response_body = DeleteExternalApplicationResponseBody()

    def external_application(self,
                             external_application: ExternalApplication) -> "DeleteExternalApplicationResponseBodyBuilder":
        self._delete_external_application_response_body.external_application = external_application
        return self

    def build(self) -> "DeleteExternalApplicationResponseBody":
        return self._delete_external_application_response_body
