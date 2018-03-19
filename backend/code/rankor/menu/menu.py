from rankor.menu.models import Menu
from rankor.menu.models import MenuElement
from rankor.auth.view_mixins import AuthMixin


class RankorMenu(Menu, AuthMixin):

    def make_menu(self):
        if self.is_authenticated():
            with self.add('Dashboard') as main:
                main.add(MenuElement('dashboard_home', 'Wallets', '#/dashboard'))
        else:
            with self.add('Menu') as main:
                main.add(MenuElement('not_logged_home', 'Home', '#/'))
