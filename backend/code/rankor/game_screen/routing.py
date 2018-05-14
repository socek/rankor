def game_view_routing(routing):
    routing.add(
        'rankor.game_screen.views.GameView',
        'game_view',
        '/game/{game_id}')
    routing.add(
        'rankor.game_screen.views.HighScoreView',
        'highscore',
        '/game/{game_id}/highscore')
