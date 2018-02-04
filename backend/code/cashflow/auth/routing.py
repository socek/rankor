def auth_routing(routing):
    routing.add(
        'cashflow.auth.views.LoginController',
        'login',
        '/auth/login')
    routing.add(
        'cashflow.auth.views.LogoutController',
        'logout',
        '/auth/logout')
    routing.add(
        'cashflow.auth.views.AuthDataController',
        'auth',
        '/auth')
