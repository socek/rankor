from sapp.plugins.pyramid.controller import RestfulController


class Home(RestfulController):
    def get(self):
        self.context = {'elo': 1}

