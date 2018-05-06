from marshmallow import Schema
from marshmallow import pre_dump
from marshmallow.fields import String


class FullQuestionSchema(Schema):
    uuid = String()
    name = String()
    status = String()
    team = String()

    @pre_dump()
    def convert(self, data):
        (question, is_correct, ga) = data

        return {
            'uuid': question.uuid,
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
    team_uuid = String(required=True)
    answer_uuid = String(required=True)
