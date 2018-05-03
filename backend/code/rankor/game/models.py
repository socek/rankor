from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Game(Model):
    __tablename__ = 'games'

    name = Column(String, nullable=False)
    contest_id = Column(Integer, ForeignKey('contests.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    contest = relationship("Contest", uselist=False)
    owner = relationship("User", uselist=False)
