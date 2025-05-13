import tkinter as tk
from PIL import Image, ImageTk
from src.models.manager.device_manager import DeviceManager
from src.util.convencions import Colors
from src.util.logger import Logger


class ViewDevice(tk.Frame):
    def __init__(self, frame: tk.Frame, width: int = 800, height: int = 800, background: str = Colors.DARK_GRAY.value):
        super().__init__(frame, bg=background, width=width, height=height, border=1)
        self.__logger = Logger(name="Device View")
        self.device_manager: DeviceManager = None
        self.width=int(width)
        self.height=int(height)
        self.initalize()


    def initalize(self):
        if not self.device_manager:
            self.not_conection() 
        else:
            self.connect()

    def set_device(self, device: DeviceManager):
        self.device_manager: DeviceManager  = device

    
    def not_conection(self):
        canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open("img/not_img.png")
        bg_image = ImageTk.PhotoImage(image)

        image_width, image_height = bg_image.width(), bg_image.height()
        x_center = (self.width - image_width) // 2
        y_center = (self.height - image_height) // 2

        canvas.create_image(x_center, y_center, anchor=tk.NW, image=bg_image)
        canvas.image = bg_image
    
    def disconnected(self):

        canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open("img/disconect.png")
        bg_image = ImageTk.PhotoImage(image)

        image_width, image_height = bg_image.width(), bg_image.height()
        x_center = (self.width - image_width) // 2
        y_center = (self.height - image_height) // 2

        canvas.create_image(x_center, y_center, anchor=tk.NW, image=bg_image)
        canvas.image = bg_image

    def __create_grid(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)


    def connect(self):
        self.__create_grid()
        self.connection_button = tk.Button(self.grid_frame, bg=self.cget('bg'), fg="white", highlightbackground="green", highlightthickness=1 )
        self.connection_button.pack()
        
        def update_frame():
            try:
                if self.device_manager.videocapture is None or not self.device_manager.videocapture.isOpened():
                    raise ConnectionAbortedError("Não foi possivel estabelecer conexão")

                while True:
                    self.device_manager.update_frame(self.width, self.height)

                    if self.device_manager.resized_frame is not None:
                        imgtk = ImageTk.PhotoImage(image=self.device_manager.resized_frame)
                        self.connection_button.imgtk = imgtk
                        self.connection_button.configure(image=imgtk)

                    self.connection_button.after(10, update_frame)
                    break

            except Exception as e:
                self.__logger.error(f"{e}")
                self.grid_frame.forget()
                self.disconnected()

        update_frame()

    
            
