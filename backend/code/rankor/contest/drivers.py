from rankor.application.drivers import Command
from rankor.application.drivers import Query

from rankor.contest.models import Contest


class ContestQuery(Query):
    model = Contest

    def list_for_owner(self, owner_id):
        return (
            self._query()
            .filter(self.model.is_active.is_(True))
            .filter(self.model.owner_id == owner_id)
            .order_by(self.model.created_at)
            .all()
        )


class ContestCommand(Command):
    model = Contest
    _query = ContestQuery

