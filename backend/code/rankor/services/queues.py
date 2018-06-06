from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@rabbitmq//')
app.conf.task_create_missing_queues = True
app.conf.task_ignore_result = True
app.conf.task_routes = {
    'rankor.services.broadcaster.*': {'queue': 'broadcaster'},
    'rankor.services.s1.*': {'queue': 's1'},
    'rankor.services.s2.*': {'queue': 's2'},
}
