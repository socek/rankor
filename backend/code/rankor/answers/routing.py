def answers_routing(routing):
    routing.add(
        'rankor.answers.views.AdminAnswerListView',
        'admin_answers',
        '/admin/contests/{contest_uuid}/questions/{question_uuid}/answers')
    routing.add(
        'rankor.answers.views.AdminAnswerView',
        'admin_answer',
        '/admin/contests/{contest_uuid}/questions/{question_uuid}/answers/{answer_uuid}')
