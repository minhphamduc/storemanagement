from ariadne import ScalarType


# Datetime scalar
datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()
