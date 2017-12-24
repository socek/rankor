from marshmallow import ValidationError
from pyramid.security import forget
from pyramid.security import remember
from sapp.plugins.pyramid.controller import HttpController
from sapp.plugins.pyramid.controller import RestfulController
from sqlalchemy.orm.exc import NoResultFound

from mypet.auth.drivers import UserReadDriver
from mypet.auth.schemas import LoginSchema
from mypet import app


class LoginController(HttpController):
    renderer = 'mypet.auth:templates/login.jinja2'

    def get(self):
        self.context['errors'] = {}
        self.context['form'] = {}

    def post(self):
        self.get()

        fields = self.request.POST
        self.context['form'] = fields
        try:
            LoginSchema(strict=True).load(fields)
            if self.authenticated(fields):
                self.on_success(fields)
            else:
                self.on_fail()
        except ValidationError as err:
            self.context['errors'] = err.messages
            return

    def authenticated(self, fields):
        with app as context:
            driver = UserReadDriver(context.dbsession)
            try:
                user = driver.get_by_email(fields['email'])
                self.user_id = user.id
                return user.validate_password(fields['password'])
            except NoResultFound:
                # user can not be authenticated if he/she does not exists
                return False

    def on_success(self, fields):
        self.context['form_error'] = ''
        self.context['validate'] = True
        headers = remember(self.request, self.user_id)
        self.request.response.headerlist.extend(headers)
        self.redirect('auth')

    def on_fail(self):
        self.context['validate'] = False
        self.context['form_error'] = "Username and/or password do not match."


class LogoutController(HttpController):
    def get(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False
        self.redirect('auth')


class AuthDataController(RestfulController):
    def get(self):
        self.context[
            'is_authenticated'] = self.request.authenticated_userid is not None
