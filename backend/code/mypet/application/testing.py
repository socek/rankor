from pytest import fixture
from webtest import TestApp

from sapp.plugins.sqlalchemy.migration import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from mypet.application.app import MypetConfigurator
from mypet.auth.models import User


class IntegrationFixture(BaseIntegrationFixture):
    CONFIGURATOR_CLASS = MypetConfigurator
    key = 'config'

    def after_configurator_start(self, config):
        paths = config.settings['paths']
        recreate = RecreateDatabases(config)
        recreate.append_database('dbsession', paths['alembic:migrations'])
        recreate.make()

    @fixture(scope="module")
    def config(self):
        """
        This fixture will create full configurator object. It can be use for
        accessing app during the tests.
        """
        if self.key not in self.SESSION_CACHE:
            config = self.CONFIGURATOR_CLASS()
            wsgi = config.start_pyramid(startpoint='tests')
            self.SESSION_CACHE[self.key] = config
            self.SESSION_CACHE[self.key + '_wsgi'] = wsgi
            self.after_configurator_start(config)
        return self.SESSION_CACHE[self.key]

    user_data = {
        'name': 'user',
        'email': 'user1@my.pl',
        'is_admin': False,
        'password': 'mypassword',
    }

    @fixture
    def user(self, app):
        user_data = dict(self.user_data)
        password = user_data.pop('password')
        user = User(**self.user_data)
        user.set_password(password)
        app.dbsession.add(user)
        app.dbsession.commit()

        yield user

        app.dbsession.delete(user)


class WebTestFixture(IntegrationFixture):
    @fixture(scope='module')
    def wsgi_app(self, config):
        return self.SESSION_CACHE[self.key + '_wsgi']

    @fixture
    def fake_app(self, wsgi_app):
        return TestApp(wsgi_app)
