from sapp.plugins.pyramid.controller import RestfulController

from rankor.menu.menu import RankorMenu


class Menu(RestfulController):
    def get(self):
        return dict(menu=RankorMenu(self.request).serialize())
