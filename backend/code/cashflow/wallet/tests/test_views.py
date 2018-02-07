from cashflow.application.testing import WebTestFixture


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
