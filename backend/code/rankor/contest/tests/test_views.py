from unittest.mock import PropertyMock
from unittest.mock import patch
from uuid import uuid4

from pytest import fixture
from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from rankor.contest.views import AdminContestListView
from rankor.contest.views import AdminContestView


class Fixtures(ControllerFixtureMixin):
    @fixture
    def mquery(self, mdbsession):
        with patch('rankor.contest.views.ContestQuery', autospec=True) as mock:
            yield mock.return_value

    @fixture
    def mcommand(self, mdbsession):
        with patch('rankor.contest.views.ContestCommand', autospec=True) as mock:
            yield mock.return_value

    @fixture
    def mget_user_id(self, view):
        with patch.object(view, 'get_user_id', autospec=True) as mock:
            yield mock

    @fixture
    def mget_contest(self, view):
        with patch.object(view, '_get_contest', autospec=True) as mock:
            yield mock


class TestAdminContestListView(Fixtures):
    @fixture
    def view(self, mroot_factory, mrequest):
        return AdminContestListView(mroot_factory, mrequest)

    @fixture
    def mdbsession(self, view):
        with patch.object(
                AdminContestListView, 'dbsession',
                new_callable=PropertyMock) as mock:
            yield mock.return_value

    def test_get(self, view, mquery, mget_user_id):
        """
        .get should return list of all contests of logged in user.
        """
        contest = {
            'name': 'one',
            'owner_id': 5,
            'uuid': 'three',
        }
        mquery.list_for_owner.return_value = [contest]

        assert view.get() == {'contests': [contest]}

    def test_post(self, view, mrequest, mcommand, mget_user_id):
        """
        .post should create new contest with ownership of logged in user.
        """
        mrequest.json_body = {'name': 'long one'}

        view.post()

        mcommand.create.assert_called_once_with(
            name='long one', owner_id=mget_user_id.return_value)


class TestAdminContestView(Fixtures):
    @fixture
    def view(self, mroot_factory, mrequest):
        return AdminContestView(mroot_factory, mrequest)

    @fixture
    def mdbsession(self, view):
        with patch.object(
                AdminContestView, 'dbsession',
                new_callable=PropertyMock) as mock:
            yield mock.return_value

    def test_get(self, view, mget_contest):
        """
        .get should return data from contest got by uuid
        """
        mget_contest.return_value = {
            'name': 'contest name'
        }

        assert view.get() == {
            'name': 'contest name',
        }

    def test_patch(self, view, mrequest, mget_contest, mcommand):
        """
        .patch should update object by uuid
        """
        uuid = uuid4().hex
        mget_contest.return_value.uuid = uuid
        mrequest.json_body = {
            'name': 'new name',
        }

        view.patch()

        mcommand.update_by_uuid.assert_called_once_with(
            uuid,
            {
                'name': 'new name'
            })
