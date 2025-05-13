import tkinter as tk

from src.util.convencions import Colors, Font

class DeviceViewCrud(tk.Frame):
    def __init__(self, frame: tk.Frame, background: str = Colors.DARK_HARD_GRAY.value):
        super().__init__(frame, background=background, pady=10)
        self.form = tk.Frame(self, bg=Colors.DARK_HARD_GRAY.value)
        self.form.pack(fill=tk.BOTH, expand=True)
        self.create_form()
      

    def create_form(self):

        configs_bnt_lbl = {
            "bg":Colors.DARK_HARD_GRAY.value, 
            "fg":Colors.COLOR_FONT_DEFAULT.value, 
            "font":Font.ROBOTO.value
        }

        config_width=25

        container_id = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_id.pack()

        container_id_label = tk.Frame(master=container_id, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_id_label.pack(side='left')
        id_label = tk.Label(master=container_id_label, text=self.__text_complete("ID"), **configs_bnt_lbl)
        id_label.pack()
        container_id_entry = tk.Frame(master=container_id, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_id_entry.pack(side='left')
        self.entry_id = tk.Entry(container_id_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_id.pack()

        container_name = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_name.pack()
        container_name_label = tk.Frame(master=container_name, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_name_label.pack(side='left')
        name_label = tk.Label(master=container_name_label, text=self.__text_complete("Nome"), **configs_bnt_lbl)
        name_label.pack()
        container_name_entry = tk.Frame(master=container_name, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_name_entry.pack(side='left')
        self.entry_name = tk.Entry(container_name_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_name.pack()

        container_host = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_host.pack()
        container_host_label = tk.Frame(master=container_host, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_host_label.pack(side='left')
        host_label = tk.Label(master=container_host_label, text=self.__text_complete("Host(IP)"), **configs_bnt_lbl)
        host_label.pack()
        container_host_entry = tk.Frame(master=container_host, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_host_entry.pack(side='left')
        self.entry_host = tk.Entry(container_host_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_host.pack()

        container_port = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_port.pack()
        container_port_label = tk.Frame(master=container_port, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_port_label.pack(side='left')
        port_label = tk.Label(master=container_port_label, text=self.__text_complete("Porta"), **configs_bnt_lbl)
        port_label.pack()
        container_port_entry = tk.Frame(master=container_port, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_port_entry.pack(side='left')
        self.entry_port = tk.Entry(container_port_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_port.pack()

        container_username = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_username.pack()
        container_username_label = tk.Frame(master=container_username, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_username_label.pack(side='left')
        username_label = tk.Label(master=container_username_label, text=self.__text_complete("Usuário"), **configs_bnt_lbl)
        username_label.pack()
        container_username_entry = tk.Frame(master=container_username, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_username_entry.pack(side='left')
        self.entry_username = tk.Entry(container_username_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_username.pack()

        container_password = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=5)
        container_password.pack()
        container_password_label = tk.Frame(master=container_password, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_password_label.pack(side='left')
        password_label = tk.Label(master=container_password_label, text=self.__text_complete("Senha"), **configs_bnt_lbl)
        password_label.pack()

        container_password_entry = tk.Frame(master=container_password, bg=Colors.DARK_HARD_GRAY.value, padx=5)
        container_password_entry.pack(side='left')
        self.entry_password = tk.Entry(container_password_entry,font=Font.ROBOTO.value, width=config_width)
        self.entry_password.pack()
        # Botôes
        container_buttons = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=25)
        container_buttons.pack()
        self.bnt_insert = tk.Button(master=container_buttons, text=self.__text_complete("Inserir"), **configs_bnt_lbl)
        self.bnt_insert.pack(side='left')
        self.bnt_uptade = tk.Button(master=container_buttons, text=self.__text_complete("Atualizar"), **configs_bnt_lbl)
        self.bnt_uptade.pack(side='left')
        self.bnt_delete = tk.Button(master=container_buttons, text=self.__text_complete("Deletar"), **configs_bnt_lbl)
        self.bnt_delete.pack(side='left')
        # Voltar
        container_voltar = tk.Frame(master=self.form , bg=Colors.DARK_HARD_GRAY.value, pady=25)
        container_voltar.pack()
        self.bnt_voltar = tk.Button(master=container_voltar, text="Voltar", **configs_bnt_lbl, width=config_width)
        self.bnt_voltar.pack(side='left')

    def __text_complete(self, text: str, lengh: int = 20):
        completation = " " * (lengh - len(text))
        return f"{text}{completation}"