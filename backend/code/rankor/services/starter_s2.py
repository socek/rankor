from rankor import app
from rankor.services.s2 import app as celery_app

app.start('pyramid')
