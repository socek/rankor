from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class GameAnswer(Model):
    __tablename__ = 'game_answers'

    name = Column(String, nullable=False)

    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    answer_id = Column(Integer, ForeignKey('answers.id'), nullable=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)

    game = relationship("Game", uselist=False)
    question = relationship("Question", uselist=False)
    answer = relationship("Answer", uselist=False)
    team = relationship("Team", uselist=False)
