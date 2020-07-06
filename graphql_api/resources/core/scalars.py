from ariadne import ScalarType


# Datetime scalar
datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime(value) -> str:
    """
    Hàm serialize giá trị value từ datetime sang string

    :param value:
    :return:
    """
    return value.isoformat()
