class Singleton(object):

    # __new__ é executado antes do método __init__
    def __new__(cls):
        # verifica se não existe o atributo 'instance'
        # significa que a classe ainda não foi instanciada
        if not hasattr(cls, 'instance'):
            # Se a classe não ainda foi instanciada
            # é criado o atributo instance que recebe uma instancia
            # da própria classe 
            cls.instance = super(Singleton, cls).__new__(cls)

            # esse print só será executado uma vez
            print(f'Criando um objeto {cls.instance}')
        
        # retorna a instancia da classe 
        return cls.instance
        
sigleton_1 = Singleton()
print(f"Instância 1: {id(sigleton_1)}")

sigleton_2 = Singleton()
print(f"Instância 2: {id(sigleton_2)}")

