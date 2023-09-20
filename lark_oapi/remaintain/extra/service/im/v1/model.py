# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
from ....event.model.event import *
import attr


@to_json_decorator
@attr.s
class Operator:
    operator_id = attr.ib(type=str, default=None, metadata={"json": "operator_id"})
    operator_type = attr.ib(type=str, default=None, metadata={"json": "operator_type"})


@to_json_decorator
@attr.s
class Emoji:
    emoji_type = attr.ib(type=str, default=None, metadata={"json": "emoji_type"})


@to_json_decorator
@attr.s
class MessageReaction:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["action_time"])
    reaction_id = attr.ib(type=str, default=None, metadata={"json": "reaction_id"})
    operator = attr.ib(type=Operator, default=None, metadata={"json": "operator"})
    action_time = attr.ib(type=int, default=None, metadata={"json": "action_time"})
    reaction_type = attr.ib(
        type=Emoji, default=None, metadata={"json": "reaction_type"}
    )


@to_json_decorator
@attr.s
class Sender:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    id_type = attr.ib(type=str, default=None, metadata={"json": "id_type"})
    sender_type = attr.ib(type=str, default=None, metadata={"json": "sender_type"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class MessageBody:
    content = attr.ib(type=str, default=None, metadata={"json": "content"})


@to_json_decorator
@attr.s
class Mention:
    key = attr.ib(type=str, default=None, metadata={"json": "key"})
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    id_type = attr.ib(type=str, default=None, metadata={"json": "id_type"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class Message:
    __int_to_string_fields__ = attr.ib(
        type=List[str], default=["create_time", "update_time"]
    )
    message_id = attr.ib(type=str, default=None, metadata={"json": "message_id"})
    root_id = attr.ib(type=str, default=None, metadata={"json": "root_id"})
    parent_id = attr.ib(type=str, default=None, metadata={"json": "parent_id"})
    msg_type = attr.ib(type=str, default=None, metadata={"json": "msg_type"})
    create_time = attr.ib(type=int, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=int, default=None, metadata={"json": "update_time"})
    deleted = attr.ib(type=bool, default=None, metadata={"json": "deleted"})
    updated = attr.ib(type=bool, default=None, metadata={"json": "updated"})
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    sender = attr.ib(type=Sender, default=None, metadata={"json": "sender"})
    body = attr.ib(type=MessageBody, default=None, metadata={"json": "body"})
    mentions = attr.ib(type=List[Mention], default=None, metadata={"json": "mentions"})
    upper_message_id = attr.ib(
        type=str, default=None, metadata={"json": "upper_message_id"}
    )


@to_json_decorator
@attr.s
class I18nNames:
    zh_cn = attr.ib(type=str, default=None, metadata={"json": "zh_cn"})
    en_us = attr.ib(type=str, default=None, metadata={"json": "en_us"})
    ja_jp = attr.ib(type=str, default=None, metadata={"json": "ja_jp"})


@to_json_decorator
@attr.s
class Chat:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    only_owner_add = attr.ib(
        type=bool, default=None, metadata={"json": "only_owner_add"}
    )
    share_allowed = attr.ib(type=bool, default=None, metadata={"json": "share_allowed"})
    only_owner_at_all = attr.ib(
        type=bool, default=None, metadata={"json": "only_owner_at_all"}
    )
    only_owner_edit = attr.ib(
        type=bool, default=None, metadata={"json": "only_owner_edit"}
    )
    owner_user_id = attr.ib(type=str, default=None, metadata={"json": "owner_user_id"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})


@to_json_decorator
@attr.s
class UserId:
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})
    open_id = attr.ib(type=str, default=None, metadata={"json": "open_id"})
    union_id = attr.ib(type=str, default=None, metadata={"json": "union_id"})


@to_json_decorator
@attr.s
class MentionEvent:
    key = attr.ib(type=str, default=None, metadata={"json": "key"})
    id = attr.ib(type=UserId, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class EventMessage:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["create_time"])
    message_id = attr.ib(type=str, default=None, metadata={"json": "message_id"})
    root_id = attr.ib(type=str, default=None, metadata={"json": "root_id"})
    parent_id = attr.ib(type=str, default=None, metadata={"json": "parent_id"})
    create_time = attr.ib(type=int, default=None, metadata={"json": "create_time"})
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    chat_type = attr.ib(type=str, default=None, metadata={"json": "chat_type"})
    message_type = attr.ib(type=str, default=None, metadata={"json": "message_type"})
    content = attr.ib(type=str, default=None, metadata={"json": "content"})
    mentions = attr.ib(
        type=List[MentionEvent], default=None, metadata={"json": "mentions"}
    )


@to_json_decorator
@attr.s
class ChatChange:
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    add_member_permission = attr.ib(
        type=str, default=None, metadata={"json": "add_member_permission"}
    )
    share_card_permission = attr.ib(
        type=str, default=None, metadata={"json": "share_card_permission"}
    )
    at_all_permission = attr.ib(
        type=str, default=None, metadata={"json": "at_all_permission"}
    )
    edit_permission = attr.ib(
        type=str, default=None, metadata={"json": "edit_permission"}
    )
    membership_approval = attr.ib(
        type=str, default=None, metadata={"json": "membership_approval"}
    )
    join_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "join_message_visibility"}
    )
    leave_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "leave_message_visibility"}
    )
    moderation_permission = attr.ib(
        type=str, default=None, metadata={"json": "moderation_permission"}
    )
    owner_id = attr.ib(type=UserId, default=None, metadata={"json": "owner_id"})


@to_json_decorator
@attr.s
class ListEventModerator:
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    user_id = attr.ib(type=UserId, default=None, metadata={"json": "user_id"})


@to_json_decorator
@attr.s
class ModeratorList:
    added_member_list = attr.ib(
        type=List[ListEventModerator],
        default=None,
        metadata={"json": "added_member_list"},
    )
    removed_member_list = attr.ib(
        type=List[ListEventModerator],
        default=None,
        metadata={"json": "removed_member_list"},
    )


@to_json_decorator
@attr.s
class EventSender:
    sender_id = attr.ib(type=UserId, default=None, metadata={"json": "sender_id"})
    sender_type = attr.ib(type=str, default=None, metadata={"json": "sender_type"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class EventMessageReader:
    reader_id = attr.ib(type=UserId, default=None, metadata={"json": "reader_id"})
    read_time = attr.ib(type=str, default=None, metadata={"json": "read_time"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class ChatMemberUser:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    user_id = attr.ib(type=UserId, default=None, metadata={"json": "user_id"})


@to_json_decorator
@attr.s
class ChatMember:
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})


@to_json_decorator
@attr.s
class ChatMemberBot:
    bot_id = attr.ib(type=str, default=None, metadata={"json": "bot_id"})


@to_json_decorator
@attr.s
class ChatMembers:
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})


@to_json_decorator
@attr.s
class ListMember:
    member_id_type = attr.ib(
        type=str, default=None, metadata={"json": "member_id_type"}
    )
    member_id = attr.ib(type=str, default=None, metadata={"json": "member_id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class ListModerator:
    user_id_type = attr.ib(type=str, default=None, metadata={"json": "user_id_type"})
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class ReadUser:
    user_id_type = attr.ib(type=str, default=None, metadata={"json": "user_id_type"})
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})
    timestamp = attr.ib(type=str, default=None, metadata={"json": "timestamp"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class UrgentReceivers:
    user_id_list = attr.ib(
        type=List[str], default=None, metadata={"json": "user_id_list"}
    )


@to_json_decorator
@attr.s
class ChatManagers:
    __int_to_string_fields__ = attr.ib(type=List[str], default=["manager_id"])
    manager_id = attr.ib(type=int, default=None, metadata={"json": "manager_id"})


@to_json_decorator
@attr.s
class ListChat:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    owner_id_type = attr.ib(type=str, default=None, metadata={"json": "owner_id_type"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class ChatUpdateReqBody:
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    add_member_permission = attr.ib(
        type=str, default=None, metadata={"json": "add_member_permission"}
    )
    share_card_permission = attr.ib(
        type=str, default=None, metadata={"json": "share_card_permission"}
    )
    at_all_permission = attr.ib(
        type=str, default=None, metadata={"json": "at_all_permission"}
    )
    edit_permission = attr.ib(
        type=str, default=None, metadata={"json": "edit_permission"}
    )
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    join_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "join_message_visibility"}
    )
    leave_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "leave_message_visibility"}
    )
    membership_approval = attr.ib(
        type=str, default=None, metadata={"json": "membership_approval"}
    )


@attr.s
class ChatListResult:
    items = attr.ib(type=List[ListChat], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})


@attr.s
class ChatGetResult:
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    add_member_permission = attr.ib(
        type=str, default=None, metadata={"json": "add_member_permission"}
    )
    share_card_permission = attr.ib(
        type=str, default=None, metadata={"json": "share_card_permission"}
    )
    at_all_permission = attr.ib(
        type=str, default=None, metadata={"json": "at_all_permission"}
    )
    edit_permission = attr.ib(
        type=str, default=None, metadata={"json": "edit_permission"}
    )
    owner_id_type = attr.ib(type=str, default=None, metadata={"json": "owner_id_type"})
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    chat_mode = attr.ib(type=str, default=None, metadata={"json": "chat_mode"})
    chat_type = attr.ib(type=str, default=None, metadata={"json": "chat_type"})
    chat_tag = attr.ib(type=str, default=None, metadata={"json": "chat_tag"})
    join_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "join_message_visibility"}
    )
    leave_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "leave_message_visibility"}
    )
    membership_approval = attr.ib(
        type=str, default=None, metadata={"json": "membership_approval"}
    )
    moderation_permission = attr.ib(
        type=str, default=None, metadata={"json": "moderation_permission"}
    )
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})


@to_json_decorator
@attr.s
class ChatCreateReqBody:
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    chat_mode = attr.ib(type=str, default=None, metadata={"json": "chat_mode"})
    chat_type = attr.ib(type=str, default=None, metadata={"json": "chat_type"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    join_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "join_message_visibility"}
    )
    leave_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "leave_message_visibility"}
    )
    membership_approval = attr.ib(
        type=str, default=None, metadata={"json": "membership_approval"}
    )


@attr.s
class ChatCreateResult:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    avatar = attr.ib(type=str, default=None, metadata={"json": "avatar"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    i18n_names = attr.ib(type=I18nNames, default=None, metadata={"json": "i18n_names"})
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    owner_id_type = attr.ib(type=str, default=None, metadata={"json": "owner_id_type"})
    add_member_permission = attr.ib(
        type=str, default=None, metadata={"json": "add_member_permission"}
    )
    share_card_permission = attr.ib(
        type=str, default=None, metadata={"json": "share_card_permission"}
    )
    at_all_permission = attr.ib(
        type=str, default=None, metadata={"json": "at_all_permission"}
    )
    edit_permission = attr.ib(
        type=str, default=None, metadata={"json": "edit_permission"}
    )
    chat_mode = attr.ib(type=str, default=None, metadata={"json": "chat_mode"})
    chat_type = attr.ib(type=str, default=None, metadata={"json": "chat_type"})
    chat_tag = attr.ib(type=str, default=None, metadata={"json": "chat_tag"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    join_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "join_message_visibility"}
    )
    leave_message_visibility = attr.ib(
        type=str, default=None, metadata={"json": "leave_message_visibility"}
    )
    membership_approval = attr.ib(
        type=str, default=None, metadata={"json": "membership_approval"}
    )
    moderation_permission = attr.ib(
        type=str, default=None, metadata={"json": "moderation_permission"}
    )


@attr.s
class ChatSearchResult:
    items = attr.ib(type=List[ListChat], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})


@attr.s
class ChatAnnouncementGetResult:
    content = attr.ib(type=str, default=None, metadata={"json": "content"})
    revision = attr.ib(type=str, default=None, metadata={"json": "revision"})
    create_time = attr.ib(type=str, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=str, default=None, metadata={"json": "update_time"})
    owner_id_type = attr.ib(type=str, default=None, metadata={"json": "owner_id_type"})
    owner_id = attr.ib(type=str, default=None, metadata={"json": "owner_id"})
    modifier_id_type = attr.ib(
        type=str, default=None, metadata={"json": "modifier_id_type"}
    )
    modifier_id = attr.ib(type=str, default=None, metadata={"json": "modifier_id"})


@to_json_decorator
@attr.s
class ChatAnnouncementPatchReqBody:
    revision = attr.ib(type=str, default=None, metadata={"json": "revision"})
    requests = attr.ib(type=List[str], default=None, metadata={"json": "requests"})


@to_json_decorator
@attr.s
class ChatMembersCreateReqBody:
    id_list = attr.ib(type=List[str], default=None, metadata={"json": "id_list"})


@attr.s
class ChatMembersCreateResult:
    invalid_id_list = attr.ib(
        type=List[str], default=None, metadata={"json": "invalid_id_list"}
    )


@to_json_decorator
@attr.s
class ChatMembersDeleteReqBody:
    id_list = attr.ib(type=List[str], default=None, metadata={"json": "id_list"})


@attr.s
class ChatMembersDeleteResult:
    invalid_id_list = attr.ib(
        type=List[str], default=None, metadata={"json": "invalid_id_list"}
    )


@attr.s
class ChatMembersGetResult:
    items = attr.ib(type=List[ListMember], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    member_total = attr.ib(type=int, default=None, metadata={"json": "member_total"})


@attr.s
class ChatMembersIsInChatResult:
    is_in_chat = attr.ib(type=bool, default=None, metadata={"json": "is_in_chat"})


@attr.s
class FileCreateResult:
    file_key = attr.ib(type=str, default=None, metadata={"json": "file_key"})


@attr.s
class ImageCreateResult:
    image_key = attr.ib(type=str, default=None, metadata={"json": "image_key"})


@attr.s
class MessageListResult:
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    items = attr.ib(type=List[Message], default=None, metadata={"json": "items"})


@to_json_decorator
@attr.s
class MessagePatchReqBody:
    content = attr.ib(type=str, default=None, metadata={"json": "content"})


@to_json_decorator
@attr.s
class MessageReplyReqBody:
    content = attr.ib(type=str, default=None, metadata={"json": "content"})
    msg_type = attr.ib(type=str, default=None, metadata={"json": "msg_type"})


@to_json_decorator
@attr.s
class MessageCreateReqBody:
    receive_id = attr.ib(type=str, default=None, metadata={"json": "receive_id"})
    content = attr.ib(type=str, default=None, metadata={"json": "content"})
    msg_type = attr.ib(type=str, default=None, metadata={"json": "msg_type"})


@attr.s
class MessageReadUsersResult:
    items = attr.ib(type=List[ReadUser], default=None, metadata={"json": "items"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})


@attr.s
class MessageGetResult:
    items = attr.ib(type=List[Message], default=None, metadata={"json": "items"})


@attr.s
class ChatUpdatedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )
    after_change = attr.ib(
        type=ChatChange, default=None, metadata={"json": "after_change"}
    )
    before_change = attr.ib(
        type=ChatChange, default=None, metadata={"json": "before_change"}
    )
    moderator_list = attr.ib(
        type=ModeratorList, default=None, metadata={"json": "moderator_list"}
    )


@attr.s
class ChatUpdatedEvent(BaseEventV2):
    event = attr.ib(type=ChatUpdatedEventData, default=None)


@attr.s
class ChatDisbandedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )


@attr.s
class ChatDisbandedEvent(BaseEventV2):
    event = attr.ib(type=ChatDisbandedEventData, default=None)


@attr.s
class ChatMemberBotAddedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )


@attr.s
class ChatMemberBotAddedEvent(BaseEventV2):
    event = attr.ib(type=ChatMemberBotAddedEventData, default=None)


@attr.s
class ChatMemberBotDeletedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )


@attr.s
class ChatMemberBotDeletedEvent(BaseEventV2):
    event = attr.ib(type=ChatMemberBotDeletedEventData, default=None)


@attr.s
class ChatMemberUserAddedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )
    users = attr.ib(type=List[ChatMemberUser], default=None, metadata={"json": "users"})


@attr.s
class ChatMemberUserAddedEvent(BaseEventV2):
    event = attr.ib(type=ChatMemberUserAddedEventData, default=None)


@attr.s
class ChatMemberUserWithdrawnEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )
    users = attr.ib(type=List[ChatMemberUser], default=None, metadata={"json": "users"})


@attr.s
class ChatMemberUserWithdrawnEvent(BaseEventV2):
    event = attr.ib(type=ChatMemberUserWithdrawnEventData, default=None)


@attr.s
class ChatMemberUserDeletedEventData:
    chat_id = attr.ib(type=str, default=None, metadata={"json": "chat_id"})
    operator_id = attr.ib(type=UserId, default=None, metadata={"json": "operator_id"})
    external = attr.ib(type=bool, default=None, metadata={"json": "external"})
    operator_tenant_key = attr.ib(
        type=str, default=None, metadata={"json": "operator_tenant_key"}
    )
    users = attr.ib(type=List[ChatMemberUser], default=None, metadata={"json": "users"})


@attr.s
class ChatMemberUserDeletedEvent(BaseEventV2):
    event = attr.ib(type=ChatMemberUserDeletedEventData, default=None)


@attr.s
class MessageReceiveEventData:
    sender = attr.ib(type=EventSender, default=None, metadata={"json": "sender"})
    message = attr.ib(type=EventMessage, default=None, metadata={"json": "message"})


@attr.s
class MessageReceiveEvent(BaseEventV2):
    event = attr.ib(type=MessageReceiveEventData, default=None)


@attr.s
class MessageMessageReadEventData:
    reader = attr.ib(type=EventMessageReader, default=None, metadata={"json": "reader"})
    message_id_list = attr.ib(
        type=List[str], default=None, metadata={"json": "message_id_list"}
    )


@attr.s
class MessageMessageReadEvent(BaseEventV2):
    event = attr.ib(type=MessageMessageReadEventData, default=None)