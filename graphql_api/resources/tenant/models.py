from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.tenant_plan.models import TenantPlan


# Đăng ký document Tenant
@MONGO_INSTANCE.register
class Tenant(Document):
    """
    Class: Tenant
    Description: Lớp tenant
    """
    name = fields.StringField(required=True,
                              validate=[validate.Length(max=255),
                                        validate.Regexp(r"[a-zA-Z ]+")]
                              )
    description = fields.StringField(validate=[validate.Length(max=255),
                                               validate.Regexp(r"[a-zA-Z ]+")])

    class Meta:
        collection_name = "tenant"
        dateformat = '%Y-%m-%dT%H:%M:%S+00:00'
