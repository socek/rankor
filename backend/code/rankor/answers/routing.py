def answers_routing(routing):
    routing.add(
        'rankor.answers.views.AdminAnswerListView',
        'admin_answers',
        '/admin/contests/{contest_id}/questions/{question_id}/answers')
    routing.add(
        'rankor.answers.views.AdminAnswerView',
        'admin_answer',
        '/admin/contests/{contest_id}/questions/{question_id}/answers/{answer_id}')
