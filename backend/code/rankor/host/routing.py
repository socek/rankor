def host_routing(routing):
    routing.add(
        'rankor.host.views.HostQuestionListView',
        'host_questions',
        '/host/{game_uuid}/questions')
    routing.add(
        'rankor.host.views.HostQuestionView',
        'host_question',
        '/host/{game_uuid}/questions/{question_uuid}')
    routing.add(
        'rankor.host.views.HostAnswerListView',
        'host_answers',
        '/host/{game_uuid}/questions/{question_uuid}/answers')
    routing.add(
        'rankor.host.views.HostTeamListView',
        'host_teams',
        '/host/{game_uuid}/teams')
