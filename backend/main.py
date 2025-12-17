from fastapi import FastAPI, HTTPException
from .mafia import ROOMS, create_room, cleanup
import random

app = FastAPI()

@app.post("/create")
def create(players: int = 6):
    cleanup()
    code = create_room(players)
    return {"code": code}

@app.post("/join")
def join(code: str, name: str):
    cleanup()
    if code not in ROOMS:
        raise HTTPException(404, "Room not found")
    room = ROOMS[code]
    if name in room["players"]:
        return {"ok": True}
    room["players"][name] = {
        "role": None,
        "alive": True,
        "vote": None
    }
    return {"ok": True}

@app.post("/start")
def start(code: str):
    if code not in ROOMS:
        raise HTTPException(404)
    room = ROOMS[code]
    names = list(room["players"].keys())
    mafia = random.choice(names)
    for n in names:
        room["players"][n]["role"] = "mafia" if n == mafia else "villager"
    room["phase"] = "night"
    return {"ok": True}

@app.post("/vote")
def vote(code: str, voter: str, target: str):
    room = ROOMS[code]
    room["players"][voter]["vote"] = target
    return {"ok": True}

@app.get("/state")
def state(code: str):
    if code not in ROOMS:
        raise HTTPException(404)
    return ROOMS[code]
