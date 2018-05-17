from sapp.plugins.pyramid.routing import Routing

from rankor.answers.routing import answers_routing
from rankor.auth.routing import auth_routing
from rankor.contest.routing import contest_routing
from rankor.game.routing import game_routing
from rankor.game_screen.routing import game_view_routing
from rankor.home.routing import home_routing
from rankor.host.routing import host_routing
from rankor.menu.routing import meny_routing
from rankor.questions.routing import questions_routing


class RankorRouting(Routing):
    def make(self):
        home_routing(self)
        auth_routing(self)
        meny_routing(self)
        contest_routing(self)
        questions_routing(self)
        answers_routing(self)
        game_routing(self)
        host_routing(self)
        game_view_routing(self)
