from sapp.plugins.logging import LoggingPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.pyramid.plugins import RoutingPlugin
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import DatabasePlugin

from rankor.application.routing import RankorRouting


class RankorConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('rankor.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(DatabasePlugin('dbsession'))
        self.add_plugin(RoutingPlugin(RankorRouting))
