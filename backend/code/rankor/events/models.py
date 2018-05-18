from datetime import timezone

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from rankor.application.model import Model


class Screen(Model):
    __tablename__ = 'screens'

    game_id = Column(
        UUID(as_uuid=True),
        ForeignKey('games.id'),
        nullable=False,
        index=True,
    )
    view = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'view': self.view,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).timestamp(),
            'updated_at': self.updated_at.replace(tzinfo=timezone.utc).timestamp()
        }


class ScreenEvent(Model):
    __tablename__ = 'screen_events'

    screen_id = Column(
        UUID(as_uuid=True),
        ForeignKey('screens.id'),
        nullable=False,
    )
    name = Column(String, nullable=True)
    view = Column(String)

    __table_args__ = (Index('screen_event_index', "created_at", "screen_id",
                            "name"), )

    def to_dict(self):
        return {
            'id': self.id,
            'screen_id': self.screen_id,
            'view': self.view,
            'name': self.name,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).timestamp(),
            'updated_at': self.updated_at.replace(tzinfo=timezone.utc).timestamp()
        }
