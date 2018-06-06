from time import time

from rankor import app
from rankor.services.events import HelloEvent


def start_gateway():
    print('starting gateway')
    app.start('pyramid')  # change this to gateway

    event = HelloEvent()

    event.broadcast({'elo11': 1, 'timestamp': time()})
    data = event.get_response()
    print('recieved', data)
    event.purge()


start_gateway()
