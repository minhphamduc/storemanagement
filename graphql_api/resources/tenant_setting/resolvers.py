from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.tenant.models import Tenant


# Khởi tạo tenant setting ObjectType
tenant_setting = ObjectType("TenantSetting")


# Setting resolver
@tenant_setting.field("tenant_setting_id")
async def resolve_tenant_setting_id(obj: Any, info: GraphQLResolveInfo,
                                    **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve tenant_setting_id

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


@tenant_setting.field("tenant_id")
async def resolve_tenant_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Tenant]:
    """
    Hàm resolve tenant_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.tenant_id:
        return await obj.tenant_id.fetch()

    return None
