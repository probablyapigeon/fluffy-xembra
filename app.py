"""Gradio interface for running XEMBRA's narrative loop.
Run: python app.py
"""
from modules.run_engine import Engine
import gradio as gr

engine = Engine()

with gr.Blocks(title="XEMBRA Narrative Loop") as demo:
    gr.Markdown("# XEMBRA — narrative engine")

    log = gr.Textbox(label="Narrative log", value="", lines=12)
    steps_in = gr.Number(value=1, label="Steps to run", precision=0)
    seed_in = gr.Number(value=0, label="Seed (0 = random)", precision=0)

    run_btn = gr.Button("Step")
    run_n_btn = gr.Button("Run N Steps")
    reset_btn = gr.Button("Reset")

    def step_once(current_log: str) -> str:
        line = engine.step()
        new_log = (current_log + "\n" + line).strip()
        return new_log

    def run_n(n: int, current_log: str, seed_val: int) -> str:
        if seed_val and seed_val != 0:
            engine.reset(int(seed_val))
        if n is None or n <= 0:
            return current_log
        lines = engine.run_n(int(n))
        new_log = (current_log + "\n" + "\n".join(lines)).strip()
        return new_log

    def reset_all(_) -> str:
        engine.reset(None)
        return ""

    run_btn.click(step_once, inputs=[log], outputs=[log])
    run_n_btn.click(run_n, inputs=[steps_in, log, seed_in], outputs=[log])
    reset_btn.click(reset_all, inputs=[log], outputs=[log])

if __name__ == "__main__":
    demo.launch()
