# flake8: noqa
from sapp.plugins.sqlalchemy.alembic import AlembicScript

from rankor import app
from rankor.application.model import Model

# import or define all models here to ensure they are attached to the
# Model.metadata prior to any initialization routines

import rankor.answers.models
import rankor.auth.models
import rankor.contest.models
import rankor.questions.models
import rankor.game.models
import rankor.team.models
import rankor.game_answer.models


AlembicScript(app, Model, 'dbsession').run()
