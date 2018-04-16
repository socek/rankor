from pytest import fixture

from rankor.application.testing import DeleteOnExit
from rankor.application.testing import IntegrationFixture
from rankor.contest.models import Contest
from rankor.questions.drivers import QuestionQuery
from rankor.questions.models import Question


class TestQuestionQuery(IntegrationFixture):
    question_user_data = {
        'name': 'name',
        'description': 'description',
        'category': 'cat',
    }

    @fixture
    def driver(self, app):
        return QuestionQuery(app.dbsession)

    @fixture
    def contest_one(self, dbsession, user):
        contest_data = dict(self.contest_user_data)
        contest_data['owner'] = user
        contest = Contest(**contest_data)

        with DeleteOnExit(dbsession, contest):
            yield contest

    @fixture
    def contest_two(self, dbsession, user):
        contest_data = dict(self.contest_user_data)
        contest_data['owner'] = user
        contest = Contest(**contest_data)

        with DeleteOnExit(dbsession, contest):
            yield contest

    @fixture
    def question_one(self, dbsession, contest_one):
        question_data = dict(self.question_user_data)
        question_data['contest_id'] = contest_one.id
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question

    @fixture
    def question_two(self, dbsession, contest_two):
        question_data = dict(self.question_user_data)
        question_data['contest_id'] = contest_two.id
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question

    def test_list_for_contest(
            self,
            driver,
            contest_one,
            contest_two,
            question_one,
            question_two,
    ):
        """
        .list_for_contest should return only questions from that specyfic contest
        """
        result = driver.list_for_contest(contest_one.uuid)
        assert [obj.uuid for obj in result] == [question_one.uuid]
