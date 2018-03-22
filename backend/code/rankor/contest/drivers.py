from rankor.application.drivers import Query
from rankor.application.drivers import Command

from rankor.contest.models import Contest


class ContestQuery(Query):
    model = Contest

    def list_for_owner(self, owner_id):
        return self.query().filter(self.model.owner_id == owner_id).all()


class ContestCommand(Command):
    model = Contest
