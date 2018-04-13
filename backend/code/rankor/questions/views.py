from sqlalchemy.orm.exc import NoResultFound
from pyramid.httpexceptions import HTTPNotFound

from rankor.application.views import RestfulController
from rankor.auth.view_mixins import AuthMixin
from rankor.contest.drivers import ContestQuery
from rankor.questions.drivers import QuestionCommand
from rankor.questions.drivers import QuestionQuery
from rankor.questions.schema import NewQuestionSchema
from rankor.questions.schema import QuestionSchema


class AdminQuestionView(RestfulController, AuthMixin):
    @property
    def contest_query(self):
        return ContestQuery(self.dbsession)

    @property
    def question_query(self):
        return QuestionQuery(self.dbsession)

    @property
    def question_command(self):
        return QuestionCommand(self.dbsession)

    def _get_contest_uuid(self):
        return self.request.matchdict['contest_uuid']

    def _get_contest(self):
        try:
            return self.contest_query.get_by_uuid(self._get_contest_uuid())
        except NoResultFound:
            raise HTTPNotFound()

    def get(self):
        self._get_contest()
        questions = self.question_query.list_for_contest(
            self._get_contest_uuid())
        schema = QuestionSchema()
        return {
            'questions':
            [schema.dump(question).data for question in questions]
        }

    def post(self):
        fields = self.get_validated_fields(NewQuestionSchema)
        fields['contest_id'] = self._get_contest().id
        self.question_command.create(**fields)
