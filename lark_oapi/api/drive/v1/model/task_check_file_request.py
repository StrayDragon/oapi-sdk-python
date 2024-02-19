# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class TaskCheckFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None

    @staticmethod
    def builder() -> "TaskCheckFileRequestBuilder":
        return TaskCheckFileRequestBuilder()


class TaskCheckFileRequestBuilder(object):

    def __init__(self) -> None:
        task_check_file_request = TaskCheckFileRequest()
        task_check_file_request.http_method = HttpMethod.GET
        task_check_file_request.uri = "/open-apis/drive/v1/files/task_check"
        task_check_file_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._task_check_file_request: TaskCheckFileRequest = task_check_file_request

    def task_id(self, task_id: str) -> "TaskCheckFileRequestBuilder":
        self._task_check_file_request.task_id = task_id
        self._task_check_file_request.add_query("task_id", task_id)
        return self

    def build(self) -> TaskCheckFileRequest:
        return self._task_check_file_request
