# ============================================================
# FULL LOG DUMP — Print ALL internal logs from XEMBRA
# ============================================================

def dump_full_logs(xembra):
    out = []

    out.append("\n================ FULL LOG DUMP ================\n")

    # ------------------------------------------------------------
    # DREAM FRAGMENTS
    # ------------------------------------------------------------
    out.append("DREAM FRAGMENTS:")
    if hasattr(xembra.memory_log, "dream_cache"):
        for frag in xembra.memory_log.dream_cache:
            out.append(f"  - {frag}")
    else:
        out.append("  (none)")

    # ------------------------------------------------------------
    # IDENTITY SNAPSHOTS
    # ------------------------------------------------------------
    out.append("\nIDENTITY SNAPSHOTS:")
    if hasattr(xembra.memory_log, "identity_snapshots"):
        for snap in xembra.memory_log.identity_snapshots:
            out.append(f"  - {snap}")
    else:
        out.append("  (none)")

    # ------------------------------------------------------------
    # EMOTIONAL SNAPSHOTS
    # ------------------------------------------------------------
    out.append("\nEMOTIONAL SNAPSHOTS:")
    if hasattr(xembra.memory_log, "emotional_snapshots"):
        for snap in xembra.memory_log.emotional_snapshots:
            out.append(f"  - {snap}")
    else:
        out.append("  (none)")

    # ------------------------------------------------------------
    # USER INTERACTIONS
    # ------------------------------------------------------------
    out.append("\nUSER INTERACTIONS:")
    if hasattr(xembra.memory_log, "user_interactions"):
        for ui in xembra.memory_log.user_interactions:
            out.append(f"  - {ui}")
    else:
        out.append("  (none)")

    # ------------------------------------------------------------
    # WORLD EVENTS
    # ------------------------------------------------------------
    out.append("\nWORLD EVENTS:")
    if hasattr(xembra.memory_log, "world_events"):
        for event in xembra.memory_log.world_events:
            out.append(f"  - {event}")
    else:
        out.append("  (none)")

    # ------------------------------------------------------------
    # LEARNING ENGINE FRAGMENTS
    # ------------------------------------------------------------
    out.append("\nLEARNING ENGINE FRAGMENTS:")
    if hasattr(xembra.learning_engine, "recent_fragments"):
        for frag in xembra.learning_engine.recent_fragments:
            out.append(f"  - {frag}")
    else:
        out.append("  (none)")

    out.append("\n================================================\n")

    return "\n".join(out)
