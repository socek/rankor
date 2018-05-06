def game_view_routing(routing):
    routing.add(
        'rankor.game_screen.views.GameView',
        'game_view',
        '/game/{game_uuid}')
