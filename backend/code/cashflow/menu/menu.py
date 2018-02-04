from cashflow.menu.models import Menu
from cashflow.menu.models import MenuElement


class CashflowMenu(Menu):

    def make_menu(self):
        with self.add('Dashboard') as main:
            main.add(MenuElement('dashboard_home', 'Home', '#/'))
