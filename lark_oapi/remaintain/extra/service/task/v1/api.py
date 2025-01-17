# Code generated by lark suite oapi sdk gen

from typing import *

from ....api import (
    Request as APIRequest,
    Response as APIResponse,
    set_timeout,
    set_tenant_key,
    set_user_access_token,
    set_path_params,
    set_query_params,
    set_response_stream,
    set_is_response_stream,
    FormData,
    FormDataFile,
)
from ....config import Config
from ....consts import (
    ACCESS_TOKEN_TYPE_TENANT,
    ACCESS_TOKEN_TYPE_USER,
    ACCESS_TOKEN_TYPE_APP,
)
from .model import *


class Service:
    def __init__(self, conf):
        # type: (Config) -> None
        self.conf = conf
        self.tasks = TaskService(self)
        self.task_comments = TaskCommentService(self)
        self.task_collaborators = TaskCollaboratorService(self)
        self.task_followers = TaskFollowerService(self)
        self.task_reminders = TaskReminderService(self)


class TaskService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def complete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskCompleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCompleteReqCall(self, request_opts=request_opts)

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Task, str, int) -> TaskCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskDeleteReqCall(self, request_opts=request_opts)

    def get(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskGetReqCall(self, request_opts=request_opts)

    def patch(self, body, tenant_key=None, timeout=None):
        # type: (TaskPatchReqBody, str, int) -> TaskPatchReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskPatchReqCall(self, body, request_opts=request_opts)

    def uncomplete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskUncompleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskUncompleteReqCall(self, request_opts=request_opts)


class TaskCommentService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Comment, str, int) -> TaskCommentCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCommentCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskCommentDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCommentDeleteReqCall(self, request_opts=request_opts)

    def get(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskCommentGetReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCommentGetReqCall(self, request_opts=request_opts)

    def update(self, body, tenant_key=None, timeout=None):
        # type: (TaskCommentUpdateReqBody, str, int) -> TaskCommentUpdateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCommentUpdateReqCall(self, body, request_opts=request_opts)


class TaskCollaboratorService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Collaborator, str, int) -> TaskCollaboratorCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCollaboratorCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskCollaboratorDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCollaboratorDeleteReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskCollaboratorListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskCollaboratorListReqCall(self, request_opts=request_opts)


class TaskFollowerService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Follower, str, int) -> TaskFollowerCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskFollowerCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskFollowerDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskFollowerDeleteReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskFollowerListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskFollowerListReqCall(self, request_opts=request_opts)


class TaskReminderService:
    def __init__(self, service):
        # type: (Service) -> None
        self.service = service

    def create(self, body, tenant_key=None, timeout=None):
        # type: (Reminder, str, int) -> TaskReminderCreateReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskReminderCreateReqCall(self, body, request_opts=request_opts)

    def delete(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskReminderDeleteReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskReminderDeleteReqCall(self, request_opts=request_opts)

    def list(self, tenant_key=None, timeout=None):
        # type: (str, int) -> TaskReminderListReqCall

        request_opts = []  # type: List[Callable[[Any], Any]]

        if timeout is not None:
            request_opts += [set_timeout(timeout)]

        if tenant_key is not None:
            request_opts += [set_tenant_key(tenant_key)]

        return TaskReminderListReqCall(self, request_opts=request_opts)


class TaskCompleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCompleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/complete",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskService, Task, List[Any]) -> None

        self.service = service
        self.body = body
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskCreateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskDeleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskGetReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskGetReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=TaskGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskPatchReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskService, TaskPatchReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskPatchReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskPatchReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskPatchResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id",
            "PATCH",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskPatchResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskUncompleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskUncompleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/uncomplete",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCollaboratorCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskCollaboratorService, Collaborator, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCollaboratorCreateReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskCollaboratorCreateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCollaboratorCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/collaborators",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskCollaboratorCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCollaboratorDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskCollaboratorService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCollaboratorDeleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_collaborator_id(self, collaborator_id):
        # type: (str) -> TaskCollaboratorDeleteReqCall
        self.path_params["collaborator_id"] = collaborator_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/collaborators/:collaborator_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCollaboratorListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskCollaboratorService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCollaboratorListReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_page_size(self, page_size):
        # type: (int) -> TaskCollaboratorListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> TaskCollaboratorListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskCollaboratorListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCollaboratorListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/collaborators",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=TaskCollaboratorListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCommentCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskCommentService, Comment, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCommentCreateReqCall
        self.path_params["task_id"] = task_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCommentCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/comments",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskCommentCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCommentDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskCommentService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCommentDeleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_comment_id(self, comment_id):
        # type: (int) -> TaskCommentDeleteReqCall
        self.path_params["comment_id"] = comment_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/comments/:comment_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCommentGetReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskCommentService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCommentGetReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_comment_id(self, comment_id):
        # type: (int) -> TaskCommentGetReqCall
        self.path_params["comment_id"] = comment_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCommentGetResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/comments/:comment_id",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=TaskCommentGetResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskCommentUpdateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskCommentService, TaskCommentUpdateReqBody, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskCommentUpdateReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_comment_id(self, comment_id):
        # type: (int) -> TaskCommentUpdateReqCall
        self.path_params["comment_id"] = comment_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskCommentUpdateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/comments/:comment_id",
            "PUT",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskCommentUpdateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskFollowerCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskFollowerService, Follower, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskFollowerCreateReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskFollowerCreateReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskFollowerCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/followers",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskFollowerCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskFollowerDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskFollowerService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskFollowerDeleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_follower_id(self, follower_id):
        # type: (str) -> TaskFollowerDeleteReqCall
        self.path_params["follower_id"] = follower_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/followers/:follower_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskFollowerListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskFollowerService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskFollowerListReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_page_size(self, page_size):
        # type: (int) -> TaskFollowerListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> TaskFollowerListReqCall
        self.query_params["page_token"] = page_token
        return self

    def set_user_id_type(self, user_id_type):
        # type: (str) -> TaskFollowerListReqCall
        self.query_params["user_id_type"] = user_id_type
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskFollowerListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/followers",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=TaskFollowerListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskReminderCreateReqCall:
    def __init__(self, service, body, request_opts=None):
        # type: (TaskReminderService, Reminder, List[Any]) -> None

        self.service = service
        self.body = body
        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskReminderCreateReqCall
        self.path_params["task_id"] = task_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskReminderCreateResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/reminders",
            "POST",
            [ACCESS_TOKEN_TYPE_TENANT],
            self.body,
            output_class=TaskReminderCreateResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskReminderDeleteReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskReminderService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskReminderDeleteReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_reminder_id(self, reminder_id):
        # type: (str) -> TaskReminderDeleteReqCall
        self.path_params["reminder_id"] = reminder_id
        return self

    def do(self):
        # type: () -> APIResponse[Type[None]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/reminders/:reminder_id",
            "DELETE",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp


class TaskReminderListReqCall:
    def __init__(self, service, request_opts=None):
        # type: (TaskReminderService, List[Any]) -> None

        self.service = service

        self.path_params = {}  # type: Dict[str, Any]
        self.query_params = {}  # type: Dict[str, Any]

        if request_opts:
            self.request_opts = request_opts
        else:
            self.request_opts = []  # type: List[Any]

    def set_task_id(self, task_id):
        # type: (str) -> TaskReminderListReqCall
        self.path_params["task_id"] = task_id
        return self

    def set_page_size(self, page_size):
        # type: (int) -> TaskReminderListReqCall
        self.query_params["page_size"] = page_size
        return self

    def set_page_token(self, page_token):
        # type: (str) -> TaskReminderListReqCall
        self.query_params["page_token"] = page_token
        return self

    def do(self):
        # type: () -> APIResponse[Type[TaskReminderListResult]]
        root_service = self.service.service

        conf = root_service.conf
        self.request_opts += [set_path_params(self.path_params)]
        self.request_opts += [set_query_params(self.query_params)]
        req = APIRequest(
            "/open-apis/task/v1/tasks/:task_id/reminders",
            "GET",
            [ACCESS_TOKEN_TYPE_TENANT],
            None,
            output_class=TaskReminderListResult,
            request_opts=self.request_opts,
        )
        resp = req.do(conf)
        return resp
