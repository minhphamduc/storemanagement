from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.tenant.models import Tenant


# Đăng ký document TenantSetting
@MONGO_INSTANCE.register
class TenantSetting(Document):
    """
    Class: TenantSetting
    Description: Lớp tenant setting
    """

    key = fields.StringField(required=True,
                             validate=[validate.Length(max=255),
                                       validate.Regexp(r"[a-zA-Z ']+")]
                             )
    value = fields.StringField(required=True,
                               validate=[validate.Length(max=255),
                                         validate.Regexp(r"[a-zA-Z ']+")]
                               )
    tenant_id = fields.ReferenceField(required=True,
                                      document=Tenant)

    class Meta:
        collection_name = "tenant_setting"
