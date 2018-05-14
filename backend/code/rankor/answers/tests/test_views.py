from unittest.mock import patch
from uuid import uuid4

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound
from pytest import fixture
from pytest import raises
from sqlalchemy.orm.exc import NoResultFound

from rankor.answers.views import AdminAnswerListView
from rankor.answers.views import AdminAnswerView
from rankor.application.testing import DictLike
from rankor.application.testing import ViewFixture


class Fixtures(ViewFixture):
    @fixture
    def mcontest_query(self, mdbsession):
        with patch('rankor.contest.views.ContestQuery') as mock:
            yield mock.return_value

    @fixture
    def mquestion_query(self, mdbsession):
        with patch('rankor.questions.views.QuestionQuery') as mock:
            yield mock.return_value

    @fixture
    def manswer_query(self, mdbsession):
        with patch('rankor.answers.views.AnswerQuery') as mock:
            yield mock.return_value

    @fixture
    def manswer_command(self, mdbsession):
        with patch('rankor.answers.views.AnswerCommand') as mock:
            yield mock.return_value

    @fixture
    def contest_id(self, matchdict):
        contest_id = uuid4().hex
        matchdict['contest_id'] = contest_id
        return contest_id

    @fixture
    def question_id(self, matchdict):
        question_id = uuid4().hex
        matchdict['question_id'] = question_id
        return question_id

    @fixture
    def answer_id(self, matchdict):
        answer_id = uuid4().hex
        matchdict['answer_id'] = answer_id
        return answer_id

    @fixture
    def manswer(self, answer_id, manswer_query, question_id):
        manswer = DictLike({
            'id': 5,
            'id': answer_id,
            'name': 'this is an answer',
            'is_correct': True,
            'question_id': question_id
        })
        manswer_query.get_by_id.return_value = manswer
        return manswer


class TestAdminAnswerListView(Fixtures):
    _view = AdminAnswerListView

    def test_get_happy_path(
            self,
            view,
            mrequest,
            manswer_query,
            mcontest_query,
            mquestion_query,
            contest_id,
            question_id,
    ):
        """
        .get should return list of all answers assigned to a contest.
        """
        manswer_query.list_for_question.return_value = [{
            'name':
            'my name',
            'description':
            'my description',
            'is_correct':
            True,
            'question_id':
            'id',
        }]
        assert view.get() == {
            'answers': [{
                'name': 'my name',
                'is_correct': True,
                'question_id': 'id',
            }]
        }

    def test_get_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            mquestion_query,
            contest_id,
            question_id,
            mget_user,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'

        mcontest_query.get_by_id.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view()

    def test_get_when_question_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            mquestion_query,
            contest_id,
            question_id,
            mget_user,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'
        mquestion_query.get_by_id.side_effect = NoResultFound

        with raises(HTTPNotFound):
            view()

    def test_post(
            self,
            view,
            mrequest,
            manswer_command,
            mcontest_query,
            mquestion_query,
            contest_id,
            question_id,
    ):
        """
        .post should create new answer assigned to the contest.
        """
        mrequest.json_body = {
            'name': 'my name',
            'is_correct': True,
        }

        view.post()

        manswer_command.create.assert_called_once_with(
            name='my name',
            is_correct=True,
            question_id=mquestion_query.get_by_id.return_value.id)

    def test_post_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            question_id,
            mquestion_query,
            mget_user,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'
        mcontest_query.get_by_id.side_effect = NoResultFound

        with raises(HTTPNotFound):
            view()

    def test_post_when_question_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            question_id,
            mquestion_query,
            mget_user,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'
        mquestion_query.get_by_id.side_effect = NoResultFound

        with raises(HTTPNotFound):
            view()

    def test_post_when_form_not_valid(self, view, mrequest, mcontest_query):
        """
        .post should raise HTTPBadRequest when form is not valid
        """
        with raises(HTTPBadRequest):
            view.post()


class TestAdminAnswerView(Fixtures):
    _view = AdminAnswerView

    def test_get(
            self,
            view,
            manswer,
            answer_id,
            contest_id,
    ):
        """
        .get should return data of the needed answer object.
        """
        assert view.get() == {
            'id': manswer['id'],
            'id': manswer['id'],
            'name': manswer['name'],
            'is_correct': manswer['is_correct'],
            'question_id': manswer['question_id']
        }

    def test_patch(
            self,
            view,
            manswer,
            answer_id,
            contest_id,
            mrequest,
            manswer_command,
    ):
        """
        .patch should update object by ids
        """
        fields = {
            'name': 'my new name',
            'is_correct': False,
        }
        mrequest.json_body = fields

        view.patch()

        manswer_command.update_by_id(answer_id, fields)

    def test_get_on_404(
            self,
            view,
            manswer,
            answer_id,
            contest_id,
            manswer_query,
    ):
        """
        .get should raise Http 404 when answer has not been found
        """
        manswer_query.get_by_id.side_effect = NoResultFound()

        with raises(HTTPNotFound):
            assert view.get()

    def test_patch_on_404(
            self,
            view,
            manswer,
            answer_id,
            contest_id,
            mrequest,
            manswer_command,
            manswer_query,
    ):
        """
        .patch should raise Http 404 when answer has not been found
        """
        fields = {
            'name': 'my new name',
            'is_correct': False,
        }
        mrequest.json_body = fields
        manswer_query.get_by_id.side_effect = NoResultFound()

        with raises(HTTPNotFound):
            view.patch()

        assert not manswer_command.update_by_id.called
