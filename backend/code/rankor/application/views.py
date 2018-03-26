from json.decoder import JSONDecodeError

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotAcceptable
from sapp.plugins.pyramid.controller import RestfulController as BaseRestfulController


class RestfulController(BaseRestfulController):
    def get_validated_fields(self, schema_cls):
        schema = schema_cls()
        try:
            fields, errors = schema.load(self.request.json_body)
        except JSONDecodeError:
            raise HTTPNotAcceptable()

        if errors:
            raise HTTPBadRequest(json=errors)

        return fields
