# ============================================================
# XEMBRA GUI — Tkinter Desktop Interface
# ============================================================

import tkinter as tk
from tkinter import scrolledtext
import threading
import time

from xembra import XEMBRA
from autonomous_cycle import run_autonomous_cycle
from memory_visualizer import MemoryVisualizer


# ------------------------------------------------------------
# AUTONOMOUS BACKGROUND THREAD
# ------------------------------------------------------------

def start_autonomous_thread(xembra, gui_callback, world_events=None, interval=3.0):
    """
    Runs XEMBRA's autonomous cycle continuously in the background.
    gui_callback: function to print autonomous output to GUI.
    """

    def loop():
        while True:
            result = run_autonomous_cycle(xembra, world_events=world_events, interval=interval)

            if result:
                if result["spontaneous_thought"]:
                    gui_callback(f"🜁 XEMBRA (thought): {result['spontaneous_thought']}")
                if result["world_reaction"]:
                    gui_callback(f"🜁 XEMBRA (world): {result['world_reaction']}")

            time.sleep(1.0)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()


# ------------------------------------------------------------
# GUI APPLICATION
# ------------------------------------------------------------

class XembraGUI:
    def __init__(self):
        self.xembra = XEMBRA(style="neutral")

        # World events for autonomous cycle
        self.world_events = [
            {"type": "sound", "name": "wind chime"},
            {"type": "environment", "name": "rain"},
            {"type": "object", "name": "mirror"},
            {"type": "light", "name": "neon glow"},
            {"type": "sound", "name": "soft hum"},
            {"type": "environment", "name": "fog"},
        ]

        # Build GUI
        self.root = tk.Tk()
        self.root.title("XEMBRA — Creature Engine GUI")
        self.root.geometry("800x600")

        # Output window
        self.output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Consolas", 12))
        self.output.pack(expand=True, fill="both")

        # Input field
        self.entry = tk.Entry(self.root, font=("Consolas", 14))
        self.entry.pack(fill="x")
        self.entry.bind("<Return>", self.send_message)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x")

        tk.Button(button_frame, text="Send", command=self.send_message).pack(side="left")
        tk.Button(button_frame, text="Memory", command=self.show_memory).pack(side="left")
        tk.Button(button_frame, text="Dreams", command=self.show_dreams).pack(side="left")
        tk.Button(button_frame, text="Identity", command=self.show_identity).pack(side="left")
        tk.Button(button_frame, text="Emotion", command=self.show_emotion).pack(side="left")
        tk.Button(button_frame, text="World", command=self.show_world).pack(side="left")
        tk.Button(button_frame, text="Interactions", command=self.show_interactions).pack(side="left")

        # Style dropdown
        self.style_var = tk.StringVar(value="neutral")
        styles = ["neutral", "soft", "warm", "curious", "surreal", "alien", "dreamlike"]
        tk.OptionMenu(button_frame, self.style_var, *styles, command=self.change_style).pack(side="right")

        # Start autonomous background thinking
        start_autonomous_thread(self.xembra, self.print_output, world_events=self.world_events)

    # --------------------------------------------------------
    # GUI OUTPUT
    # --------------------------------------------------------
    def print_output(self, text):
        self.output.insert(tk.END, f"{text}\n")
        self.output.see(tk.END)

    # --------------------------------------------------------
    # SEND USER MESSAGE
    # --------------------------------------------------------
    def send_message(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return

        self.print_output(f"You: {user_text}")
        self.entry.delete(0, tk.END)

        reply = self.xembra.talk(user_text)
        self.print_output(f"XEMBRA: {reply}")

    # --------------------------------------------------------
    # STYLE CHANGE
    # --------------------------------------------------------
    def change_style(self, style):
        self.xembra.set_style(style)
        self.print_output(f"Style changed to: {style}")

    # --------------------------------------------------------
    # MEMORY VISUALIZATION
    # --------------------------------------------------------
    def show_memory(self):
        viz = MemoryVisualizer()
        self.print_output(viz.summarize())

    def show_dreams(self):
        viz = MemoryVisualizer()
        self.print_output(viz.dream_digest())

    def show_identity(self):
        viz = MemoryVisualizer()
        self.print_output(viz.identity_graph())

    def show_emotion(self):
        viz = MemoryVisualizer()
        self.print_output(viz.emotional_timeline())

    def show_world(self):
        viz = MemoryVisualizer()
        self.print_output(viz.world_summary())

    def show_interactions(self):
        viz = MemoryVisualizer()
        self.print_output(viz.interaction_summary())

    # --------------------------------------------------------
    # RUN GUI
    # --------------------------------------------------------
    def run(self):
        self.print_output("XEMBRA GUI initialized. Begin interaction.")
        self.root.mainloop()


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    gui = XembraGUI()
    gui.run()
