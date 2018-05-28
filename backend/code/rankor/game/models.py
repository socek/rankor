from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Game(Model):
    __tablename__ = 'games'

    name = Column(String, nullable=False)
    contest_id = Column(UUID(as_uuid=True), ForeignKey('contests.id'), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    welcome_message = Column(Text())

    contest = relationship("Contest", uselist=False)
    owner = relationship("User", uselist=False)
