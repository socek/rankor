from marshmallow import Schema
from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.validate import Length


class GameSchema(Schema):
    uuid = String()
    contest_uuid = String()
    owner_id = Integer()
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
