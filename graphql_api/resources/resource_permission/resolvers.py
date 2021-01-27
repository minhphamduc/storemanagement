from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.resource.models import Resource
from graphql_api.resources.user.models import User
from graphql_api.resources.group.models import Group
from graphql_api.resources.tenant.models import Tenant


# Khởi tạo resource permission ObjectType
resource_permission = ObjectType("ResourcePermission")


# ResourcePermission resolver
@resource_permission.field("resource_permission_id")
async def resolve_resource_permission_id(obj: Any, info: GraphQLResolveInfo,
                                         **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve resource_permission_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj:
        json_data = obj.dump()
        if 'id' in json_data:
            return str(json_data['id'])

        return None

    return None


@resource_permission.field("resource_id")
async def resolve_resource_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Resource]:
    """
    Hàm resolve resource_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.resource_id:
        return await obj.resource_id.fetch()

    return None


@resource_permission.field("user_id")
async def resolve_user_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[User]:
    """
    Hàm resolve user_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.user_id:
        return await obj.user_id.fetch()

    return None


@resource_permission.field("group_id")
async def resolve_group_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Group]:
    """
    Hàm resolve group_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.group_id:
        return await obj.group_id.fetch()

    return None


@resource_permission.field("tenant_id")
async def resolve_tenant_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Tenant]:
    """
    Hàm resolve tenant_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.tenant_id:
        return await obj.tenant_id.fetch()

    return None
