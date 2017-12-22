from mypet import app


def uwsgi(settings):
    return app.start_pyramid()
