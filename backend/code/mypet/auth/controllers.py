from pyramid.security import forget
from pyramid.security import remember
from sapp.plugins.pyramid.controller import RestfulController

from mypet import app
from mypet.auth.drivers import UserReadDriver
from mypet.auth.schemas import LoginSchema


class FormSerializer(object):
    def __init__(self, schema):
        self._create_clean_form()
        self.schema = schema
        self.serialized = None

    def _create_clean_form(self):
        self.fullform = {
            'error': None,
            'validated': False,
            'fields': {},
        }

    def parse_json(self, json):
        for name, field in json.items():
            self.fullform['fields'][name] = {
                'error': None,
                'value': field['value'],
            }

    def fields(self):
        data = {}
        for name, field in self.fullform['fields'].items():
            data[name] = field['value']
        return data

    def validate(self):
        self.serialized, errors = self.schema.load(self.fields())
        if errors:
            for name, errors in errors.items():
                self.fullform['fields'][name]['error'] = errors[0]
            return False
        else:
            self.set_form_error(None)
            return True

    def set_form_error(self, error):
        self.fullform['validated'] = False
        self.fullform['error'] = error

    def set_form_ok(self):
        self.fullform['validated'] = True


class LoginController(RestfulController):
    def post(self):
        form = FormSerializer(LoginSchema())
        form.parse_json(self.request.json_body)
        self.context['form'] = form.fullform

        if form.validate():
            user_id = self.authenticated(form.fields())
            if user_id:
                self.on_success(form, user_id)
            else:
                self.on_fail(form)

    def authenticated(self, fields):
        with app as context:
            driver = UserReadDriver(context.dbsession)
            return driver.get_user_id(fields['email'], fields['password'])

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
