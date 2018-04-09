def auth_routing(routing):
    routing.add(
        'rankor.auth.views.LoginController',
        'login',
        '/auth/login')
    routing.add(
        'rankor.auth.views.SignUpView',
        'sign_up',
        '/auth/signup')
