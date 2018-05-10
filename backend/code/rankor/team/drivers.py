from sqlalchemy import func

from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.game.models import Game
from rankor.game_answer.models import GameAnswer
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

    def list_high_score(self, game_uuid):
        return (
            self.database.query(
                self.model.name.label('name'),
                func.count(GameAnswer.id).label('count'),
                func.count(1).filter(Answer.is_correct).label('wins'))
            .join(Game, self.model.game_id == Game.id)
            .join(GameAnswer, GameAnswer.team_id == self.model.id)
            .join(Answer, GameAnswer.answer_id == Answer.id)
            .filter(Game.uuid == game_uuid)
            .group_by(self.model.id)
            .all()
        )


class TeamCommand(Command):
    model = Team
    _query = TeamQuery
