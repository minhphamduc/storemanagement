from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType


# Khởi tạo plan ObjectType
plan = ObjectType("Plan")


# Plan resolver
@plan.field("plan_id")
async def resolve_plan_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve plan_id

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
