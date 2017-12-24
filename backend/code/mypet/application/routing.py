from sapp.plugins.pyramid.routing import Routing


class MypetRouting(Routing):
    def make(self):
        self.add('mypet.home.controllers.Home', 'home', '/')
        self.add('mypet.auth.controllers.LoginController', 'login', '/login')
        self.add('mypet.auth.controllers.LogoutController', 'logout', '/logout')
        self.add('mypet.auth.controllers.AuthDataController', 'auth', '/auth')
