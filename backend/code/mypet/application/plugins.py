from sapp.plugin import Plugin

from mypet.home.controllers import Home


class Routing(Plugin):
    def start_pyramid(self, pyramid):
        pyramid.add_route('home', '/')
        pyramid.add_view(Home, renderer='json', route_name='home')
