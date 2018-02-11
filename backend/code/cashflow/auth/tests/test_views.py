from pytest import fixture
from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from cashflow.auth.views import AuthDataController
from cashflow.auth.views import LoginController
from cashflow.auth.views import LogoutController


class TestAuthDataController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return AuthDataController(mroot_factory, mrequest)

    def test_get(self, ctrl, mrequest):
        """
        .get should return information about authentication status
        """
        mrequest.method = 'GET'

        assert ctrl() == {'is_authenticated': True, 'groups': ['authenticated']}


class TestLoginController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return LoginController(mroot_factory, mrequest)


class TestLogoutController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return LogoutController(mroot_factory, mrequest)
