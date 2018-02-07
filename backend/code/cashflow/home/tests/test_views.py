from pytest import fixture

from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from cashflow.home.views import Home


class TestHome(ControllerFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return Home(mroot_factory, mrequest)

    def test_get(self, view):
        """
        This is sample test.
        """
        assert view.get() == {'elo': 1}
