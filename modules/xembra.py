# ============================================================
# XEMBRA CORE — Hybrid Cognitive Agent (Stable Build)
# ============================================================

from emotional_governor import EmotionalGovernor
from personality_drift import PersonalityDriftEngine
from goal_formation import GoalFormationEngine
from world_state_engine import WorldStateEngine
from world_state_llm_expansion import WorldStateLLMExpansion
from dream_cycle import DreamCycleEngine
from dream_surrealism_layer import DreamSurrealismLayer
from learning_engine import LearningEngine
from identity_engine import IdentityEngine
from identity_llm_narration import IdentityLLMNarration
from coherence_engine import update_coherence
from memory_consolidation import consolidate_memory, build_autobiographical_memory
from timeline_engine import TimelineEngine
from xembra_narrative_engine.llm_adapter import XembraLLMAdapter


class XEMBRA:
    def __init__(self):

        # ------------------------------------------------------------
        # NEW MODULES
        # ------------------------------------------------------------
        self.goal_formation = GoalFormationEngine()
        self.world_expansion = WorldStateLLMExpansion()
        self.dream_expansion = DreamSurrealismLayer()
        self.identity_expansion = IdentityLLMNarration()
        self.timeline_engine = TimelineEngine()

        # ------------------------------------------------------------
        # Core Cognitive State
        # ------------------------------------------------------------
        self.identity_engine = IdentityEngine()
        self.identity_state = self.identity_engine.initial_state()

        self.emotional_state = {
            "mood": 50,
            "curiosity": 50,
            "vector": [0.5, 0.5],
            "history": []
        }

        # ------------------------------------------------------------
        # Cognitive Modules
        # ------------------------------------------------------------
        self.emotion_engine = EmotionalGovernor()
        self.personality_engine = PersonalityDriftEngine()
        self.world_engine = WorldStateEngine()
        self.dream_engine = DreamCycleEngine()
        self.learning_engine = LearningEngine()
        self.llm = XembraLLMAdapter()

        # ------------------------------------------------------------
        # Logs
        # ------------------------------------------------------------
        self.logs = []
        self.dream_log = []
        self.identity_log = []
        self.emotion_log = []

        self.autonomous = True
        self.style = "default"


    # ============================================================
    # MAIN AGENT LOOP — TALK
    # ============================================================

    def talk(self, user_input):

        # 1. Emotional Update
        self.emotional_state = self.emotion_engine.compute(user_input, self.emotional_state)
        self.emotion_log.append(f"Mood {self.emotional_state['mood']}, Curiosity {self.emotional_state['curiosity']}")

        # 2. Identity Update
        self.identity_state = self.identity_engine.update(self.identity_state, self.emotional_state)
        self.identity_log.append(f"Identity drift: {self.identity_state['drift']}")

        # 2b. Identity → LLM Narration
        identity_expanded = self.identity_expansion.expand(self.identity_state)

        # 3. Personality Drift
        personality_state = self.personality_engine.compute(
            self.emotional_state,
            self.identity_state,
            self.learning_engine
        )

        # 4. World-State Update
        world_state = self.world_engine.update(user_input)

        # 4b. World-State → LLM Expansion
        world_expanded = self.world_expansion.expand(world_state["snapshot"])

        # 5. Dream Cycle Update
        self.dream_engine.update(self.identity_state)

        # 5b. Dream Expression
        dream_expression = self.dream_engine.express()
        dream_expanded = self.dream_expansion.expand(dream_expression)

        if dream_expression:
            self.dream_log.append(dream_expression["description"])

        # 6. Learning Update
        self.learning_engine.update(user_input)

        # 6b. Learning Expression
        learning_expression = self.learning_engine.express()

        # 7. Goals & Motivations (legacy)
        goals_state = {
            "basin": "default",
            "probabilities": [0.5, 0.5],
            "drift": self.identity_state["drift"],
            "memory_kernel": 0.5,
            "level": "stable"
        }

        # 7b. Advanced Goal Formation
        goal_formation_state = self.goal_formation.update(
            self.emotional_state,
            self.identity_state,
            self.learning_engine
        )

        # 8. Coherence Update
        self.identity_state["coherence"] = update_coherence(
            self.identity_state,
            self.emotional_state,
            self.learning_engine
        )

        # 9. Symbolic Memory Fragment
        fragment = consolidate_memory(
            self.identity_state,
            self.learning_engine,
            self.emotional_state
        )

        # 10. Full Autobiographical Memory
        memory_state = build_autobiographical_memory(
            self.identity_state,
            self.learning_engine,
            self.emotional_state,
            self.personality_engine,
            world_state,
            self.dream_engine,
            self.timeline_engine,
            dream_expression=dream_expression,
            learning_expression=learning_expression,
            world_expanded=world_expanded,
            dream_expanded=dream_expanded,
            identity_expanded=identity_expanded,
            goal_formation_state=goal_formation_state
        )

        # 11. Generate Narrative Page
        page = self.llm.generate_page(
            self.identity_state,
            goals_state,
            memory_state
        )

        # 12. Store Timeline
        self.timeline_engine.add(page)

        # 13. Log Interaction
        self.logs.append(f"[USER] {user_input}")
        self.logs.append(f"[XEMBRA] {page}")

        return page


    # ============================================================
    # ACCESSORS
    # ============================================================

    def show_memory(self):
        return "\n".join(self.timeline_engine.get_timeline()[-10:])

    def show_identity(self):
        return "\n".join(self.identity_log[-10:])

    def show_emotion(self):
        return "\n".join(self.emotion_log[-10:])

    def show_dreams(self):
        return "\n".join(self.dream_log[-10:])

    def show_logs(self):
        return "\n".join(self.logs[-30:])
