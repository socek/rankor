from rankor.answers.drivers import AnswerCommand
from rankor.answers.drivers import AnswerQuery
from rankor.answers.schema import AnswerSchema
from rankor.questions.views import QuestionBaseView


class AnswerBaseView(QuestionBaseView):
    @property
    def answer_query(self):
        return AnswerQuery(self.dbsession)

    @property
    def answer_command(self):
        return AnswerCommand(self.dbsession)


class AdminAnswerListView(AnswerBaseView):
    def get(self):
        self._get_contest()
        self._get_question()

        answers = self.answer_query.list_for_question(
            self._get_question_uuid())
        schema = AnswerSchema()
        return {'answers': [schema.dump(answer) for answer in answers]}

    def post(self):
        self._get_contest()
        question = self._get_question()

        fields = self.get_validated_fields(AnswerSchema())
        fields['question_id'] = question.id

        answer = self.answer_command.create(**fields)

        return {
            'answer_uuid': answer.uuid,
        }
