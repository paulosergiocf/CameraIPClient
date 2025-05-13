import tkinter as tk
from tkinter import PhotoImage
from src.util.convencions import Colors, Font

class ControlsViewDevice(tk.Frame):
    def __init__(self, frame: tk.Frame):
        super().__init__(master=frame, background=Colors.DARK_GRAY.value)
        self.load_constrols()
      
    def load_constrols(self):
        constrols = tk.Frame(self, background=Colors.DARK_GRAY.value, pady=10)
        constrols.pack()

        self.img_view = PhotoImage(file="img/full.png")
        self.botao_view = tk.Button(
            constrols,
            image=self.img_view,
            font=Font.ROBOTO,
            border=0,
            relief='raised',
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            highlightbackground=Colors.DARK_GRAY.value, 
            highlightthickness=1  
        )

        self.botao_view.image = self.img_view
        self.botao_view.pack(side='left', padx=5)

        img_rec = PhotoImage(file="img/rec.png")
        self.botao_record = tk.Button(
            constrols,
            image=img_rec,
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            highlightbackground=Colors.DARK_GRAY.value, 
            highlightthickness=1 

        )
        self.botao_record.image = img_rec

        self.botao_record.config(state=tk.DISABLED)
        self.botao_record.pack(side='left', padx=5)

        img_edit = PhotoImage(file="img/edit.png")
        self.botao_mng_device = tk.Button(
            constrols,
            image=img_edit,
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            highlightbackground=Colors.DARK_GRAY.value, 
            highlightthickness=1 

        )
        self.botao_mng_device.image = img_edit
        self.botao_mng_device.pack(side='left', padx=5)

        img_default = PhotoImage(file="img/default.png")
        self.botao_disconnect = tk.Button(
            constrols,
            image=img_default,
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            highlightbackground=Colors.DARK_GRAY.value, 
            highlightthickness=1 

        )
        self.botao_disconnect.image = img_default
        self.botao_disconnect.pack(side='left', padx=5)