from rankor.application.drivers import Query
from rankor.application.drivers import Command

from rankor.auth.models import User


class UserQuery(Query):
    model = User

    def _get_by_email(self, email):
        return self._query().filter(self.model.email == email)

    def find_by_email(self, email):
        return self._get_by_email(email).first()


class UserCommand(Command):
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
