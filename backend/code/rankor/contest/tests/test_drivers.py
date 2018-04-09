from pytest import fixture

from rankor.application.testing import IntegrationFixture
from rankor.contest.drivers import ContestQuery


class TestContestQuery(IntegrationFixture):
    @fixture
    def query(self, app):
        return ContestQuery(app.dbsession)

    def test_list_for_owner(
            self,
            query,
            user,
            contest_from_user,
            contest_from_second_user,
    ):
        """
        .list_for_owner should return contests only from provided owner.
        """
        result = query.list_for_owner(user.id)
        assert result[0].uuid == contest_from_user.uuid
        assert len(result)
