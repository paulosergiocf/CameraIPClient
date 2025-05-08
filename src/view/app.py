
from src.util.logger import Logger
import tkinter as tk
from tkinter import ttk
from src.util.convencions import Colors, Font, Labels
from src.models.repositories.devices_repository import DeviceRepository
from src.models.manager.device_manager import DeviceManager
from src.view.device_view import ViewDevice
from src.view.grid_view import ViewGrid
from src.view.layout_view import Layout
from src.view.table_device_view import TableDeviceView
from src.view.title_view import Title

class App(tk.Frame):

    def __init__(self, main):
        super().__init__(main)
        self.__logger = Logger(name='App')
        self.main = main
        self.__config()
        self.init()
        
    
    def __config(self):
        """
        Descrição
            Configurações da interface.
        """ 
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        self.main.geometry(f"{screen_width}x{screen_height}")
        self.main.title(Labels.TITLE.value)
        self.main["bg"] = Colors.DARK_GRAY.value
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.Treeview", 
                background=Colors.DARK_GRAY.value, 
                fieldbackground=Colors.DARK_GRAY.value, 
                foreground=Colors.COLOR_FONT_DEFAULT.value)
        style.configure("Custom.Treeview.Heading", 
                background=Colors.DARK_HARD_GRAY.value, 
                foreground=Colors.COLOR_FONT_DEFAULT.value)
 
        photo = tk.PhotoImage(file='img/logo.png')
        self.main.iconphoto(False, photo)
        self.__logger.info("carregada as configurações da interface")
        self.container_main = None

      

    def init(self):
        self.create_container_main()
        
        # Título
        container_title = tk.Frame(self.container_main, bg=Colors.DARK_GRAY.value)
        container_title.pack(fill="x", pady=10)
        title = Title(container_title)
        title.pack()

        # Conteúdo principal
        container_content = tk.Frame(self.container_main, bg=Colors.DARK_GRAY.value)
        container_content.pack(fill="both", expand=True, padx=10, pady=10)

        # Dashboard (lado esquerdo)
        self.layout = Layout(frame=container_content)
        self.layout.dashboard.pack(side="left", fill="y", padx=5)

        devices = list(DeviceRepository.get_all())
        self.table = TableDeviceView(frame=self.layout.dashboard,devices=devices)
        self.table.botao_view.config(command=self.__view_full_image)
        self.table.botao_disconnect.config(command=self.__close)
        self.table.pack()

        # Conteúdo (lado direito)
        self.layout.content.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.__create_grid(devices)

        
        botao_test = tk.Button(
            self.layout.dashboard,
            text="Sair",
            relief="flat",
            font=Font.ROBOTO,
            border=0,
            bg=Colors.DARK_GRAY.value,
            fg=Colors.COLOR_FONT_DEFAULT.value,
            width=20,
            height=1,
            command=quit
        )
        botao_test.pack(pady=10)

        

    def __create_grid(self, devices: list):
        self.create_container_tmp(self.layout.content)
        content_devices = ViewGrid(self.container_content_base)
        content_devices.pack(fill="both", expand=True)
        self.table.botao_disconnect.config(state=tk.DISABLED)

        content_devices.create_grid()
        for index_device in range(0,6):
            if index_device < len(devices):
                content_devices.grid_list[index_device].set_device(DeviceManager(devices[index_device]))

        for device  in content_devices.grid_list:
            if device.device_manager:
                device.initalize()
            
    def __view_full_image(self):
        if not self.table.selected_item:
            return
        
        self.create_container_tmp(self.layout.content)
        self.table.botao_disconnect.config(state=tk.ACTIVE)

        device = DeviceRepository.get_by_id(self.table.selected_item)
        base_screen = min([self.layout.content.winfo_screenwidth(),self.layout.content.winfo_screenheight()])
        device_view = ViewDevice(frame=self.container_content_base, width=base_screen, height=base_screen)
        device_view.set_device(DeviceManager(device=device))
        device_view.pack()

        device_view.initalize()
    
    def __record(self):
        pass
    
    def __close(self):
        self.__create_grid(DeviceRepository.get_all())

    def create_container_main(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.container_main = tk.Frame(self.main, bg=Colors.DARK_GRAY.value)
        self.container_main.pack(fill="both", expand=True)

    def create_container_tmp(self, frame):
        if hasattr(self, 'container_content_base') and self.container_content_base:
            self.container_content_base.destroy()

        self.container_content_base = tk.Frame(frame, bg=Colors.DARK_GRAY.value)
        self.container_content_base.pack(fill="both", expand=True)

    def __get_width_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return int(frame.winfo_width())
    
    def __get_height_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return int(frame.winfo_height())
    
    def __calc_grid(self, width: int, heigth: int) -> int:
        return int(width / 3) , int(heigth / 2)