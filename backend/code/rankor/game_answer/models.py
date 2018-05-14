from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from rankor.application.model import Model
from rankor.team.models import Team


class GameAnswer(Model):
    __tablename__ = 'game_answers'

    game_id = Column(UUID, ForeignKey('games.id'), nullable=False)
    question_id = Column(UUID, ForeignKey('questions.id'), nullable=False)
    answer_id = Column(UUID, ForeignKey('answers.id'), nullable=True)
    team_id = Column(UUID, ForeignKey('teams.id'), nullable=True)

    game = relationship("Game", uselist=False)
    question = relationship("Question", uselist=False)
    answer = relationship("Answer", uselist=False)
    team = relationship(Team, uselist=False)

