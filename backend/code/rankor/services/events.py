from time import sleep
from uuid import uuid4
from logging import getLogger

from rankor import app
from rankor.services.broadcaster import broadcast

log = getLogger(__name__)


class Event(object):
    def __init__(self, event, ready_at=0, request_id=None):
        self.event = event
        self.ready_at = ready_at
        self.request_id = request_id or uuid4().hex

    def _redis_key(self, source):
        key = 'event.data.{}.{}.{}|'.format(self.event, self.request_id,
                                            source)
        return key

    @property
    def _redis_list_key(self):
        return 'event.list.{}.{}'.format(self.event, self.request_id)

    def broadcast(self, payload):
        print('broadcast request_id {}'.format(self.request_id))
        broadcast.delay(self.event, self.request_id, payload={'payload': 1})

    def get_data(self):
        with app as context:
            data = {}
            for source in self.get_sources():
                result = context.redis.hgetall(self._redis_key(source))
                data[source] = result
            return data

    def get_sources(self):
        with app as context:
            value = context.redis.lrange(self._redis_list_key, 0, -1)
            return [v.decode('utf8') for v in value] or []

    def is_ready(self):
        return len(self.get_sources()) >= self.ready_at

    def get_response(self):
        while True:
            if self.is_ready():
                return self.get_data()
            else:
                print('Waiting...')
                sleep(0.01)

    def send_response(self, source, payload):
        log.info('sending response from {} for request_id {} = {}'.format(
            source, self.request_id, payload))
        with app as context:
            key = self._redis_key(source)
            context.redis.hmset(key, payload)

            context.redis.rpush(self._redis_list_key, source)

    def purge(self):
        print('purging...')
        with app as context:
            for source in self.get_sources():
                context.redis.delete(self._redis_key(source))
            context.redis.delete(self._redis_list_key)


class HelloEvent(Event):
    def __init__(self, request_id=None):
        super().__init__('hello', 2, request_id)
