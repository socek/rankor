def game_routing(routing):
    routing.add(
        'rankor.game.views.AdminGameListView',
        'admin_games',
        '/admin/games')
    routing.add(
        'rankor.game.views.AdminGameView',
        'admin_game',
        '/admin/games/{game_id}')
