# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .remove_dependencies_task_request_body import RemoveDependenciesTaskRequestBody


class RemoveDependenciesTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_guid: Optional[str] = None
        self.request_body: Optional[RemoveDependenciesTaskRequestBody] = None

    @staticmethod
    def builder() -> "RemoveDependenciesTaskRequestBuilder":
        return RemoveDependenciesTaskRequestBuilder()


class RemoveDependenciesTaskRequestBuilder(object):

    def __init__(self) -> None:
        remove_dependencies_task_request = RemoveDependenciesTaskRequest()
        remove_dependencies_task_request.http_method = HttpMethod.POST
        remove_dependencies_task_request.uri = "/open-apis/task/v2/tasks/:task_guid/remove_dependencies"
        remove_dependencies_task_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._remove_dependencies_task_request: RemoveDependenciesTaskRequest = remove_dependencies_task_request

    def task_guid(self, task_guid: str) -> "RemoveDependenciesTaskRequestBuilder":
        self._remove_dependencies_task_request.task_guid = task_guid
        self._remove_dependencies_task_request.paths["task_guid"] = str(task_guid)
        return self

    def request_body(self, request_body: RemoveDependenciesTaskRequestBody) -> "RemoveDependenciesTaskRequestBuilder":
        self._remove_dependencies_task_request.request_body = request_body
        self._remove_dependencies_task_request.body = request_body
        return self

    def build(self) -> RemoveDependenciesTaskRequest:
        return self._remove_dependencies_task_request
