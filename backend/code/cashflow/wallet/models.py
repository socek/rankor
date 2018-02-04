from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from cashflow.application.model import Model


class Wallet(Model):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(32), nullable=False, default=uuid4, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', backref='wallets')
