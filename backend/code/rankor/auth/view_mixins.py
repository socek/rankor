from sapp.decorators import WithContext
from pyramid.httpexceptions import HTTPUnauthorized

from rankor import app
from rankor.auth.drivers import UserQuery
from rankor.auth.jwt import decode_jwt


class AuthMixin(object):
    @WithContext(app, args=['dbsession'])
    def get_user(self, dbsession):
        # TODO: think about caching this per request or context?
        user_rd = UserQuery(dbsession)

        payload = self.decoded_jwt()
        return user_rd.get_by_uuid(payload['uuid'])

    def is_authenticated(self):
        return self.request.headers.get('JWT') is not None

    def get_user_id(self):
        return self.decoded_jwt()['id']

    def get_user_uuid(self):
        return self.decoded_jwt()['uuid']

    def decoded_jwt(self):
        jwt = self.request.headers.get('JWT')
        if jwt:
            return decode_jwt(jwt)
        else:
            raise HTTPUnauthorized()
