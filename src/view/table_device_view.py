import tkinter as tk
from tkinter import ttk
from src.util.convencions import Colors

class TableDeviceView(tk.Frame):
    def __init__(self, frame: tk.Frame, devices: list ):
        super().__init__(master=frame, background=Colors.DARK_GRAY.value)
        self.devices = devices
        self.selected_item = None
        self.update_table()
        
    def update_table(self):
        table = tk.Frame(self, background=Colors.DARK_GRAY.value, pady=10)
        table.pack()
        
        self.tree = ttk.Treeview(table, style="Custom.Treeview")
        self.tree["columns"] = ("Dispositivos", "ID")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.heading("Dispositivos", text="Dispositivos", anchor=tk.CENTER)
        self.tree.column("ID", width=0, stretch=tk.NO)

        self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        self.load_data()

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

