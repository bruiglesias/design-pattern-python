# No padrão singleton monostate nós temos instâncias 
# diferentes de uma mesma classe mas que compartilham
# o mesmo estado, por iso é chamado de monostate

class Monostate(object):
    
    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
    


monostate_1 = Monostate()
print(f"monostate 1 id: {id(monostate_1)}")
print(monostate_1.__dict__)

monostate_2 = Monostate()
print(f"monostate 2 id: {id(monostate_2)}")
print(monostate_2.__dict__)

monostate_1.nome = 'Felicity'

print(f"monostate 1 dict : {monostate_1.__dict__}")
print(f"monostate 2 dict : {monostate_2.__dict__}")
