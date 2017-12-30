from pytest import fixture

from mypet.auth.models import User


class TestUser(object):

    @fixture
    def user(self):
        return User()

    def test_set_password(self, user):
        """
        .set_password should hash the password
        """
        user.set_password('password')

        assert user.password != 'password'

    def test_validating_password(self, user):
        """
        .validate_password should validate only proper password
        """
        user.set_password('elo')

        assert user.validate_password('elo')
        assert not user.validate_password('no')

    def test_validate_empty_password(self, user):
        """
        .validate_password should not validate empty password
        """
        assert not user.validate_password(None)
