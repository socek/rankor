from pytest import fixture

from rankor.application.testing import IntegrationFixture
from rankor.game.drivers import GameCommand
from rankor.game.drivers import GameQuery


class TestGameQuery(IntegrationFixture):
    @fixture
    def query(self, app):
        return GameQuery(app.dbsession)

    def test_list_for_owner(
            self,
            query,
            user,
            game_from_user,
            game_from_second_user,
    ):
        """
        .list_for_owner should return games only from provided owner.
        """
        result = query.list_for_owner(user.id)
        assert result[0].id == game_from_user.id
        assert len(result)


class TestGameCommand(IntegrationFixture):
    @fixture
    def query(self, app):
        return GameQuery(app.dbsession)

    @fixture
    def command(self, app):
        return GameCommand(app.dbsession)

    def test_update_by_id(self, command, query, game_from_user):
        """
        .update_by_id should update object by id.
        """
        command.update_by_id(game_from_user.id, {'name': 'new name'})

        game = query.get_by_id(game_from_user.id)

        assert game.name == 'new name'
