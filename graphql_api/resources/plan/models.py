from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE


# Đăng ký document Plan
@MONGO_INSTANCE.register
class Plan(Document):
    """
    Class: Plan
    Description: Lớp pricing plan
    """

    name = fields.StringField(required=True,
                              validate=[validate.Length(max=255),
                                        validate.Regexp(r"[a-zA-Z ']+")]
                              )
    max_facebook = fields.IntegerField(required=True,
                                       validate=validate.Range(min=1, max=10))
    max_instagram = fields.IntegerField(required=True,
                                        validate=validate.Range(min=1, max=10))
    max_tiki = fields.IntegerField(required=True,
                                   validate=validate.Range(min=1, max=10))
    max_lazada = fields.IntegerField(required=True,
                                     validate=validate.Range(min=1, max=10))
    max_shopee = fields.IntegerField(required=True,
                                     validate=validate.Range(min=1, max=10))
    period = fields.IntegerField(required=True,
                                 validate=validate.OneOf([1, 3, 6, 12]))

    class Meta:
        collection_name = "plan"
