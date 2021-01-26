from umongo import Document, fields
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.plan.models import Plan
from graphql_api.resources.tenant.models import Tenant


# Đăng ký document TenantPlan
@MONGO_INSTANCE.register
class TenantPlan(Document):
    """
    Class: TenantPlan
    Description: Lớp tenant plan
    """
    plan_id = fields.ReferenceField(required=True,
                                    document=Plan)
    tenant_id = fields.ReferenceField(required=True,
                                      document=Tenant)
    start_at = fields.DateTimeField(required=True)
    expire_at = fields.DateTimeField(required=True)

    class Meta:
        collection_name = "tenant_plan"
        dateformat = '%Y-%m-%dT%H:%M:%S+00:00'
