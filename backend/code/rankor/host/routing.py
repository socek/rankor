def host_routing(routing):
    routing.add(
        'rankor.host.views.HostQuestionListView',
        'host_questions',
        '/host/{game_id}/questions')
    routing.add(
        'rankor.host.views.HostTeamListView',
        'host_teams',
        '/host/{game_id}/teams')
    routing.add(
        'rankor.host.views.HostQuestionView',
        'host_question',
        '/host/{game_id}/questions/{question_id}')
