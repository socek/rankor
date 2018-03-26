from pyramid.httpexceptions import HTTPBadRequest
from pyramid.security import forget
from pyramid.security import remember
from sapp.decorators import WithContext

from rankor import app
from rankor.application.views import RestfulController
from rankor.auth.drivers import UserQuery
from rankor.auth.schemas import LoginSchema

GROUPS = ['authenticated']


class LoginController(RestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def query(self, dbsession):
        return UserQuery(dbsession)

    def post(self):
        fields = self.get_validated_fields(LoginSchema)
        user_id = self.get_authenticated_user_id(fields)
        if user_id:
            self.on_success(user_id)
        else:
            raise HTTPBadRequest(
                json={'_form': ['Username and/or password do not match.']})

    def get_authenticated_user_id(self, fields):
        user = self.query.find_by_email(fields['email'])
        if user and user.validate_password(fields['password']):
            return user.id

    def on_success(self, user_id):
        headers = remember(self.request, user_id)
        self.request.response.headerlist.extend(headers)


class LogoutController(RestfulController):
    def get(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        return dict(is_authenticated=False, groups=[])


class AuthDataController(RestfulController):
    def get(self):
        is_authenticated = self.request.authenticated_userid is not None
        groups = GROUPS if is_authenticated else []
        return dict(is_authenticated=is_authenticated, groups=groups)
