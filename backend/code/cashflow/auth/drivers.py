from sapp.plugins.sqlalchemy.driver import ReadDriver
from sapp.plugins.sqlalchemy.driver import WriteDriver

from cashflow.auth.models import User


class UserReadDriver(ReadDriver):
    model = User

    def _get_by_email(self, email):
        return self.query().filter(self.model.email == email)

    def get_by_uuid(self, uuid):
        return self.query().filter(self.model.uuid == uuid).one()

    def find_by_email(self, email):
        return self._get_by_email(email).first()

    def get_id_by_uuid(self, uuid):
        return self.database.query(self.model).filter(self.model.uuid == uuid).one().id


class UserWriteDriver(WriteDriver):
    model = User

    def create(self, **kwargs):
        password = None
        obj = self.model()
        password = kwargs.pop('password', None)

        for key, value in kwargs.items():
            setattr(obj, key, value)

        if password:
            obj.set_password(password)

        self.database.add(obj)
        self.database.commit()

        return obj
