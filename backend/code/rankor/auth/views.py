from pyramid.security import forget
from pyramid.security import remember
from sapp.plugins.pyramid.controller import RestfulController
from sapp.decorators import WithContext

from rankor import app
from rankor.application.forms import FormSerializer
from rankor.auth.drivers import UserQuery
from rankor.auth.schemas import LoginSchema

GROUPS = ['authenticated']


class LoginController(RestfulController):
    def post(self):
        form = FormSerializer(LoginSchema())
        form.parse_json(self.request.json_body)

        if form.validate():
            user_id = self.authenticated_user_id(form.fields())
            if user_id:
                self.on_success(form, user_id)
            else:
                self.on_fail(form, 'Username and/or password do not match.')
        else:
            self.on_fail(form)

        return dict(form=form.fullform)

    @WithContext(app, args=['dbsession'])
    def authenticated_user_id(self, fields, dbsession):
        driver = UserQuery(dbsession)
        user = driver.find_by_email(fields['email'])
        if user and user.validate_password(fields['password']):
            return user.id

    def on_success(self, form, user_id):
        headers = remember(self.request, user_id)
        self.request.response.headerlist.extend(headers)
        form.set_form_ok()

    def on_fail(self, form, message=None):
        if message:
            form.set_form_error(message)
        self.request.response.status_code = 400


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
