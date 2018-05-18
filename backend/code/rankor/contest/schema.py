from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.validate import Length

from rankor.application.marshmellow import UUID


class ContestSchema(Schema):
    id = UUID()
    owner_id = UUID()
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
