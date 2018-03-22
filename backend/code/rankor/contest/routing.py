def contest_routing(routing):
    routing.add(
        'rankor.contest.views.AdminContestView',
        'admin_contests',
        '/admin/contests')
