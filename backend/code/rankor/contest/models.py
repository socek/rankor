from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Contest(Model):
    __tablename__ = 'contests'

    name = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship("User", uselist=False, backref='contests')
