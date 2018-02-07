from sapp.plugins.pyramid.routing import Routing

from cashflow.auth.routing import auth_routing
from cashflow.home.routing import home_routing
from cashflow.menu.routing import meny_routing
from cashflow.wallet.routing import wallet_routing


class CashflowRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
        wallet_routing(self)
