from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Contest(Model):
    __tablename__ = 'contests'

    name = Column(String, nullable=False)

    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    owner = relationship("User", uselist=False, backref='contests')
