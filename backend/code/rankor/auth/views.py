from pyramid.httpexceptions import HTTPBadRequest
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
            return {'jwt': encode_jwt_from_user(user)}
        else:
            raise HTTPBadRequest(
                json={'_schema': ['Username and/or password do not match.']})

    def get_authenticated_user(self, fields):
        user = self.query.find_by_email(fields['email'])
        if user and user.validate_password(fields['password']):
            return user


class SignUpView(RestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def command(self, dbsession):
        return UserCommand(dbsession)

    def post(self):
        fields = self.get_validated_fields(SignUpSchema)
        try:
            user = self.create_user(fields)
            return {'jwt': encode_jwt_from_user(user)}
        except IntegrityError:
            raise HTTPBadRequest(
                json={'_schema': ['User with that email already exists']})

    def create_user(self, fields):
        return self.command.create(
            email=fields['email'], password=fields['password'])
