from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.answers.models import Answer
from rankor.contest.models import Contest
from rankor.game.models import Game
from rankor.game_answer.models import GameAnswer
from rankor.questions.models import Question
from rankor.team.models import Team


class QuestionQuery(Query):
    model = Question

    def list_for_contest(self, contest_id):
        return (
            self._query()
            .join(Contest)
            .filter(Contest.id == contest_id)
            .order_by(self.model.category.desc())
            .order_by(self.model.created_at)
            .all()
        )

    def list_for_game(self, game_id):
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
            .filter(Game.id == game_id)
            .order_by(self.model.category.desc())
            .order_by(self.model.created_at)
            .all()
        )

    def get_for_answer(self, id, game_id):
        return (
            self.database.query(
                self.model.id.label('id'),
                self.model.name.label('name'),
                self.model.category.label('category'),
                self.model.description.label('description'),
                Contest.id.label('contest_id'),
                Team.name.label('team')
            )
            .join(Contest)
            .join(Game)
            .outerjoin(GameAnswer, GameAnswer.question_id == self.model.id)
            .outerjoin(Answer, GameAnswer.answer_id == Answer.id)
            .outerjoin(Team, GameAnswer.team_id == Team.id)
            .filter(Game.id == game_id)
            .filter(self.model.id == id)
            .one()
        )


class QuestionCommand(Command):
    model = Question
    _query = QuestionQuery
