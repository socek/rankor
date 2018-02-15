from cashflow.application.testing import WebTestFixture
from cashflow.wallet.drivers import WalletReadDriver


class TestWalletList(WebTestFixture):
    url = '/wallets'

    def test_unauthenticated(self, fake_app):
        """
        Service should return 403 when this endpoint will be called without
        authorization.
        """
        fake_app.get(self.url, status=403)

    def test_empty_list(self, fake_app, authenticated_user):
        """
        Service should return empty list if no elements is present.
        """
        result = fake_app.get(self.url)
        assert result.json == {'elements': []}

    def test_one_element_list(self, fake_app, wallet, authenticated_user,
                              authenticated_user_wallet):
        """
        Service should return all element if elements are present.
        """
        result = fake_app.get(self.url)
        assert result.json == {
            'elements': [{
                'name': authenticated_user_wallet.name,
                'uuid': authenticated_user_wallet.uuid
            }]
        }


class TestWalletCreate(WebTestFixture):
    url = '/wallets'

    def test_unauthenticated(self, fake_app):
        """
        Service should return 403 when this endpoint will be called without
        authorization.
        """
        result = fake_app.post_json(self.url, dict(name='new'), status=403)
        assert result.status_code == 403

    def test_creating_new_wallet(self, fake_app, authenticated_user,
                                 dbsession):
        """
        Service should create proper wallet.
        """
        result = fake_app.post_json(self.url, {'name': {'value': 'new'}})
        driver = WalletReadDriver(dbsession)
        wallet = driver.get_by_uuid(result.json['uuid'])

        try:
            assert wallet.name == 'new'
            assert wallet.user == authenticated_user
        finally:
            dbsession.delete(wallet)

    def test_validate_form(self, fake_app, authenticated_user, dbsession):
        """
        Endpoint should validate the form.
        """
        result = fake_app.post_json(self.url, {'name': {'value': ''}}, status=400)
        assert result.json['form']['fields']['name']['error'] == 'Field cannot be blank'
