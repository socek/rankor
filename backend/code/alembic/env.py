# flake8: noqa
from sapp.plugins.sqlalchemy.env import AlembicEnv

from rankor import app
from rankor.application.model import Model

# import or define all models here to ensure they are attached to the
# Model.metadata prior to any initialization routines

import rankor.auth.models

AlembicEnv(app, Model, 'dbsession').run()
