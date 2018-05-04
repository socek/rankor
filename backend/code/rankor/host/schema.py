from marshmallow import Schema
from marshmallow import pre_dump
from marshmallow.fields import String


class FullQuestionSchema(Schema):
    uuid = String()
    name = String()
    status = String()

    @pre_dump()
    def convert(self, data):
        (question, is_correct) = data
        return {
            'uuid': question.uuid,
            'name': question.name,
            'status': self._get_status(is_correct),
        }

    def _get_status(self, is_correct):
        if is_correct is None:
            return 'not started'
        elif is_correct is True:
            return 'correct'
        else:
            return 'incorrect'
