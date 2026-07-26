# ============================================================
# DREAM CYCLE ENGINE — Subconscious Expression & Symbolic Drift
# ============================================================

import random

class DreamCycleEngine:

    def __init__(self):
        self.state = {
            "mode": "awake",            # awake | dreaming | deepdream
            "residue": [],
            "motifs": [],
            "intensity": 0.0,
            "history": []
        }

        # Symbolic dream motifs
        self.motif_bank = [
            "mirrors", "shadows", "floating lights", "fractured rooms",
            "endless corridors", "soft voices", "glowing symbols",
            "shifting landscapes", "echoing footsteps", "spirals",
            "distant figures", "broken clocks", "drifting feathers"
        ]

    # ============================================================
    # DREAM MODE UPDATE
    # ============================================================
    def update(self, identity_state):
        """
        Updates dream mode based on identity drift and coherence.
        """

        drift = identity_state.get("drift", 0.0)
        coherence = identity_state.get("coherence", 0.5)

        # Dream mode logic
        if drift > 0.8 and coherence < 0.4:
            self.state["mode"] = "dreaming"
        elif drift > 1.2 and coherence < 0.3:
            self.state["mode"] = "deepdream"
        else:
            self.state["mode"] = "awake"

        # Dream intensity
        self.state["intensity"] = min(1.0, drift * (1.0 - coherence))

        # Generate motifs if dreaming
        if self.state["mode"] in ["dreaming", "deepdream"]:
            self.generate_motifs()

        # Log dream state
        snapshot = {
            "mode": self.state["mode"],
            "intensity": self.state["intensity"],
            "motifs": list(self.state["motifs"]),
            "residue": list(self.state["residue"])
        }

        self.state["history"].append(snapshot)

        return self.state

    # ============================================================
    # GENERATE DREAM MOTIFS
    # ============================================================
    def generate_motifs(self):
        """
        Creates symbolic dream motifs based on intensity.
        """

        count = 1 + int(self.state["intensity"] * 4)
        motifs = random.sample(self.motif_bank, count)

        self.state["motifs"] = motifs

        # Add motifs to dream residue
        for m in motifs:
            self.state["residue"].append(f"Dream motif: {m}")

    # ============================================================
    # DREAM EXPRESSION (FOR LLM)
    # ============================================================
    def express(self):
        """
        Produces a symbolic dream expression fragment for the LLM.
        """

        mode = self.state["mode"]
        motifs = self.state["motifs"]
        intensity = self.state["intensity"]

        if mode == "awake":
            return None

        if mode == "dreaming":
            return {
                "mode": mode,
                "intensity": intensity,
                "description": f"A soft dream filled with {', '.join(motifs)}."
            }

        if mode == "deepdream":
            return {
                "mode": mode,
                "intensity": intensity,
                "description": f"A surreal deepdream where {', '.join(motifs)} twist into impossible shapes."
            }

    # ============================================================
    # GET DREAM RESIDUE
    # ============================================================
    def get_residue(self):
        return self.state["residue"]

    # ============================================================
    # GET DREAM HISTORY
    # ============================================================
    def get_history(self):
        return self.state["history"]
