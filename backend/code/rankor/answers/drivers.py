from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.questions.models import Question


class AnswerQuery(Query):
    model = Answer

    def list_for_question(self, question_uuid):
        return (
            self._query()
            .join(Question)
            .filter(Question.uuid == question_uuid)
            .order_by(self.model.created_at)
            .all()
        )


class AnswerCommand(Command):
    model = Answer

    def upsert_collection(self, question_id, collection):
        for data in collection:
            element = self.model(**data)
            element.question_id = question_id

            self.database.merge(element)
        self.database.commit()

    @property
    def query(self):
        return AnswerQuery(self.database)

    def update_by_uuid(self, uuid, update):
        update_raw = {}
        for key, value in update.items():
            update_raw[getattr(self.model, key)] = value
        self.query._get_by_uuid(uuid).update(update_raw)
        self.database.commit()
