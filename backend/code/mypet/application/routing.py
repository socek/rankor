from sapp.plugins.pyramid.routing import Routing


class MypetRouting(Routing):
    def make(self):
        self.add('mypet.home.controllers.Home', 'home', '/')
        self.add('mypet.auth.controllers.LoginController', 'login', '/auth/login')
        self.add('mypet.auth.controllers.LogoutController', 'logout', '/auth/logout')
        self.add('mypet.auth.controllers.AuthDataController', 'auth', '/auth')
