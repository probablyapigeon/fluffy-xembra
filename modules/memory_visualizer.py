import json
import os
import time

# ============================================================
# MEMORY VISUALIZER — Readable Summaries of XEMBRA's Mind
# ============================================================

class MemoryVisualizer:
    def __init__(self, path="logs/xembra_memory.json"):
        self.path = path
        self.memory = self._load()

    # ------------------------------------------------------------
    # LOAD MEMORY FILE
    # ------------------------------------------------------------
    def _load(self):
        if not os.path.exists(self.path):
            return None
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    # ------------------------------------------------------------
    # GENERAL SUMMARY
    # ------------------------------------------------------------
    def summarize(self):
        if not self.memory:
            return "No memory data available."

        vocab_size = len(self.memory.get("vocab", {}))
        concept_size = len(self.memory.get("concepts", {}))
        identity_entries = len(self.memory.get("identity_history", []))
        emotional_entries = len(self.memory.get("emotional_history", []))
        dream_entries = len(self.memory.get("dream_fragments", []))
        world_entries = len(self.memory.get("world_events", []))
        interaction_entries = len(self.memory.get("user_interactions", []))

        return (
            f"XEMBRA Memory Summary:\n"
            f"- Vocabulary size: {vocab_size}\n"
            f"- Concept count: {concept_size}\n"
            f"- Identity snapshots: {identity_entries}\n"
            f"- Emotional snapshots: {emotional_entries}\n"
            f"- Dream fragments: {dream_entries}\n"
            f"- World events: {world_entries}\n"
            f"- User interactions: {interaction_entries}\n"
        )

    # ------------------------------------------------------------
    # IDENTITY DRIFT GRAPH (ASCII)
    # ------------------------------------------------------------
    def identity_graph(self, width=40):
        history = self.memory.get("identity_history", [])
        if not history:
            return "No identity history."

        graph = "Identity Drift Timeline:\n"

        for entry in history[-50:]:  # last 50 entries
            drift = entry.get("drift", 0.0)
            bar = "#" * int(drift * width)
            graph += f"{bar}\n"

        return graph

    # ------------------------------------------------------------
    # EMOTIONAL TIMELINE
    # ------------------------------------------------------------
    def emotional_timeline(self, limit=20):
        history = self.memory.get("emotional_history", [])
        if not history:
            return "No emotional history."

        lines = ["Emotional Timeline (recent):"]

        for entry in history[-limit:]:
            mood = entry.get("mood", 50)
            curiosity = entry.get("curiosity", 50)
            closeness = entry.get("closeness", 0.5)

            lines.append(
                f"- Mood: {mood}, Curiosity: {curiosity}, Closeness: {closeness}"
            )

        return "\n".join(lines)

    # ------------------------------------------------------------
    # DREAM FRAGMENT DIGEST
    # ------------------------------------------------------------
    def dream_digest(self, limit=10):
        dreams = self.memory.get("dream_fragments", [])
        if not dreams:
            return "No dream fragments stored."

        lines = ["Dream Fragment Digest (recent):"]

        for entry in dreams[-limit:]:
            fragment = entry.get("fragment", "")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entry["time"]))
            lines.append(f"[{timestamp}] {fragment}")

        return "\n".join(lines)

    # ------------------------------------------------------------
    # WORLD EVENT SUMMARY
    # ------------------------------------------------------------
    def world_summary(self, limit=15):
        events = self.memory.get("world_events", [])
        if not events:
            return "No world events stored."

        lines = ["World Interaction Summary (recent):"]

        for entry in events[-limit:]:
            event = entry.get("event", {})
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entry["time"]))
            lines.append(f"[{timestamp}] {event}")

        return "\n".join(lines)

    # ------------------------------------------------------------
    # USER INTERACTION SUMMARY
    # ------------------------------------------------------------
    def interaction_summary(self, limit=15):
        interactions = self.memory.get("user_interactions", [])
        if not interactions:
            return "No user interactions stored."

        lines = ["User Interaction Summary (recent):"]

        for entry in interactions[-limit:]:
            user = entry.get("user", "")
            reply = entry.get("reply", "")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entry["time"]))
            lines.append(f"[{timestamp}] User: {user}\n           XEMBRA: {reply}")

        return "\n".join(lines)

    # ------------------------------------------------------------
    # CONCEPT OVERVIEW
    # ------------------------------------------------------------
    def concept_overview(self, limit=20):
        concepts = self.memory.get("concepts", {})
        if not concepts:
            return "No concepts stored."

        # Sort by frequency
        sorted_concepts = sorted(
            concepts.items(),
            key=lambda x: x[1].get("frequency", 0),
            reverse=True
        )

        lines = ["Top Concepts:"]

        for name, data in sorted_concepts[:limit]:
            freq = data.get("frequency", 0)
            drift_w = data.get("drift_weight", 0.0)
            dream_w = data.get("dream_weight", 0.0)
            lines.append(
                f"- {name} (freq: {freq}, drift_w: {drift_w:.2f}, dream_w: {dream_w:.2f})"
            )

        return "\n".join(lines)
