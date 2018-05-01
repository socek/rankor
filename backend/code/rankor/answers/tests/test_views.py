from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from unittest.mock import patch
from uuid import uuid4

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ViewFixtureMixin
from sqlalchemy.orm.exc import NoResultFound

from rankor.answers.views import AdminAnswerListView


class TestAdminAnswerListView(ViewFixtureMixin):
    @fixture
    def mrequest(self):
        request = MagicMock()
        request._cache = {}
        return request

    @fixture
    def mdbsession(self, view):
        with patch.object(
                AdminAnswerListView, 'dbsession',
                new_callable=PropertyMock) as mock:
            yield mock.return_value

    @fixture
    def view(self, mroot_factory, mrequest):
        return AdminAnswerListView(mroot_factory, mrequest)

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
    def matchdict(self, mrequest):
        mrequest.matchdict = {}
        return mrequest.matchdict

    @fixture
    def contest_uuid(self, matchdict):
        contest_uuid = uuid4().hex
        matchdict['contest_uuid'] = contest_uuid
        return contest_uuid

    @fixture
    def question_uuid(self, matchdict):
        question_uuid = uuid4().hex
        matchdict['question_uuid'] = question_uuid
        return question_uuid

    def test_get_happy_path(
            self,
            view,
            mrequest,
            manswer_query,
            mcontest_query,
            mquestion_query,
            contest_uuid,
            question_uuid,
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
            'question_uuid':
            'uuid',
        }]
        assert view.get() == {
            'answers': [{
                'name': 'my name',
                'is_correct': True,
                'question_uuid': 'uuid',
            }]
        }

    def test_get_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            mquestion_query,
            contest_uuid,
            question_uuid,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mcontest_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_get_when_question_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            mquestion_query,
            contest_uuid,
            question_uuid,
    ):
        """
        .get should raise HTTPNotFound when contest not found
        """
        mquestion_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_post(
            self,
            view,
            mrequest,
            manswer_command,
            mcontest_query,
            mquestion_query,
            contest_uuid,
            question_uuid,
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
            question_id=mquestion_query.get_by_uuid.return_value.id
        )

    def test_post_when_contest_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_uuid,
            question_uuid,
            mquestion_query,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mcontest_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_post_when_question_not_found(
            self,
            view,
            mrequest,
            mcontest_query,
            contest_uuid,
            question_uuid,
            mquestion_query,
    ):
        """
        .post should raise HTTPNotFound when contest not found
        """
        mquestion_query.get_by_uuid.side_effect = NoResultFound
        with raises(HTTPNotFound):
            view.get()

    def test_post_when_form_not_valid(self, view, mrequest, mcontest_query):
        """
        .post should raise HTTPBadRequest when form is not valid
        """
        with raises(HTTPBadRequest):
            view.post()
