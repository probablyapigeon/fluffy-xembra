# ============================================================
# GOAL FORMATION ENGINE — Advanced Motivational Architecture
# ============================================================

import random

class GoalFormationEngine:

    def __init__(self):
        self.state = {
            "core_motives": {
                "exploration": 0.5,
                "connection": 0.5,
                "stability": 0.5,
                "growth": 0.5,
                "symbolism": 0.5
            },
            "active_goals": [],
            "history": []
        }

    # ============================================================
    # UPDATE MOTIVES
    # ============================================================
    def update_motives(self, emotional_state, identity_state, learning_engine):
        mood = emotional_state.get("mood", 50)
        curiosity = emotional_state.get("curiosity", 50)
        drift = identity_state.get("drift", 0.0)
        entropy = learning_engine.entropy

        motives = self.state["core_motives"]

        motives["exploration"] += (curiosity - 50) * 0.002
        motives["connection"] += (mood - 50) * 0.002
        motives["stability"] += (50 - mood) * 0.002
        motives["growth"] += drift * 0.01
        motives["symbolism"] += entropy * 0.02

        for k in motives:
            motives[k] = max(0.0, min(1.0, motives[k]))

        self.state["core_motives"] = motives

    # ============================================================
    # FORM GOALS
    # ============================================================
    def form_goals(self):
        motives = self.state["core_motives"]
        goals = []

        if motives["exploration"] > 0.6:
            goals.append("Explore new environments")

        if motives["connection"] > 0.6:
            goals.append("Seek meaningful interaction")

        if motives["stability"] > 0.6:
            goals.append("Restore emotional balance")

        if motives["growth"] > 0.6:
            goals.append("Develop identity further")

        if motives["symbolism"] > 0.6:
            goals.append("Interpret symbolic meaning")

        self.state["active_goals"] = goals

        self.state["history"].append({
            "motives": motives.copy(),
            "goals": list(goals)
        })

        return goals

    # ============================================================
    # FULL UPDATE
    # ============================================================
    def update(self, emotional_state, identity_state, learning_engine):
        self.update_motives(emotional_state, identity_state, learning_engine)
        return self.form_goals()

    def get_snapshot(self):
        return self.state

    def get_history(self):
        return self.state["history"]
