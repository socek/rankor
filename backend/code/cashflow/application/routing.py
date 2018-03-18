from sapp.plugins.pyramid.routing import Routing

from rankor.auth.routing import auth_routing
from rankor.home.routing import home_routing
from rankor.menu.routing import meny_routing
from rankor.wallet.routing import wallet_routing


class RankorRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
        wallet_routing(self)
