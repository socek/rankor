from asyncio import sleep
from json import dumps
from json import loads
from logging import getLogger
from time import time

log = getLogger(__name__)


class Client(object):
    def __init__(self, context, websocket):
        self.context = context
        self.redis = context.redis
        self.websocket = websocket
        self.game_uuid = None

    async def run(self):
        log.info('Connection established')
        async for message in self.websocket:
            if message.startswith('game_uuid:'):
                self.game_uuid = message.split(':')[1]
                try:
                    await self.run_loop()
                finally:
                    log.info('Connection lost')
            else:
                log.error('not understanding: {}'.format(message))

    def _get_game_key(self):
        return self.game_uuid + ':game_view'

    def _get_value(self):
        key = self._get_game_key()
        value = self.redis.get(key)
        if value:
            return loads(value)
        else:
            self._set_value(view=None)
            return self.redis.get(key)

    def _set_value(self, **kwargs):
        key = self._get_game_key()
        data = dict(timestamp=time())
        data.update(kwargs)
        return self.redis.set(key, dumps(data))

    async def run_loop(self):
        timestamp = time()
        value = self._get_value()
        await self.websocket.send(dumps(value))

        while True:
            while value['timestamp'] <= timestamp:
                await sleep(0.1)
                value = self._get_value()
            await self.websocket.send(dumps(value))
            timestamp = value['timestamp']
            log.debug('New value sent')
