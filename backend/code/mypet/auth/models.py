from bcrypt import checkpw
from bcrypt import gensalt
from bcrypt import hashpw
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from mypet.application.model import Model


class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    password = Column(String(100), nullable=True)

    def set_password(self, password):
        pwhash = hashpw(password.encode('utf8'), gensalt())
        self.password = pwhash.decode('utf8')

    def validate_password(self, password):
        if self.password:
            expected_hash = self.password.encode('utf8')
            password = password.encode('utf8')
            return checkpw(password, expected_hash)
        else:
            return False
