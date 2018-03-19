from pyramid.security import authenticated_userid
from sapp.decorators import WithContext

from rankor import app
from rankor.auth.drivers import UserQuery


class AuthMixin(object):
    @WithContext(app, args=['dbsession'])
    def get_user(self, dbsession):
        # TODO: think about caching this per request or context?
        user_rd = UserQuery(dbsession)
        return user_rd.get_by_id(self.get_user_id())

    def get_user_id(self):
        return authenticated_userid(self.request)

    def is_authenticated(self):
        return authenticated_userid(self.request) is not None
