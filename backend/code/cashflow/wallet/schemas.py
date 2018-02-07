from marshmallow import Schema
from marshmallow import fields


class WalletSchema(Schema):
    uuid = fields.String()
    name = fields.String()
