from sapp.plugins.pyramid.views import RestfulView

from rankor.menu.menu import RankorMenu


class Menu(RestfulView):
    def get(self):
        return dict(menu=RankorMenu(self.request).serialize())
