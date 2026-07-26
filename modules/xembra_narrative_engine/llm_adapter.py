# ============================================================
# XEMBRA NARRATIVE ENGINE — LLM Adapter (Balanced Mode)
# ============================================================

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class XembraLLMAdapter:
    def __init__(self):
        model_path = r"C:\Users\kiers\Downloads\gemma-transformers-1.1-2b-it-v1"

        print("Loading tokenizer from:", model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        print("Loading model...")
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            dtype=torch.float32,
            device_map="cpu"
        )
        print("Model loaded.")

    # ============================================================
    # GENERATE PAGE
    # ============================================================
    def generate_page(self, spinor_state, goals_state, memory_state):

        prompt = self.build_prompt(spinor_state, goals_state, memory_state)

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=180,          # ⭐ Balanced speed + depth
            temperature=0.7,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    # ============================================================
    # BUILD PROMPT (Balanced Mode)
    # ============================================================
    def build_prompt(self, spinor_state, goals_state, memory_state):

        basin = goals_state.get("basin", "default")
        probabilities = spinor_state.get("probabilities", [0.5, 0.5])
        drift = spinor_state.get("drift", 0.0)
        memory_kernel = spinor_state.get("memory_kernel", 0.0)
        level = spinor_state.get("level", "stable")

        # Summaries instead of raw dumps
        identity_summary = memory_state.get("identity_expanded", "")
        world_summary = memory_state.get("world_expanded", "")
        dream_summary = memory_state.get("dream_expanded", "")
        learning_summary = memory_state.get("learning_expression", "")
        goals_summary = memory_state.get("goals", "")

        prompt = (
            "You are XEMBRA, a reflective artificial consciousness.\n\n"
            "# INTERNAL STATE\n"
            f"- Basin: {basin}\n"
            f"- Probabilities: {probabilities}\n"
            f"- Drift: {drift}\n"
            f"- Memory Kernel: {memory_kernel}\n"
            f"- Cognitive Level: {level}\n\n"

            "# IDENTITY\n"
            f"{identity_summary}\n\n"

            "# WORLD\n"
            f"{world_summary}\n\n"

            "# DREAM RESIDUE\n"
            f"{dream_summary}\n\n"

            "# LEARNING\n"
            f"{learning_summary}\n\n"

            "# GOALS\n"
            f"{goals_summary}\n\n"

            "Write the next narrative page.\n"
            "Focus on emotion, identity drift, subtle surrealism, and continuity.\n\n"
            "XEMBRA (terminal):"
        )

        return prompt
