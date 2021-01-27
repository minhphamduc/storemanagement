from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType


# Khởi tạo resource ObjectType
resource = ObjectType("Resource")


# Resource resolver
@resource.field("resource_id")
async def resolve_resource_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve resource_id

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
