from rankor.events.drivers import ScreenCommand
from rankor.events.drivers import ScreenQuery
from rankor.events.schemas import ScreenSchema
from rankor.host.views import HostBaseView


class ScreenBaseView(HostBaseView):
    @property
    def screen_query(self):
        return ScreenQuery(self.dbsession)

    @property
    def screen_command(self):
        return ScreenCommand(self.dbsession)


class HostScreenListView(ScreenBaseView):
    def get(self):
        game_id = self._get_game_id()
        elements = self.screen_query.list_for_game(game_id)
        result = ScreenSchema(many=True).dump(elements)
        return result

    def post(self):
        game_id = self._get_game_id()
        screen = self.screen_command.create_screen(game_id)
        return {
            'id': screen.id,
        }


class HostScreenView(ScreenBaseView):
    def _get_screen_id(self):
        return self.request.matchdict['screen_id']

    def delete(self):
        self.screen_command.delete_screen(self._get_screen_id())
