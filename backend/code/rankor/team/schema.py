from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Length


class TeamSchema(Schema):
    uuid = String()
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
