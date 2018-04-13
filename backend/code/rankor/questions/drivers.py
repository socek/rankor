from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.questions.models import Answer
from rankor.questions.models import Question

from rankor.contest.models import Contest


class QuestionQuery(Query):
    model = Question

    def list_for_contest(self, contest_uuid):
        return self.query().join(Contest).filter(Contest.uuid == contest_uuid).all()


class QuestionCommand(Command):
    model = Question


class AnswerQuery(Query):
    model = Answer


class AnswerCommand(Command):
    model = Answer
