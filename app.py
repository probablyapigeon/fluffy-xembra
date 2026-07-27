"""Gradio interface that uses the original XEMBRA agent (talk loop).
Run: python app.py
"""
from modules.xembra import XEMBRA
import gradio as gr
import os
from fastapi import Request, HTTPException

# Create the XEMBRA agent instance
agent = XEMBRA()

with gr.Blocks(title="XEMBRA Narrative Loop") as demo:
    gr.Markdown("# XEMBRA — interactive agent")

    user_in = gr.Textbox(label="You", placeholder="Say something to XEMBRA...", lines=2)
    send_btn = gr.Button("Send")

    convo = gr.Textbox(label="Conversation", value="", lines=18)
    identity = gr.Textbox(label="Identity / State", value="", lines=8)

    def send_message(user_text: str, current_convo: str):
        if not user_text:
            return current_convo, identity.value if hasattr(identity, 'value') else ""
        # Get agent response using its talk() method
        resp = agent.talk(user_text)
        new_convo = (current_convo + "\n[YOU] " + user_text + "\n[XEMBRA] " + resp).strip()
        # Try to show some internal state if available
        try:
            state_view = agent.show_identity() + "\n\n" + agent.show_memory()
        except Exception:
            state_view = "(no state available)"
        return new_convo, state_view

    send_btn.click(send_message, inputs=[user_in, convo], outputs=[convo, identity])

# Optional token-based access control. Set XEMBRA_TOKEN in the environment
# to require requests to provide the token via the `token` query param or
# the `x-xembra-token` HTTP header.
XEMBRA_TOKEN = os.getenv("XEMBRA_TOKEN")
app = demo.server_app

if XEMBRA_TOKEN:
    @app.middleware("http")
    async def require_token(request: Request, call_next):
        provided = request.headers.get("x-xembra-token") or request.query_params.get("token")
        if not provided or provided != XEMBRA_TOKEN:
            raise HTTPException(status_code=401, detail="Unauthorized: missing or invalid token")
        return await call_next(request)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
