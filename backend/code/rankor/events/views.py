from rankor.events.actions import AttachTeamEvent
from rankor.events.actions import ChangeViewEvent
from rankor.events.actions import SelectAnswerEvent
from rankor.events.actions import ShowQuestionEvent
from rankor.events.drivers import ScreenCommand
from rankor.events.drivers import ScreenQuery
from rankor.events.schemas import AttachTeamCommandSchema
from rankor.events.schemas import ChangeViewCommandSchema
from rankor.events.schemas import CommandSchema
from rankor.events.schemas import ScreenSchema
from rankor.events.schemas import SelectAnswerCommandSchema
from rankor.events.schemas import ShowQuestionCommandSchema
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

    schemas = {
        'change_view': ChangeViewCommandSchema(),
        'show_question': ShowQuestionCommandSchema(),
        'attach_team': AttachTeamCommandSchema(),
        'select_answer': SelectAnswerCommandSchema(),
    }

    def patch(self):
        fields = self.get_validated_fields(CommandSchema())
        schema = self.schemas[fields['name']]
        fields = self.get_validated_fields(schema)

        method = getattr(self, fields['name'])
        return method(fields['data'])

    def change_view(self, fields):
        ChangeViewEvent(self._get_screen_id(), fields['view']).send()

    def show_question(self, fields):
        ShowQuestionEvent(
            self._get_screen_id(),
            fields['question_id'],
            fields['team_id'],
            fields['answer_id']
        ).send()

    def attach_team(self, fields):
        AttachTeamEvent(self._get_screen_id(), fields['team_id']).send()

    def select_answer(self, fields):
        SelectAnswerEvent(self._get_screen_id(), fields['answer_id']).send()
