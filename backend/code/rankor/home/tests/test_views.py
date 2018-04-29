from pytest import fixture

from sapp.plugins.pyramid.testing import ViewFixtureMixin

from rankor.home.views import Home


class TestHome(ViewFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return Home(mroot_factory, mrequest)

    def test_get(self, view):
        """
        This is sample test.
        """
        assert view.get() == {}
