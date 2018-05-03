from pytest import fixture

from rankor.answers.drivers import AnswerCommand
from rankor.answers.drivers import AnswerQuery
from rankor.answers.models import Answer
from rankor.application.testing import DeleteOnExit
from rankor.application.testing import IntegrationFixture
from rankor.questions.models import Question


class Fixtures(IntegrationFixture):
    question_user_data = {
        'name': 'name',
        'description': 'description',
        'category': 'cat',
    }

    answer_user_data = {
        'name': 'name',
        'is_correct': False,
    }

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

    @fixture
    def query(self, app):
        return AnswerQuery(app.dbsession)

    @fixture
    def command(self, app):
        return AnswerCommand(app.dbsession)


class TestAnswerQuery(Fixtures):
    def test_list_for_question(
            self,
            query,
            question_one,
            answer_one,
            answer_two,
    ):
        """
        .list_for_question should return only answers from that specyfic question
        """
        result = query.list_for_question(question_one.uuid)
        assert [obj.uuid for obj in result] == [answer_one.uuid]


class TestAnswerCommand(Fixtures):
    def test_upsert_collection(
            self,
            command,
            query,
            question_one,
            answer_one,
            dbsession,
    ):
        """
        .upsert_collection should update the whole collection of objects
        """
        answer_one_data = dict(
            name=answer_one.name,
            is_correct=True,
            id=answer_one.id,
            uuid=answer_one.uuid)

        answer_two_data = dict(
            name='second',
            is_correct=False,
        )

        try:
            command.upsert_collection(
                question_one.id,
                [answer_one_data, answer_two_data],
            )

            names = set([
                answer.name
                for answer in query.list_for_question(question_one.uuid)
            ])

            assert names == set(['name', 'second'])
        finally:
            (dbsession.query(Answer)
             .filter(Answer.question_id == question_one.id)
             .filter(Answer.name == 'second').delete())
            dbsession.commit()

    def test_update_by_uuid(self, command, answer_one, dbsession):
        """
        .update_by_uuid should update object
        """
        command.update_by_uuid(answer_one.uuid, {'name': 'updated'})

        dbsession.refresh(answer_one)
        assert answer_one.name == 'updated'
