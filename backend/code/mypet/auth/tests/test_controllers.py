from pytest import fixture
from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from mypet.auth.controllers import AuthDataController
from mypet.auth.controllers import LoginController
from mypet.auth.controllers import LogoutController


class TestAuthDataController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return AuthDataController(mroot_factory, mrequest)

    def test_get(self, ctrl, mrequest):
        """
        .get should return information about authentication status
        """
        mrequest.method = 'GET'

        assert ctrl() == {'is_authenticated': True}


class TestLoginController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return LoginController(mroot_factory, mrequest)


class TestLogoutController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return LogoutController(mroot_factory, mrequest)
