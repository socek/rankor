from json import dumps
from json import loads
from time import sleep
from time import time

from pyramid.httpexceptions import HTTPNotFound
from sapp.decorators import WithContext
from sqlalchemy.orm.exc import NoResultFound

from rankor import app
from rankor.application.cache import cache_per_request
from rankor.application.views import RestfulView
from rankor.game.drivers import GameQuery
from rankor.game_screen.schemas import GameViewSchema


class GameView(RestfulView):
    @property
    @WithContext(app, args=['redis'])
    def redis(self, redis):
        return redis  # pragma: no cover

    @property
    def game_query(self):
        return GameQuery(self.dbsession)

    def _get_game_uuid(self):
        return self.request.matchdict['game_uuid']

    @cache_per_request('game')
    def _get_game(self):
        try:
            return self.game_query.get_by_uuid(self._get_game_uuid())
        except NoResultFound:
            raise HTTPNotFound()

    def validate(self):
        super().validate()
        self._get_game()

    def _get_game_key(self):
        return self.request.matchdict['game_uuid'] + ':game_view'

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

    def get(self):
        try:
            timestamp = float(self.request.GET.get('timestamp'))
        except (ValueError, TypeError):
            timestamp = 0

        value = self._get_value()
        while value['timestamp'] <= timestamp:
            sleep(0.1)
            value = self._get_value()
        return value

    def post(self):
        fields = self.get_validated_fields(GameViewSchema())
        self._set_value(**fields)
