from unittest.mock import MagicMock
from unittest.mock import patch
from uuid import uuid4

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound
from pytest import fixture
from pytest import raises
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.testing import ViewFixture
from rankor.questions.views import AdminQuestionListView
from rankor.questions.views import AdminQuestionView


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
    def mquestion_command(self, mdbsession):
        with patch('rankor.questions.views.QuestionCommand') as mock:
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


class TestAdminQuestionView(Fixtures):
    _view = AdminQuestionView

    def test_get_happy_path(
            self,
            view,
            mrequest,
            mquestion_query,
            mcontest_query,
            contest_id,
            question_id,
    ):
        """
        .get should return list of all questions assigned to a contest.
        """
        obj = MagicMock()
        obj.category = 'my cat'
        mquestion_query.get_by_id.return_value = obj

        assert view.get() == {
            'id': str(obj['id']),
            'name': str(obj['name']),
            'description': str(obj['description']),
            'category': str(obj['my cat']),
            'contest_id': str(obj['contest_id'])
        }

    def test_get_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            mget_user,
            question_id,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'
        mcontest_query.get_by_id.side_effect = NoResultFound

        with raises(HTTPNotFound):
            view()

    def test_patch(
            self,
            view,
            mrequest,
            mquestion_command,
            mcontest_query,
            contest_id,
            mquestion_query,
    ):
        """
        .patch should create new question assigned to the contest.
        """
        id = uuid4().hex
        mrequest.json_body = {
            'name': 'my name',
            'description': 'my description',
            'category': 'cat'
        }
        mquestion_query.get_by_id.return_value.id = id
        mrequest.matchdict = {'question_id': id}

        view.patch()

        mquestion_command.update_by_id.assert_called_once_with(
            id, mrequest.json_body)

    def test_patch_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            mget_user,
    ):
        """
        .patch should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'patch'
        mcontest_query.get_by_id.side_effect = NoResultFound

        with raises(HTTPNotFound):
            view()

    def test_patch_when_form_not_valid(
            self,
            view,
            mrequest,
            mcontest_query,
    ):
        """
        .patch should raise HTTPBadRequest when form is not valid
        """
        with raises(HTTPBadRequest):
            view.patch()


class TestAdminQuestionListView(Fixtures):
    _view = AdminQuestionListView

    def test_get_happy_path(
            self,
            view,
            mrequest,
            mquestion_query,
            mcontest_query,
            contest_id,
    ):
        """
        .get should return list of all questions assigned to a contest.
        """
        obj = MagicMock()
        obj.category = 'my cat'
        mquestion_query.list_for_contest.return_value = [obj]
        assert dict(view.get()['categories']) == {
            'my cat': [{
                'id': str(obj['id']),
                'name': str(obj['name']),
                'description': str(obj['description']),
                'category': str(obj['my cat']),
                'contest_id': str(obj['contest_id'])
            }]
        }

    def test_get_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            mget_user,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'get'
        mcontest_query.get_by_id.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view()

    def test_post(
            self,
            view,
            mrequest,
            mquestion_command,
            mcontest_query,
            contest_id,
    ):
        """
        .post should create new question assigned to the contest.
        """
        mrequest.json_body = {
            'name': 'my name',
            'description': 'my description',
            'category': 'cat'
        }

        view.post()

        mquestion_command.create.assert_called_once_with(
            name='my name',
            description='my description',
            category='cat',
            contest_id=mcontest_query.get_by_id.return_value.id)

    def test_post_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_id,
            mget_user,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mrequest.method = 'POST'
        mcontest_query.get_by_id.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view()

    def test_post_when_form_not_valid(
            self,
            view,
            mrequest,
            mcontest_query,
    ):
        """
        .post should raise HTTPBadRequest when form is not valid
        """
        with raises(HTTPBadRequest):
            view.post()
