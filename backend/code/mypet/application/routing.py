from sapp.plugins.pyramid.routing import Routing

from mypet.menu.routing import meny_routing
from mypet.home.routing import home_routing
from mypet.auth.routing import auth_routing


class MypetRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
