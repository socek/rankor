from asyncio import get_event_loop
from logging import getLogger

from websockets import serve

from rankor import app
from rankor.game_screen.client import Client

log = getLogger(__name__)


async def echo(websocket, path):
    with app as context:
        await Client(context, websocket).run()


def start_websockets():
    app.start('pyramid')  # change this to websockets


def run_event_loop():
    log.info("Starting wesockets")
    loop = get_event_loop()
    loop.run_until_complete(serve(echo, '', 8765))
    loop.run_forever()
