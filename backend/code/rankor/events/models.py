from logging import getLogger

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from rankor.answers.models import Answer
from rankor.application.model import Model
from rankor.auth.models import User # noqa
from rankor.contest.models import Contest # noqa
from rankor.game.models import Game # noqa
from rankor.game_answer.models import GameAnswer
from rankor.questions.models import Question
from rankor.team.models import Team

log = getLogger(__name__)


class ScreenMixin(object):
    view = Column(String, default='welcome')

    @declared_attr
    def question_id(cls):  # noqa
        return Column(
            UUID(as_uuid=True), ForeignKey('questions.id'), nullable=True)

    @declared_attr
    def answer_id(cls):  # noqa
        return Column(
            UUID(as_uuid=True), ForeignKey('answers.id'), nullable=True)

    @declared_attr
    def team_id(cls):  # noqa
        return Column(
            UUID(as_uuid=True), ForeignKey('teams.id'), nullable=True)

    @declared_attr
    def game_answer_id(cls):  # noqa
        return Column(
            UUID(as_uuid=True), ForeignKey('game_answers.id'), nullable=True)

    @declared_attr
    def question(cls):  # noqa
        return relationship(Question, uselist=False)

    @declared_attr
    def answer(cls):  # noqa
        return relationship(Answer, uselist=False)

    @declared_attr
    def team(cls):  # noqa
        return relationship(Team, uselist=False)

    @declared_attr
    def game_answer(cls):  # noqa
        return relationship(GameAnswer, uselist=False)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'view': self.view,
            'question_id': self.question_id,
            'answer_id': self.answer_id,
            'team_id': self.team_id,
            'game_answer_id': self.game_answer_id,
        })
        if self.question:
            data['question'] = self.question.to_dict()
        if self.team:
            data['team'] = self.team.to_dict()
        if self.answer:
            data['answer'] = self.answer.to_dict()
        if self.game_answer:
            data['game_answer'] = self.game_answer.to_dict()

        if self.answer and self.game_answer_id:
            data['is_correct'] = self.answer.is_correct or False
        else:
            data['is_correct'] = None

        return data


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
