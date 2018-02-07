from cashflow.application.testing import WebTestFixture
from cashflow.wallet.drivers import WalletReadDriver


class TestWalletList(WebTestFixture):
    url = '/wallets'

    def test_empty_list(self, fake_app):
        result = fake_app.get(self.url)
        assert result.json == {'elements': []}

    def test_one_element_list(self, fake_app, wallet):
        result = fake_app.get(self.url)
        assert result.json == {
            'elements': [{
                'name': wallet.name,
                'uuid': wallet.uuid
            }]
        }


class TestWalletCreate(WebTestFixture):
    url = '/wallet'

    def test_empty_list(self, fake_app, user, dbsession):
        result = fake_app.post_json(self.url,
                                    dict(user_uuid=user.uuid, name='new'))
        driver = WalletReadDriver(dbsession)
        wallet = driver.get_by_uuid(result.json['uuid'])

        try:
            assert wallet.name == 'new'
            assert wallet.user == user
        finally:
            dbsession.delete(wallet)
