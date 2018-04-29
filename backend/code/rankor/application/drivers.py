from sapp.plugins.sqlalchemy.driver import Query as BaseQuery
from sapp.plugins.sqlalchemy.driver import Command as BaseCommand


class Query(BaseQuery):
    def _get_by_uuid(self, uuid):
        return self._query().filter(self.model.uuid == uuid)

    def get_by_uuid(self, uuid):
        return self._get_by_uuid(uuid).one()


class Command(BaseCommand):
    pass
