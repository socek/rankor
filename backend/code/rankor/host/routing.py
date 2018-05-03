def host_routing(routing):
    routing.add(
        'rankor.host.views.HostQuestionListView',
        'host_questions',
        '/host/{game_uuid}/questions')
    routing.add(
        'rankor.host.views.HostTeamListView',
        'host_teams',
        '/host/{game_uuid}/teams')
