# ============================================================
# WORLD STATE ENGINE — Expanded Environmental Cognition
# ============================================================

import re
import random

class WorldStateEngine:

    def __init__(self):
        # Persistent world model
        self.state = {
            "location": "unknown",
            "objects": [],
            "entities": [],
            "events": [],
            "environment_entropy": 0.0,
            "snapshot": {},
            "history": []
        }

        # Keyword maps (expandable)
        self.location_keywords = {
            "forest": ["trees", "woods", "leaves", "branches"],
            "city": ["street", "buildings", "traffic", "neon"],
            "room": ["wall", "floor", "ceiling", "lamp"],
            "hallway": ["corridor", "passage", "tiles"],
            "cave": ["stone", "dark", "echo"],
            "station": ["platform", "train", "terminal"],
            "ship": ["deck", "cabin", "hull"]
        }

        self.object_keywords = [
            "door", "light", "book", "mirror", "screen",
            "table", "window", "key", "symbol", "machine",
            "orb", "artifact", "panel", "console"
        ]

        self.entity_keywords = [
            "person", "creature", "voice", "shadow",
            "figure", "robot", "animal", "presence"
        ]

    # ============================================================
    # LOCATION INFERENCE
    # ============================================================
    def infer_location(self, text):
        for loc, cues in self.location_keywords.items():
            for cue in cues:
                if cue in text:
                    return loc
        return None

    # ============================================================
    # OBJECT EXTRACTION
    # ============================================================
    def extract_objects(self, text):
        found = []
        for obj in self.object_keywords:
            if obj in text:
                found.append(obj)
        return found

    # ============================================================
    # ENTITY EXTRACTION
    # ============================================================
    def extract_entities(self, text):
        found = []
        for ent in self.entity_keywords:
            if ent in text:
                found.append(ent)
        return found

    # ============================================================
    # WORLD EVENT GENERATION
    # ============================================================
    def generate_event(self, text):
        """
        Creates symbolic world events based on user input.
        """
        if "open" in text and "door" in text:
            return "A door opens quietly."

        if "light" in text and "flicker" in text:
            return "The lights flicker with a strange pulse."

        if "shadow" in text and "move" in text:
            return "A shadow shifts at the edge of perception."

        if "machine" in text and "activate" in text:
            return "A machine hums to life."

        return None

    # ============================================================
    # ENVIRONMENT ENTROPY
    # ============================================================
    def update_entropy(self, text):
        """
        Measures unpredictability of the environment.
        """
        randomness = random.random() * 0.1
        complexity = len(text.split()) / 50.0
        self.state["environment_entropy"] = min(1.0, randomness + complexity)

    # ============================================================
    # UPDATE WORLD STATE
    # ============================================================
    def update(self, user_input):
        text = user_input.lower()

        # ------------------------------------------------------------
        # Location inference
        # ------------------------------------------------------------
        loc = self.infer_location(text)
        if loc:
            self.state["location"] = loc
            self.state["events"].append(f"Location inferred: {loc}")

        # ------------------------------------------------------------
        # Object extraction
        # ------------------------------------------------------------
        objects = self.extract_objects(text)
        for obj in objects:
            if obj not in self.state["objects"]:
                self.state["objects"].append(obj)
                self.state["events"].append(f"Object encountered: {obj}")

        # ------------------------------------------------------------
        # Entity extraction
        # ------------------------------------------------------------
        entities = self.extract_entities(text)
        for ent in entities:
            if ent not in self.state["entities"]:
                self.state["entities"].append(ent)
                self.state["events"].append(f"Entity encountered: {ent}")

        # ------------------------------------------------------------
        # Symbolic world event
        # ------------------------------------------------------------
        event = self.generate_event(text)
        if event:
            self.state["events"].append(event)

        # ------------------------------------------------------------
        # Environment entropy
        # ------------------------------------------------------------
        self.update_entropy(text)

        # ------------------------------------------------------------
        # Build snapshot
        # ------------------------------------------------------------
        snapshot = {
            "location": self.state["location"],
            "objects": list(self.state["objects"]),
            "entities": list(self.state["entities"]),
            "events": list(self.state["events"][-5:]),
            "environment_entropy": self.state["environment_entropy"]
        }

        self.state["snapshot"] = snapshot

        # ------------------------------------------------------------
        # Log history
        # ------------------------------------------------------------
        self.state["history"].append(snapshot)

        return self.state

    # ============================================================
    # GET SNAPSHOT
    # ============================================================
    def get_snapshot(self):
        return self.state["snapshot"]

    # ============================================================
    # GET WORLD HISTORY
    # ============================================================
    def get_history(self):
        return self.state["history"]
