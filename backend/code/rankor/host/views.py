from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from rankor.answers.drivers import AnswerQuery
from rankor.answers.schema import AnswerSchema
from rankor.application.cache import cache_per_request
from rankor.auth.view_mixins import AuthenticatedView
from rankor.game.drivers import GameQuery
from rankor.game_answer.drivers import GameAnswerCommand
from rankor.game_answer.drivers import GameAnswerQuery
from rankor.host.schema import AnswerPostSchema
from rankor.host.schema import FullQuestionSchema
from rankor.questions.drivers import QuestionQuery
from rankor.questions.schema import QuestionSchema
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
        result = FullQuestionSchema(many=True).dump(elements)
        return result


class HostQuestionView(HostBaseView):
    def _get_question_uuid(self):
        return self.request.matchdict['question_uuid']

    @cache_per_request('question')
    def _get_question(self):
        try:
            return self.question_query.get_by_uuid(self._get_question_uuid())
        except NoResultFound:
            raise HTTPNotFound()

    def get(self):
        return QuestionSchema().dump(self._get_question())


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


class HostAnswerListView(HostQuestionView):
    @property
    def team_query(self):
        return TeamQuery(self.dbsession)

    @property
    def answer_query(self):
        return AnswerQuery(self.dbsession)

    @property
    def game_answer_command(self):
        return GameAnswerCommand(self.dbsession)

    @property
    def game_answer_query(self):
        return GameAnswerQuery(self.dbsession)

    def get(self):
        game = self._get_game()
        question = self._get_question()

        answers = self.answer_query.list_for_question(
            self._get_question_uuid())
        schema = AnswerSchema()
        result = {'answers': [schema.dump(answer) for answer in answers]}
        try:
            game_answer = self.game_answer_query.get_by_game_and_question(
                game.id,
                question.id,
            )
            result['answer'] = {
                'team_uuid': game_answer.team.uuid,
                'answer_uuid': game_answer.answer.uuid
            }
        except NoResultFound:
            result['answer'] = {'team_uuid': None, 'answer_uuid': None}
        return result

    def post(self):
        fields = self.get_validated_fields(AnswerPostSchema())
        game = self._get_game()
        question = self._get_question()
        team = self.team_query.get_by_uuid(fields['team_uuid'])
        answer = self.answer_query.get_by_uuid(fields['answer_uuid'])
        self.game_answer_command.upsert(
            game.id,
            question.id,
            team.id,
            answer.id,
        )
