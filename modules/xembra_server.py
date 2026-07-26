# ============================================================
# XEMBRA SERVER — FastAPI Web Interface
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import threading
import time

from xembra import XEMBRA
from autonomous_cycle import run_autonomous_cycle
from memory_visualizer import MemoryVisualizer


# ------------------------------------------------------------
# REQUEST MODELS
# ------------------------------------------------------------

class UserMessage(BaseModel):
    text: str

class WorldEvent(BaseModel):
    type: str
    name: str

class StyleChange(BaseModel):
    style: str


# ------------------------------------------------------------
# INITIALIZE SERVER + XEMBRA INSTANCE
# ------------------------------------------------------------

app = FastAPI(title="XEMBRA Creature Engine")

xembra = XEMBRA(style="neutral")


# ------------------------------------------------------------
# AUTONOMOUS BACKGROUND THREAD
# ------------------------------------------------------------

def autonomous_loop():
    while True:
        result = run_autonomous_cycle(xembra)
        # You can log autonomous output here if desired
        time.sleep(1.0)

thread = threading.Thread(target=autonomous_loop, daemon=True)
thread.start()


# ------------------------------------------------------------
# ENDPOINTS
# ------------------------------------------------------------

@app.post("/talk")
def talk_to_xembra(msg: UserMessage):
    reply = xembra.talk(msg.text)
    return {"reply": reply}


@app.post("/sense")
def sense_world(event: WorldEvent):
    reaction = xembra.sense({"type": event.type, "name": event.name})
    return {"reaction": reaction}


@app.post("/style")
def change_style(style: StyleChange):
    xembra.set_style(style.style)
    return {"status": "ok", "style": style.style}


@app.get("/memory")
def memory_summary():
    viz = MemoryVisualizer()
    return {"summary": viz.summarize()}


@app.get("/dreams")
def dream_digest():
    viz = MemoryVisualizer()
    return {"dreams": viz.dream_digest()}


@app.get("/identity")
def identity_timeline():
    viz = MemoryVisualizer()
    return {"identity_graph": viz.identity_graph()}


@app.get("/emotion")
def emotion_timeline():
    viz = MemoryVisualizer()
    return {"emotion_timeline": viz.emotional_timeline()}


@app.get("/world")
def world_events():
    viz = MemoryVisualizer()
    return {"world_summary": viz.world_summary()}


@app.get("/interactions")
def interaction_history():
    viz = MemoryVisualizer()
    return {"interaction_summary": viz.interaction_summary()}


# ------------------------------------------------------------
# SERVER ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    uvicorn.run("xembra_server:app", host="0.0.0.0", port=8000, reload=True)
