import tkinter as tk
from tkinter import PhotoImage
from src.util.convencions import Colors, Font

class Messagebox():
    def __init__(self, message: str):
        self.window = tk.Toplevel()
        self.window.title("Atenção")
        self.window["bg"] = Colors.DARK_GRAY.value
        self.window.geometry("500x150")
        self.message = message
        self.img_view = PhotoImage(file="img/message.png")
        self.window.protocol("WM_DELETE_WINDOW", self.close_window) 
        self.build_message()
        self.window.mainloop()
      
    def build_message(self):
        frame_row1 = tk.Frame(self.window, background=Colors.DARK_GRAY.value, pady=10)
        frame_row1.pack()

        self.imagem = tk.Label(
            frame_row1,
            image=self.img_view,
            font=Font.ROBOTO,
           
           
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,

        )

        self.imagem.image = self.img_view
        self.imagem.pack(side='left', padx=5)

        self.label_text = tk.Label(
            frame_row1,
            text=self.message,
            font=Font.ROBOTO,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
        )
        self.label_text.pack(side='left', padx=5)
        
        frame_row2 = tk.Frame(self.window, background=Colors.DARK_GRAY.value, pady=10)
        frame_row2.pack()
        self.label_text = tk.Button(
            frame_row2,
            text="Ok",
            font=Font.ROBOTO,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            command=self.close_window,
            width=15
        )
        self.label_text.pack(side='left', padx=5)

    def close_window(self):
        self.window.destroy()

   


