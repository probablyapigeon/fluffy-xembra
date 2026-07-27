"""Gradio interface that uses the original XEMBRA agent (talk loop).
Run: python app.py
"""
import sys
import os

# Ensure modules folder is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

import gradio as gr
from fastapi import Request, HTTPException

# Try to import the full XEMBRA agent; fall back to simple narrative if it fails
agent = None
error_msg = ""
try:
    from modules.xembra import XEMBRA
    agent = XEMBRA()
    print("✓ Full XEMBRA agent loaded successfully.")
except Exception as e:
    error_msg = f"Failed to load XEMBRA agent: {type(e).__name__}: {e}"
    print(f"✗ {error_msg}")
    print(f"  Falling back to simple narrative engine.")
    # Fall back to simple Engine if XEMBRA fails
    try:
        from run_engine import Engine
        agent = Engine()
        print("✓ Simple Engine loaded as fallback.")
    except Exception as e2:
        error_msg += f"\nFallback also failed: {type(e2).__name__}: {e2}"
        print(f"✗ {error_msg}")
        agent = None

with gr.Blocks(title="XEMBRA Narrative Loop") as demo:
    gr.Markdown("# XEMBRA — interactive agent")

    user_in = gr.Textbox(label="You", placeholder="Say something to XEMBRA...", lines=2)
    send_btn = gr.Button("Send")

    convo = gr.Textbox(label="Conversation", value="", lines=18)
    identity = gr.Textbox(label="Identity / State", value="", lines=8)

    def send_message(user_text: str, current_convo: str):
        if not user_text:
            return current_convo, identity.value if hasattr(identity, 'value') else ""
        
        if agent is None:
            return current_convo + "\n[ERROR] Agent not loaded: " + error_msg, "(agent initialization failed)"
        
        # Get agent response
        try:
            resp = agent.talk(user_text)
        except Exception as e:
            resp = f"[Agent error: {type(e).__name__}]"
        
        new_convo = (current_convo + "\n[YOU] " + user_text + "\n[XEMBRA] " + resp).strip()
        
        # Try to show some internal state if available
        try:
            if hasattr(agent, 'show_identity') and hasattr(agent, 'show_memory'):
                state_view = agent.show_identity() + "\n\n" + agent.show_memory()
            else:
                state_view = "(no state methods available)"
        except Exception:
            state_view = "(no state available)"
        
        return new_convo, state_view

    send_btn.click(send_message, inputs=[user_in, convo], outputs=[convo, identity])

# Optional token-based access control. Set XEMBRA_TOKEN in the environment
# to require requests to provide the token via the `token` query param or
# the `x-xembra-token` HTTP header.
XEMBRA_TOKEN = os.getenv("XEMBRA_TOKEN")

if __name__ == "__main__":
    port = int(os.getenv("GRADIO_SERVER_PORT", "7860"))
    
    if XEMBRA_TOKEN:
        # Add token middleware before launch
        app = demo.server_app
        @app.middleware("http")
        async def require_token(request: Request, call_next):
            provided = request.headers.get("x-xembra-token") or request.query_params.get("token")
            if not provided or provided != XEMBRA_TOKEN:
                raise HTTPException(status_code=401, detail="Unauthorized: missing or invalid token")
            return await call_next(request)
    
    demo.launch(server_name="0.0.0.0", server_port=port, share=False)
