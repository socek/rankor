from pytest import fixture

from rankor.application.testing import DeleteOnExit
from rankor.application.testing import IntegrationFixture
from rankor.contest.models import Contest
from rankor.questions.drivers import QuestionCommand
from rankor.questions.drivers import QuestionQuery
from rankor.questions.models import Question


class Fixtures(IntegrationFixture):
    question_user_data = {
        'name': 'name',
        'description': 'description',
        'category': 'cat',
    }

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
        question_data['contest_id'] = contest_one.id.hex
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question

    @fixture
    def question_two(self, dbsession, contest_two):
        question_data = dict(self.question_user_data)
        question_data['contest_id'] = contest_two.id.hex
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question


class TestQuestionQuery(Fixtures):
    @fixture
    def driver(self, app):
        return QuestionQuery(app.dbsession)

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
        result = driver.list_for_contest(contest_one.id)
        assert [obj.id for obj in result] == [question_one.id]


class TestQuestionCommand(Fixtures):
    @fixture
    def driver(self, app):
        return QuestionCommand(app.dbsession)

    def test_update_by_id(self, driver, question_one, dbsession):
        """
        .update_by_id should update object by id
        """
        driver.update_by_id(question_one.id, {'name': 'new fine name'})

        dbsession.refresh(question_one)
        assert question_one.name == 'new fine name'
