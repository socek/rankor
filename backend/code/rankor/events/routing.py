def screen_routing(routing):
    routing.add(
        'rankor.events.views.HostScreenListView',
        'host_screens',
        '/host/{game_id}/screens')

    routing.add(
        'rankor.events.views.HostScreenView',
        'host_screen',
        '/host/{game_id}/screens/{screen_id}')
