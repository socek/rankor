from marshmallow.exceptions import ValidationError
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
        data = {
            'email': 'fake@email.com',
            'password': 'one',
            'confirmPassword': 'one'
        }
        fields = schema.load(data)
        assert fields == data

    def test_password_not_match(self, schema):
        """
        SignUpSchema should not validate if password do not match.
        """
        try:
            schema.load({
                'email': 'fake@email.com',
                'password': 'one',
                'confirmPassword': 'two'
            })
            assert False
        except ValidationError as error:
            assert error.messages == {'_schema': ['Password do not match!']}
