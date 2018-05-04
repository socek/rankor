from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.cache import cache_per_request
from rankor.auth.view_mixins import AuthenticatedView
from rankor.game.drivers import GameQuery
from rankor.host.schema import QuestionSchema
from rankor.questions.drivers import QuestionQuery
from rankor.team.drivers import TeamCommand
from rankor.team.drivers import TeamQuery
from rankor.team.schema import TeamSchema


class HostBaseView(AuthenticatedView):
    @property
    def game_query(self):
        return GameQuery(self.dbsession)

    @property
    def question_query(self):
        return QuestionQuery(self.dbsession)

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


class HostQuestionListView(HostBaseView):
    def get(self):
        uuid = self._get_game_uuid()
        elements = self.question_query.list_for_game(uuid)
        result = QuestionSchema(many=True).dump(elements)
        return result


class HostTeamListView(HostBaseView):
    @property
    def team_query(self):
        return TeamQuery(self.dbsession)

    @property
    def team_command(self):
        return TeamCommand(self.dbsession)

    def get(self):
        uuid = self._get_game_uuid()
        elements = self.team_query.list_for_game(uuid)
        result = TeamSchema(many=True).dump(elements)
        return result

    def post(self):
        game = self._get_game()

        fields = self.get_validated_fields(TeamSchema())
        fields['game_id'] = game.id

        team = self.team_command.create(**fields)

        return {
            'team_uuid': team.uuid,
        }
