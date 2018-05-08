from marshmallow import Schema
from marshmallow.fields import String


class GameViewSchema(Schema):
    view = String()
    question_uuid = String()
    team_name = String()
    answer_uuid = String()
