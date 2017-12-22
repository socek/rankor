from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.settings import SettingsPlugin


class MypetConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('mypet.application.settings'))
