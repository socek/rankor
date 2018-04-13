from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.answers.drivers import AnswerCommand
from rankor.answers.drivers import AnswerQuery
from rankor.answers.schema import AnswerSchema
from rankor.answers.schema import NewAnswerSchema
from rankor.questions.views import QuestionBaseView


class AnswerBaseView(QuestionBaseView):
    @property
    def answer_query(self):
        return AnswerQuery(self.dbsession)

    @property
    def answer_command(self):
        return AnswerCommand(self.dbsession)

    def _get_answer_uuid(self):
        return self.request.matchdict['answer_uuid']

    def _get_answer(self):
        try:
            return self.answer_query.get_by_uuid(self._get_answer_uuid())
        except NoResultFound:
            raise HTTPNotFound()


class AdminAnswerView(AnswerBaseView):
    def get(self):
        self._get_contest()
        self._get_question()

        answers = self.question_query.list_for_question(
            self._get_question_uuid())
        schema = AnswerSchema()
        return {
            'answers':
            [schema.dump(answer).data for answer in answers]
        }

    def post(self):
        self._get_contest()
        self._get_question()

        fields = self.get_validated_fields(NewAnswerSchema)
        fields['question_id'] = self._get_contest().id
        self.question_command.create(**fields)
