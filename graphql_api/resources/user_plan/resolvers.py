from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.user.models import User


# Khởi tạo user plan ObjectType
user_plan = ObjectType("UserPlan")


# UserPlan resolver
@user_plan.field("user_plan_id")
async def resolve_user_plan_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[str]:
    """

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


@user_plan.field("user_id")
async def resolve_user_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[User]:
    """

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if obj and obj.user_id:
        return await obj.user_id.fetch()

    return None


@user_plan.field("plan_id")
async def resolve_plan_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Plan]:
    """

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if obj and obj.plan_id:
        return await obj.plan_id.fetch()

    return None
