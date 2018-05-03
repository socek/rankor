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
        assert result[0].uuid == game_from_user.uuid
        assert len(result)


class TestGameCommand(IntegrationFixture):
    @fixture
    def query(self, app):
        return GameQuery(app.dbsession)

    @fixture
    def command(self, app):
        return GameCommand(app.dbsession)

    def test_update_by_uuid(self, command, query, game_from_user):
        """
        .update_by_uuid should update object by uuid.
        """
        command.update_by_uuid(game_from_user.uuid, {'name': 'new name'})

        game = query.get_by_uuid(game_from_user.uuid)

        assert game.name == 'new name'
