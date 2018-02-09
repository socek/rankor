from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow
from pyramid.security import Everyone
from sapp.plugin import Plugin


class MainRoot(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, 'authenticated', 'edit'),
    ]

    def __init__(self, request):
        self.request = request


class AuthPlugin(Plugin):
    """
    Add authorization to the pyramid app.
    """

    def start(self, configurator):
        self.settings = configurator.settings

    def start_pyramid(self, pyramid):
        authn_policy = AuthTktAuthenticationPolicy(
            self.settings['secret'],
            callback=self.groupfinder,
            hashalg='sha512')
        authz_policy = ACLAuthorizationPolicy()
        pyramid.set_authentication_policy(authn_policy)
        pyramid.set_authorization_policy(authz_policy)
        pyramid.set_root_factory(MainRoot)

    def groupfinder(self, userid, request):
        return ['authenticated']
