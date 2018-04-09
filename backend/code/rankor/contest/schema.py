from marshmallow import Schema
from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.validate import Length


class NewContestSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )


class ContestSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    owner_id = Integer()
    uuid = String()
