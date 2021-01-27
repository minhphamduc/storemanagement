from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE


# Đăng ký document Resource
@MONGO_INSTANCE.register
class Resource(Document):
    """
    Class: Resource
    Description: Lớp resource
    """

    name = fields.StringField(required=True,
                              validate=[validate.Length(max=255),
                                        validate.Regexp(r"[a-zA-Z ']+")]
                              )

    class Meta:
        collection_name = "resource"
