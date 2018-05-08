from marshmallow import Schema
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
    category = String()


class QuestionSchema(NewQuestionSchema):
    uuid = String()
    contest_uuid = String(
        required=True,
        allow_none=False,
    )
    team = String()
    category = String()
