import tkinter as tk
from src.view.device_view import ViewDevice
from src.util.convencions import Colors


class ViewGrid(tk.Frame):
    def __init__(self, frame: tk.Frame, background: str = Colors.DARK_HARD_GRAY.value):
        super().__init__(frame, bg=background, border=1)
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def create_grid(self):

        self.width_grid, self.heigth_grid = self.__calc_grid(self.__get_width_frame(self), self.__get_height_frame(self))

        device1 = ViewDevice(frame=self, width=self.width_grid, height=self.heigth_grid)
        device1.grid(row=0, column=0, padx=5, pady=5)
        device2 = ViewDevice(frame=self, width=self.width_grid, height=self.heigth_grid)
        device2.grid(row=0, column=1, padx=5, pady=5)
        device3 = ViewDevice(frame=self,  width=self.width_grid, height=self.heigth_grid)
        device3.grid(row=0, column=2, padx=5, pady=5)
        device4 = ViewDevice(frame=self, width=self.width_grid, height=self.heigth_grid)
        device4.grid(row=1, column=1, padx=5, pady=5)
        device5 = ViewDevice(frame=self, width=self.width_grid, height=self.heigth_grid)
        device5.grid(row=1, column=0, padx=5, pady=5)
        device6 = ViewDevice(frame=self, width=self.width_grid, height=self.heigth_grid)
        device6.grid(row=1, column=2, padx=5, pady=5)
        self.grid_list = [device1, device2, device3, device4, device5, device6]

    def __get_width_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return frame.winfo_width()
    
    def __get_height_frame(self, frame: tk.Frame) -> int:
        self.update_idletasks()
        return frame.winfo_height()
    
    def __calc_grid(self, width: int, heigth: int):
        return (width / 3) , (heigth / 2)

