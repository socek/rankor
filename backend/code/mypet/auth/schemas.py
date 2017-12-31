from marshmallow import Schema
from marshmallow import fields


class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str()
