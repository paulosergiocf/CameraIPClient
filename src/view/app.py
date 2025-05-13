
from src.util.encript import Encript
from src.util.logger import Logger
import tkinter as tk
from tkinter import PhotoImage, ttk
from src.util.convencions import Colors, Font, Labels
from src.models.repositories.devices_repository import DeviceRepository
from src.models.manager.device_manager import DeviceManager
from src.util.validation import Validation
from src.view.controls_view import ControlsViewDevice
from src.view.device_view import ViewDevice
from src.view.edit_device import DeviceViewCrud
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
        self.container_main = tk.Frame(self.main, bg=Colors.DARK_GRAY.value)
        self.container_main.pack(fill="both", expand=True)
        
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

        self.container_row1 = tk.Frame(self.layout.dashboard, bg=Colors.DARK_GRAY.value)
        self.container_row1.pack()
        self.__update_table()

        self.container_row2 = tk.Frame(self.layout.dashboard, bg=Colors.DARK_GRAY.value)
        self.container_row2.pack()
        self.controls_device = ControlsViewDevice(frame=self.container_row2)
        self.controls_device.botao_view.config(command=self.__view_full_image)
        self.controls_device.botao_disconnect.config(command=self.__close)
        self.controls_device.botao_mng_device.config(command=self.__edit_device_view)
        self.controls_device.pack()

        # Conteúdo (lado direito)
        self.layout.content.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        self.__create_grid(devices)
        self.container_row3 = tk.Frame(self.layout.dashboard, bg=Colors.DARK_GRAY.value)
        self.container_row3.pack()
        botao_test = tk.Button(
            self.container_row3,
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

    def __create_grid(self, devices: list = None):
        if not devices:
            devices = list(DeviceRepository.get_all())

        self.view_image = PhotoImage(file="img/full.png")
        self.controls_device.botao_view.config(image=self.view_image, command=self.__view_full_image)
        

        self.create_container_tmp(self.layout.content)
        content_devices = ViewGrid(self.container_content_base)
        content_devices.pack(fill="both", expand=True)
        self.controls_device.botao_disconnect.config(state=tk.DISABLED)

        content_devices.create_grid()
        for index_device in range(0,6):
            if index_device < len(devices):
                content_devices.grid_list[index_device].set_device(DeviceManager(devices[index_device]))

        for device  in content_devices.grid_list:
            if device.device_manager:
                device.initalize()

    def __update_table(self):
        self.create_container_table(self.container_row1)
        devices = list(DeviceRepository.get_all())
        self.table = TableDeviceView(frame=self.container_content_table, devices=devices)
        self.table.pack()
            
    def __view_full_image(self):
        if not self.table.selected_item:
            return
        
        self.view_image = PhotoImage(file="img/low.png")
        self.controls_device.botao_view.config(image=self.view_image, command=self.__create_grid)
        
        self.create_container_tmp(self.layout.content)
        self.controls_device.botao_disconnect.config(state=tk.ACTIVE)

        width_grid, heigth_grid = self.__get_width_frame(self), self.__get_height_frame(self)

        frame = tk.Frame(self.container_content_base, bg=Colors.DARK_HARD_GRAY.value, width=width_grid, height=heigth_grid)
        frame.pack(fill="both", expand=True)

        device = DeviceRepository.get_by_id(self.table.selected_item)

        base_screen = min([self.layout.content.winfo_screenwidth(),self.layout.content.winfo_screenheight()])
        device_view = ViewDevice(frame=frame, width=base_screen, height=base_screen)
        device_view.set_device(DeviceManager(device=device))
        device_view.pack()

        device_view.initalize()
    
    def __edit_device_view(self):
        
        self.create_container_tmp(self.layout.content)
        width_grid, heigth_grid = self.__get_width_frame(self), self.__get_height_frame(self)

        frame = tk.Frame(master=self.container_content_base, bg=Colors.DARK_HARD_GRAY.value, width=width_grid, height=heigth_grid, pady=10)
        frame.pack(fill="both", expand=True)

        self.screen = DeviceViewCrud(frame=frame)
        self.screen.bnt_insert.config(command=self.__add_device)
        self.screen.bnt_uptade.config(command=self.__update_device)
        self.screen.bnt_delete.config(command=self.__delete_device)
        self.screen.bnt_voltar.config(command=self.__create_grid)

        if not self.table.selected_item:
            self.screen.bnt_delete.config(state=tk.DISABLED)
            self.screen.bnt_uptade.config(state=tk.DISABLED)
            self.screen.entry_id.config(state=tk.DISABLED)
        else:
            device = DeviceRepository.get_by_id(self.table.selected_item)
            self.screen.entry_id.insert(0, device.id)
            self.screen.entry_name.insert(0, device.name_device)
            self.screen.entry_host.insert(0, device.host)
            self.screen.entry_port.insert(0, device.port)
            self.screen.entry_username.insert(0, device.username)
            self.screen.entry_password.insert(0, Encript.decrypt_AES_CBC(device.password))
            self.table.selected_item = None

        self.screen.pack()
    
    def __record(self):
        # TODO implementar captura de video de dispositivo
        pass
    
    def __close(self):
        self.__create_grid(DeviceRepository.get_all())


    # ------ CRUD DEVICE ---------
    
    def __add_device(self):
        
        name_device = Validation.string(entry=self.screen.entry_name.get(), size=45)
        host = Validation.string(entry=self.screen.entry_host.get(), size=45)
        port = Validation.integer(entry=self.screen.entry_port.get())
        username = Validation.string(entry=self.screen.entry_username.get(), size=45)
        password = Validation.string(entry=self.screen.entry_password.get(), size=250)

        DeviceRepository.create_device(
            name_device=name_device, host=host, port=port,
            username=username, password=Encript.encrypt_AES_CBC(password))

        self.__clear_entries()
        self.__update_table()

    def __delete_device(self):
        id_device = Validation.integer(self.screen.entry_id.get())
        DeviceRepository.delete_device(id_device)
        self.__clear_entries()
        self.__update_table()
        self.__create_grid()

    def __update_device(self):
        id_device = Validation.integer(entry=self.screen.entry_id.get())
        name_device = Validation.string(entry=self.screen.entry_name.get(), size=45)
        host = Validation.string(entry=self.screen.entry_host.get(), size=45)
        port = Validation.integer(entry=self.screen.entry_port.get())
        username = Validation.string(entry=self.screen.entry_username.get(), size=45)
        password = Validation.string(entry=self.screen.entry_password.get(), size=250)

        DeviceRepository.update_device(
            device_id=id_device,
            name_device=name_device, host=host, port=port,
            username=username, password=Encript.encrypt_AES_CBC(password))

        self.__clear_entries()
        self.__update_table()
        self.__create_grid()
    
    def __clear_entries(self):
        self.screen.entry_id.delete(0, tk.END)
        self.screen.entry_name.delete(0, tk.END)
        self.screen.entry_host.delete(0, tk.END)
        self.screen.entry_port.delete(0, tk.END)
        self.screen.entry_username.delete(0, tk.END)
        self.screen.entry_password.delete(0, tk.END)
        

    # -- UTIL VIEW ---

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

    def create_container_table(self, frame):
        if hasattr(self, 'container_content_table') and self.container_content_table:
            self.container_content_table.destroy()

        self.container_content_table = tk.Frame(frame, bg=Colors.DARK_GRAY.value)
        self.container_content_table.pack()

    def __get_width_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return int(frame.winfo_width())
    
    def __get_height_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return int(frame.winfo_height())
    