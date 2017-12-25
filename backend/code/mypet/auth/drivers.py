from sapp.plugins.sqlalchemy.driver import ReadDriver
from sapp.plugins.sqlalchemy.driver import WriteDriver
from sqlalchemy.orm.exc import NoResultFound

from mypet.auth.models import User


class UserReadDriver(ReadDriver):
    model = User

    def get_by_email(self, email):
        return self.query().filter(self.model.email == email).one()

    def get_user_id(self, email, password):
        try:
            user = self.get_by_email(email)
            if user.validate_password(password):
                return user.id
        except NoResultFound:
            # user can not be authenticated if he/she does not exists
            return


class UserWriteDriver(WriteDriver):
    model = User

    def create(self, **kwargs):
        password = None
        obj = self.model()
        if 'password' in kwargs:
            password = kwargs.pop('password')

        for key, value in kwargs.items():
            setattr(obj, key, value)

        if password:
            obj.set_password(password)

        self.database.add(obj)
        self.database.commit()

        return obj
