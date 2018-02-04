def auth_routing(routing):
    routing.add(
        'cashflow.auth.controllers.LoginController',
        'login',
        '/auth/login')
    routing.add(
        'cashflow.auth.controllers.LogoutController',
        'logout',
        '/auth/logout')
    routing.add(
        'cashflow.auth.controllers.AuthDataController',
        'auth',
        '/auth')
