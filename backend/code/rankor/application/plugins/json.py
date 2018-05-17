"""
This hack allows to encode uuid4 in json
"""
from json import JSONEncoder
from uuid import UUID

from sapp.plugin import Plugin


class JsonPlugin(Plugin):
    def start(self, configurator):
        default = JSONEncoder.default

        def new_default(newself, o):
            if isinstance(o, UUID):
                return o.hex
            return default(newself, o)

        JSONEncoder.default = new_default
