from uuid import UUID

from sapp.plugins.sqlalchemy.driver import Command as BaseCommand
from sapp.plugins.sqlalchemy.driver import Query as BaseQuery


class Query(BaseQuery):
    """
    You need to set up:
    - model
    """

    def _ensure_uuid(self, uuid):
        if isinstance(uuid, UUID):
            return uuid.hex
        else:
            return uuid

    def _get_by_id(self, id):
        return self._query().filter(self.model.id == id)

    def get_by_id(self, id):
        return self._get_by_id(id).one()


class Command(BaseCommand):
    """
    You need to set up:
    - model
    - _query
    """

    def _ensure_uuid(self, uuid):
        if isinstance(uuid, UUID):
            return uuid.hex
        else:
            return uuid

    @property
    def query(self):
        return self._query(self.database)

    def update_by_id(self, id, update):
        update_raw = {}
        for key, value in update.items():
            update_raw[getattr(self.model, key)] = value
        self.query._get_by_id(id).update(update_raw)
        self.database.commit()
