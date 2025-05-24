import tkinter as tk
from src.util.convencions import Colors

class Layout(tk.Frame):
    def __init__(self, frame: tk.Frame, background: str = Colors.DARK_HARD_GRAY.value):
        super().__init__(frame, bg=background, border=1)
        self.dashboard = tk.Frame(frame, bg=Colors.DARK_GRAY.value, border=2)
        self.content = tk.Frame(frame, bg=Colors.DARK_HARD_GRAY.value)
