from pytest import fixture

from sapp.plugins.pyramid.testing import BaseWebTestFixture
from sapp.plugins.sqlalchemy.migration import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from cashflow.application.app import CashflowConfigurator
from cashflow.auth.models import User
from cashflow.wallet.models import Wallet


class CashflowFixturesMixin(object):
    CONFIGURATOR_CLASS = CashflowConfigurator

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
    def wallet(self, user, dbsession):
        wallet = Wallet(name='my wallet', user=user)

        dbsession.add(wallet)
        dbsession.commit()

        yield wallet

        dbsession.delete(wallet)


class IntegrationFixture(CashflowFixturesMixin, BaseIntegrationFixture):
    pass


class WebTestFixture(CashflowFixturesMixin, BaseWebTestFixture):
    pass
