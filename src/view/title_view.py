import tkinter as tk
from tkinter import PhotoImage
from ..util.convencions import Colors, Font, Labels

class Title(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=Colors.DARK_GRAY.value)

        logo = PhotoImage(file="img/logo.png")
        title = tk.Label(self, font=Font.ROBOTO_TITLE.value, image=logo,text=F'{Labels.TITLE.value}', bg=Colors.DARK_GRAY.value, fg=Colors.COLOR_FONT_DEFAULT.value)
        title.image = logo
        title.pack()

class Layout(tk.Frame):
    def __init__(self, frame: tk.Frame, background: str = Colors.DARK_HARD_GRAY.value):
        super().__init__(frame, bg=background, border=1)
        self.dashboard = tk.Frame(frame, bg=Colors.DARK_GRAY.value, border=2)
        self.content = tk.Frame(frame, bg=Colors.DARK_HARD_GRAY.value)
