import tkinter as tk
from tkinter import PhotoImage, ttk
from src.util.convencions import Colors, Font

class TableDeviceView(tk.Frame):
    def __init__(self, frame: tk.Frame, devices: list, **kwargs, ):
        super().__init__(frame, background=Colors.DARK_GRAY.value, **kwargs)
        self.devices = devices
        self.selected_item = None
 
        table = tk.Frame(self, background=Colors.DARK_GRAY.value, pady=10)
        table.pack()
        
        self.tree = ttk.Treeview(table, style="Custom.Treeview")
        self.tree["columns"] = ("Dispositivos", "ID")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.heading("Dispositivos", text="Dispositivos", anchor=tk.CENTER)
        self.tree.column("ID", width=0, stretch=tk.NO)

        self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.load_constrols()
        self.load_data()
    
    def load_constrols(self):
        constrols = tk.Frame(self, background=Colors.DARK_GRAY.value, pady=10)
        constrols.pack()

        img_view = PhotoImage(file="img/full.png")
        self.botao_view = tk.Button(
            constrols,
            image=img_view,
            font=Font.ROBOTO,
            border=0,
            relief='raised',
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value        
        )
        self.botao_view.image = img_view
        self.botao_view.pack(side='left', padx=5)

        img_rec = PhotoImage(file="img/rec.png")
        self.botao_record = tk.Button(
            constrols,
            image=img_rec,
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value

        )
        self.botao_record.image = img_rec

        self.botao_record.config(state=tk.DISABLED)
        self.botao_record.pack(side='left', padx=5)

        img_low = PhotoImage(file="img/low.png")
        self.botao_disconnect = tk.Button(
            constrols,
            image=img_low,
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,

        )
        self.botao_disconnect.image = img_low
        self.botao_disconnect.pack(side='left', padx=5)


    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for device in self.devices:
            values = (device.name_device, device.id)
            self.tree.insert("", tk.END, values=values)

    def on_item_selected(self, event):
        selected = self.tree.selection()
        if selected:
            self.selected_item = self.tree.item(selected, "values")[1]  