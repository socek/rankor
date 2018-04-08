from pytest import fixture

from sapp.plugins.pyramid.testing import BaseWebTestFixture
from sapp.plugins.sqlalchemy.migration import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from rankor.application.app import RankorConfigurator
from rankor.auth.models import User


class RankorFixturesMixin(object):
    CONFIGURATOR_CLASS = RankorConfigurator

    def after_configurator_start(self, config):
        paths = config.settings['paths']
        recreate = RecreateDatabases(config)
        recreate.append_database('dbsession', paths['alembic:migrations'])
        recreate.make()

    user_data = {
        'name': 'user1',
        'email': 'user1@my.pl',
        'is_admin': False,
        'password': 'mypassword',
    }

    second_user_data = {
        'name': 'user2',
        'email': 'user2@my.pl',
        'is_admin': False,
        'password': 'mypassword',
    }

    @fixture
    def dbsession(self, app):
        return app.dbsession

    @fixture
    def user(self, dbsession):
        user_data = dict(self.user_data)
        password = user_data.pop('password')
        user = User(**self.user_data)
        user.set_password(password)
        dbsession.add(user)
        dbsession.commit()

        yield user

        dbsession.delete(user)

    @fixture
    def second_user(self, dbsession):
        user_data = dict(self.second_user_data)
        password = user_data.pop('password')
        user = User(**self.second_user_data)
        user.set_password(password)
        dbsession.add(user)
        dbsession.commit()

        yield user

        dbsession.delete(user)


class IntegrationFixture(RankorFixturesMixin, BaseIntegrationFixture):
    pass


class WebTestFixture(RankorFixturesMixin, BaseWebTestFixture):
    login_url = '/auth/login'
    authenticated_user_data = {
        'name': 'user3',
        'email': 'user3@my.pl',
        'is_admin': False,
        'password': 'mypassword',
    }

    @fixture
    def authenticated_user(self, dbsession, fake_app):
        user_data = dict(self.authenticated_user_data)
        password = user_data.pop('password')
        user = User(**user_data)
        user.set_password(password)
        dbsession.add(user)
        dbsession.commit()

        params = dict(email=user_data['email'], password=password)
        fake_app.post_json(self.login_url, params=params, status=200)

        yield user

        dbsession.delete(user)

