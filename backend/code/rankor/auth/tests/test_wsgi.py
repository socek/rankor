from unittest.mock import patch
from uuid import uuid4

from pytest import fixture

from rankor.application.testing import WebTestFixture
from rankor.auth.jwt import encode_jwt_from_user


class TestWebAuthView(WebTestFixture):
    url = '/auth'
    login_url = '/auth/login'

    # TODO: remove database from this tests

    def test_login_with_bad_email(self, fake_app):
        """
        /auth/login should return error when bad email was provided.
        """
        params = dict(email='mycreazy', password='x')

        result = fake_app.post_json(self.login_url, params=params, status=400)

        assert result.json == {
            'email': ['Not a valid email address.'],
        }

    def test_login_with_bad_credentials(self, fake_app, user):
        """
        /auth/login should return error when bad email was provided.
        """
        params = dict(email=user.email, password='x')

        result = fake_app.post_json(self.login_url, params=params, status=400)

        assert result.json == {
            '_schema': ['Username and/or password do not match.'],
        }

    def test_login_with_good_credentials(self, fake_app, user):
        """
        /auth/login should login the user on good credentials
        """
        params = dict(
            email=self.user_data['email'], password=self.user_data['password'])

        result = fake_app.post_json(self.login_url, params=params, status=200)

        assert result.json == {'jwt': encode_jwt_from_user(user)}


class TestWebSignUpFormView(WebTestFixture):
    url = '/auth/signup'

    @fixture
    def mcommand(self):
        with patch('rankor.auth.views.UserCommand') as mock:
            yield mock.return_value

    def test_signup_happy_path(self, fake_app, mcommand):
        """
        /auth/signup should create a proper formed user
        """
        new_user = {
            'email': 'new@email.com',
            'password': 'fake1',
            'confirmPassword': 'fake1',
        }
        mcommand.return_value.id = 10
        muser = mcommand.create.return_value
        muser.id = uuid4()

        result = fake_app.post_json(self.url, params=new_user)

        mcommand.create.assert_called_once_with(
            email='new@email.com', password='fake1')

        assert result.json_body == {'jwt': encode_jwt_from_user(muser)}
