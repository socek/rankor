from pytest import fixture

from sapp.plugins.pyramid.testing import BaseWebTestFixture
from sapp.plugins.sqlalchemy.migration import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture

from rankor.application.app import RankorConfigurator
from rankor.auth.models import User
from rankor.contest.models import Contest


class DeleteOnExit(object):
    def __init__(self, dbsession, obj):
        self.obj = obj
        self.dbsession = dbsession

    def __enter__(self):
        self.dbsession.add(self.obj)
        self.dbsession.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.dbsession.delete(self.obj)
        self.dbsession.commit()


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

    contest_user_data = {
        'name': 'contest1 from user1',
    }

    contest_second_user_data = {
        'name': 'contest1 from user2',
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

        with DeleteOnExit(dbsession, user):
            yield user

    @fixture
    def second_user(self, dbsession):
        user_data = dict(self.second_user_data)
        password = user_data.pop('password')
        user = User(**self.second_user_data)
        user.set_password(password)

        with DeleteOnExit(dbsession, user):
            yield user

    @fixture
    def contest_from_user(self, dbsession, user):
        contest_data = dict(self.contest_user_data)
        contest_data['owner'] = user
        contest = Contest(**contest_data)

        with DeleteOnExit(dbsession, contest):
            yield contest

    @fixture
    def contest_from_second_user(self, dbsession, second_user):
        contest_data = dict(self.contest_second_user_data)
        contest_data['owner'] = second_user
        contest = Contest(**contest_data)

        with DeleteOnExit(dbsession, contest):
            yield contest


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

        with DeleteOnExit(dbsession, user):
            yield user

    @fixture
    def jwt(self, authenticated_user, fake_app):
        user_data = dict(self.authenticated_user_data)
        params = dict(email=user_data['email'], password=user_data['password'])
        result = fake_app.post_json(self.login_url, params=params, status=200)
        return result.json_body['jwt']
