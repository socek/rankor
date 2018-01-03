from mypet.application.testing import WebTestFixture


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
                    'name': 'dashboard_home',
                    'text': 'Home',
                    'url': '#/'
                }],
                'name':
                'Dashboard'
            }]
        }
