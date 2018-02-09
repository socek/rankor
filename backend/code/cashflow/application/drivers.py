from sapp.plugins.sqlalchemy.driver import ReadDriver as BaseReadDriver
from sapp.plugins.sqlalchemy.driver import WriteDriver as BaseWriteDriver


class ReadDriver(BaseReadDriver):
    def get_by_uuid(self, uuid):
        return self.query().filter(self.model.uuid == uuid).one()


class WriteDriver(BaseWriteDriver):
    pass
