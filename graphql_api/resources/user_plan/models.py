from umongo import Document, fields
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.user.models import User
from graphql_api.resources.plan.models import Plan


# Đăng ký document UserPan
@MONGO_INSTANCE.register
class UserPlan(Document):
    """
    Class: UserPan
    Description: Lớp user plan
    """
    user_id = fields.ReferenceField(required=True,
                                    document=User)
    plan_id = fields.ReferenceField(required=True,
                                    document=Plan)
    start_ad = fields.DateTimeField(required=True)
    expire_at = fields.DateTimeField(required=True)

    class Meta:
        collection_name = "user_plan"
        dateformat = '%Y-%m-%dT%H:%M:%S+00:00'
