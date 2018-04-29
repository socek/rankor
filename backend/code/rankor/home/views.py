from sapp.plugins.pyramid.views import RestfulView


class Home(RestfulView):
    def get(self):
        return {}

