def host_routing(routing):
    routing.add(
        'rankor.host.views.HostQuestionListView',
        'host_questions',
        '/host/{game_uuid}/questions')
