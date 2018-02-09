from cashflow.application.drivers import ReadDriver
from cashflow.application.drivers import WriteDriver

from cashflow.auth.models import User


class UserReadDriver(ReadDriver):
    model = User

    def _get_by_email(self, email):
        return self.query().filter(self.model.email == email)

    def find_by_email(self, email):
        return self._get_by_email(email).first()


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
