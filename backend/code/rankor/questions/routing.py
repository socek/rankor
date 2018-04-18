def questions_routing(routing):
    routing.add(
        'rankor.questions.views.AdminQuestionListView',
        'admin_questions',
        '/admin/contests/{contest_uuid}/questions')
