from rankor.application.views import RestfulController
from rankor.auth.view_mixins import AuthMixin
from rankor.contest.drivers import ContestCommand
from rankor.contest.drivers import ContestQuery
from rankor.contest.schema import ContestSchema
from rankor.contest.schema import NewContestSchema


class AdminContestView(RestfulController, AuthMixin):
    @property
    def query(self):
        return ContestQuery(self.dbsession)

    @property
    def command(self):
        return ContestCommand(self.dbsession)

    def get(self):
        user = self.get_user()
        contests = self.query.list_for_owner(user.id)
        schema = ContestSchema()
        return {
            'contests': [schema.dump(contest).data for contest in contests]
        }

    def post(self):
        fields = self.get_validated_fields(NewContestSchema)
        fields['owner_id'] = self.get_user_id()
        self.command.create(**fields)
