from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from rankor.application.model import Model
from rankor.questions.models import Question


class Answer(Model):
    __tablename__ = 'answers'

    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    index = Column(Integer, default=0)
    is_correct = Column(Boolean, nullable=False, default=False)

    question_id = Column(Integer, ForeignKey(Question.id), nullable=False)
    question = relationship("Question", uselist=False, backref='answers')