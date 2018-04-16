from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from unittest.mock import patch
from uuid import uuid4

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ControllerFixtureMixin
from sqlalchemy.orm.exc import NoResultFound

from rankor.questions.views import AdminQuestionView


class TestAdminQuestionView(ControllerFixtureMixin):
    @fixture
    def mdbsession(self, view):
        with patch.object(
                AdminQuestionView, 'dbsession',
                new_callable=PropertyMock) as mock:
            yield mock.return_value

    @fixture
    def view(self, mroot_factory, mrequest):
        return AdminQuestionView(mroot_factory, mrequest)

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
    def contest_uuid(self, mrequest):
        contest_uuid = uuid4().hex
        mrequest.matchdict = {'contest_uuid': contest_uuid}
        return contest_uuid

    def test_get_happy_path(
            self,
            view,
            mrequest,
            mquestion_query,
            mcontest_query,
            contest_uuid,
    ):
        """
        .get should return list of all questions assigned to a contest.
        """
        obj = MagicMock()
        obj.category = 'my cat'
        mquestion_query.list_for_contest.return_value = [obj]
        assert dict(view.get()['categories']) == {
            'my cat': [{
                'name': str(obj['name']),
                'description': str(obj['description']),
                'category': str(obj['my cat']),
                'contest_uuid': str(obj['contest_uuid'])
            }]
        }

    def test_get_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_uuid,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mcontest_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_post(
            self,
            view,
            mrequest,
            mquestion_command,
            mcontest_query,
            contest_uuid,
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
            contest_id=mcontest_query.get_by_uuid.return_value.id)

    def test_post_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_uuid,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mcontest_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_post_when_form_not_valid(self, view, mrequest, mcontest_query):
        """
        .post should raise HTTPBadRequest when form is not valid
        """
        with raises(HTTPBadRequest):
            view.post()
