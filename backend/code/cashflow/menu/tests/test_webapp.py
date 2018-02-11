from cashflow.application.testing import WebTestFixture


class TestWebAdsController(WebTestFixture):
    url = '/menu'

    def test_normal(self, fake_app):
        """
        /menu should return information about accesible menu elements
        """
        result = fake_app.get(self.url)
        assert result.json == {
            'menu': [{
                'elements': [{
                    'is_active': False,
                    'name': 'not_logged_home',
                    'text': 'Home',
                    'url': '#/'
                }],
                'name':
                'Menu'
            }]
        }

    def test_authenticated_user(self, fake_app, authenticated_user):
        """
        /menu should return information about accesible menu elements for
        authenticated user
        """
        result = fake_app.get(self.url)
        assert result.json == {
            'menu': [{
                'elements': [{
                    'is_active': False,
                    'name': 'dashboard_home',
                    'text': 'Wallets',
                    'url': '#/dashboard'
                }],
                'name':
                'Dashboard'
            }]
        }
