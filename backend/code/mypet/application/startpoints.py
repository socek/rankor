from mypet import app


def uwsgi(settings):
    return app.start_pyramid()


def tests(settings):
    app.start('tests')
