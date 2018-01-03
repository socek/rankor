from sapp.plugins.pyramid.controller import RestfulController

from mypet.menu.menu import MypetMenu


class Menu(RestfulController):
    def get(self):
        return dict(menu=MypetMenu(self.request).serialize())
