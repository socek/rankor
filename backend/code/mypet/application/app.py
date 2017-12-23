from sapp.plugins.logging import LoggingPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import Database

from mypet.application.plugins import Routing


class MypetConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('mypet.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(Database('dbsession'))
        self.add_plugin(Routing())
