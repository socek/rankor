from marshmallow import ValidationError
from pyramid.security import forget
from pyramid.security import remember
from sapp.plugins.pyramid.controller import RestfulController
from sqlalchemy.orm.exc import NoResultFound

from mypet import app
from mypet.auth.drivers import UserReadDriver
from mypet.auth.schemas import LoginSchema


class FormSerializer(object):
    schema = LoginSchema

    def __init__(self):
        self._create_clean_form()

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
        try:
            self.schema(strict=True).load(self.fields())
            self.set_form_error(None)
            return True
        except ValidationError as err:
            for name, errors in err.messages.items():
                self.fullform['fields'][name]['error'] = errors[0]
            return False

    def set_form_error(self, error):
        self.fullform['validated'] = False
        self.fullform['error'] = error

    def set_form_ok(self):
        self.fullform['validated'] = True


class LoginController(RestfulController):
    def post(self):
        form = FormSerializer()
        form.parse_json(self.request.json_body)
        self.context['form'] = form.fullform

        if form.validate():
            if self.authenticated(form.fields()):
                self.on_success(form)
            else:
                self.on_fail(form)

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

    def on_success(self, form):
        headers = remember(self.request, self.user_id)
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
