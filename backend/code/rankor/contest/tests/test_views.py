from unittest.mock import PropertyMock
from unittest.mock import patch

from pytest import fixture
from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from rankor.contest.views import AdminContestView


class TestAdminContestView(ControllerFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return AdminContestView(mroot_factory, mrequest)

    @fixture
    def mdbsession(self, view):
        with patch.object(
                AdminContestView, 'dbsession',
                new_callable=PropertyMock) as mock:
            yield mock.return_value

    @fixture
    def mquery(self, mdbsession):
        with patch('rankor.contest.views.ContestQuery') as mock:
            yield mock.return_value

    @fixture
    def mcommand(self, mdbsession):
        with patch('rankor.contest.views.ContestCommand') as mock:
            yield mock.return_value

    @fixture
    def mget_user(self, view):
        with patch.object(view, 'get_user') as mock:
            yield mock

    def test_get(self, view, mquery, mget_user):
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
