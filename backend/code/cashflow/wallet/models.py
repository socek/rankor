from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rankor.application.model import Model
from rankor.application.model import uuid_default


class Wallet(Model):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(32), nullable=False, default=uuid_default, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', backref='wallets')
