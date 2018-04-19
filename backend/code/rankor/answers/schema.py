from marshmallow import Schema
from marshmallow.fields import Boolean
from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.validate import Length


class AnswerSchema(Schema):
    id = Integer()
    uuid = String()
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    description = String()
    is_correct = Boolean(required=True)
    question_uuid = String(
        allow_none=False,
    )
