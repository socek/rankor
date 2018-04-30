def questions_routing(routing):
    routing.add(
        'rankor.questions.views.AdminQuestionListView',
        'admin_questions',
        '/admin/contests/{contest_uuid}/questions')
    routing.add(
        'rankor.questions.views.AdminQuestionView',
        'admin_question',
        '/admin/contests/{contest_uuid}/questions/{question_uuid}')
