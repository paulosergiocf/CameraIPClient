import os
import logging
from datetime import datetime

class Logger(logging.Logger):
    DIRETORIO_LOG = 'logs'
    
    def __init__(self, name: str, nivel=logging.INFO):
        """Descrição
            Classe para padronizar a gravação de logs na aplicação.

        Args:
            nome (str): nome da classe em que está sendo instanciada.
            nivel (opcional): tipo do log conforme lib logging. padrão logging.INFO.
        """
        super().__init__(name=name, level=nivel)
        self.__create_path(self.DIRETORIO_LOG)
        self.path = os.path.join(os.getcwd(), self.DIRETORIO_LOG)
        self.nome = name
        self.file_log = os.path.join(self.path, f"{str(datetime.now().strftime('%Y-%m-%d'))}.log")
        self.__settings()
        
    def __settings(self):
        """
        Descrição.
            Define configuração do logger.
        """
        file_handler = logging.FileHandler(self.file_log, mode='a', encoding='utf-8')
        formato = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(formato)
        self.addHandler(file_handler)
    
    def info(self, msg):
        super().info(msg=f"{self.nome} - {msg}.")
    
    def warning(self, msg):
        super().warning(msg=f"{self.nome} - {msg}.")

    def error(self, msg):
        super().error(msg=f"{self.nome} - {msg}.", exc_info=True)
    

    def __create_path(self, diretorio: str):
        """Descrição

        Args:
            diretorio (str): diretorio
        """
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
