from json.decoder import JSONDecodeError
from unittest.mock import MagicMock
from unittest.mock import sentinel

from marshmallow.exceptions import ValidationError
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotAcceptable
from pytest import fixture
from pytest import raises
from sapp.plugins.pyramid.testing import ControllerFixtureMixin

from rankor.application.views import RestfulController


class TestRestfulController(ControllerFixtureMixin):
    @fixture
    def view(self, mroot_factory, mrequest):
        return RestfulController(mroot_factory, mrequest)

    @fixture
    def mschema_cls(self):
        return MagicMock()

    def test_get_validated_fields_no_error(self, view, mschema_cls):
        """
        .get_validated_fields should return validated fields when schema is
        validated good
        """
        mschema_cls.return_value.load.return_value = sentinel.fields
        assert view.get_validated_fields(mschema_cls) == sentinel.fields

    def test_get_validated_fields_with_error(self, view, mschema_cls):
        """
        .get_validated_fields should raise HTTPBadRequest with errors as return
        data
        """
        mschema_cls.return_value.load.side_effect = ValidationError('msg')
        with raises(HTTPBadRequest):
            view.get_validated_fields(mschema_cls)

    def test_get_validated_fields_with_malformed_json(self, view, mschema_cls):
        """
        .get_validated_fields should raise HTTPNotAcceptable, when provided json
        is malformed
        """
        mschema_cls.return_value.load.side_effect = JSONDecodeError(
            None, '', 0)
        with raises(HTTPNotAcceptable):
            view.get_validated_fields(mschema_cls)
