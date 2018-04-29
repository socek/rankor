from rankor.application.drivers import Query
from rankor.application.drivers import Command

from rankor.contest.models import Contest


class ContestQuery(Query):
    model = Contest

    def list_for_owner(self, owner_id):
        return (
            self._query()
            .filter(self.model.owner_id == owner_id)
            .order_by(self.model.created_at)
            .all()
        )


class ContestCommand(Command):
    model = Contest

    @property
    def query(self):
        return ContestQuery(self.database)

    def update_by_uuid(self, uuid, update):
        update_raw = {}
        for key, value in update.items():
            update_raw[getattr(self.model, key)] = value
        self.query._get_by_uuid(uuid).update(update_raw)
        self.database.commit()
