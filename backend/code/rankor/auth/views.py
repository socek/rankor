from pyramid.httpexceptions import HTTPBadRequest
from pyramid.security import forget
from pyramid.security import remember
from sapp.decorators import WithContext
from sqlalchemy.exc import IntegrityError

from rankor import app
from rankor.application.views import RestfulController
from rankor.auth.drivers import UserCommand
from rankor.auth.drivers import UserQuery
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
        user_id = self.get_authenticated_user_id(fields)
        if user_id:
            self.on_success(user_id)
        else:
            raise HTTPBadRequest(
                json={'_schema': ['Username and/or password do not match.']})

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


class SignUpView(RestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def dbsession(self, dbsession):
        return dbsession

    @property
    def command(self):
        return UserCommand(self.dbsession)

    def post(self):
        fields = self.get_validated_fields(SignUpSchema)
        with app:  # This is for managing transaction
            try:
                user_id = self.create_user(fields)
            except IntegrityError:
                raise HTTPBadRequest(
                    json={'_schema': ['User with that email already exists']})
        self.on_success(user_id)

    def create_user(self, fields):
        user = self.command.create(
            email=fields['email'], password=fields['password'])
        return user.id

    def on_success(self, user_id):
        headers = remember(self.request, user_id)
        self.request.response.headerlist.extend(headers)
