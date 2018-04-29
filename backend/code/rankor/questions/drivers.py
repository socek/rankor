from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.contest.models import Contest
from rankor.questions.models import Question


class QuestionQuery(Query):
    model = Question

    def list_for_contest(self, contest_uuid):
        return (
            self._query()
            .join(Contest)
            .filter(Contest.uuid == contest_uuid)
            .order_by(self.model.category.desc())
            .order_by(self.model.created_at)
            .all()
        )


class QuestionCommand(Command):
    model = Question
