from cashflow.application.testing import WebTestFixture


class TestWebAdsController(WebTestFixture):
    url = '/auth'
    login_url = '/auth/login'
    logout_url = '/auth/logout'

    def test_auth_information(self, fake_app):
        """
        /auth should return information about authentication status
        """
        result = fake_app.get(self.url, status=200)
        assert result.json == {'is_authenticated': False, 'groups': []}

    def test_login_with_bad_email(self, fake_app):
        """
        /auth/login should return error when bad email was provided.
        """
        params = self.generate_form_json(dict(
            email='mycreazy',
            password='x'))

        result = fake_app.post_json(
            self.login_url,
            params=params,
            status=200)

        assert result.json == {
            'form': {
                'error': None,
                'validated': False,
                'fields': {
                    'email': {
                        'error': 'Not a valid email address.',
                        'value': 'mycreazy',
                    },
                    'password': {
                        'error': None,
                        'value': 'x',
                    },
                }
            }
        }

    def test_login_with_bad_credentials(self, fake_app, user):
        """
        /auth/login should return error when bad email was provided.
        """
        params = self.generate_form_json(dict(
            email=user.email,
            password='x'))

        result = fake_app.post_json(
            self.login_url,
            params=params,
            status=200)

        assert result.json == {
            'form': {
                'error': 'Username and/or password do not match.',
                'validated': False,
                'fields': {
                    'email': {
                        'error': None,
                        'value': user.email,
                    },
                    'password': {
                        'error': None,
                        'value': 'x',
                    },
                }
            }
        }

    def test_login_with_good_credentials(self, fake_app, user):
        """
        /auth/login should login the user on good credentials
        """
        params = self.generate_form_json(dict(
            email=self.user_data['email'],
            password=self.user_data['password']))

        result = fake_app.post_json(
            self.login_url,
            params=params,
            status=200)

        assert result.json == {
            'form': {
                'error': None,
                'validated': True,
                'fields': {
                    'email': {
                        'error': None,
                        'value': self.user_data['email'],
                    },
                    'password': {
                        'error': None,
                        'value': self.user_data['password'],
                    },
                }
            }
        }

        result = fake_app.get(self.url, status=200)
        assert result.json == {'is_authenticated': True, 'groups': ['authenticated']}

    def test_logout(self, fake_app, user):
        """
        /auth/logout should logout the user
        """
        # create logout form
        params = self.generate_form_json(dict(
            email=self.user_data['email'],
            password=self.user_data['password']))

        # login the user
        fake_app.post_json(
            self.login_url,
            params=params,
            status=200)

        # logout the user
        fake_app.get(
            self.logout_url,
            status=200)

        result = fake_app.get(self.url, status=200)
        assert result.json == {'is_authenticated': False, 'groups': []}
