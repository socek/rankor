from time import time

from pytest import fixture

from rankor.application.testing import DeleteOnExit
from rankor.application.testing import IntegrationFixture
from rankor.events.drivers import ScreenCommand
from rankor.events.drivers import ScreenQuery
from rankor.events.models import Screen
from rankor.game.models import Game


class TestScreenDrivers(IntegrationFixture):
    game_data = {
        'name': 'game name',
    }

    @fixture
    def query(self, dbsession):
        return ScreenQuery(dbsession)

    @fixture
    def command(self, dbsession):
        return ScreenCommand(dbsession)

    @fixture
    def game(self, dbsession, contest_from_user):
        game_data = dict(self.game_data)
        game_data['contest_id'] = contest_from_user.id
        game_data['owner_id'] = contest_from_user.owner_id
        game = Game(**game_data)

        with DeleteOnExit(dbsession, game):
            yield game

    @fixture
    def screen(self, dbsession, game):
        screen = Screen(game_id=game.id)

        with DeleteOnExit(dbsession, screen):
            yield screen

    def test_get_by_id(self, screen, query):
        """
        .get_by_id should return screen by id
        """
        assert query.get_by_id(screen.id) == screen

    def test_list_for_game(self, screen, game, query):
        """
        .list_for_game should return list of screens for specyfied game
        """
        result = query.list_for_game(game.id)
        assert len(result) == 1
        assert result[0].id == screen.id

    def test_list_for_game_failed(self, game, query):
        """
        .list_for_game should return empty list of screens for specyfied game
        when no screen found
        """
        result = query.list_for_game(game.id)
        assert len(result) == 0

    def test_create_screen(self, game, query, command, dbsession):
        """
        .create_screen should create screen for game
        """
        screen = command.create_screen(game.id)
        with DeleteOnExit(dbsession, screen):
            assert screen

            result = query.list_for_game(game.id)
            assert len(result) == 1
            assert result[0].id == screen.id

    def test_send_event(self, screen, query, command, dbsession):
        """
        .send_event should create event and update screen object
        """
        event = command.send_event('change view', screen.id, view='newview')
        with DeleteOnExit(dbsession, event):
            dbsession.refresh(screen)

            assert screen.view == 'newview'
            assert event.screen_id == screen.id

    def test_list_event_after(self, screen, query, command, dbsession):
        """
        .list_event_after should list events after specyfic date in order of
        creation
        """
        event1 = command.send_event('view', screen.id)
        event2 = command.send_event('view', screen.id)
        event3 = command.send_event('view', screen.id)

        with DeleteOnExit(dbsession, event1):
            with DeleteOnExit(dbsession, event2):
                with DeleteOnExit(dbsession, event3):
                    result = query.list_events_after(screen.id, event1.created_at)
                    assert len(result) == 2
                    assert result[0].id == event2.id
                    assert result[1].id == event3.id

    def test_list_event_after_with_timestamp(self, screen, query, command, dbsession):
        """
        .list_event_after should list events after specyfic timestamp in order of
        creation
        """
        timestamp = time()
        event = command.send_event('view', screen.id)

        with DeleteOnExit(dbsession, event):
            result = query.list_events_after(screen.id, timestamp)
            assert len(result) == 1
            assert result[0].id == event.id
