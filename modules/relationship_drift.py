import random
import time

def update_relationship(relationship, user_input):
    trust = relationship.get("trust", 0.5)
    bond = relationship.get("bond", 0.5)

    # Trust grows with gentle interactions
    if any(word in user_input.lower() for word in ["hi", "welcome", "thank", "good", "nice"]):
        trust += 0.03
        bond += 0.02

    # Trust drops with harsh interactions
    if any(word in user_input.lower() for word in ["bad", "hate", "stop", "no"]):
        trust -= 0.05

    # Natural drift
    trust += random.uniform(-0.01, 0.01)
    bond += random.uniform(-0.01, 0.01)

    trust = max(0.0, min(1.0, trust))
    bond = max(0.0, min(1.0, bond))

    relationship["trust"] = trust
    relationship["bond"] = bond
    relationship["last_interaction"] = time.time()

    return relationship
