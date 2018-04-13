from marshmallow import Schema
from marshmallow.fields import Boolean
from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.validate import Length


class NewAnswerSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    description = String()
    index = Integer(required=True)
    is_correct = Boolean(required=True)


class AnswerSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    description = String()
    index = Integer(required=True)
    is_correct = Boolean(required=True)
    question_uuid = String(
        required=True,
        allow_none=False,
    )
