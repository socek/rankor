from marshmallow import Schema, fields


class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str()
