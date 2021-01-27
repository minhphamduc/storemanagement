from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType


# Khởi tạo tenant ObjectType
tenant = ObjectType("Tenant")


# Tenant resolver
@tenant.field("tenant_id")
async def resolve_tenant_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve tenant_id

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
