# flake8: noqa
from sapp.plugins.sqlalchemy.env import AlembicEnv

from cashflow import app
from cashflow.application.model import Model

# import or define all models here to ensure they are attached to the
# Model.metadata prior to any initialization routines

import cashflow.auth.models
import cashflow.wallet.models

AlembicEnv(app, Model, 'dbsession').run()
