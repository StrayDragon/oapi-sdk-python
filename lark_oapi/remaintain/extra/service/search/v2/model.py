# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr


@to_json_decorator
@attr.s
class SchemaDisplayOption:
    display_label = attr.ib(type=str, default=None, metadata={"json": "display_label"})
    display_type = attr.ib(type=str, default=None, metadata={"json": "display_type"})


@to_json_decorator
@attr.s
class SchemaPropertyDefinition:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    is_returnable = attr.ib(type=bool, default=None, metadata={"json": "is_returnable"})
    is_repeatable = attr.ib(type=bool, default=None, metadata={"json": "is_repeatable"})
    is_sortable = attr.ib(type=bool, default=None, metadata={"json": "is_sortable"})
    is_facetable = attr.ib(type=bool, default=None, metadata={"json": "is_facetable"})
    is_wildcard_searchable = attr.ib(
        type=bool, default=None, metadata={"json": "is_wildcard_searchable"}
    )
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    display_options = attr.ib(
        type=SchemaDisplayOption, default=None, metadata={"json": "display_options"}
    )


@to_json_decorator
@attr.s
class Schema:
    property_definitions = attr.ib(
        type=List[SchemaPropertyDefinition],
        default=None,
        metadata={"json": "property_definitions"},
    )
    id = attr.ib(type=str, default=None, metadata={"json": "id"})


@to_json_decorator
@attr.s
class ItemMetadata:
    title = attr.ib(type=str, default=None, metadata={"json": "title"})
    source_url = attr.ib(type=str, default=None, metadata={"json": "source_url"})
    create_time = attr.ib(type=int, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=int, default=None, metadata={"json": "update_time"})


@to_json_decorator
@attr.s
class ItemContent:
    format = attr.ib(type=str, default=None, metadata={"json": "format"})
    content_data = attr.ib(type=str, default=None, metadata={"json": "content_data"})


@to_json_decorator
@attr.s
class Acl:
    access = attr.ib(type=str, default=None, metadata={"json": "access"})
    value = attr.ib(type=str, default=None, metadata={"json": "value"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})


@to_json_decorator
@attr.s
class Item:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    acl = attr.ib(type=List[Acl], default=None, metadata={"json": "acl"})
    metadata = attr.ib(type=ItemMetadata, default=None, metadata={"json": "metadata"})
    structured_data = attr.ib(
        type=str, default=None, metadata={"json": "structured_data"}
    )
    content = attr.ib(type=ItemContent, default=None, metadata={"json": "content"})
    field_acl = attr.ib(type=str, default=None, metadata={"json": "field_acl"})


@to_json_decorator
@attr.s
class ConnectDataSource:
    service_url = attr.ib(type=str, default=None, metadata={"json": "service_url"})
    project_name = attr.ib(type=str, default=None, metadata={"json": "project_name"})
    display_name = attr.ib(type=str, default=None, metadata={"json": "display_name"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    icon_url = attr.ib(type=str, default=None, metadata={"json": "icon_url"})
    project_description = attr.ib(
        type=str, default=None, metadata={"json": "project_description"}
    )
    contact_email = attr.ib(type=str, default=None, metadata={"json": "contact_email"})
    tenant_name = attr.ib(type=str, default=None, metadata={"json": "tenant_name"})


@to_json_decorator
@attr.s
class DataSource:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    state = attr.ib(type=int, default=None, metadata={"json": "state"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})
    create_time = attr.ib(type=str, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=str, default=None, metadata={"json": "update_time"})
    is_exceed_quota = attr.ib(
        type=bool, default=None, metadata={"json": "is_exceed_quota"}
    )
    icon_url = attr.ib(type=str, default=None, metadata={"json": "icon_url"})
    template = attr.ib(type=str, default=None, metadata={"json": "template"})


@attr.s
class DataSourceCreateResult:
    data_source = attr.ib(
        type=DataSource, default=None, metadata={"json": "data_source"}
    )


@attr.s
class DataSourceGetResult:
    data_source = attr.ib(
        type=DataSource, default=None, metadata={"json": "data_source"}
    )


@attr.s
class DataSourceListResult:
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    items = attr.ib(type=List[DataSource], default=None, metadata={"json": "items"})


@to_json_decorator
@attr.s
class DataSourcePatchReqBody:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    state = attr.ib(type=int, default=None, metadata={"json": "state"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})


@attr.s
class DataSourcePatchResult:
    data_source = attr.ib(
        type=DataSource, default=None, metadata={"json": "data_source"}
    )


@attr.s
class DataSourceItemGetResult:
    item = attr.ib(type=Item, default=None, metadata={"json": "item"})
