from pytest import fixture

from rankor.application.testing import IntegrationFixture
from rankor.contest.drivers import ContestCommand
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
        assert result[0].id == contest_from_user.id
        assert len(result)


class TestContestCommand(IntegrationFixture):
    @fixture
    def query(self, app):
        return ContestQuery(app.dbsession)

    @fixture
    def command(self, app):
        return ContestCommand(app.dbsession)

    def test_update_by_id(self, command, query, contest_from_user):
        """
        .update_by_id should update object by id.
        """
        command.update_by_id(contest_from_user.id, {'name': 'new name'})

        contest = query.get_by_id(contest_from_user.id)

        assert contest.name == 'new name'
