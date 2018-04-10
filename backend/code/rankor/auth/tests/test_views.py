from unittest.mock import patch

from pyramid.httpexceptions import HTTPBadRequest
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ControllerFixtureMixin
from sqlalchemy.exc import IntegrityError

from rankor.auth.views import LoginController
from rankor.auth.views import SignUpView


class TestLoginController(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return LoginController(mroot_factory, mrequest)


class TestSignUpView(ControllerFixtureMixin):
    @fixture
    def ctrl(self, mroot_factory, mrequest):
        return SignUpView(mroot_factory, mrequest)

    @fixture
    def mcreate_user(self, ctrl):
        with patch.object(ctrl, 'create_user') as mock:
            yield mock

    def test_post_on_integrity_error(self, ctrl, mcreate_user, mrequest):
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
            ctrl.post()

