from typing import Any, Optional
from bson.objectid import ObjectId
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.group.models import Group
from graphql_api.resources.user.models import User
from graphql_api.resources.user_plan.models import UserPlan


# Khởi tạo query ObjectType
query = ObjectType("Query")


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


@query.field("user_plan")
async def resolve_user_plan(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[UserPlan]:
    """
    Hàm resolve user plan
    Tham số query:
        - user_plan_id: ObjectID dạng string

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if 'user_plan_id' in kwargs:
        return await UserPlan.find_one({'_id': ObjectId(
            kwargs['user_plan_id']
        )})

    else:
        return None
