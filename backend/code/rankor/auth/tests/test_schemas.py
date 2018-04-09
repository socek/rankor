from pytest import fixture

from rankor.auth.schemas import SignUpSchema


class TestSignUpSchema(object):
    @fixture
    def schema(self):
        return SignUpSchema()

    def test_password_match(self, schema):
        """
        SignUpSchema should validate if password match.
        """
        fields, errors = schema.load({
            'email': 'fake@email.com',
            'password': 'one',
            'confirmPassword': 'one'
        })
        assert errors == {}

    def test_password_not_match(self, schema):
        """
        SignUpSchema should not validate if password do not match.
        """
        fields, errors = schema.load({
            'email': 'fake@email.com',
            'password': 'one',
            'confirmPassword': 'two'
        })
        assert errors == {'_schema': ['Password do not match!']}
