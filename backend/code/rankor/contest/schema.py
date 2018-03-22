from marshmallow import Schema
from marshmallow.fields import Integer
from marshmallow.fields import String


class ContestSchema(Schema):
    name = String(required=True)
    owner_id = Integer()
