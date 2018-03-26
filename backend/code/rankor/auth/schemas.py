from marshmallow import Schema
from marshmallow.fields import String
from marshmallow.fields import Email


class LoginSchema(Schema):
    email = Email(required=True, allow_none=False)
    password = String(required=True, allow_none=False)
