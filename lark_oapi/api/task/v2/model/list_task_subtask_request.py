# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListTaskSubtaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.task_guid: Optional[str] = None

    @staticmethod
    def builder() -> "ListTaskSubtaskRequestBuilder":
        return ListTaskSubtaskRequestBuilder()


class ListTaskSubtaskRequestBuilder(object):

    def __init__(self) -> None:
        list_task_subtask_request = ListTaskSubtaskRequest()
        list_task_subtask_request.http_method = HttpMethod.GET
        list_task_subtask_request.uri = "/open-apis/task/v2/tasks/:task_guid/subtasks"
        list_task_subtask_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_task_subtask_request: ListTaskSubtaskRequest = list_task_subtask_request

    def page_size(self, page_size: int) -> "ListTaskSubtaskRequestBuilder":
        self._list_task_subtask_request.page_size = page_size
        self._list_task_subtask_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListTaskSubtaskRequestBuilder":
        self._list_task_subtask_request.page_token = page_token
        self._list_task_subtask_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListTaskSubtaskRequestBuilder":
        self._list_task_subtask_request.user_id_type = user_id_type
        self._list_task_subtask_request.add_query("user_id_type", user_id_type)
        return self

    def task_guid(self, task_guid: str) -> "ListTaskSubtaskRequestBuilder":
        self._list_task_subtask_request.task_guid = task_guid
        self._list_task_subtask_request.paths["task_guid"] = str(task_guid)
        return self

    def build(self) -> ListTaskSubtaskRequest:
        return self._list_task_subtask_request
