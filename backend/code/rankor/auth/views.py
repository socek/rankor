from pyramid.httpexceptions import HTTPBadRequest
from pyramid.security import forget
from pyramid.security import remember
from sapp.decorators import WithContext
from sqlalchemy.exc import IntegrityError

from rankor import app
from rankor.application.views import RestfulController
from rankor.auth.drivers import UserCommand
from rankor.auth.drivers import UserQuery
from rankor.auth.jwt import encode_jwt_from_user
from rankor.auth.schemas import LoginSchema
from rankor.auth.schemas import SignUpSchema

GROUPS = ['authenticated']


class LoginController(RestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def query(self, dbsession):
        return UserQuery(dbsession)

    def post(self):
        fields = self.get_validated_fields(LoginSchema)
        user = self.get_authenticated_user(fields)
        if user:
            self.on_success(user.id)
            return {'jwt': encode_jwt_from_user(user)}
        else:
            raise HTTPBadRequest(
                json={'_schema': ['Username and/or password do not match.']})

    def get_authenticated_user(self, fields):
        user = self.query.find_by_email(fields['email'])
        if user and user.validate_password(fields['password']):
            return user

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


class SignUpView(RestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def command(self, dbsession):
        return UserCommand(dbsession)

    def post(self):
        fields = self.get_validated_fields(SignUpSchema)
        try:
            user = self.create_user(fields)
            self.on_success(user.id)
            return {'jwt': encode_jwt_from_user(user)}
        except IntegrityError:
            raise HTTPBadRequest(
                json={'_schema': ['User with that email already exists']})

    def create_user(self, fields):
        return self.command.create(
            email=fields['email'], password=fields['password'])

    def on_success(self, user_id):
        headers = remember(self.request, user_id)
        self.request.response.headerlist.extend(headers)
