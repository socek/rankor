from marshmallow import Schema
from marshmallow import pre_dump
from marshmallow.fields import String


class FullQuestionSchema(Schema):
    id = String()
    name = String()
    status = String()
    team = String()

    @pre_dump()
    def convert(self, data):
        (question, is_correct, ga) = data

        return {
            'id': question.id.hex,
            'name': question.name,
            'status': self._get_status(is_correct),
            'team': self._get_team(ga)
        }

    def _get_status(self, is_correct):
        if is_correct is None:
            return 'not started'
        elif is_correct is True:
            return 'correct'
        else:
            return 'incorrect'

    def _get_team(self, ga):
        if ga and ga.team:
            return ga.team.name


class AnswerPostSchema(Schema):
    team_id = String()
    answer_id = String()
