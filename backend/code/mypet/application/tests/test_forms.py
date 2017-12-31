from marshmallow import Schema
from marshmallow import fields
from pytest import fixture

from mypet.application.forms import FormSerializer


class ExampleSchema(Schema):
    one = fields.Email()
    two = fields.Str(required=True)


class TestFormSerializer(object):
    good_json = {
        'one': {
            'value': 'sample@email.com',
        },
        'two': {
            'value': 'sample',
        }
    }

    bad_json = {
        'one': {
            'value': 'sample',
        },
        'two': {
            'value': None,
        }
    }

    @fixture
    def serializer(self):
        return FormSerializer(ExampleSchema())

    def test_parsing(self, serializer):
        """
        .parse_json should parse data which will come from the frontend
        """
        serializer.parse_json(self.good_json)

        assert serializer.fullform == {
            'error': None,
            'validated': False,
            'fields': {
                'one': {
                    'value': 'sample@email.com',
                    'error': None,
                },
                'two': {
                    'value': 'sample',
                    'error': None,
                },
            },
        }

    def test_validate(self, serializer):
        """
        .validate should set fullform['validate'] and fullform['error'] to
        proper values on success
        """
        serializer.parse_json(self.good_json)

        assert serializer.validate()
        assert serializer.fullform['validated']
        assert serializer.fullform['error'] is None

    def test_bad_validation(self, serializer):
        """
        .validate should set fullform['validate'] and fullform['error'] to
        proper values on fail. Also it should set errors on fields.
        """
        serializer.parse_json(self.bad_json)

        assert not serializer.validate()
        assert not serializer.fullform['validated']

        assert serializer.fullform == {
            'error': None,
            'validated': False,
            'fields': {
                'one': {
                    'value': 'sample',
                    'error': 'Not a valid email address.',
                },
                'two': {
                    'error': 'Field may not be null.',
                    'value': None
                }
            },
        }

    def test_set_form_error(self, serializer):
        """
        .set_form_error should set validated to false an error to proper value
        """
        serializer.set_form_error('error is here')
        assert serializer.fullform == {
            'error': 'error is here',
            'validated': False,
            'fields': {}
        }
