def contest_routing(routing):
    routing.add(
        'rankor.contest.views.AdminContestListView',
        'admin_contests',
        '/admin/contests')
    routing.add(
        'rankor.contest.views.AdminContestView',
        'admin_contest',
        '/admin/contests/{contest_id}')
