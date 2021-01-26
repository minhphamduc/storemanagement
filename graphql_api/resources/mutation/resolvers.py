from typing import Any, Dict, Union
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.group.models import Group
from graphql_api.resources.user.models import User
from graphql_api.resources.tenant.models import Tenant
from graphql_api.resources.tenant_setting.models import TenantSetting
from graphql_api.resources.tenant_plan.models import TenantPlan
from graphql_api.resources.user_setting.models import UserSetting


# Khởi tạo mutation ObjectType
mutation = ObjectType("Mutation")


@mutation.field("createPlan")
async def resolve_create_plan(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Dict[str, Union[bool, str, Plan]]:
    """
    Hàm resolve createPlan

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        plan = Plan(**kwargs["input"])
        result = await plan.commit()
        if result:
            return {"status": True, "message": "Plan is created", "data": plan}

        return {"status": False, "message": "Cannot create plan"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createGroup")
async def resolve_create_group(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Dict[str, Union[bool, str, Group]]:
    """
    Hàm resolve createGroup

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        group = Group(**kwargs["input"])
        result = await group.commit()
        if result:
            return {"status": True, "message": "Group is created",
                    "data": group}

        return {"status": False, "message": "Cannot create group"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createUser")
async def resolve_create_user(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Dict[str, Union[bool, str, User]]:
    """
    Hàm resolve createUser

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        user = User(**kwargs["input"])
        result = await user.commit()
        if result:
            return {"status": True, "message": "User is created",
                    "data": user}

        return {"status": False, "message": "Cannot create user"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createUserSetting")
async def resolve_create_user_setting(obj: Any,
                                      info: GraphQLResolveInfo,
                                      **kwargs) -> Dict[str,
                                                        Union[bool, str,
                                                              UserSetting]]:
    """
    Hàm resolve createUserSetting

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        user_setting = UserSetting(**kwargs["input"])
        result = await user_setting.commit()
        if result:
            return {"status": True, "message": "User Setting is created",
                    "data": user_setting}

        return {"status": False, "message": "Cannot create user setting"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createTenant")
async def resolve_create_tenant(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Dict[str, Union[bool, str, Tenant]]:
    """
    Hàm resolve createTenant

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        tenant = Tenant(**kwargs["input"])
        result = await tenant.commit()
        if result:
            return {"status": True, "message": "Tenant is created",
                    "data": tenant}

        return {"status": False, "message": "Cannot create tenant"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createTenantSetting")
async def resolve_create_tenant_setting(obj: Any, info: GraphQLResolveInfo,
                                        **kwargs) \
        -> Dict[str, Union[bool, str, TenantSetting]]:
    """
    Hàm resolve createTenantSetting

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        tenant_setting = TenantSetting(**kwargs["input"])
        result = await tenant_setting.commit()
        if result:
            return {"status": True, "message": "Tenant Setting is created",
                    "data": tenant_setting}

        return {"status": False, "message": "Cannot create tenant user_setting"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createTenantPlan")
async def resolve_create_tenant_plan(obj: Any, info: GraphQLResolveInfo,
                                     **kwargs) \
        -> Dict[str, Union[bool, str, TenantPlan]]:
    """
    Hàm resolve createTenantPlan

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        tenant_plan = TenantPlan(**kwargs["input"])
        result = await tenant_plan.commit()
        if result:
            return {"status": True, "message": "Tenant Plan is created",
                    "data": tenant_plan}

        return {"status": False, "message": "Cannot create tenant plan"}

    return {"status": False, "message": "Invalid input"}
