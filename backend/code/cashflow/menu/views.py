from sapp.plugins.pyramid.controller import RestfulController

from cashflow.menu.menu import CashflowMenu


class Menu(RestfulController):
    def get(self):
        return dict(menu=CashflowMenu(self.request).serialize())
