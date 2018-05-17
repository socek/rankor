from redis import StrictRedis

from sapp.plugin import Plugin


class RedisPlugin(Plugin):
    def start(self, configurator):
        self.settings = configurator.settings

    def enter(self, context):
        params = dict(
            host=self.settings['redis:host'],
            port=self.settings['redis:port'],
            db=self.settings['redis:db'],
        )
        setattr(context, 'redis', StrictRedis(**params))
