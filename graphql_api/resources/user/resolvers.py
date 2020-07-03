from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.group.models import Group
from graphql_api.resources.user.models import User


# Khởi tạo user ObjectType
user = ObjectType("User")


# User resolver
@user.field("user_id")
async def resolve_user_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
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


@user.field("group_id")
async def resolve_group_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Group]:
    """

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if obj and obj.group_id:
        return await obj.group_id.fetch()

    return None


@user.field("root_id")
async def resolve_root_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[User]:
    """

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    if obj and obj.root_id:
        return await User.find_one({'_id': obj.root_id})

    return None
