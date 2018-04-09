from json.decoder import JSONDecodeError

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotAcceptable
from sapp.decorators import WithContext
from sapp.plugins.pyramid.controller import RestfulController as BaseRestfulController

from rankor import app


class RestfulController(BaseRestfulController):
    @property
    @WithContext(app, args=['dbsession'])
    def dbsession(self, dbsession):
        return dbsession  # pragma: no cover

    def get_validated_fields(self, schema_cls):
        schema = schema_cls()
        try:
            fields, errors = schema.load(self.request.json_body)
        except JSONDecodeError:
            raise HTTPNotAcceptable()

        if errors:
            raise HTTPBadRequest(json=errors)

        return fields
