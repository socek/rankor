from marshmallow import Schema
from marshmallow.fields import String


class GameViewSchema(Schema):
    view = String()
    team_name = String(allow_none=True)
    question_id = String(allow_none=True)
    answer_id = String(allow_none=True)
