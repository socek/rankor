from bcrypt import checkpw
from bcrypt import gensalt
from bcrypt import hashpw
from sqlalchemy import Binary
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String

from rankor.application.model import Model


class User(Model):
    __tablename__ = 'users'

    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    password = Column(Binary(100), nullable=True)

    def set_password(self, password):
        self.password = hashpw(password.encode('utf8'), gensalt())

    def validate_password(self, password):
        if self.password:
            password = password.encode('utf8')
            return checkpw(password, self.password)
        else:
            return False


