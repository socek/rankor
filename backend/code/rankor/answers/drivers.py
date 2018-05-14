from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.questions.models import Question


class AnswerQuery(Query):
    model = Answer

    def list_for_question(self, question_id):
        return (
            self._query()
            .join(Question)
            .filter(Question.id == question_id)
            .order_by(self.model.created_at)
            .all()
        )


class AnswerCommand(Command):
    model = Answer
    _query = AnswerQuery

    def upsert_collection(self, question_id, collection):
        for data in collection:
            element = self.model(**data)
            element.question_id = question_id

            self.database.merge(element)
        self.database.commit()
