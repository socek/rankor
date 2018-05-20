from rankor import app
from rankor.events.drivers import ScreenCommand


class Event(object):
    def __init__(self, **kwargs):
        self.data = kwargs

    def send(self):
        with app as context:
            command = ScreenCommand(context.dbsession)
            command.send_event(self.name, **self.data)


class ChangeViewEvent(Event):
    name = 'change_view'

    _views = ('welcome', 'highscore', 'question')

    def __init__(self, screen_id, view):
        assert view in self._views
        super().__init__(screen_id=screen_id, view=view)


class ShowQuestionEvent(Event):
    name = 'show_question'

    def __init__(self, screen_id, question_id, team_id):
        super().__init__(
            screen_id=screen_id,
            view='question',
            question_id=question_id,
            team_id=team_id
        )


class AttachTeamEvent(Event):
    name = 'attach_team'

    def __init__(self, screen_id, team_id):
        super().__init__(
            screen_id=screen_id,
            view='question',
            team_id=team_id,
        )


class SelectAnswerEvent(Event):
    name = 'select_answer'

    def __init__(self, screen_id, question_id, answer_id):
        super().__init__(
            screen_id=screen_id,
            view='question',
            question_id=question_id,
            answer_id=answer_id,
        )


class VeryfiAnswerEvent(Event):
    name = 'veryfi_answer'

    def __init__(self, screen_id, question_id, team_id, answer_id):
        super().__init__(
            screen_id=screen_id,
            view='question',
            question_id=question_id,
            answer_id=answer_id,
            team_id=team_id,
        )
