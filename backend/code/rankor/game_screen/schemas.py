from marshmallow import Schema
from marshmallow.fields import String


class GameViewSchema(Schema):
    view = String()
