from rankor import app


def uwsgi(settings):
    app.start('pyramid')
    return app.make_wsgi_object()


def tests(settings):
    app.start('tests')
