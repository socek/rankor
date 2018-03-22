from rankor.application.drivers import Query
from rankor.application.drivers import Command

from rankor.contest.models import Contest


class ContestQuery(Query):
    model = Contest


class ContestCommand(Command):
    model = Contest
