from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import post_load
from marshmallow.fields import Email
from marshmallow.fields import String


class LoginSchema(Schema):
    email = Email(required=True, allow_none=False)
    password = String(required=True, allow_none=False)


class SignUpSchema(Schema):
    email = Email(required=True, allow_none=False)
    password = String(required=True, allow_none=False)
    confirmPassword = String(required=True, allow_none=False)

    @post_load
    def validate_passwords(self, data):
        if data['confirmPassword'] != data['password']:
            raise ValidationError('Password do not match!')
        return data
