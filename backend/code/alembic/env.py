# flake8: noqa
from sapp.plugins.sqlalchemy.env import AlembicEnv

from mypet import app
from mypet.application.model import Model

# import or define all models here to ensure they are attached to the
# Model.metadata prior to any initialization routines

AlembicEnv(main, Model, 'database').run()
