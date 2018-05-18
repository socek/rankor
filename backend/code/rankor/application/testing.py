from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from unittest.mock import patch

from pytest import fixture
from sapp.plugins.pyramid.testing import BaseWebTestFixture
from sapp.plugins.pyramid.testing import ViewFixtureMixin
from sapp.plugins.sqlalchemy.recreate import RecreateDatabases
from sapp.plugins.sqlalchemy.testing import BaseIntegrationFixture
from sqlalchemy.exc import InvalidRequestError

from rankor.application.app import RankorConfigurator
from rankor.auth.models import User
from rankor.contest.models import Contest
from rankor.game.models import Game


class DeleteOnExit(object):
    def __init__(self, dbsession, obj):
        self.obj = obj
        self.dbsession = dbsession

    def __enter__(self):
        self.dbsession.add(self.obj)
        self.dbsession.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        self.dbsession.delete(self.obj)
        try:
            self.dbsession.commit()
        except InvalidRequestError:
            self.dbsession.rollback()


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

    game_user_data = {
        'name': 'first game',
    }

    game_second_user_data = {
        'name': 'second game',
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

    @fixture
    def game_from_user(self, dbsession, user, contest_from_user):
        game_data = dict(self.game_user_data)
        game_data['owner'] = user
        game_data['contest'] = contest_from_user
        game = Game(**game_data)

        with DeleteOnExit(dbsession, game):
            yield game

    @fixture
    def game_from_second_user(self, dbsession, second_user, contest_from_user):
        game_data = dict(self.game_second_user_data)
        game_data['owner'] = second_user
        game_data['contest'] = contest_from_user
        game = Game(**game_data)

        with DeleteOnExit(dbsession, game):
            yield game


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


class DictLike(object):
    def __init__(self, data=None, **kwargs):
        data = dict(data)
        data.update(kwargs)
        for name, value in data.items():
            setattr(self, name, value)

    def __getitem__(self, name):
        return getattr(self, name)


class ViewFixture(ViewFixtureMixin):
    _view = None

    @fixture
    def view(self, mroot_factory, mrequest):
        return self._view(mroot_factory, mrequest)

    @fixture
    def mrequest(self):
        request = MagicMock()
        request._cache = {}
        return request

    @fixture
    def matchdict(self, mrequest):
        mrequest.matchdict = {}
        return mrequest.matchdict

    @fixture
    def mdbsession(self, view):
        with patch.object(
                self._view, 'dbsession', new_callable=PropertyMock) as mock:
            yield mock.return_value

    @fixture
    def mget_user(self, view):
        with patch.object(view, 'get_user', autospec=True) as mock:
            yield mock
