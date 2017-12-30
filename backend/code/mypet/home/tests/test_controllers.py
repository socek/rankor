from pytest import fixture

from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from mypet.home.controllers import Home


class TestHome(ControllerFixtureMixin):
    @fixture
    def controller(self, mroot_factory, mrequest):
        return Home(mroot_factory, mrequest)

    def test_get(self, controller):
        """
        This is sample test.
        """
        controller.get()

        assert controller.context == {'elo': 1}
