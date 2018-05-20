from datetime import timezone

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr

from rankor.application.model import Model


class ScreenMixin(object):
    view = Column(String, default='welcome')

    @declared_attr
    def question_id(cls):
        return Column(UUID(as_uuid=True), ForeignKey('questions.id'), nullable=True)

    @declared_attr
    def answer_id(cls):
        return Column(UUID(as_uuid=True), ForeignKey('answers.id'), nullable=True)

    @declared_attr
    def team_id(cls):
        return Column(UUID(as_uuid=True), ForeignKey('teams.id'), nullable=True)

    @declared_attr
    def game_answer_id(cls):
        return Column(UUID(as_uuid=True), ForeignKey('game_answers.id'), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'view': self.view,
            'created_at': self.created_at.replace(tzinfo=timezone.utc).timestamp(),
            'updated_at': self.updated_at.replace(tzinfo=timezone.utc).timestamp(),
            'question_id': self.question_id,
            'answer_id': self.answer_id,
            'team_id': self.team_id,
            'game_answer_id': self.game_answer_id,
        }


class Screen(ScreenMixin, Model):
    __tablename__ = 'screens'

    game_id = Column(
        UUID(as_uuid=True),
        ForeignKey('games.id'),
        nullable=False,
        index=True,
    )

    def to_dict(self):
        data = super().to_dict()
        data['game_id'] = self.game_id
        return data


class ScreenEvent(ScreenMixin, Model):
    __tablename__ = 'screen_events'

    screen_id = Column(
        UUID(as_uuid=True),
        ForeignKey('screens.id'),
        nullable=False,
    )
    name = Column(String, nullable=True)

    __table_args__ = (Index('screen_event_index', "created_at", "screen_id",
                            "name"), )

    def to_dict(self):
        data = super().to_dict()
        data['screen_id'] = self.screen_id
        data['name'] = self.name
        return data
