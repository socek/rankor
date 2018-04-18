from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.cache import cache_per_request
from rankor.application.views import RestfulController
from rankor.auth.view_mixins import AuthMixin
from rankor.contest.drivers import ContestCommand
from rankor.contest.drivers import ContestQuery
from rankor.contest.schema import ContestSchema
from rankor.contest.schema import NewContestSchema


class ContestBaseView(RestfulController, AuthMixin):
    @property
    def contest_query(self):
        return ContestQuery(self.dbsession)

    @property
    def contest_command(self):
        return ContestCommand(self.dbsession)

    def _get_contest_uuid(self):
        return self.request.matchdict['contest_uuid']

    @cache_per_request('contest')
    def _get_contest(self):
        try:
            return self.contest_query.get_by_uuid(self._get_contest_uuid())
        except NoResultFound:
            raise HTTPNotFound()


class AdminContestListView(ContestBaseView):
    def get(self):
        contests = self.contest_query.list_for_owner(self.get_user_id())
        schema = ContestSchema()
        return {
            'contests': [schema.dump(contest).data for contest in contests]
        }

    def post(self):
        fields = self.get_validated_fields(NewContestSchema)
        fields['owner_id'] = self.get_user_id()
        self.contest_command.create(**fields)


class AdminContestView(ContestBaseView):
    def get(self):
        schema = ContestSchema()
        contest = self._get_contest()
        return schema.dump(contest).data

    def patch(self):
        contest = self._get_contest()
        fields = self.get_validated_fields(NewContestSchema)
        self.contest_command.update_by_uuid(contest.uuid, fields)
