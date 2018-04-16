from collections import defaultdict

from sqlalchemy.orm.exc import NoResultFound
from pyramid.httpexceptions import HTTPNotFound

from rankor.questions.drivers import QuestionCommand
from rankor.questions.drivers import QuestionQuery
from rankor.questions.schema import NewQuestionSchema
from rankor.questions.schema import QuestionSchema
from rankor.contest.views import ContestBaseView


class QuestionBaseView(ContestBaseView):
    @property
    def question_query(self):
        return QuestionQuery(self.dbsession)

    @property
    def question_command(self):
        return QuestionCommand(self.dbsession)

    def _get_question_uuid(self):
        return self.request.matchdict['question_uuid']

    def _get_question(self):
        try:
            return self.question_query.get_by_uuid(self._get_question_uuid())
        except NoResultFound:
            raise HTTPNotFound()


class AdminQuestionView(QuestionBaseView):
    def get(self):
        self._get_contest()
        questions = self.question_query.list_for_contest(
            self._get_contest_uuid())
        schema = QuestionSchema()
        result = {'categories': defaultdict(list)}
        for question in questions:
            result['categories'][question.category].append(schema.dump(question).data)
        return result

    def post(self):
        self._get_contest()
        fields = self.get_validated_fields(NewQuestionSchema)
        fields['contest_id'] = self._get_contest().id
        self.question_command.create(**fields)
