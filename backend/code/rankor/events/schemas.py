from marshmallow import Schema

from rankor.application.marshmellow import UUID


class ScreenSchema(Schema):
    id = UUID()
