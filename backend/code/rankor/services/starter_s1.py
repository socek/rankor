from rankor import app
from rankor.services.s1 import app as celery_app

print('get celery app for s1')

app.start('pyramid')
