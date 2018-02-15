from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate


not_blank = validate.Length(min=1, error='Field cannot be blank')


class WalletSchema(Schema):
    uuid = fields.String()
    name = fields.String()


class CreateWalletSchema(Schema):
    name = fields.String(required=True, validate=not_blank)
