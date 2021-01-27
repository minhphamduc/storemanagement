from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.resource.models import Resource
from graphql_api.resources.user.models import User
from graphql_api.resources.group.models import Group
from graphql_api.resources.tenant.models import Tenant


# Đăng ký document ResourcePermission
@MONGO_INSTANCE.register
class ResourcePermission(Document):
    """
    Class: ResourcePermission
    Description: Lớp resource permission
    """
    resource_id = fields.ReferenceField(required=True,
                                        document=Resource)
    permission = fields.ListField(
        fields.StringField(required=True,
                           validate=validate.OneOf(['read', 'creat',
                                                    'update', 'delete'])
                           ),
        required=True)
    user_id = fields.ReferenceField(document=User)
    group_id = fields.ReferenceField(document=Group)
    tenant_id = fields.ReferenceField(document=Tenant)

    class Meta:
        collection_name = "resource_permission"
        dateformat = '%Y-%m-%dT%H:%M:%S+00:00'
