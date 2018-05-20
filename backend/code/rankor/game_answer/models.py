from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from rankor.application.model import Model
from rankor.team.models import Team


class GameAnswer(Model):
    __tablename__ = 'game_answers'

    game_id = Column(UUID(as_uuid=True), ForeignKey('games.id'), nullable=False)
    question_id = Column(UUID(as_uuid=True), ForeignKey('questions.id'), nullable=False)
    answer_id = Column(UUID(as_uuid=True), ForeignKey('answers.id'), nullable=True)
    team_id = Column(UUID(as_uuid=True), ForeignKey('teams.id'), nullable=True)

    game = relationship("Game", uselist=False)
    question = relationship("Question", uselist=False)
    answer = relationship("Answer", uselist=False)
    team = relationship(Team, uselist=False)

    def to_dict(self):
        data = super().to_dict()
        data['game_id'] = self.game_id
        data['question_id'] = self.question_id
        data['answer_id'] = self.answer_id
        data['team_id'] = self.team_id
        return data
