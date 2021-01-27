from typing import Any, Optional
from bson.objectid import ObjectId
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.group.models import Group
from graphql_api.resources.user.models import User
from graphql_api.resources.tenant.models import Tenant
from graphql_api.resources.tenant_setting.models import TenantSetting
from graphql_api.resources.tenant_plan.models import TenantPlan
from graphql_api.resources.user_setting.models import UserSetting
from graphql_api.resources.resource.models import Resource
from graphql_api.resources.resource_permission.models import ResourcePermission


# Khởi tạo query ObjectType
query = ObjectType("Query")


@query.field("resource")
async def resolve_resource(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Resource]:
    """
    Hàm resolve resource
    Tham số query:
        - resource_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'resource_id' in kwargs:
        return await Resource.find_one({'_id': ObjectId(
            kwargs['resource_id']
        )})

    else:
        return None


@query.field("tenant")
async def resolve_tenant(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Tenant]:
    """
    Hàm resolve tenant
    Tham số query:
        - tenant_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'tenant_id' in kwargs:
        return await Tenant.find_one({'_id': ObjectId(kwargs['tenant_id'])})

    else:
        return None


@query.field("tenant_setting")
async def resolve_tenant_setting(obj: Any, info: GraphQLResolveInfo,
                                 **kwargs) \
        -> Optional[TenantSetting]:
    """
    Hàm resolve tenant setting
    Tham số query:
        - tenant_setting_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'tenant_setting_id' in kwargs:
        return await TenantSetting.find_one(
            {'_id': ObjectId(kwargs['tenant_setting_id'])}
        )

    else:
        return None


@query.field("plan")
async def resolve_plan(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Plan]:
    """
    Hàm resolve plan
    Tham số query:
        - plan_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'plan_id' in kwargs:
        return await Plan.find_one({'_id': ObjectId(kwargs['plan_id'])})

    else:
        return None


@query.field("tenant_plan")
async def resolve_tenant_plan(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[TenantPlan]:
    """
    Hàm resolve tenant plan
    Tham số query:
        - tenant_plan_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'tenant_plan_id' in kwargs:
        return await TenantPlan.find_one({'_id': ObjectId(
            kwargs['tenant_plan_id']
        )})

    else:
        return None


@query.field("group")
async def resolve_group(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Group]:
    """
    Hàm resolve group
    Tham số query:
        - group_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'group_id' in kwargs:
        return await Group.find_one({'_id': ObjectId(kwargs['group_id'])})

    else:
        return None


@query.field("user")
async def resolve_user(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[User]:
    """
    Hàm resolve user
    Tham số query:
        - user_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'user_id' in kwargs:
        return await User.find_one({'_id': ObjectId(kwargs['user_id'])})

    else:
        return None


@query.field("user_setting")
async def resolve_user_setting(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[UserSetting]:
    """
    Hàm resolve user_setting
    Tham số query:
        - user_setting_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'user_setting_id' in kwargs:
        return await UserSetting.find_one({'_id': ObjectId(
            kwargs['user_setting_id']
        )})

    else:
        return None


@query.field("resource_permission")
async def resolve_resource_permission(obj: Any, info: GraphQLResolveInfo,
                                      **kwargs) \
        -> Optional[ResourcePermission]:
    """
    Hàm resolve resource_permission
    Tham số query:
        - resource_permission_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if 'resource_permission_id' in kwargs:
        return await ResourcePermission.find_one({'_id': ObjectId(
            kwargs['resource_permission_id']
        )})

    else:
        return None
