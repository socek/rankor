from sapp.decorators import WithContext

from rankor import app
from rankor.application.views import RestfulController
from rankor.auth.view_mixins import AuthMixin
from rankor.contest.drivers import ContestCommand
from rankor.contest.drivers import ContestQuery
from rankor.contest.schema import ContestSchema


class AdminContestView(RestfulController, AuthMixin):
    @property
    @WithContext(app, args=['dbsession'])
    def query(self, dbsession):
        return ContestQuery(dbsession)

    @property
    @WithContext(app, args=['dbsession'])
    def command(self, dbsession):
        return ContestCommand(dbsession)

    def get(self):
        contests = self.query.list_for_owner(self.get_user_id())
        schema = ContestSchema()
        return {
            'contests': [schema.dump(contest).data for contest in contests]
        }

    @WithContext(app, args=['dbsession'])
    def post(self, dbsession):
        schema = ContestSchema()
        data, errors = schema.load(self.request.json_body)
        if errors:
            self.request.response.status_int = 400
            return errors

        data['owner_id'] = self.get_user_id()
        self.command.create(**data)
        return {}
