from unittest.mock import MagicMock
from unittest.mock import patch

from pytest import fixture
from pytest import mark
from undecorated import undecorated

from rankor.auth.view_mixins import AuthMixin


class TestAuthMixin(object):
    @fixture
    def mixin(self):
        return AuthMixin()

    @fixture
    def mdb(self):
        return MagicMock

    @fixture
    def mauthenticated_userid(self):
        with patch('rankor.auth.view_mixins.authenticated_userid') as mock:
            yield mock

    @fixture
    def muser_query(self):
        with patch('rankor.auth.view_mixins.UserQuery') as mock:
            yield mock

    @fixture
    def mrequest(self, mixin):
        mrequest = MagicMock()
        mixin.request = mrequest
        return mrequest

    def test_get_user(
            self,
            mixin,
            mdb,
            mauthenticated_userid,
            muser_query,
            mrequest,
    ):
        """
        .get_user should return authenticated user from the database.
        """
        mquery = muser_query.return_value
        fun = undecorated(mixin.get_user)

        assert fun(mixin, dbsession=mdb) == mquery.get_by_id.return_value

        muser_query.assert_called_once_with(mdb)
        mquery.get_by_id.assert_called_once_with(
            mauthenticated_userid.return_value)
        mauthenticated_userid.assert_called_once_with(mrequest)

    @mark.parametrize('return_value, is_auth', [
        [None, False],
        [1, True],
    ])
    def test_is_authenticated(
            self,
            mixin,
            mrequest,
            mauthenticated_userid,
            return_value,
            is_auth,
    ):
        """
        .is_authenticated should return True only if user is authenticated.
        """
        mauthenticated_userid.return_value = return_value

        assert mixin.is_authenticated() is is_auth
