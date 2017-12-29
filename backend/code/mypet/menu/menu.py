from mypet.menu.models import Menu
from mypet.menu.models import MenuElement


class MypetMenu(Menu):

    def make_menu(self):
        with self.add('Dashboard') as main:
            main.add(MenuElement('dashboard_home', 'Home', '#/'))
