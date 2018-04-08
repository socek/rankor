def auth_routing(routing):
    routing.add(
        'rankor.auth.views.LoginController',
        'login',
        '/auth/login')
    routing.add(
        'rankor.auth.views.LogoutController',
        'logout',
        '/auth/logout')
    routing.add(
        'rankor.auth.views.AuthDataController',
        'auth',
        '/auth')
    routing.add(
        'rankor.auth.views.SignUpView',
        'sign_up',
        '/auth/signup')
