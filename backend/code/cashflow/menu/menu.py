from cashflow.menu.models import Menu
from cashflow.menu.models import MenuElement
from cashflow.auth.view_mixins import AuthMixin


class CashflowMenu(Menu, AuthMixin):

    def make_menu(self):
        if self.is_authenticated():
            with self.add('Dashboard') as main:
                main.add(MenuElement('dashboard_home', 'Wallets', '#/dashboard'))
        else:
            with self.add('Menu') as main:
                main.add(MenuElement('not_logged_home', 'Home', '#/'))
