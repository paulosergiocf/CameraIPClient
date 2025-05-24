from src.util.logger import Logger
from src.view.app import App
from dotenv import load_dotenv
import tkinter as tk
load_dotenv()

if __name__=='__main__':
    logger = Logger(name='Main')
    try:
        logger.info("inicio da execução da aplicação")
        window = tk.Tk() 
        app = App(window)
        app.mainloop()
    except KeyboardInterrupt as erro:
        logger.error("Aplicação abortada pelo usuario.")
        
    except Exception as erro:
        logger.error(erro)

    finally:
        logger.info("fim da execução")

