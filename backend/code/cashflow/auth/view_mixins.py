from pyramid.security import authenticated_userid
from sapp.decorators import WithContext

from cashflow import app
from cashflow.auth.drivers import UserReadDriver


class AuthMixin(object):
    @WithContext(app, args=['dbsession'])
    def get_user(self, dbsession):
        user_id = authenticated_userid(self.request)
        user_rd = UserReadDriver(dbsession)
        return user_rd.get_by_id(user_id)
