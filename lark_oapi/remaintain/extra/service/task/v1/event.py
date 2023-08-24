# Code generated by lark suite oapi sdk gen

from typing import Callable

from ....config import Config
from ....context import Context
from ....event.event import set_event_callback

from .model import *


class TaskUpdatedEventHandler:
    def __init__(self, callback):
        # type: (Callable[[Context, Config, TaskUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(
        self, ctx, conf, event
    ):  # type: (Context, Config, TaskUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, TaskUpdatedEvent], Any]) -> None
        handler = TaskUpdatedEventHandler(callback)
        set_event_callback(
            conf, "task.task.updated_v1", handler.handle, clazz=TaskUpdatedEvent
        )


class TaskCommentUpdatedEventHandler:
    def __init__(self, callback):
        # type: (Callable[[Context, Config, TaskCommentUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(
        self, ctx, conf, event
    ):  # type: (Context, Config, TaskCommentUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, TaskCommentUpdatedEvent], Any]) -> None
        handler = TaskCommentUpdatedEventHandler(callback)
        set_event_callback(
            conf,
            "task.task.comment.updated_v1",
            handler.handle,
            clazz=TaskCommentUpdatedEvent,
        )