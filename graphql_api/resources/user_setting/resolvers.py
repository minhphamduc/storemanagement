from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.user.models import User


# Khởi tạo user_setting ObjectType
user_setting = ObjectType("UserSetting")


# Setting resolver
@user_setting.field("user_setting_id")
async def resolve_user_setting_id(obj: Any, info: GraphQLResolveInfo,
                                  **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve user_setting_id

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


@user_setting.field("user_id")
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
