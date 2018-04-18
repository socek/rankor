from sapp.plugins.sqlalchemy.driver import ReadDriver as BaseQuery
from sapp.plugins.sqlalchemy.driver import WriteDriver as BaseCommand


class Query(BaseQuery):
    def _get_by_uuid(self, uuid):
        return self.query().filter(self.model.uuid == uuid)

    def get_by_uuid(self, uuid):
        return self._get_by_uuid(uuid).one()


class Command(BaseCommand):
    pass
