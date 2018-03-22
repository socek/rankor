from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.questions.models import Answer
from rankor.questions.models import Question


class QuestionQuery(Query):
    model = Question


class QuestionCommand(Command):
    model = Question


class AnswerQuery(Query):
    model = Answer


class AnswerCommand(Command):
    model = Answer
