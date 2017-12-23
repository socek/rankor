from sapp.plugins.pyramid.controller import RestfulController

from mypet.home.models import User


class Home(RestfulController):
    def get(self):
        self.context = {'elo': 1, 'users': list(self._get_users())}

    def _get_users(self):
        with self.application as context:
            for user in context.dbsession.query(User):
                yield user.name
