from sapp.plugins.pyramid.routing import Routing

from rankor.auth.routing import auth_routing
from rankor.contest.routing import contest_routing
from rankor.home.routing import home_routing
from rankor.menu.routing import meny_routing


class RankorRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
        contest_routing(self)
