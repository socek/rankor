class FormSerializer(object):
    def __init__(self, schema):
        self._create_clean_form()
        self.schema = schema
        self.serialized = None

    def _create_clean_form(self):
        self.fullform = {
            'error': None,
            'validated': False,
            'fields': {},
        }

    def parse_json(self, json):
        for name, field in json.items():
            self.fullform['fields'][name] = {
                'error': None,
                'value': field['value'],
            }

    def fields(self):
        data = {}
        for name, field in self.fullform['fields'].items():
            data[name] = field['value']
        return data

    def validate(self):
        self.serialized, errors = self.schema.load(self.fields())
        if errors:
            for name, errors in errors.items():
                self.fullform['fields'][name]['error'] = errors[0]
            return False
        else:
            self.set_form_ok()
            return True

    def set_form_error(self, error):
        self.fullform['validated'] = False
        self.fullform['error'] = error

    def set_form_ok(self):
        self.fullform['validated'] = True
        self.fullform['error'] = None
