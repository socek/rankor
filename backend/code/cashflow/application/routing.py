from sapp.plugins.pyramid.routing import Routing

from cashflow.menu.routing import meny_routing
from cashflow.home.routing import home_routing
from cashflow.auth.routing import auth_routing


class CashflowRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
