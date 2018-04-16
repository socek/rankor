from pytest import fixture

from rankor.answers.drivers import AnswerQuery
from rankor.answers.models import Answer
from rankor.application.testing import DeleteOnExit
from rankor.application.testing import IntegrationFixture
from rankor.questions.models import Question


class TestAnswerQuery(IntegrationFixture):
    question_user_data = {
        'name': 'name',
        'description': 'description',
        'category': 'cat',
    }

    answer_user_data = {
        'name': 'name',
        'description': 'description',
        'is_correct': False,
    }

    @fixture
    def driver(self, app):
        return AnswerQuery(app.dbsession)

    @fixture
    def question_one(self, dbsession, contest_from_user):
        question_data = dict(self.question_user_data)
        question_data['contest_id'] = contest_from_user.id
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question

    @fixture
    def question_two(self, dbsession, contest_from_user):
        question_data = dict(self.question_user_data)
        question_data['contest_id'] = contest_from_user.id
        question = Question(**question_data)

        with DeleteOnExit(dbsession, question):
            yield question

    @fixture
    def answer_one(self, dbsession, question_one):
        answer_data = dict(self.answer_user_data)
        answer_data['question_id'] = question_one.id
        answer = Answer(**answer_data)

        with DeleteOnExit(dbsession, answer):
            yield answer

    @fixture
    def answer_two(self, dbsession, question_two):
        answer_data = dict(self.answer_user_data)
        answer_data['question_id'] = question_two.id
        answer = Answer(**answer_data)

        with DeleteOnExit(dbsession, answer):
            yield answer

    def test_list_for_question(
            self,
            driver,
            question_one,
            answer_one,
            answer_two,
    ):
        """
        .list_for_question should return only answers from that specyfic question
        """
        result = driver.list_for_question(question_one.uuid)
        assert [obj.uuid for obj in result] == [answer_one.uuid]
