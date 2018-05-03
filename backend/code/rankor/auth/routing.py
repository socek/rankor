def auth_routing(routing):
    routing.add(
        'rankor.auth.views.LoginView',
        'login',
        '/auth/login')
    routing.add(
        'rankor.auth.views.SignUpView',
        'sign_up',
        '/auth/signup')
