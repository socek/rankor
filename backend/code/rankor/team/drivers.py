from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.game.models import Game
from rankor.team.models import Team


class TeamQuery(Query):
    model = Team

    def list_for_game(self, game_uuid):
        """
        List all questions for the started game. Add information about question
        status (success, fail, not started).
        """
        return (
            self.database.query(self.model)
            .join(Game)
            .filter(Game.uuid == game_uuid)
            .order_by(self.model.created_at)
            .all()
        )


class TeamCommand(Command):
    model = Team
    _query = TeamQuery
