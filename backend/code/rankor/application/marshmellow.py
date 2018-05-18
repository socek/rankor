from marshmallow.fields import String
from marshmallow.fields import UUID as BaseUUID


class UUID(BaseUUID):
    def _serialize(self, value, attr, obj):
        validated = self._validated(value).hex if value is not None else None
        return super(String, self)._serialize(validated, attr, obj)
