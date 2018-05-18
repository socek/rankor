from rankor import app
from rankor.events.drivers import ScreenCommand


class Event(object):
    def __init__(self, **kwargs):
        self.data = kwargs

    def send(self):
        with app as context:
            command = ScreenCommand(context.dbsession)
            command.send_event(self.name, **self.data)


class ChangeView(Event):
    name = 'change_view'

    _views = (
        'welcome',
        'highscore',
        'question'
    )

    def __init__(self, screen_id, view):
        assert view in self._views
        super().__init__(screen_id=screen_id, view=view)
