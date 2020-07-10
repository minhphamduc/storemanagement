from marshmallow import Schema, fields
import datetime


class MyDateTimeField(fields.DateTime):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.datetime):
            return value
        return super()._deserialize(value, attr, data)


class SomeSchema(Schema):
    element = MyDateTimeField()


def test_datetime_loading_accepts_datetime_object():
    schema = SomeSchema(strict=True)
    resp = schema.load({"element": datetime.datetime.now()})
    return resp
