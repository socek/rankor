from pytest import fixture

from rankor.application.testing import IntegrationFixture
from rankor.auth.drivers import UserQuery
from rankor.auth.drivers import UserCommand
from rankor.auth.models import User


class TestUserQuery(IntegrationFixture):
    @fixture
    def driver(self, app):
        return UserQuery(app.dbsession)

    def test_find_by_email(self, driver, user):
        assert driver.find_by_email(self.user_data['email']).id == user.id

    def test_find_by_email_with_no_user(self, driver):
        assert driver.find_by_email(self.user_data['email']) is None


class TestUserCommand(IntegrationFixture):
    data = dict(
        name='user1',
        email='user1@my.pl',
        is_admin=False,
        password='mypassword')

    @fixture
    def driver(self, app):
        yield UserCommand(app.dbsession)
        app.dbsession.commit()

    def test_create(self, driver, app):
        """
        .create should create user in database and hash the password.
        """
        user = driver.create(**self.data)

        assert app.dbsession.query(User).filter(User.id == user.id).one()
        assert user.password != self.data['password']
        app.dbsession.delete(user)

    def test_create_with_no_password(self, driver, app):
        """
        .create should create user even without password
        """
        data = dict(self.data)
        data.pop('password')

        user = driver.create(**data)
        assert app.dbsession.query(User).filter(User.id == user.id).one()
        assert not user.password

        app.dbsession.delete(user)
