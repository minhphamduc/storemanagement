from typing import Any, Dict, Union
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.group.models import Group
from graphql_api.resources.user.models import User
from graphql_api.resources.user_plan.models import UserPlan


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
            return {"status": True, "message": "Plan is created", "plan": plan}

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
                    "group": group}

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
                    "user": user}

        return {"status": False, "message": "Cannot create user"}

    return {"status": False, "message": "Invalid input"}


@mutation.field("createUserPlan")
async def resolve_create_user(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Dict[str, Union[bool, str, UserPlan]]:
    """
    Hàm resolve createUserPlan

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if kwargs and "input" in kwargs:
        user_plan = UserPlan(**kwargs["input"])
        result = await user_plan.commit()
        if result:
            return {"status": True, "message": "User Plan is created",
                    "user_plan": user_plan}

        return {"status": False, "message": "Cannot create user plan"}

    return {"status": False, "message": "Invalid input"}
