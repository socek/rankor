from pyramid.security import forget
from pyramid.security import remember
from sapp.plugins.pyramid.controller import RestfulController

from mypet import app
from mypet.application.forms import FormSerializer
from mypet.auth.drivers import UserReadDriver
from mypet.auth.schemas import LoginSchema


class LoginController(RestfulController):
    def post(self):
        form = FormSerializer(LoginSchema())
        form.parse_json(self.request.json_body)
        self.context['form'] = form.fullform

        if form.validate():
            user_id = self.authenticated_user_id(form.fields())
            if user_id:
                self.on_success(form, user_id)
            else:
                self.on_fail(form)

    def authenticated_user_id(self, fields):
        with app as context:
            driver = UserReadDriver(context.dbsession)
            user = driver.find_by_email(fields['email'])
            if user and user.validate_password(fields'password']):
                return user.id

    def on_success(self, form, user_id):
        headers = remember(self.request, user_id)
        self.request.response.headerlist.extend(headers)
        form.set_form_ok()

    def on_fail(self, form):
        form.set_form_error('Username and/or password do not match.')


class LogoutController(RestfulController):
    def get(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False


class AuthDataController(RestfulController):
    def get(self):
        self.context[
            'is_authenticated'] = self.request.authenticated_userid is not None
