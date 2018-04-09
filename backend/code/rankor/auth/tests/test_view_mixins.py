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
    def muser_query(self):
        with patch('rankor.auth.view_mixins.UserQuery') as mock:
            yield mock

    @fixture
    def mdecode_jwt(self):
        with patch('rankor.auth.view_mixins.decode_jwt') as mock:
            yield mock

    @fixture
    def mrequest(self, mixin):
        mrequest = MagicMock()
        mrequest.headers = {}
        mixin.request = mrequest
        return mrequest

    @fixture
    def get_user(self, mixin):
        return undecorated(mixin.get_user)

    def test_get_user(
            self,
            mixin,
            mdb,
            mauthenticated_userid,
            muser_query,
            mrequest,
            get_user,
    ):
        """
        .get_user should return authenticated user from the database.
        """
        mquery = muser_query.return_value

        assert get_user(mixin, dbsession=mdb) == mquery.get_by_id.return_value

        muser_query.assert_called_once_with(mdb)
        mquery.get_by_id.assert_called_once_with(
            mauthenticated_userid.return_value)
        mauthenticated_userid.assert_called_once_with(mrequest)

    def test_get_user_on_proper_jwt(
            self,
            mixin,
            mdb,
            muser_query,
            mrequest,
            get_user,
            mdecode_jwt,
    ):
        """
        .get_user should return authenticated user when proper jwt provided
        """
        mquery = muser_query.return_value
        mrequest.headers['JWT'] = 'proper.jwt.token'
        mdecode_jwt.return_value = {
            'uuid': 'uuid1'
        }

        assert get_user(mixin, dbsession=mdb) == mquery.get_by_uuid.return_value

        muser_query.assert_called_once_with(mdb)
        mquery.get_by_uuid.assert_called_once_with('uuid1')
        mdecode_jwt.assert_called_once_with('proper.jwt.token')

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
