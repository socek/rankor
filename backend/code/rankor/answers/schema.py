from marshmallow import Schema
from marshmallow.fields import Boolean
from marshmallow.fields import String
from marshmallow.validate import Length

from rankor.application.marshmellow import UUID


class AnswerSchema(Schema):
    id = UUID()
    name = String(
        required=True,
        allow_none=False,
        validate=[
            Length(min=4, error="Name must have at lest {min} characters.")
        ],
    )
    is_correct = Boolean(required=True)
    question_id = UUID(allow_none=False, )
