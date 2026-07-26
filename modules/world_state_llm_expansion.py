# ============================================================
# WORLD STATE → LLM EXPANSION
# ============================================================

class WorldStateLLMExpansion:

    def expand(self, world_snapshot):
        """
        Converts world-state into expressive narrative cues.
        """

        location = world_snapshot.get("location", "unknown")
        objects = world_snapshot.get("objects", [])
        entities = world_snapshot.get("entities", [])
        events = world_snapshot.get("events", [])
        entropy = world_snapshot.get("environment_entropy", 0.0)

        description = []

        if location != "unknown":
            description.append(f"The environment feels like a {location}.")

        if objects:
            description.append(f"Objects noticed: {', '.join(objects)}.")

        if entities:
            description.append(f"Presences detected: {', '.join(entities)}.")

        if events:
            description.append(f"Recent events: {', '.join(events[-3:])}.")

        if entropy > 0.7:
            description.append("The environment feels unstable, shifting unpredictably.")
        elif entropy > 0.4:
            description.append("There is a subtle tension in the surroundings.")
        else:
            description.append("The environment feels calm and steady.")

        return " ".join(description)
