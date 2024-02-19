# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .avatar_info import AvatarInfo
from .department_detail import DepartmentDetail
from .user_assign_info import UserAssignInfo
from .user_custom_attr import UserCustomAttr
from .user_order import UserOrder
from .user_status import UserStatus


class User(object):
    _types = {
        "union_id": str,
        "user_id": str,
        "open_id": str,
        "name": str,
        "en_name": str,
        "nickname": str,
        "email": str,
        "mobile": str,
        "mobile_visible": bool,
        "gender": int,
        "avatar_key": str,
        "avatar": AvatarInfo,
        "status": UserStatus,
        "department_ids": List[str],
        "leader_user_id": str,
        "city": str,
        "country": str,
        "work_station": str,
        "join_time": int,
        "is_tenant_manager": bool,
        "employee_no": str,
        "employee_type": int,
        "orders": List[UserOrder],
        "custom_attrs": List[UserCustomAttr],
        "enterprise_email": str,
        "job_title": str,
        "is_frozen": bool,
        "geo": str,
        "job_level_id": str,
        "job_family_id": str,
        "subscription_ids": List[int],
        "assign_info": List[UserAssignInfo],
        "department_path": List[DepartmentDetail],
        "dotted_line_leader_user_ids": List[int],
    }

    def __init__(self, d=None):
        self.union_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.open_id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.nickname: Optional[str] = None
        self.email: Optional[str] = None
        self.mobile: Optional[str] = None
        self.mobile_visible: Optional[bool] = None
        self.gender: Optional[int] = None
        self.avatar_key: Optional[str] = None
        self.avatar: Optional[AvatarInfo] = None
        self.status: Optional[UserStatus] = None
        self.department_ids: Optional[List[str]] = None
        self.leader_user_id: Optional[str] = None
        self.city: Optional[str] = None
        self.country: Optional[str] = None
        self.work_station: Optional[str] = None
        self.join_time: Optional[int] = None
        self.is_tenant_manager: Optional[bool] = None
        self.employee_no: Optional[str] = None
        self.employee_type: Optional[int] = None
        self.orders: Optional[List[UserOrder]] = None
        self.custom_attrs: Optional[List[UserCustomAttr]] = None
        self.enterprise_email: Optional[str] = None
        self.job_title: Optional[str] = None
        self.is_frozen: Optional[bool] = None
        self.geo: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.subscription_ids: Optional[List[int]] = None
        self.assign_info: Optional[List[UserAssignInfo]] = None
        self.department_path: Optional[List[DepartmentDetail]] = None
        self.dotted_line_leader_user_ids: Optional[List[int]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserBuilder":
        return UserBuilder()


class UserBuilder(object):
    def __init__(self) -> None:
        self._user = User()

    def union_id(self, union_id: str) -> "UserBuilder":
        self._user.union_id = union_id
        return self

    def user_id(self, user_id: str) -> "UserBuilder":
        self._user.user_id = user_id
        return self

    def open_id(self, open_id: str) -> "UserBuilder":
        self._user.open_id = open_id
        return self

    def name(self, name: str) -> "UserBuilder":
        self._user.name = name
        return self

    def en_name(self, en_name: str) -> "UserBuilder":
        self._user.en_name = en_name
        return self

    def nickname(self, nickname: str) -> "UserBuilder":
        self._user.nickname = nickname
        return self

    def email(self, email: str) -> "UserBuilder":
        self._user.email = email
        return self

    def mobile(self, mobile: str) -> "UserBuilder":
        self._user.mobile = mobile
        return self

    def mobile_visible(self, mobile_visible: bool) -> "UserBuilder":
        self._user.mobile_visible = mobile_visible
        return self

    def gender(self, gender: int) -> "UserBuilder":
        self._user.gender = gender
        return self

    def avatar_key(self, avatar_key: str) -> "UserBuilder":
        self._user.avatar_key = avatar_key
        return self

    def avatar(self, avatar: AvatarInfo) -> "UserBuilder":
        self._user.avatar = avatar
        return self

    def status(self, status: UserStatus) -> "UserBuilder":
        self._user.status = status
        return self

    def department_ids(self, department_ids: List[str]) -> "UserBuilder":
        self._user.department_ids = department_ids
        return self

    def leader_user_id(self, leader_user_id: str) -> "UserBuilder":
        self._user.leader_user_id = leader_user_id
        return self

    def city(self, city: str) -> "UserBuilder":
        self._user.city = city
        return self

    def country(self, country: str) -> "UserBuilder":
        self._user.country = country
        return self

    def work_station(self, work_station: str) -> "UserBuilder":
        self._user.work_station = work_station
        return self

    def join_time(self, join_time: int) -> "UserBuilder":
        self._user.join_time = join_time
        return self

    def is_tenant_manager(self, is_tenant_manager: bool) -> "UserBuilder":
        self._user.is_tenant_manager = is_tenant_manager
        return self

    def employee_no(self, employee_no: str) -> "UserBuilder":
        self._user.employee_no = employee_no
        return self

    def employee_type(self, employee_type: int) -> "UserBuilder":
        self._user.employee_type = employee_type
        return self

    def orders(self, orders: List[UserOrder]) -> "UserBuilder":
        self._user.orders = orders
        return self

    def custom_attrs(self, custom_attrs: List[UserCustomAttr]) -> "UserBuilder":
        self._user.custom_attrs = custom_attrs
        return self

    def enterprise_email(self, enterprise_email: str) -> "UserBuilder":
        self._user.enterprise_email = enterprise_email
        return self

    def job_title(self, job_title: str) -> "UserBuilder":
        self._user.job_title = job_title
        return self

    def is_frozen(self, is_frozen: bool) -> "UserBuilder":
        self._user.is_frozen = is_frozen
        return self

    def geo(self, geo: str) -> "UserBuilder":
        self._user.geo = geo
        return self

    def job_level_id(self, job_level_id: str) -> "UserBuilder":
        self._user.job_level_id = job_level_id
        return self

    def job_family_id(self, job_family_id: str) -> "UserBuilder":
        self._user.job_family_id = job_family_id
        return self

    def subscription_ids(self, subscription_ids: List[int]) -> "UserBuilder":
        self._user.subscription_ids = subscription_ids
        return self

    def assign_info(self, assign_info: List[UserAssignInfo]) -> "UserBuilder":
        self._user.assign_info = assign_info
        return self

    def department_path(self, department_path: List[DepartmentDetail]) -> "UserBuilder":
        self._user.department_path = department_path
        return self

    def dotted_line_leader_user_ids(self, dotted_line_leader_user_ids: List[int]) -> "UserBuilder":
        self._user.dotted_line_leader_user_ids = dotted_line_leader_user_ids
        return self

    def build(self) -> "User":
        return self._user
