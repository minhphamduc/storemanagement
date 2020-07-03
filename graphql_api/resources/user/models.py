from umongo import Document, fields, validate
from graphql_api.settings.connects import MONGO_INSTANCE
from graphql_api.resources.group.models import Group


# Đăng ký document User
@MONGO_INSTANCE.register
class User(Document):
    """
    Class: User
    Description: Lớp user
    """

    username = fields.StringField(required=True,
                                  validate=[validate.Length(max=255),
                                            validate.Regexp(r"[a-zA-Z0-9]+")]
                                  )
    password = fields.StringField(required=True,
                                  validate=[validate.Length(max=255),
                                            validate.Regexp(r"[a-zA-Z0-9]+")]
                                  )
    email = fields.EmailField(required=True,
                              validate=validate.Email())
    phone = fields.StringField(validate=[validate.Length(max=255),
                                         validate.Regexp(r"[0-9]+")]
                               )
    first_name = fields.StringField(validate=[validate.Length(max=255),
                                              validate.Regexp(r"[a-zA-Z ]+")]
                                    )
    last_name = fields.StringField(validate=[validate.Length(max=255),
                                             validate.Regexp(r"[a-zA-Z ]+")]
                                   )
    group_id = fields.ReferenceField(required=True,
                                     document=Group)
    root_id = fields.StringField(validate=[validate.Length(max=255),
                                           validate.Regexp(r"[a-zA-Z0-9]+")]
                                 )
    is_root = fields.BooleanField(required=True, default=False,
                                  validate=validate.OneOf([True, False]))

    class Meta:
        collection_name = "user"
