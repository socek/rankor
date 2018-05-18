from marshmallow import Schema
from marshmallow.fields import String

from rankor.application.marshmellow import UUID


class GameViewSchema(Schema):
    view = String()
    team_name = String(allow_none=True)
    question_id = UUID(allow_none=True)
    answer_id = UUID(allow_none=True)
