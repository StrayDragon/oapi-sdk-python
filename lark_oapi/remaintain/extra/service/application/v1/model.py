# Code generated by lark suite oapi sdk gen

from typing import List, Dict
from ....utils.dt import to_json_decorator
from ....event.model.event import *
import attr


@to_json_decorator
@attr.s
class Application:
    pass


@to_json_decorator
@attr.s
class UserId:
    open_id = attr.ib(type=str, default=None, metadata={"json": "open_id"})
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})


@attr.s
class AppOpenEventData:
    app_id = attr.ib(type=str, default=None, metadata={"json": "app_id"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    applicants = attr.ib(
        type=List[UserId], default=None, metadata={"json": "applicants"}
    )
    installer = attr.ib(type=UserId, default=None, metadata={"json": "installer"})


@attr.s
class AppOpenEvent(BaseEvent):
    event = attr.ib(type=AppOpenEventData, default=None)


@attr.s
class AppStatusChangeEventData:
    app_id = attr.ib(type=str, default=None, metadata={"json": "app_id"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    status = attr.ib(type=str, default=None, metadata={"json": "status"})


@attr.s
class AppStatusChangeEvent(BaseEvent):
    event = attr.ib(type=AppStatusChangeEventData, default=None)


@attr.s
class AppUninstalledEventData:
    app_id = attr.ib(type=str, default=None, metadata={"json": "app_id"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})


@attr.s
class AppUninstalledEvent(BaseEvent):
    event = attr.ib(type=AppUninstalledEventData, default=None)


@attr.s
class OrderPaidEventData:
    app_id = attr.ib(type=str, default=None, metadata={"json": "app_id"})
    tenant_key = attr.ib(type=str, default=None, metadata={"json": "tenant_key"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    order_id = attr.ib(type=str, default=None, metadata={"json": "order_id"})
    price_plan_id = attr.ib(type=str, default=None, metadata={"json": "price_plan_id"})
    price_plan_type = attr.ib(
        type=str, default=None, metadata={"json": "price_plan_type"}
    )
    seats = attr.ib(type=int, default=None, metadata={"json": "seats"})
    buy_count = attr.ib(type=int, default=None, metadata={"json": "buy_count"})
    create_time = attr.ib(type=str, default=None, metadata={"json": "create_time"})
    pay_time = attr.ib(type=str, default=None, metadata={"json": "pay_time"})
    buy_type = attr.ib(type=str, default=None, metadata={"json": "buy_type"})
    src_order_id = attr.ib(type=str, default=None, metadata={"json": "src_order_id"})
    order_pay_price = attr.ib(
        type=int, default=None, metadata={"json": "order_pay_price"}
    )


@attr.s
class OrderPaidEvent(BaseEvent):
    event = attr.ib(type=OrderPaidEventData, default=None)
