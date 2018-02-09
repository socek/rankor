from pyramid.session import SignedCookieSessionFactory
from sapp.plugins.logging import LoggingPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.pyramid.plugins import RoutingPlugin
from sapp.plugins.pyramid.plugins import SessionPlugin
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import Database

from cashflow.application.routing import CashflowRouting
from cashflow.application.security import AuthPlugin


class CashflowConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('cashflow.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(Database('dbsession'))
        self.add_plugin(RoutingPlugin(CashflowRouting))
        self.add_plugin(SessionPlugin(SignedCookieSessionFactory))
        self.add_plugin(AuthPlugin())
