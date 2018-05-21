from datetime import datetime

from rankor.events.models import Screen
from rankor.events.models import ScreenEvent


class Driver(object):
    def __init__(self, database):
        self.database = database

    @property
    def _query(self):
        return self.database.query

    def objects(self):
        return self._query(Screen)

    def events(self):
        return self._query(ScreenEvent)


class ScreenQuery(Driver):
    def get_by_id(self, id):
        return self.objects().filter(Screen.id == id).one()

    def list_for_game(self, game_id):
        return (
            self.objects()
            .filter(Screen.game_id == game_id)
            .order_by(Screen.created_at)
            .all()
        )

    def list_events_after(self, screen_id, date):
        if type(date) is float:
            # This is a timestamp
            date = datetime.utcfromtimestamp(date)

        return (
            self.events()
            .filter(ScreenEvent.screen_id == screen_id)
            .filter(ScreenEvent.created_at > date)
            .order_by(ScreenEvent.created_at)
            .all()
        )


class ScreenCommand(Driver):
    def create_screen(self, game_id):
        screen = Screen()
        screen.game_id = game_id
        self.database.add(screen)
        self.database.commit()
        return screen

    def _create_event(self, screen_id, name, **kwargs):
        event = ScreenEvent()
        event.screen_id = screen_id
        event.name = name
        for name, value in kwargs.items():
            setattr(event, name, value)
        self.database.add(event)
        return event

    def _update_screen(self, screen_id, **kwargs):
        self.objects().filter(Screen.id == screen_id).update(kwargs)

    def send_event(self, name, screen_id, **kwargs):
        now = datetime.utcnow()
        self._update_screen(screen_id, updated_at=now, **kwargs)
        event = self._create_event(screen_id, name, created_at=now, **kwargs)
        self.database.commit()
        return event

    def delete_screen(self, screen_id):
        self.events().filter(ScreenEvent.screen_id == screen_id).delete()
        self.objects().filter(Screen.id == screen_id).delete()
        self.database.commit()
