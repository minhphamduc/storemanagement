from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE


# Đăng ký document Group
@MONGO_INSTANCE.register
class Group(Document):
    """
    Class: Group
    Description: Lớp group
    """

    name = fields.StringField(required=True,
                              validate=[validate.Length(max=255),
                                        validate.Regexp(r"[a-zA-Z ']+")]
                              )

    class Meta:
        collection_name = "group"
