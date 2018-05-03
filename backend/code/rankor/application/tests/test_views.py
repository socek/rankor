from json.decoder import JSONDecodeError
from unittest.mock import MagicMock
from unittest.mock import sentinel

from marshmallow.exceptions import ValidationError
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotAcceptable
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ViewFixtureMixin

from rankor.application.views import RestfulView


class TestRestfulView(ViewFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return RestfulView(mroot_factory, mrequest)

    @fixture
    def mschema(self):
        return MagicMock()

    def test_get_validated_fields_no_error(self, view, mschema):
        """
        .get_validated_fields should return validated fields when schema is
        validated good
        """
        mschema.load.return_value = sentinel.fields
        assert view.get_validated_fields(mschema) == sentinel.fields

    def test_get_validated_fields_with_error(self, view, mschema):
        """
        .get_validated_fields should raise HTTPBadRequest with errors as return
        data
        """
        mschema.load.side_effect = ValidationError('msg')
        with raises(HTTPBadRequest):
            view.get_validated_fields(mschema)

    def test_get_validated_fields_with_malformed_json(self, view, mschema):
        """
        .get_validated_fields should raise HTTPNotAcceptable, when provided json
        is malformed
        """
        mschema.load.side_effect = JSONDecodeError(
            None, '', 0)
        with raises(HTTPNotAcceptable):
            view.get_validated_fields(mschema)
