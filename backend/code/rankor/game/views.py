from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.cache import cache_per_request
from rankor.auth.view_mixins import AuthenticatedView
from rankor.contest.drivers import ContestQuery
from rankor.game.drivers import GameCommand
from rankor.game.drivers import GameQuery
from rankor.game.schema import GameSchema


class GameBaseView(AuthenticatedView):
    @property
    def game_query(self):
        return GameQuery(self.dbsession)

    @property
    def game_command(self):
        return GameCommand(self.dbsession)

    @property
    def contest_query(self):
        return ContestQuery(self.dbsession)

    def _get_game_id(self):
        return self.request.matchdict['game_id']

    @cache_per_request('game')
    def _get_game(self):
        try:
            return self.game_query.get_by_id(self._get_game_id())
        except NoResultFound:
            raise HTTPNotFound()

    def _contest_id_to_id(self, contest_id):
        try:
            contest = self.contest_query.get_by_id(contest_id)
        except NoResultFound:
            raise self._object_validation('Contest does not exists!')

        if contest.owner.id != self.get_user().id:
            raise self._object_validation('Contest does not exists!')

        return contest.id


class AdminGameListView(GameBaseView):
    def get(self):
        games = self.game_query.list_for_owner(self.get_user_id())
        schema = GameSchema()
        return {'games': [schema.dump(game) for game in games]}

    def post(self):
        fields = self.get_validated_fields(GameSchema())
        fields['owner_id'] = self.get_user_id()
        fields['contest_id'] = (self._contest_id_to_id(
            fields.pop('contest_id')).hex)
        self.game_command.create(**fields)


class AdminGameView(GameBaseView):
    def get(self):
        game = self._get_game()
        return GameSchema().dump(game)

    def patch(self):
        game = self._get_game()
        fields = self.get_validated_fields(GameSchema())
        self.game_command.update_by_id(game.id, fields)
