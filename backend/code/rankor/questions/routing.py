def questions_routing(routing):
    routing.add(
        'rankor.questions.views.AdminQuestionView',
        'admin_questions',
        '/admin/contests/{contest_uuid}/questions')
