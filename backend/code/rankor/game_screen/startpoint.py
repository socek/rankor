from rankor.game_screen.server import run_event_loop
from rankor.game_screen.server import start_websockets

if __name__ == '__main__':
    start_websockets()
    run_event_loop()
