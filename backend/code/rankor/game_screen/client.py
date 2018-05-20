from asyncio import sleep
from json import dumps
from json import loads
from json.decoder import JSONDecodeError
from logging import getLogger

from rankor.events.drivers import ScreenQuery

log = getLogger(__name__)


class Client(object):
    PING_EVERY = 100

    def __init__(self, context, websocket):
        self.context = context
        self.redis = context.redis
        self.dbsession = context.dbsession
        self.websocket = websocket
        self.game_id = None
        self.screen_id = None
        self.tick = 0

    @property
    def screen_query(self):
        return ScreenQuery(self.dbsession)

    async def _send(self, data):
        return await self.websocket.send(dumps(data))

    async def run(self):
        log.info('Connection established')
        async for message in self.websocket:
            try:
                data = loads(message)
                self.game_id = data['game_id']
                self.screen_id = data['screen_id']
                log.info('Game_id: {}'.format(self.game_id))
                log.info('Screen_id: {}'.format(self.screen_id))
                try:
                    timestamp = await self.send_current_state()
                    await self.run_loop(timestamp)
                except Exception as error:
                    log.error(error, exc_info=True)
                finally:
                    log.info('Connection lost')
            except JSONDecodeError:
                log.error(
                    'not understanding: {}'.format(message), exc_info=True)

    async def run_loop(self, timestamp):
        while True:
            events = self.screen_query.list_events_after(
                self.screen_id, timestamp)
            for event in events:
                log.debug('sending event {}:{}'.format(event.name,
                                                       event.id.hex))
                await self._send(event.to_dict())
                timestamp = event.created_at

            await self.send_ping()
            await sleep(0.1)

    async def send_current_state(self):
        screen = self.screen_query.get_by_id(self.screen_id)
        data = screen.to_dict()
        data['name'] = 'init'
        await self._send(data)
        return screen.updated_at

    async def send_ping(self):
        self.tick += 1
        if self.tick % self.PING_EVERY == 0:
            self.tick = 0
            log.debug('sending ping')
            await self._send({'name': 'ping'})
