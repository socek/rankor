from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from mypet.application.model import Model


class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
