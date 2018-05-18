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


class ScreenEvent(Model):
    __tablename__ = 'screen_events'

    screen_id = Column(
        UUID(as_uuid=True),
        ForeignKey('screens.id'),
        nullable=False,
    )
    name = Column(String, nullable=True)
    view = Column(String)

    __table_args__ = (
        Index('screen_event_index', "created_at", "screen_id", "name"),
    )
