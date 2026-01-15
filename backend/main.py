from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {}

@app.post("/login")
def login(data: dict):
    tg_id = str(data["tg_id"])

    if tg_id not in users:
        users[tg_id] = {"balance": 1000}

    return users[tg_id]


@app.post("/spin")
def spin(data: dict):
    tg_id = str(data["tg_id"])
    user = users[tg_id]

    bet = 50
    roll = random.randint(1, 7)

    if roll == 7:
        user["balance"] += 300
        win = True
    else:
        user["balance"] -= bet
        win = False

    return {
        "roll": roll,
        "win": win,
        "balance": user["balance"]
    }
