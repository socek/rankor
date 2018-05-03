from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.game.models import Game


class GameQuery(Query):
    model = Game

    def list_for_owner(self, owner_id):
        return (
            self._query()
            .filter(self.model.owner_id == owner_id)
            .order_by(self.model.created_at)
            .all()
        )


class GameCommand(Command):
    model = Game
    _query = GameQuery
