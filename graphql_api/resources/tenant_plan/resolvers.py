from typing import Any, Optional
from graphql.type import GraphQLResolveInfo
from ariadne import ObjectType
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.tenant.models import Tenant


# Khởi tạo tenant plan ObjectType
tenant_plan = ObjectType("TenantPlan")


# TenantPlan resolver
@tenant_plan.field("tenant_plan_id")
async def resolve_tenant_plan_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[str]:
    """
    Hàm resolve tenant_plan_id

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


@tenant_plan.field("plan_id")
async def resolve_plan_id(obj: Any, info: GraphQLResolveInfo, **kwargs) \
        -> Optional[Plan]:
    """
    Hàm resolve plan_id

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """

    if obj and obj.plan_id:
        return await obj.plan_id.fetch()

    return None


@tenant_plan.field("tenant_id")
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
