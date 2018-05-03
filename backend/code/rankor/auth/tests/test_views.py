from unittest.mock import patch

from pyramid.httpexceptions import HTTPBadRequest
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ViewFixtureMixin
from sqlalchemy.exc import IntegrityError

from rankor.auth.views import LoginView
from rankor.auth.views import SignUpView


class TestLoginView(ViewFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return LoginView(mroot_factory, mrequest)


class TestSignUpView(ViewFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return SignUpView(mroot_factory, mrequest)

    @fixture
    def mcreate_user(self, view):
        with patch.object(view, 'create_user') as mock:
            yield mock

    def test_post_on_integrity_error(self, view, mcreate_user, mrequest):
        """
        .post should raise HTTPBadRequest when integrity error raised by the
        database (this means, user with the same name already exists)
        """
        mcreate_user.side_effect = IntegrityError(None, None, None)
        mrequest.json_body = {
            'email': 'new@email.com',
            'password': 'fake1',
            'confirmPassword': 'fake1',
        }

        with raises(HTTPBadRequest):
            view.post()

