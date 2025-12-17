import random
import time

ROOMS = {}

def create_room(max_players):
    code = ''.join(random.choices("ABCDEFGHJKLMNPQRSTUVWXYZ23456789", k=5))
    ROOMS[code] = {
        "players": {},
        "phase": "lobby",
        "created": time.time(),
        "expires": time.time() + 1800
    }
    return code

def cleanup():
    now = time.time()
    for code in list(ROOMS.keys()):
        if now > ROOMS[code]["expires"]:
            del ROOMS[code]
