from sapp.plugin import Plugin


class Jinja2Plugin(Plugin):
    def start_pyramid(self, pyramid):
        pyramid.include('pyramid_jinja2')
