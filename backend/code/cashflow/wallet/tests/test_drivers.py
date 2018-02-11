from pytest import fixture
from pytest import mark
from pytest import raises

from cashflow.application.testing import IntegrationFixture
from cashflow.wallet.drivers import WalletReadDriver


class TestWalletReadDriver(IntegrationFixture):
    @fixture
    def driver(self, app):
        return WalletReadDriver(app.dbsession)

    @mark.parametrize('user, user_id, user_uuid',
                      [[1, 2, 3], [None, 2, 3], [1, None, 3], [1, 2, None],
                       [None, None, None]])
    def test_list_for_user_with_bad_arguments(self, driver, user, user_id,
                                              user_uuid):
        """
        .list_for_user should accept only 1 argument at a time.
        """
        with raises(ValueError):
            driver.list_for_user(
                user=user, user_id=user_id, user_uuid=user_uuid)

    def test_list_for_user_with_user(self, driver, user, wallet, wallet_second_user):
        """
        .list_for_user should find all wallets from the user.
        """
        result = driver.list_for_user(user=user)

        assert len(result) == 1
        assert result[0].id == wallet.id

    def test_list_for_user_with_user_id(self, driver, user, wallet, wallet_second_user):
        """
        .list_for_user should find all wallets from the user.
        """
        result = driver.list_for_user(user_id=user.id)

        assert len(result) == 1
        assert result[0].id == wallet.id

    def test_list_for_user_with_user_uuid(self, driver, user, wallet, wallet_second_user):
        """
        .list_for_user should find all wallets from the user.
        """
        result = driver.list_for_user(user_uuid=user.uuid)

        assert len(result) == 1
        assert result[0].id == wallet.id
