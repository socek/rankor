from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import SignedCookieSessionFactory
from sapp.plugins.logging import LoggingPlugin
from sapp.plugins.pyramid.configurator import ConfiguratorWithPyramid
from sapp.plugins.pyramid.plugins import AuthPlugin
from sapp.plugins.pyramid.plugins import RoutingPlugin
from sapp.plugins.pyramid.plugins import SessionPlugin
from sapp.plugins.settings import SettingsPlugin
from sapp.plugins.sqlalchemy.plugin import Database

from mypet.application.routing import MypetRouting


class MypetConfigurator(ConfiguratorWithPyramid):
    def append_plugins(self):
        self.add_plugin(SettingsPlugin('mypet.application.settings'))
        self.add_plugin(LoggingPlugin())
        self.add_plugin(Database('dbsession'))
        self.add_plugin(RoutingPlugin(MypetRouting))
        self.add_plugin(SessionPlugin(SignedCookieSessionFactory))
        self.add_plugin(
            AuthPlugin(AuthTktAuthenticationPolicy, ACLAuthorizationPolicy))
