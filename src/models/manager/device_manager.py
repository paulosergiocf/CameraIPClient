import cv2
from PIL import Image

from src.models.devices import Device

class DeviceManager:
    def __init__(self, device: Device):
        self.device: Device = device
        self.string_connection = None
        self.resized_frame = None
        self.videocapture = None
        self.validate_str_connection()

    def __get_string_connection(self):
        """
        Returns:
            str: string de conexão RSTP
        """
        return f'rtsp://{self.device.host}:{self.device.port}/user={self.device.username}&password={self.device.password}&channel=1&stream=0'

    def validate_str_connection(self):
       
        self.videocapture = cv2.VideoCapture(self.__get_string_connection())
        
        if not self.videocapture.isOpened():
            self.videocapture = None

    def update_frame(self, frame_width: int, frame_height: int):
        """
        Atualiza o quadro (frame) capturado pela câmera, redimensionando-o para as dimensões especificadas.
        Args:
            frame_width (int): Largura desejada para o quadro redimensionado.
            frame_height (int): Altura desejada para o quadro redimensionado.
        Comportamento:
            - Se o objeto `videpcapture` ainda não estiver inicializado, ele será criado usando a string de conexão.
            - Captura um quadro da câmera.
            - Converte o quadro de BGR para RGB.
            - Transforma o quadro em uma imagem PIL.
            - Redimensiona o quadro para as dimensões especificadas usando o filtro LANCZOS.
        """
        
        if not self.videocapture:
            self.videocapture = cv2.VideoCapture(self.__get_string_connection())

        done, image_array = self.videocapture.read()

        if done:
            image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
            image_array = Image.fromarray(image_array)

            self.resized_frame = image_array.resize((frame_width, frame_height), Image.LANCZOS)