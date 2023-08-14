# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
from ....event.model.event import *
import attr


@to_json_decorator
@attr.s
class Href:
    url = attr.ib(type=str, default=None, metadata={"json": "url"})
    title = attr.ib(type=str, default=None, metadata={"json": "title"})


@to_json_decorator
@attr.s
class Origin:
    platform_i18n_name = attr.ib(
        type=str, default=None, metadata={"json": "platform_i18n_name"}
    )
    href = attr.ib(type=Href, default=None, metadata={"json": "href"})


@to_json_decorator
@attr.s
class Due:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["time"])
    time = attr.ib(type=int, default=None, metadata={"json": "time"})
    timezone = attr.ib(type=str, default=None, metadata={"json": "timezone"})
    is_all_day = attr.ib(type=bool, default=None, metadata={"json": "is_all_day"})


@to_json_decorator
@attr.s
class Task:
    __int_to_string_fields__ = attr.ib(
        type=List[str], default=["complete_time", "create_time", "update_time"]
    )
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    summary = attr.ib(type=str, default=None, metadata={"json": "summary"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    complete_time = attr.ib(type=int, default=None, metadata={"json": "complete_time"})
    creator_id = attr.ib(type=str, default=None, metadata={"json": "creator_id"})
    extra = attr.ib(type=str, default=None, metadata={"json": "extra"})
    create_time = attr.ib(type=int, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=int, default=None, metadata={"json": "update_time"})
    due = attr.ib(type=Due, default=None, metadata={"json": "due"})
    origin = attr.ib(type=Origin, default=None, metadata={"json": "origin"})
    can_edit = attr.ib(type=bool, default=None, metadata={"json": "can_edit"})
    custom = attr.ib(type=str, default=None, metadata={"json": "custom"})


@to_json_decorator
@attr.s
class Collaborator:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})


@to_json_decorator
@attr.s
class Comment:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["parent_id", "id"])
    content = attr.ib(type=str, default=None, metadata={"json": "content"})
    parent_id = attr.ib(type=int, default=None, metadata={"json": "parent_id"})
    id = attr.ib(type=int, default=None, metadata={"json": "id"})


@to_json_decorator
@attr.s
class Follower:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})


@to_json_decorator
@attr.s
class Reminder:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["id"])
    id = attr.ib(type=int, default=None, metadata={"json": "id"})
    relative_fire_minute = attr.ib(
        type=int, default=None, metadata={"json": "relative_fire_minute"}
    )


@attr.s
class TaskCreateResult:
    task = attr.ib(type=Task, default=None, metadata={"json": "task"})


@attr.s
class TaskGetResult:
    task = attr.ib(type=Task, default=None, metadata={"json": "task"})


@to_json_decorator
@attr.s
class TaskPatchReqBody:
    task = attr.ib(type=Task, default=None, metadata={"json": "task"})
    update_fields = attr.ib(
        type=List[str], default=None, metadata={"json": "update_fields"}
    )


@attr.s
class TaskPatchResult:
    task = attr.ib(type=Task, default=None, metadata={"json": "task"})


@attr.s
class TaskCollaboratorCreateResult:
    collaborator = attr.ib(
        type=Collaborator, default=None, metadata={"json": "collaborator"}
    )


@attr.s
class TaskCollaboratorListResult:
    items = attr.ib(type=List[Collaborator], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})


@attr.s
class TaskCommentCreateResult:
    comment = attr.ib(type=Comment, default=None, metadata={"json": "comment"})


@attr.s
class TaskCommentGetResult:
    comment = attr.ib(type=Comment, default=None, metadata={"json": "comment"})


@to_json_decorator
@attr.s
class TaskCommentUpdateReqBody:
    content = attr.ib(type=str, default=None, metadata={"json": "content"})


@attr.s
class TaskCommentUpdateResult:
    comment = attr.ib(type=Comment, default=None, metadata={"json": "comment"})


@attr.s
class TaskFollowerCreateResult:
    follower = attr.ib(type=Follower, default=None, metadata={"json": "follower"})


@attr.s
class TaskFollowerListResult:
    items = attr.ib(type=List[Follower], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})


@attr.s
class TaskReminderCreateResult:
    reminder = attr.ib(type=Reminder, default=None, metadata={"json": "reminder"})


@attr.s
class TaskReminderListResult:
    items = attr.ib(type=List[Reminder], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})


@attr.s
class TaskUpdatedEventData:
    task_id = attr.ib(type=str, default=None, metadata={"json": "task_id"})
    obj_type = attr.ib(type=int, default=None, metadata={"json": "obj_type"})


@attr.s
class TaskUpdatedEvent(BaseEventV2):
    event = attr.ib(type=TaskUpdatedEventData, default=None)


@attr.s
class TaskCommentUpdatedEventData:
    task_id = attr.ib(type=str, default=None, metadata={"json": "task_id"})
    comment_id = attr.ib(type=str, default=None, metadata={"json": "comment_id"})
    parent_id = attr.ib(type=str, default=None, metadata={"json": "parent_id"})
    obj_type = attr.ib(type=int, default=None, metadata={"json": "obj_type"})


@attr.s
class TaskCommentUpdatedEvent(BaseEventV2):
    event = attr.ib(type=TaskCommentUpdatedEventData, default=None)
