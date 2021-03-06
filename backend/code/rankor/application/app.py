from sapp.plugins.logging import LoggingPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.pyramid.plugins import RoutingPlugin
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import DatabasePlugin

from rankor.application.plugins.json import JsonPlugin
from rankor.application.plugins.redis import RedisPlugin
from rankor.application.plugins.routing import RankorRouting


class RankorConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('rankor.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(DatabasePlugin('dbsession'))
        self.add_plugin(RoutingPlugin(RankorRouting))
        self.add_plugin(RedisPlugin())
        self.add_plugin(JsonPlugin())
