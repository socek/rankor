def auth_routing(routing):
    routing.add(
        'mypet.auth.controllers.LoginController',
        'login',
        '/auth/login')
    routing.add(
        'mypet.auth.controllers.LogoutController',
        'logout',
        '/auth/logout')
    routing.add(
        'mypet.auth.controllers.AuthDataController',
        'auth',
        '/auth')
