from time import time
from rankor.services.broadcaster import broadcast
from rankor.services.events import HelloEvent
from rankor.services.queues import app


@app.task
def s2(event, request_id, payload=None):
    print('s2 recieved', event, payload)
    if event == 'register':
        register.delay(event, payload)
    elif event == 'hello':
        hello.delay(event, request_id, payload)


@app.task
def register(event, request_id, payload):
    broadcast.delay('new event', ignores=[s2.__name__])


@app.task
def hello(event, request_id, payload):
    HelloEvent(request_id).send_response('s2', {'s2': 'payload', 'timestamp': time()})
