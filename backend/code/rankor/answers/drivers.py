from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.questions.models import Question


class AnswerQuery(Query):
    model = Answer

    def list_for_question(self, question_uuid):
        return (
            self.query()
            .join(Question)
            .filter(Question.uuid == question_uuid)
            .all()
        )


class AnswerCommand(Command):
    model = Answer
