from json import dumps
from json import loads
from time import time


class GameScreen(object):
    def __init__(self, redis, game_uuid):
        self.game_uuid = game_uuid
        self.redis = redis

    def _get_game_key(self):
        return self.game_uuid + ':game_view'

    def set_value(self, **kwargs):
        key = self._get_game_key()
        data = dict(timestamp=time())
        data.update(kwargs)
        return self.redis.set(key, dumps(data))

    def get_value(self):
        key = self._get_game_key()
        value = self.redis.get(key)
        if value:
            return loads(value)
        else:
            self.set_value(view=None)
            return self.redis.get(key)
