from time import time

from rankor.services.queues import app
from rankor.services.events import HelloEvent


@app.task
def s1(event, request_id, payload=None):
    print('s1 recieved', event, payload)
    if event == 'hello':
        HelloEvent(request_id).send_response('s1', {'s1': 'payload', 'timestamp': time()})


