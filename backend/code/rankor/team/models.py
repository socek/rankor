from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Team(Model):
    __tablename__ = 'teams'

    name = Column(String, nullable=False)

    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)
    game = relationship("Game", uselist=False, backref='teams')
