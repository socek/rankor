from marshmallow import Schema
from marshmallow.fields import Integer
from marshmallow.fields import String
from marshmallow.validate import Length


class NewQuestionSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    description = String()
    index = Integer(required=True)
    category = String()


class QuestionSchema(Schema):
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    description = String()
    index = Integer(required=True)
    category = String()
    contest_uuid = String(
        required=True,
        allow_none=False,
    )
