# Meta classes podem ser usadas para criar singletons

class MetaSingleton(type):
    
    __instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

# A metaclasse irá controlar a criação de instâncias
# de Logger, implementando o padrão singleton    
class Logger(metaclass=MetaSingleton):
    pass

logger_1 = Logger()
print(f"Log 1: {id(logger_1)}")

logger_2 = Logger()
print(f"Log 2: {id(logger_2)}")
