#LOG
import colorlog
import logging

#--------------
log_format = "%(log_color)s%(levelname)s%(reset)s - %(log_color)s%(message)s%(reset)s"

logger_raiz = logging.getLogger('')
logger_raiz.handlers = []  # Eliminar los controladores por defecto

# Configurar el controlador de consola con colores y el nuevo formato
console_handler = logging.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(log_format))
logger_raiz.addHandler(console_handler)




class LoggerManager():
    
    def __init__(self, class_name, level="DEBUG"):
        logger = logging.getLogger(class_name)
        logger.setLevel(logging.getLevelName(level))
        self.logger: logging.Logger = logger
    
    def get_logger(self) -> logging.Logger:
        return self.logger
        
