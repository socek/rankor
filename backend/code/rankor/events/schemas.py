from marshmallow import Schema
from marshmallow.fields import Dict
from marshmallow.fields import Nested
from marshmallow.fields import String

from rankor.application.marshmellow import UUID


class ScreenSchema(Schema):
    id = UUID()
    question_id = UUID()
    answer_id = UUID()
    team_id = UUID()
    game_answer_id = UUID()
    view = String()


class CommandSchema(Schema):
    name = String()
    data = Dict()


class ChangeViewCommandSchema(CommandSchema):
    class ChangeView(Schema):
        view = String()

    data = Nested(ChangeView)


class ShowQuestionCommandSchema(CommandSchema):
    class ShowQuestion(Schema):
        view = String()
        question_id = UUID()
        team_id = UUID()
        answer_id = UUID(allow_none=True)

    data = Nested(ShowQuestion)


class AttachTeamCommandSchema(CommandSchema):
    class AttachTeam(Schema):
        view = String()
        team_id = UUID()

    data = Nested(AttachTeam)


class SelectAnswerCommandSchema(CommandSchema):
    class SelectAnswer(Schema):
        view = String()
        answer_id = UUID()

    data = Nested(SelectAnswer)
