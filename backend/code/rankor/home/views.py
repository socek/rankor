from sapp.plugins.pyramid.controller import RestfulController


class Home(RestfulController):
    def get(self):
        return {'elo': 1}

