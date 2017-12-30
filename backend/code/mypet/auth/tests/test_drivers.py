from pytest import fixture

from sapp.plugins.sqlalchemy.migration import recreate_database
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from mypet.application.app import MypetConfigurator
from mypet.auth.drivers import UserReadDriver
from mypet.auth.drivers import UserWriteDriver
from mypet.auth.models import User


class IntegrationFixture(BaseIntegrationFixture):
    CONFIGURATOR_CLASS = MypetConfigurator

    @fixture(scope="module")
    def config(self):
        """
        This fixture will create full configurator object. It can be use for
        accessing app during the tests.
        """
        key = 'config'
        if key not in self.SESSION_CACHE:
            config = self.CONFIGURATOR_CLASS()
            config.start('tests')

            recreate_database(config.dbplugins['dbsession'],
                              config.settings['paths']['alembic:migrations'])

            self.SESSION_CACHE[key] = config
        return self.SESSION_CACHE[key]

    @fixture
    def app(self, config):
        with config as app:
            yield app


class TestUserReadDriver(IntegrationFixture):
    email = 'user1@my.pl'

    @fixture
    def user1(self, app):
        user = User(
            name='user1',
            email=self.email,
            is_admin=False,
            password='mypassword')
        app.dbsession.add(user)
        app.dbsession.flush()

        yield user

        app.dbsession.rollback()

    @fixture
    def driver(self, app):
        return UserReadDriver(app.dbsession)

    def test_find_by_email(self, driver, user1):
        assert driver.find_by_email(self.email).id == user1.id

    def test_find_by_email_with_no_user(self, driver):
        assert driver.find_by_email(self.email) is None


class TestUserWriteDriver(IntegrationFixture):
    data = dict(
        name='user1',
        email='user1@my.pl',
        is_admin=False,
        password='mypassword')

    @fixture
    def driver(self, app):
        yield UserWriteDriver(app.dbsession)
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
