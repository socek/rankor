from json.decoder import JSONDecodeError

from marshmallow.exceptions import ValidationError
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
        try:
            return schema_cls().load(self.request.json_body)
        except JSONDecodeError:
            raise HTTPNotAcceptable()
        except ValidationError as error:
            raise HTTPBadRequest(json=error.messages)
