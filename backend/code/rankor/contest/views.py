from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.cache import cache_per_request
from rankor.auth.view_mixins import AuthenticatedView
from rankor.contest.drivers import ContestCommand
from rankor.contest.drivers import ContestQuery
from rankor.contest.schema import ContestSchema


class ContestBaseView(AuthenticatedView):
    @property
    def contest_query(self):
        return ContestQuery(self.dbsession)

    @property
    def contest_command(self):
        return ContestCommand(self.dbsession)

    def _get_contest_id(self):
        return self.request.matchdict['contest_id']

    @cache_per_request('contest')
    def _get_contest(self):
        try:
            return self.contest_query.get_by_id(self._get_contest_id())
        except NoResultFound:
            raise HTTPNotFound()


class AdminContestListView(ContestBaseView):
    def get(self):
        contests = self.contest_query.list_for_owner(self.get_user_id())
        schema = ContestSchema()
        return {'contests': [schema.dump(contest) for contest in contests]}

    def post(self):
        fields = self.get_validated_fields(ContestSchema())
        fields['owner_id'] = self.get_user_id()
        self.contest_command.create(**fields)


class AdminContestView(ContestBaseView):
    def get(self):
        contest = self._get_contest()
        return ContestSchema().dump(contest)

    def patch(self):
        contest = self._get_contest()
        fields = self.get_validated_fields(ContestSchema())
        self.contest_command.update_by_id(contest.id, fields)

    def delete(self):
        contest = self._get_contest()
        self.contest_command.soft_delete(contest.id)
