from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.user.models import User


# Đăng ký document UserSetting
@MONGO_INSTANCE.register
class UserSetting(Document):
    """
    Class: UserSetting
    Description: Lớp user setting
    """

    key = fields.StringField(required=True,
                             validate=[validate.Length(max=255),
                                       validate.Regexp(r"[a-zA-Z ']+")]
                             )
    value = fields.StringField(required=True,
                               validate=[validate.Length(max=255),
                                         validate.Regexp(r"[a-zA-Z ']+")]
                               )
    user_id = fields.ReferenceField(required=True,
                                    document=User)

    class Meta:
        collection_name = "user_setting"
