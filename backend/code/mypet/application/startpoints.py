from mypet import app


def uwsgi(settings):
    app.start('pyramid')
    return app.start_pyramid()


def tests(settings):
    app.start('tests')
