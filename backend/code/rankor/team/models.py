from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from rankor.application.model import Model


class Team(Model):
    __tablename__ = 'teams'

    name = Column(String, nullable=False)

    game_id = Column(UUID(as_uuid=True), ForeignKey('games.id'), nullable=False)
    game = relationship("Game", uselist=False, backref='teams')

    def to_dict(self):
        data = super().to_dict()
        data['name'] = self.name
        return data
