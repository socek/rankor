from sqlalchemy.orm.exc import NoResultFound

from rankor.application.drivers import Command
from rankor.application.drivers import Query
from rankor.game_answer.models import GameAnswer


class GameAnswerQuery(Query):
    model = GameAnswer

    def get_by_game_and_question(self, game_id, question_id):
        return (
            self._query()
            .filter(self.model.game_id == game_id)
            .filter(self.model.question_id == question_id)
            .one())


class GameAnswerCommand(Command):
    model = GameAnswer
    _query = GameAnswerQuery

    def upsert(self, game_id, question_id, team_id, answer_id):
        try:
            game_answer = self.query.get_by_game_and_question(
                game_id, question_id)
            game_answer.team_id = team_id
            game_answer.answer_id = answer_id
            self.database.commit()
            return game_answer
        except NoResultFound:
            return self.create(
                game_id=game_id,
                question_id=question_id,
                team_id=team_id,
                answer_id=answer_id)
