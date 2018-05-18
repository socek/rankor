from marshmallow import Schema
from marshmallow.fields import Dict
from marshmallow.fields import Nested
from marshmallow.fields import String

from rankor.application.marshmellow import UUID


class ScreenSchema(Schema):
    id = UUID()


class CommandSchema(Schema):
    name = String()
    data = Dict()


class ChangeViewCommandSchema(CommandSchema):
    class ChangeView(Schema):
        view = String()

    data = Nested(ChangeView)
