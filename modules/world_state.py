# ============================================================
# WORLD STATE ENGINE — Environment Tracking
# ============================================================

import re

class WorldStateEngine:

    def __init__(self):
        # Persistent world model
        self.state = {
            "location": "unknown",
            "objects": [],
            "entities": [],
            "last_event": None,
            "snapshot": {}
        }

        # Simple keyword maps
        self.location_keywords = [
            "room", "forest", "city", "hallway", "cave",
            "street", "tower", "lab", "station", "ship"
        ]

        self.object_keywords = [
            "door", "light", "book", "mirror", "screen",
            "table", "window", "key", "symbol", "machine"
        ]

        self.entity_keywords = [
            "person", "creature", "voice", "shadow",
            "figure", "robot", "animal"
        ]

    # ============================================================
    # UPDATE WORLD STATE FROM USER INPUT
    # ============================================================
    def update(self, user_input):
        """
        Extracts world cues from user input and updates the world model.
        """

        text = user_input.lower()

        # ------------------------------------------------------------
        # Detect location
        # ------------------------------------------------------------
        for loc in self.location_keywords:
            if loc in text:
                self.state["location"] = loc
                self.state["last_event"] = f"Location changed to {loc}"

        # ------------------------------------------------------------
        # Detect objects
        # ------------------------------------------------------------
        for obj in self.object_keywords:
            if obj in text and obj not in self.state["objects"]:
                self.state["objects"].append(obj)
                self.state["last_event"] = f"Object encountered: {obj}"

        # ------------------------------------------------------------
        # Detect entities
        # ------------------------------------------------------------
        for ent in self.entity_keywords:
            if ent in text and ent not in self.state["entities"]:
                self.state["entities"].append(ent)
                self.state["last_event"] = f"Entity encountered: {ent}"

        # ------------------------------------------------------------
        # Build snapshot for memory + LLM
        # ------------------------------------------------------------
        self.state["snapshot"] = {
            "location": self.state["location"],
            "objects": list(self.state["objects"]),
            "entities": list(self.state["entities"]),
            "last_event": self.state["last_event"]
        }

        return self.state

    # ============================================================
    # GET WORLD SNAPSHOT
    # ============================================================
    def get_snapshot(self):
        return self.state["snapshot"]
