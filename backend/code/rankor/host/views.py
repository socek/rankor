from pyramid.httpexceptions import HTTPNotFound
from sapp.decorators import WithContext
from sqlalchemy.orm.exc import NoResultFound

from rankor import app
from rankor.answers.drivers import AnswerQuery
from rankor.answers.schema import AnswerSchema
from rankor.application.cache import cache_per_request
from rankor.auth.view_mixins import AuthenticatedView
from rankor.game.drivers import GameQuery
from rankor.game_answer.drivers import GameAnswerCommand
from rankor.game_answer.drivers import GameAnswerQuery
from rankor.game_screen.models import GameScreen
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

    @property
    def team_query(self):
        return TeamQuery(self.dbsession)

    @property
    def team_command(self):
        return TeamCommand(self.dbsession)

    @property
    def answer_query(self):
        return AnswerQuery(self.dbsession)

    @property
    def game_answer_command(self):
        return GameAnswerCommand(self.dbsession)

    @property
    def game_answer_query(self):
        return GameAnswerQuery(self.dbsession)

    @WithContext(app, args=['redis'])
    def game_screen(self, redis):
        return GameScreen(redis, self._get_game_id())

    def _get_game_id(self):
        return self.request.matchdict['game_id']

    @cache_per_request('game')
    def _get_game(self):
        try:
            return self.game_query.get_by_id(self._get_game_id())
        except NoResultFound:
            raise HTTPNotFound()

    def validate(self):
        super().validate()
        self._get_game()


class HostQuestionBaseView(HostBaseView):
    def _get_question_id(self):
        return self.request.matchdict['question_id']

    @cache_per_request('question')
    def _get_question(self):
        try:
            return self.question_query.get_for_answer(
                self._get_question_id(), self._get_game_id())
        except NoResultFound:
            raise HTTPNotFound()

    def validate(self):
        super().validate()
        self._get_question()


class HostQuestionListView(HostBaseView):
    def get(self):
        id = self._get_game_id()
        elements = self.question_query.list_for_game(id)
        result = FullQuestionSchema(many=True).dump(elements)
        return result


class HostQuestionView(HostQuestionBaseView):
    def get(self):
        result = {}
        result['question'] = self._get_question_result()
        result['teams'] = self._get_teams_result()
        result['answers'] = self._get_answers_result()
        result['answer'] = self._get_current_answer_result()
        return result

    def _get_question_result(self):
        return QuestionSchema().dump(self._get_question())

    def _get_teams_result(self):
        id = self._get_game_id()
        elements = self.team_query.list_for_game(id)
        return TeamSchema(many=True).dump(elements)

    def _get_answers_result(self):
        answers = self.answer_query.list_for_question(
            self._get_question_id())
        schema = AnswerSchema()
        return [schema.dump(answer) for answer in answers]

    def _get_current_answer_result(self):
        game = self._get_game()
        question = self._get_question()

        try:
            game_answer = self.game_answer_query.get_by_game_and_question(
                game.id,
                question.id,
            )
            return {
                'team_id': game_answer.team.id,
                'answer_id': game_answer.answer.id
            }
        except NoResultFound:
            return {'team_id': None, 'answer_id': None}

    def post(self):
        fields = self.get_validated_fields(AnswerPostSchema())
        game = self._get_game()
        question = self._get_question()
        team = self.team_query.get_by_id(fields['team_id'])
        answer = self.answer_query.get_by_id(fields['answer_id'])
        self.game_answer_command.upsert(
            game.id,
            question.id,
            team.id,
            answer.id,
        )
        self.game_screen().set_value(
            view='question',
            view_data={
                'team_name': team.name,
                'question_id': question.id,
                'answer_id': answer.id,
                'is_correct': answer.is_correct
            })


class HostTeamListView(HostBaseView):
    def get(self):
        id = self._get_game_id()
        elements = self.team_query.list_for_game(id)
        result = TeamSchema(many=True).dump(elements)
        return result

    def post(self):
        game = self._get_game()

        fields = self.get_validated_fields(TeamSchema())
        fields['game_id'] = game.id

        team = self.team_command.create(**fields)

        return {
            'team_id': team.id,
        }
