from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.contest.models import Contest
from rankor.game.models import Game
from rankor.game_answer.models import GameAnswer
from rankor.questions.models import Question


class QuestionQuery(Query):
    model = Question

    def list_for_contest(self, contest_uuid):
        return (
            self._query()
            .join(Contest)
            .filter(Contest.uuid == contest_uuid)
            .order_by(self.model.category.desc())
            .order_by(self.model.created_at)
            .all()
        )

    def list_for_game(self, game_uuid):
        """
        List all questions for the started game. Add information about question
        status (success, fail, not started).
        """
        return (
            self.database.query(self.model, Answer.is_correct, GameAnswer)
            .join(Contest)
            .join(Game)
            .outerjoin(GameAnswer, GameAnswer.question_id == self.model.id)
            .outerjoin(Answer, GameAnswer.answer_id == Answer.id)
            .filter(Game.uuid == game_uuid)
            .order_by(self.model.category.desc())
            .order_by(self.model.created_at)
            .all()
        )


class QuestionCommand(Command):
    model = Question
    _query = QuestionQuery
