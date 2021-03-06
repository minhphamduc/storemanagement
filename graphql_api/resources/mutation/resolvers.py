from typing import Any, Dict, Union
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


# Khởi tạo mutation ObjectType
mutation = ObjectType("Mutation")


@mutation.field("createResource")
async def resolve_create_resource(obj: Any, info: GraphQLResolveInfo,
                                  **kwargs) \
        -> Dict[str, Union[bool, str, Resource]]:
    """
    Hàm resolve createResource

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        # Validate dữ liệu
        try:
            resource = Resource(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await resource.commit()
        if result:
            return {"status": True, "message": "Resource is created",
                    "data": resource}

        return {"status": False, "message": "Cannot create resource"}

    return {"status": False, "message": "Input is empty"}


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
        # Validate dữ liệu
        try:
            tenant = Tenant(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await tenant.commit()
        if result:
            return {"status": True, "message": "Tenant is created",
                    "data": tenant}

        return {"status": False, "message": "Cannot create tenant"}

    return {"status": False, "message": "Input is empty"}


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
        # Kiểm tra tenant_id
        if "tenant_id" in kwargs["input"].keys() \
                and kwargs["input"]["tenant_id"]:
            tenant = await Tenant.find_one(
                {'_id': ObjectId(kwargs["input"]["tenant_id"])}
            )
            if tenant is not None:
                kwargs["input"]["tenant_id"] = tenant

            # Trả lỗi nếu tenant không tồn tại
            else:
                return {"status": False, "message": "Tenant not found"}

        # Validate dữ liệu
        try:
            tenant_setting = TenantSetting(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await tenant_setting.commit()
        if result:
            return {"status": True, "message": "Tenant Setting is created",
                    "data": tenant_setting}

        return {"status": False, "message": "Cannot create tenant setting"}

    return {"status": False, "message": "Input is empty"}


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
        # Validate dữ liệu
        try:
            plan = Plan(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await plan.commit()
        if result:
            return {"status": True, "message": "Plan is created", "data": plan}

        return {"status": False, "message": "Cannot create plan"}

    return {"status": False, "message": "Input is empty"}


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
        # Kiểm tra plan_id
        if "plan_id" in kwargs["input"].keys() \
                and kwargs["input"]["plan_id"]:
            plan = await Plan.find_one(
                {'_id': ObjectId(kwargs["input"]["plan_id"])}
            )
            if plan is not None:
                kwargs["input"]["plan_id"] = plan

            # Trả lỗi nếu plan không tồn tại
            else:
                return {"status": False, "message": "Plan not found"}

        # Kiểm tra tenant_id
        if "tenant_id" in kwargs["input"].keys() \
                and kwargs["input"]["tenant_id"]:
            tenant = await Tenant.find_one(
                {'_id': ObjectId(kwargs["input"]["tenant_id"])}
            )
            if tenant is not None:
                kwargs["input"]["tenant_id"] = tenant

            # Trả lỗi nếu tenant không tồn tại
            else:
                return {"status": False, "message": "Tenant not found"}

        # Validate dữ liệu
        try:
            tenant_plan = TenantPlan(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await tenant_plan.commit()
        if result:
            return {"status": True, "message": "Tenant Plan is created",
                    "data": tenant_plan}

        return {"status": False, "message": "Cannot create tenant plan"}

    return {"status": False, "message": "Input is empty"}


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
        # Validate dữ liệu
        try:
            group = Group(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await group.commit()
        if result:
            return {"status": True, "message": "Group is created",
                    "data": group}

        return {"status": False, "message": "Cannot create group"}

    return {"status": False, "message": "Input is empty"}


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
        # Kiểm tra group_id
        if "group_id" in kwargs["input"].keys() \
                and kwargs["input"]["group_id"]:
            group = await Group.find_one(
                {'_id': ObjectId(kwargs["input"]["group_id"])}
            )
            if group is not None:
                kwargs["input"]["group_id"] = group

            # Trả lỗi nếu group không tồn tại
            else:
                return {"status": False, "message": "Group not found"}

        # Kiểm tra tenant_id
        if "tenant_id" in kwargs["input"].keys() \
                and kwargs["input"]["tenant_id"]:
            tenant = await Tenant.find_one(
                {'_id': ObjectId(kwargs["input"]["tenant_id"])}
            )
            if tenant is not None:
                kwargs["input"]["tenant_id"] = tenant

            # Trả lỗi nếu tenant không tồn tại
            else:
                return {"status": False, "message": "Tenant not found"}

        # Validate dữ liệu
        try:
            user = User(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await user.commit()
        if result:
            return {"status": True, "message": "User is created",
                    "data": user}

        return {"status": False, "message": "Cannot create user"}

    return {"status": False, "message": "Input is empty"}


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
        # Kiểm tra user_id
        if "user_id" in kwargs["input"].keys() \
                and kwargs["input"]["user_id"]:
            user = await User.find_one(
                {'_id': ObjectId(kwargs["input"]["user_id"])}
            )
            if user is not None:
                kwargs["input"]["user_id"] = user

            # Trả lỗi nếu user không tồn tại
            else:
                return {"status": False, "message": "User not found"}

        # Validate dữ liệu
        try:
            user_setting = UserSetting(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await user_setting.commit()
        if result:
            return {"status": True, "message": "User Setting is created",
                    "data": user_setting}

        return {"status": False, "message": "Cannot create user setting"}

    return {"status": False, "message": "Input is empty"}


@mutation.field("createResourcePermission")
async def resolve_create_resource_permission(obj: Any,
                                             info: GraphQLResolveInfo,
                                             **kwargs) \
        -> Dict[str, Union[bool, str, ResourcePermission]]:
    """
    Hàm resolve createResourcePermission

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if kwargs and "input" in kwargs:
        # Kiểm tra resource_id
        if "resource_id" in kwargs["input"].keys() \
                and kwargs["input"]["resource_id"]:
            resource = await Resource.find_one(
                {'_id': ObjectId(kwargs["input"]["resource_id"])}
            )
            if resource is not None:
                kwargs["input"]["resource_id"] = resource

            # Trả lỗi nếu resource không tồn tại
            else:
                return {"status": False, "message": "Resource not found"}

        # Kiểm tra user_id
        if "user_id" in kwargs["input"].keys() \
                and kwargs["input"]["user_id"]:
            user = await User.find_one(
                {'_id': ObjectId(kwargs["input"]["user_id"])}
            )
            if user is not None:
                kwargs["input"]["user_id"] = user

            # Trả lỗi nếu user không tồn tại
            else:
                return {"status": False, "message": "User not found"}

        # Kiểm tra group_id
        if "group_id" in kwargs["input"].keys() \
                and kwargs["input"]["group_id"]:
            group = await Group.find_one(
                {'_id': ObjectId(kwargs["input"]["group_id"])}
            )
            if group is not None:
                kwargs["input"]["group_id"] = group

            # Trả lỗi nếu group không tồn tại
            else:
                return {"status": False, "message": "Group not found"}

        # Kiểm tra tenant_id
        if "tenant_id" in kwargs["input"].keys() \
                and kwargs["input"]["tenant_id"]:
            tenant = await Tenant.find_one(
                {'_id': ObjectId(kwargs["input"]["tenant_id"])}
            )
            if tenant is not None:
                kwargs["input"]["tenant_id"] = tenant

            # Trả lỗi nếu tenant không tồn tại
            else:
                return {"status": False, "message": "Tenant not found"}

        # Validate dữ liệu
        try:
            resource_permission = ResourcePermission(**kwargs["input"])

        except TypeError:
            return {"status": False, "message": "Invalid input"}

        result = await resource_permission.commit()
        if result:
            return {"status": True, "message": "Resource Permission is created",
                    "data": resource_permission}

        return {"status": False, "message": "Cannot create resource permission"}

    return {"status": False, "message": "Input is empty"}
