from pytest import fixture

from sapp.plugins.pyramid.testing import BaseWebTestFixture
from sapp.plugins.sqlalchemy.migration import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from mypet.application.app import MypetConfigurator
from mypet.auth.models import User


class MypetFixturesMixin(object):
    CONFIGURATOR_CLASS = MypetConfigurator

    def after_configurator_start(self, config):
        paths = config.settings['paths']
        recreate = RecreateDatabases(config)
        recreate.append_database('dbsession', paths['alembic:migrations'])
        recreate.make()

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


class IntegrationFixture(MypetFixturesMixin, BaseIntegrationFixture):
    pass


class WebTestFixture(MypetFixturesMixin, BaseWebTestFixture):
    pass
