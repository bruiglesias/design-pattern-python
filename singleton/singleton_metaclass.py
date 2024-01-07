class MyMetaClass(type):
    
    # call é chamado ao criar um instância de MyClass
    def __call__(cls, *args, **kwargs):
        print(f"=== Estes são os argumentos: {args}")
        return type.__call__(cls, *args, **kwargs)
    
class MyClass(metaclass=MyMetaClass):
    def __init__(self, valor_1, valor_2):
        self.valor_1 = valor_1
        self.valor_2 = valor_2


object_1 = MyClass(32, 23)
print(object_1)