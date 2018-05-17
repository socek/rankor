from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.answers.drivers import AnswerCommand
from rankor.answers.drivers import AnswerQuery
from rankor.answers.schema import AnswerSchema
from rankor.application.cache import cache_per_request
from rankor.questions.views import QuestionBaseView


class AnswerBaseView(QuestionBaseView):
    @property
    def answer_query(self):
        return AnswerQuery(self.dbsession)

    @property
    def answer_command(self):
        return AnswerCommand(self.dbsession)

    def _get_answer_id(self):
        return self.request.matchdict['answer_id']

    @cache_per_request('answer')
    def _get_answer(self):
        try:
            return self.answer_query.get_by_id(self._get_answer_id())
        except NoResultFound:
            raise HTTPNotFound()

    def validate(self):
        super().validate()
        self._get_question()


class AdminAnswerListView(AnswerBaseView):
    def get(self):
        answers = self.answer_query.list_for_question(
            self._get_question_id())
        schema = AnswerSchema()
        return {'answers': [schema.dump(answer) for answer in answers]}

    def post(self):
        question = self._get_question()

        fields = self.get_validated_fields(AnswerSchema())
        fields['question_id'] = question.id

        answer = self.answer_command.create(**fields)

        return {
            'answer_id': answer.id,
        }


class AdminAnswerView(AnswerBaseView):
    def get(self):
        schema = AnswerSchema()
        answer = self._get_answer()
        return schema.dump(answer)

    def patch(self):
        answer = self._get_answer()
        fields = self.get_validated_fields(AnswerSchema())
        self.answer_command.update_by_id(answer.id, fields)
