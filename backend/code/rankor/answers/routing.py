def answers_routing(routing):
    routing.add(
        'rankor.answers.views.AdminAnswerListView',
        'admin_answers',
        '/admin/contests/{contest_uuid}/questions/{question_uuid}')
