from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.contest.models import Contest
from rankor.questions.models import Question


class QuestionQuery(Query):
    model = Question

    def list_for_contest(self, contest_uuid):
        return self.query().join(Contest).filter(
            Contest.uuid == contest_uuid).all()


class QuestionCommand(Command):
    model = Question
