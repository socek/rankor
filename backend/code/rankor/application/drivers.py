from sapp.plugins.sqlalchemy.driver import Query as BaseQuery
from sapp.plugins.sqlalchemy.driver import Command as BaseCommand


class Query(BaseQuery):
    """
    You need to set up:
    - model
    """

    def _get_by_uuid(self, uuid):
        return self._query().filter(self.model.uuid == uuid)

    def get_by_uuid(self, uuid):
        return self._get_by_uuid(uuid).one()


class Command(BaseCommand):
    """
    You need to set up:
    - model
    - _query
    """

    @property
    def query(self):
        return self._query(self.database)

    def update_by_uuid(self, uuid, update):
        update_raw = {}
        for key, value in update.items():
            update_raw[getattr(self.model, key)] = value
        self.query._get_by_uuid(uuid).update(update_raw)
        self.database.commit()
